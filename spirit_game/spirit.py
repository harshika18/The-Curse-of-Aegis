import time
from random import randint, choice, random

from spirit_game.functions import collide_with_object
from spirit_game.settings import *
from spirit_game.smoke import Smoke

import global_variables


class spirit(pg.sprite.Sprite):

    def __init__(self, game, x, y):
        self._layer = spirit_LAYER
        self.groups = game.all_sprites, game.spirits
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.spirit_img.copy()
        self.image2 = game.spirit_img2.copy()
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.position = vector(x, y)
        self.rect.center = self.position
        self.hit_rect = spirit_HIT_RECT.copy()
        self.hit_rect.center = self.rect.center
        self.vel = vector(0, 0)
        self.acc = vector(0, 0)
        self.rotation = 0
        self.shield = spirit_SHIELD
        self.shield_bar = None
        self.speed = choice(game.spirit_speeds)
        self.target = game.player
        self.damaged = False
        self.damage_alpha = None

    def draw_shield(self):
        if self.shield > 60:
            color = GREEN
        elif self.shield > 30:
            color = YELLOW
        else:
            color = RED
        width = int(self.rect.width * self.shield / spirit_SHIELD)
        self.shield_bar = pg.Rect(0, 0, width, 7)
        if self.shield < spirit_SHIELD:
            pg.draw.rect(self.image, color, self.shield_bar)

    def update(self):
        target_distance = self.target.position - self.position
        if target_distance.length_squared() < DETECT_RADIUS ** 2:
            self._update_spirit_moan_sounds()
            self._update_image()
            self._update_damage()
            self._update_position()
            self._update_collisisions()
        if self.shield <= 0:
            self.die()

    def die(self):
        self.game.player.total_accuracy += 10
        size = randint(70, 120)
        Smoke(self.game, self.rect.center, self.game.spirit_death_smoke, size)
        if global_variables.is_mute == False:
            choice(self.game.spirit_die_sounds).play()
        self.kill()
        self.game.map_img.blit(choice(self.game.splats), self.position - vector(32, 32))

    def _update_collisisions(self):
        self._avoid_other_spirits()
        collide_with_object(self, self.game.walls, 'x')
        collide_with_object(self, self.game.walls, 'y')

    def _avoid_other_spirits(self):
        for spirit in self.game.spirits:
            if spirit != self:
                distance = self.position - spirit.position
                if 0 < distance.length() < AVOID_RADIUS:
                    self.acc += distance.normalize()

    def _update_spirit_moan_sounds(self):
        if random() < 0.002:
            if global_variables.is_mute == False:
                choice(self.game.spirit_moan_sounds).play()

    def _update_damage(self):
        if self.damaged:
            try:
                self.image.fill((255, 0, 0, next(self.damage_alpha)), special_flags=pg.BLEND_RGB_MULT)
            except StopIteration:
                self.damaged = False

    def _update_image(self):
        self.rotation = (self.game.player.position - self.position).angle_to(vector(1, 0))
        if int(round(time.time()))%2==0:
            self.image = pg.transform.rotate(self.game.spirit_img, self.rotation)
        else:
            self.image = pg.transform.rotate(self.game.spirit_img2, self.rotation)

    def _update_position(self):
        self.rect = self.image.get_rect()
        self.rect.center = self.position
        self.acc = vector(1, 0).rotate(-self.rotation)
        self.acc.scale_to_length(self.speed)
        self.acc += self.vel * (-1)
        self.vel += self.acc * self.game.dt
        self.position += self.vel * self.game.dt + (self.acc * self.game.dt ** 2) / 2
        self.hit_rect.centerx = self.position.x
        self.hit_rect.centery = self.position.y
        self.rect.center = self.hit_rect.center
