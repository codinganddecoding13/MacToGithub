    # check if missile overlaps any other object
    if self.overlapping_sprites:
        for sprite in self.overlapping_sprites
            sprite.die()
        self.die()

    def die(self)
        """ Destroy the missile. """
        self.destroy()

    # check if ship overlaps any other object
    if self.overlapping_sprites
        for sprite in self.overlapping_sprites:
            sprite.die()
        self.die()

    def die(self):
        """ Destroy ship. """
        self.destroy()

    SPAWN = 2

    def die(self):
        """ Destroy asteroid. """
        # if asteroid isn't small, replace it with two smaller asteroids
        if self.size != Asteroid.SMALL:
            for i in range(Asteroid.SPAWN):
                new_asteroid = Asteroid(x = self.x,
                                        y = self.y,
                                        size = self.size - 1)
                    games.screen.add(new_asteroid)
                self.destroy()