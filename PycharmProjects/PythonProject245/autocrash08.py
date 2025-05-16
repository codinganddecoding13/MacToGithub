from livewires import games, color

class Game(object):
    """ The game itself. """
    def __init__(self):
        """ Initialize the Game object. """
        # set level
        self.level = 0

        # load sound for level advance
        self.sound = games.load_sound("level.wav")

        # create score
        self.score = games.Text(value = 0,
                                size = 30,
                                color = color.white,
                                top = 5,
                                right = games.screen.width - 10
                                is_collideable = False)
        games.screen.add(self.score)

        # create player's ship
        self.ship = Ship(game = self,
                         x = games.screen.width/2,
                         y = games.screen.height/2)
        games.screen.add(self.ship)

    def play(self):
        """ Play the game. """
        # begin theme music
        games.music.load("theme.mid")
        games.music.play(-1)

        # load and set background
        nebula_image = games.load_image("nebula.jpg")
        games.screen.ackground = nebula_image

        # advance to level 1
        self.advance()

        # start play
        games.screen.mainloop()

    def advance(self):
        """ Advance to the next game level. """
        self.level += 1

        # amount of space around ship to preserve when creating asteroids
        BUFFER = 150

        # create new asteroids
        for i in range(self.level):
            # calculate an x and y at least BUFFER distance from the ship

            # choose minimum distance along x-axis and y-axis
            x_min = random.randrange(BUFFER)
            y_min = BUFFER - x_min

            # choose distance along x-axis and y-axis based on minimum distance
            x_distance = random.randrange(x_min, games.screen.width - x_min)
            y_distance = random.randrange(y_min, games.screen.height - y_min)

            # calculate location based on distance
            x = self.ship.x + x_distance
            y = self.ship.y + y_distance

            # wrap around screen, if necessary
            x %= games.screen.width
            y %= games.screen.height

            # create the asteroid
            new_asteroid = Asteroid(game = self,
                                    x = x, y = y,
                                    size = Asteroid.LARGE)
            games.screen.add(new_asteroid)

            #dispay level number
            level_message = games.Message(value = "Level " + str(self.level),
                                          size = 40,
                                          color = clor.yellow,
                                          x = games.screen.width/2,
                                          y = games.screen.width/10,
                                          lifetime = 3 * games.screen.fps,
                                          is_collideable = False)
            games.screen.add(level_message)

            # play new level sound (except at first level)
            if self.level > 1:
                self.sound.play()

    def end(self):
        """ End the game. """
        # show 'Game Over' for 5 seconds
        end_message = games.Message(value = "Game Over",
                                    size = 90,
                                    color = color.red,
                                    x = games.screen.width/2,
                                    y = games.screen.height/2,
                                    lifetime = 5 * games.screen.fps,
                                    after_death = games.screen.quit,
                                    is_collideable = False)
        games.screen.add(end_message)

POINTS = 30

        total = 0

        Asteroid.total += 1

    def __init__(self,game, x, y, size):
        self.game = game

        Asteroid.total -= 1

        self.game.score.value += int(Asteroid.POINTS / self.size)
        self.game.score.right = games.screen.width - 10

        new_asteroid = Asteroid(game = self.game,
                                # if all asteroids are gone, advance to the next level
        if Asteroid.total == 0:
            self.game.advance()
        )

VELOCITY_MAX = 3

        def __init__(self, game, x, y):
            self.game = game

            # cap velocity in each direction
            self.dx = min(max(self.dx, -Ship.VELOCITY_MAX), Ship.VELOCITY_MAX)
            self.dy = min(max(self.dy, -Ship.VELOCITY_MAX), Ship.VELOCITY_MAX)

        def die(self):
            """ Destroy ship and end the game. """
            self.game.end()
            super(Ship, self).die()

        def main():
            astrocrash = Game()
            astrocrash.play()

# kick it off!
main()