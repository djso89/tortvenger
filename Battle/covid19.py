#!/usr/bin/env python3
import pygame
import sys
from pygame.locals import *
from display import *
from stage import *
import random
from spritesheet import SpriteSheet

NumCells = 3

class COVID19(pygame.sprite.Sprite):
    """COVID19 Class """
    def __init__(self, x, y):
        """ initialize COVID19 Cell """
        super().__init__()
        sprite_sheet = SpriteSheet("images/C19_rdy.png")
        sprite_sheet_dmg_cut = SpriteSheet("images/C19_dmg_cut.png")
        ss = sprite_sheet.sprite_sheet
        ss_dmg_cut = sprite_sheet_dmg_cut.sprite_sheet

        # frame counter
        self.cnt = 0

        # action frames
        self.ready = []
        self.dmg_cut = []

        #load all the ready images
        for i in range (0, 6, 1):
            width = ss_dmg_cut.get_width()
            height = ss_dmg_cut.get_height()
            image = sprite_sheet_dmg_cut.get_image((width / 6) * i, 0,
                                                   (width / 6), height)
            self.dmg_cut.append(image)

        for i in range (0, 14, 1):
            width = ss.get_width()
            height = ss.get_height()
            image = sprite_sheet.get_image(width/14 * i, 0,
                                           width/14, height)
            self.ready.append(image)

        #kinematic factors
        self.pos = vec(x, y)
        self.vel = vec(0, 0)

        # image frame
        self.image = self.ready[0]
        self.rect = self.image.get_rect(topleft=self.pos)
        self.vel.x = random.randint(1, 10) / 2 

        # action flags
        # 0 - go right
        # 1 - go left
        self.direction = random.randint(0, 1)

        # wait flag when cell get hit with player attack
        self.hitCell = False
        self.cnt_hc = 0


    def place_cell(self, x, y):
        self.pos.x = x
        self.pos.y = y

    def pause(self):
        period = 9
        if self.hitCell:
            if self.cnt_hc >= period * (len(self.dmg_cut) - 1) :
                self.cnt_hc = 0
                self.hitCell = False
            else:
                self.image = self.dmg_cut[self.cnt_hc // period]
                self.cnt_hc += 1

    def move(self):
        """Make the cell move by itself """
        if self.pos.x <= 0:
            self.direction = 0
        elif self.pos.x >= (WIN_W - self.image.get_width()):
            self.direction = 1

        if not self.hitCell:
            if self.direction == 0:
                self.pos.x += self.vel.x
            if self.direction == 1:
                self.pos.x -= self.vel.x
            self.rect.x = self.pos.x
            self.rect.y = self.pos.y

    def ani_move(self):
        """ animate the left right movement"""
        frame = (self.pos.x // 30) % len(self.ready)
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
        x = random.randrange(0, WIN_W - 100)
        y = random.randrange(0, WIN_H - 200)
        cell = COVID19(x, y)
        Cells.add(cell)
    
#cell_gen()

C19 = COVID19(900, 500)
C1 = COVID19(400,300)
Cells.add(C19)
Cells.add(C1)
