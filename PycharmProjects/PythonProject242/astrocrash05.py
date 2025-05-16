            MISSILE_DELAY = 25

        def __init__(self, x, y):
            """ Initialize ship sprite. """
            super(Ship, self).__init__(image = Ship.image, x = x, y = y)
            self.missile_wait = 0

    # if waiting until the ship can fire next, decrease wait
    if self.missile_wait > 0:
        self.missile_wait -= 1

    # fire missile if spacebar pressed and missile wait is over
    if games.keyboard.is_pressed(games.K_SPACE) and self.missile_wait == 0:
        games.screen.add(new_missile)
        self.missile_wait = Ship.MISSILE_DELAY