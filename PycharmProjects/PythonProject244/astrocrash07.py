class Wrapper(games.Sprite):
    """ A sprite that wraps around the screen. """
    def update(self):
        """ Wrap sprite around screen. """
        if self.top > games.screen.height:
            self.bottom = 0

        if self.bottom < 0:
            self.top = games.screen.height

        if self.left > games.screen.width:
            self.right = 0

        if self.right < 0:
            self.left = gmaes.screen.width

        def die(self):
            """ Destroy self. """
            self.destroy()

class Collider(Wrapper):
    """ A wrapper that can collide with another object. """
    def update(self):
        """ Check for overlapping sprites. """
        super(Collider, self).update()

        if self.overlapping_sprites:
            for sprite in self.overlapping_sprites:
                sprite.die()
            self.die()

    def die(self):
        """ Destroy self and leave explosion behind. """
        new_explosion = Explosion(x = self.x, y = self.y)
        games.screen.add(new_explosion)
        self.destroy()

class Asteroid(Wrapper):
    super(Asteroid, self).die()

class Ship(Collider):
    super(Ship, self).update()

class Missile(Collider):
    super(Missile, self).update()

class Explosion(games.Animation):
    """ Explosion animation. """
    sound = games.load_sound("explosion.wav")
    images = ["explosion1.bmp",
              "explosion2.bmp",
              "explosion3.bmp",
              "explosion4.bmp",
              "explosion5.bmp",
              "explosion6.bmp",
              "explosion7.bmp",
              "explosion8.bmp",
              "explosion9.bmp"]

    def __init__(self, x, y):
        super(Explosion, self).__init__(images = Explosion.images,
                                        x = x, y = y,
                                        repeat_interval = 4, n_repeats = 1,
                                        is_collideable = False)
        Explosion.sound.play()
        