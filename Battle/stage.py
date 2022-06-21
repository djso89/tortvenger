#!/usr/bin/env python3
from stageobjects_1_0 import Bldgs, platforms, Plats, Bricks, Cars, alph, Portals
import pygame

from covid19 import *
from display import *
from block import *
from portal import Portal




class Stage(pygame.sprite.Sprite):
    """ class Stage """

    def GND_LAYER(self):
        """ generate the ground layers """
        Ground = Block()
        self.platforms.add(Ground)
        for i in range(1, self.num_bg, 1):
            Ground = Block()
            Ground.newBlock(i * WIDTH, HEIGHT - 20, WIDTH, 20, alph)
            self.platforms.add(Ground)

    def __init__(self):
        """initialize the Stage """
        self.num_bg = 10
        self.scroll = 0

        # stage objects
        self.Bldgs = Bldgs
        self.platforms = platforms
        self.GND_LAYER()
        self.Plats = Plats
        self.Bricks = Bricks
        self.Cars = Cars

        self.warp_doors = Portals

        # battlemode switch
        self.battlemode = True
        self.steps = 0

        # enemies to generate
        self.cells = Cells

        self.cell_plats = pygame.sprite.Group()




        # stage objects to display
        self.StageBlocks = pygame.sprite.Group()
        self.StageBlocks.add(self.Plats)
        self.StageBlocks.add(self.platforms)
        self.StageBlocks.add(self.Cars)
        self.StageBlocks.add(self.Bldgs)
        self.StageBlocks.add(self.Bricks)

        self.bgimg = pygame.image.load("images/stages/stage1-1/1_1_0.png").convert()
        self.bgimg1 = pygame.image.load("images/stages/stage1-1/1_1_1.png").convert()
        self.bg_rpt = pygame.image.load("images/stages/stage1-1/1_1_RPT.png").convert()

        self.stagesurf = pygame.Surface([self.num_bg * self.bgimg.get_width(),\
                                         self.bgimg.get_height()]).convert()

        left_corner = (0, 0)
        self.stagesurf.blit(self.bgimg, left_corner)

        left_corner = (self.bgimg1.get_width(), 0)
        self.stagesurf.blit(self.bgimg1, left_corner)

        for i in range(2, self.num_bg, 1):
            if i % 2 == 0:
                left_corner = (i * self.bg_rpt.get_width(), 0)
                self.stagesurf.blit(self.bg_rpt, left_corner)
            else:
                left_corner = (i * self.bg_rpt.get_width(), 0)
                bg_rpt1 = pygame.transform.flip(self.bg_rpt, True, False)
                self.stagesurf.blit(bg_rpt1, left_corner)

    def insert_bg(self, bg_num, image_path):
        """change the background at specific background index(bg_num) """
        bgimg = pygame.image.load(image_path).convert()
        left_corner = ((bg_num - 1) * self.bg_rpt.get_width(), 0)
        self.stagesurf.blit(bgimg, left_corner)



    def move_stage(self, shift):
        """move the background """
        self.scroll += round(shift)

        """move the stage background and stage objects """
        for Plat in self.Plats:
            Plat.rect.x += round(shift)

        """move the stage background and stage objects """
        for platform in self.platforms:
            platform.rect.x += round(shift)

        """move the Bricks """
        for brick in self.Bricks:
            brick.rect.x += round(shift)

        for car in self.Cars:
            car.rect.x += round(shift)


        """move the Bldgs """
        for bldg in self.Bldgs:
            bldg.rect.x += round(shift)

        for door in self.warp_doors:
            door.pos.x += round(shift)





    def draw(self, screen, SB_SW):
        screen.fill(setting.bg_color)
        screen.blit(self.stagesurf, (self.scroll, 0))
        for block in self.Bricks:
            screen.blit(block.surf, block.rect)
        if SB_SW:
            for block in self.StageBlocks:
                screen.blit(block.surf, block.rect)

        for door in self.warp_doors:
            door.render()



ST1 = Stage()
