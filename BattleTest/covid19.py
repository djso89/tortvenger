#!/usr/bin/env python3
import pygame
import sys
from pygame.locals import *
from display import *
from stage import *
from spritesheet import SpriteSheet


class COVID19(pygame.sprite.Sprite):
    """COVID19 Class """
    def __init__(self):
        """ initialize COVID19 Cell """
        super().__init__()
        sprite_sheet = SpriteSheet("images/C19_rdy.png")
        ss = sprite_sheet.sprite_sheet

        # frame counter
        self.cnt = 0

        # action frames
        self.ready = []

        #load all the ready images
        for i in range (0, 14, 1):
            width = ss.get_width()
            height = ss.get_height()
            image = sprite_sheet.get_image(width/14 * i, 0,
                                           width/14, height)
            self.ready.append(image)

        #kinematic factors
        self.pos = vec((974, 73))
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

        self.image = self.ready[0]
        self.rect = self.image.get_rect(topleft=self.pos)


    def move(self):
        self.acc = vec(0, 0)


    def update(self):
        #moving along X
        self.acc.x += self.vel.x * FRIC
        self.vel.x += self.acc.x
        self.pos.x += self.vel.x + 0.5 * self.acc.x

        self.rect.x = self.pos.x

        self.vel.y += self.acc.y
        self.pos.y += self.vel.y + 0.5 * self.acc.y

        self.rect.y = self.pos.y


    def render(self):
        """paste the COVID19 cell into screen """
        screen.blit(self.image, self.pos,
                    (0, 0, self.image.get_width(),
                     self.image.get_height()))



Cells = pygame.sprite.Group()
C19 = COVID19()
Cells.add(C19)
