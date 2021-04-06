#!/usr/bin/env python3
import pygame
import sys
from pygame.locals import *
from display import *
from stage import *
import random
from spritesheet import SpriteSheet
from stageobject import *
from c19gauge import *


NumCells = 7
black = (0, 0, 0)

class COVID19(C19_Gauge, pygame.sprite.Sprite):
    """COVID19 Class """
    def __init__(self, x, y):
        """ initialize COVID19 Cell """
        pygame.sprite.Sprite.__init__(self)
        C19_Gauge.__init__(self)
        sprite_sheet = SpriteSheet("images/C19_rdy.png", black)
        sprite_sheet_dmg_cut = SpriteSheet("images/C19_dmg_cut.png", black)
        sprite_sheet_dmg_envk = SpriteSheet("images/C19_dmg_envk.png", black)
        sprite_sheet_dmg_expk = SpriteSheet("images/C19_dmg_expk.png", black)

        ss = sprite_sheet.sprite_sheet
        ss_dmg_cut = sprite_sheet_dmg_cut.sprite_sheet
        ss_dmg_envk = sprite_sheet_dmg_envk.sprite_sheet
        ss_dmg_expk = sprite_sheet_dmg_expk.sprite_sheet

        # frame counter
        self.cnt = 0

        # action frames
        self.ready = []
        self.dmg_cut = []
        self.dmg_envk = []
        self.dmg_expk = []


        #load all the ready images
        for i in range (0, 6, 1):
            width = ss_dmg_cut.get_width()
            height = ss_dmg_cut.get_height()
            image = sprite_sheet_dmg_cut.get_image((width / 6) * i, 0,
                                                   (width / 6), height)
            self.dmg_cut.append(image)

        for i in range (0, 6, 1):
            width = ss_dmg_envk.get_width()
            height = ss_dmg_envk.get_height()
            image = sprite_sheet_dmg_envk.get_image((width / 6) * i, 0,
                                                   (width / 6), height)
            self.dmg_envk.append(image)


        for i in range (0, 6, 1):
            width = ss_dmg_expk.get_width()
            height = ss_dmg_expk.get_height()
            image = sprite_sheet_dmg_expk.get_image((width / 6) * i, 0,
                                                   (width / 6), height)
            self.dmg_expk.append(image)

        for i in range (0, 14, 1):
            width = ss.get_width()
            height = ss.get_height()
            image = sprite_sheet.get_image(width/14 * i, 0,
                                           width/14, height)
            self.ready.append(image)

        #kinematic factors
        self.pos = vec(x, y)
        self.start_x = 0
        self.end_x = 0
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
        self.hitCell_envk = False
        self.hitCell_expk = False
        self.cnt_hc = 0

    def set_range(self, start_x, end_x):
        self.start_x = start_x
        self.end_x = end_x

    def place_cell(self, x, y):
        self.pos.x = x
        self.pos.y = y

    def ani_dmg_cut(self):
        period = 9
        if self.cnt_hc >= period * (len(self.dmg_cut) - 1) :
            self.cnt_hc = 0
            self.hitCell = False
        else:
            self.image = self.dmg_cut[self.cnt_hc // period]
            self.cnt_hc += 1

    def ani_dmg_envk(self):
        period = 9
        if self.cnt_hc >= period * (len(self.dmg_envk) - 1):
            self.cnt_hc = 0
            self.hitCell_envk = False
        else:
            self.image = self.dmg_envk[self.cnt_hc // period]
            self.cnt_hc += 1

    def ani_dmg_expk(self):
        period = 9
        if self.cnt_hc >= period * (len(self.dmg_expk) - 1):
            self.cnt_hc = 0
            self.hitCell_expk = False
        else:
            self.image = self.dmg_expk[self.cnt_hc // period]
            self.cnt_hc += 1


    def pause(self):
        if self.hitCell:
            self.ani_dmg_cut()
        if self.hitCell_envk:
            self.ani_dmg_envk()
        if self.hitCell_expk:
            self.ani_dmg_expk()

    def move(self):
        """Make the cell move by itself """
        if self.pos.x < 0:
            self.direction = 0
        if self.pos.x <= self.start_x:
            self.direction = 0
        if self.pos.x >= self.end_x - self.rect.width : # (800):#
            self.direction = 1
        if self.pos.x >= WIN_W - self.rect.width:
            self.direction = 1

        if not (self.hitCell or self.hitCell_envk or self.hitCell_expk):
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
        self.show_gauge()
        self.pause()


    def render(self):
        """paste the COVID19 cell into screen """
        screen.blit(self.image, self.pos,
                    (0, 0, self.image.get_width(),
                     self.image.get_height()))
        if self.show_hp:
            self.show_gauge()
            screen.blit(self.hp_stat, self.pos)



Cells = pygame.sprite.Group()

def cell_gen(numcells):
    for i in range (0, numcells, 1):
        cp = random.choice(cell_plats.sprites())
        x = random.randint(cp.rect.left, cp.rect.right)
        x_ext_l = random.randrange(-200, 200, 25)
        x_ext_r = random.randrange(100, 200, 25)
        y = cp.rect.y
        cell = COVID19(x, y)
        cell.place_cell(x, y - cell.image.get_height())
        cell.set_range(cp.rect.left + x_ext_l, cp.rect.right + x_ext_r)
        Cells.add(cell)

#cell_gen(NumCells)

C19 = COVID19(900, 500)
C19.set_range(0, 1200)
C1 = COVID19(400,300)
C1.set_range(0, 1200)
Cells.add(C19)
#Cells.add(C1)
