# fire missile if spacebar pressed
if games.keyboard.is_pressed(games.K_SPACE):
    new_missle = Missle(self.x, self.y, self.angle)
    games.screen.add(new_missile)

    class Missile(games.Sprite):
        """ A missile launched by the player's ship. """
        image = games.load_image("missile.bmp")
        sound = games.load_sound("missile.wav")
        BUFFER = 40
        VELOCITY_FACTOR = 7
        LIFETIME = 40

        def __init__(self, ship_x, ship_y, ship_angle):
            """ Initialize missile sprite. """
            Missile.sound.play()

            # convert to radians
            angle = ship_angle * math.pi / 180

            # calculate missile's starting position
            buffer_x = Missile.BUFFER * math.sin(angle)
            buffer_y = Missile.BUFFER * -math.cos(angle)
            x = ship_x + buffer_x
            y = ship_y + buffer_y

            # calculate missile's velocity components
            dx = Missile.VELOCITY_FACTOR * math.sin(angle)
            dy = Missile.VELOCITY_FACTOR * -math.cos(angle)

            # create the missile
            super(Missile, self)._init__(image = Missile.image,
                                         x = x, y = y,
                                         dx = dx, dy = dy)
            self.lifetime = Missile.LIFETIME

        def update(self):
            """ Move the missile. """
            # if lifetime is up, destroy the missile
            self.lifetime -= 1
            if self.lifetime == 0:
                self.destroy()

            # wrap the missile around screen
            if self.top > games.screen.height:
                self.bottom = 0

            if self.bottom < 0:
                self.top = games.screen.height

            if self.left > games.screen.width:
                self.right = 0

            if self.right < 0:
                self.left = games.screen.width