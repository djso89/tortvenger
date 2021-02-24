#!/usr/bin/env python3
import pygame
import sys
from pygame.locals import *
from display import *
from stage import *
import random
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
        self.pos = vec(0, 0)
        self.vel = vec(0, 0)

        # image frame
        self.image = self.ready[0]
        self.rect = self.image.get_rect()

        # action flags
        self.direction = random.randint(0, 1)
        self.vel.x = random.randint(2, 6) / 1
        
        if self.direction == 0:
            self.pos.x = 0
            self.pos.y = 235
        if self.direction == 1:
            self.pos.x = 500
            self.pos.y = 300

    def move(self):
        if self.pos.x <= 0:
            self.direction = 0
        elif self.pos.x >= (WIDTH - self.image.get_width()):
            self.direction = 1
        
        if self.direction == 0:
            self.pos.x += self.vel.x
        if self.direction == 1:
            self.pos.x -=self.vel.x
        self.rect.center = self.pos
        
    def ani_move(self):
        """ animate the left right movement"""
        if self.direction == 1:
            frame = (self.pos.x // 30) % len(self.ready)
            self.image = self.ready[int(frame)]


        elif self.direction == 0:
            frame = (self.pos.x // 30) % len(self.ready)
            self.image = self.ready[int(frame)]

    def render(self):
        """paste the COVID19 cell into screen """
        screen.blit(self.image, self.pos,
                    (0, 0, self.image.get_width(),
                     self.image.get_height()))



Cells = pygame.sprite.Group()
C19 = COVID19()
Cells.add(C19)
