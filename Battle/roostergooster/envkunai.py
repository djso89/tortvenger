import pygame
import sys
from pygame.locals import *
from display import *
from spritesheet import SpriteSheet
import random

black = (0, 0, 0)

class ENV_K(pygame.sprite.Sprite):
    """envelop kunai class for Gooster """
    def empty_frames(self):
        self.envk_r = []
        self.envk_l = []

    def load_images(self):
        sprite_sheet = SpriteSheet('images/env_kunai.png', black)
        ss = sprite_sheet.sprite_sheet

        for i in range(0, 4, 1):
            width = ss.get_width()
            height = ss.get_height()
            image = sprite_sheet.get_image(i *width / 4, 0, width / 4, height)
            self.envk_r.append(image)
            image = pygame.transform.flip(image, True, False)
            self.envk_l.append(image)

    def __init__(self, x, y, orientation):
        """ initialize envelop Kunai object"""
        super().__init__()
        self.empty_frames()
        self.load_images()

        self.pos = vec((x, y))
        self.range = random.randint(300, 600)
        self.endpt_xr = self.pos.x + self.range
        self.endpt_xl = self.pos.x - self.range

        self.vel = vec(15, 0)

        self.image = self.envk_r[0]
        self.rect = self.image.get_rect(topleft=self.pos)

        self.orientation = orientation
        self.hitlanded = False

    def move(self):
        if self.orientation == 'right':
            self.pos.x += self.vel.x
            if self.pos.x >= self.endpt_xr:
                self.kill()
            if self.pos.x >= WIN_W - self.rect.width:
                self.kill()
            if self.hitlanded == True:
                self.hitlanded = False
                self.kill()
        if self.orientation == 'left':
            self.pos.x -= self.vel.x
            if self.pos.x < 0:
                self.pos.x = 0
                self.kill()
            if self.pos.x <= self.endpt_xl:
                self.kill()
            if self.hitlanded == True:
                self.hitlanded = False
                self.kill()
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y

    def ani_move(self):
        frame = (self.pos.x // 40) % len(self.envk_r)
        if self.orientation == 'left':
            self.image = self.envk_l[int(frame)]
        if self.orientation == 'right':
            self.image = self.envk_r[int(frame)]

    def animate(self):
        self.ani_move()


    def render(self):
        width = self.image.get_width()
        height = self.image.get_height()
        screen.blit(self.image, self.pos, (0, 0, width, height))

envk_bullets = pygame.sprite.Group()
