#!/usr/bin/env python3
import pygame
import sys
from pygame.locals import *
from display import *
from stage import *
import random
from spritesheet import SpriteSheet

NumCells = 70

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
        self.vel.x = random.randint(2, 6) / 1

        # action flags
        self.direction = random.randint(0, 1)
        
        
        if self.direction == 0:
            self.pos.x = 0
            self.pos.y = 235
        if self.direction == 1:
            self.pos.x = 500
            self.pos.y = 300
    
    def place_cell(self, x, y):
        self.pos.x = x
        self.pos.y = y

    def move(self):
        """Make the cell move by itself """
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
        frame = (self.pos.x // 15) % len(self.ready)
        self.image = self.ready[int(frame)]
            
    def animate(self):
        self.ani_move()

    def render(self):
        """paste the COVID19 cell into screen """
        screen.blit(self.image, self.pos,
                    (0, 0, self.image.get_width(),
                     self.image.get_height()))



Cells = pygame.sprite.Group()

def cell_gen():
    for i in range (0, NumCells, 1):
        cell = COVID19()
        x = random.randrange(0, WIN_W - cell.image.get_width())
        y = random.randrange(0, WIN_H - cell.image.get_height())
        cell.place_cell(x, y)
        Cells.add(cell)
    
cell_gen()
C19 = COVID19()
C1 = COVID19()
C1.place_cell(900, 20)
C19.place_cell(0, 200)
Cells.add(C19)
Cells.add(C1)
