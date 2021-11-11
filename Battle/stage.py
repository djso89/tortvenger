#!/usr/bin/env python3
from stageobjects_1_0 import Bldgs, platforms, Plats, Bricks, Cars, alph
import pygame
from display import *
from block import *




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
        self.Bldgs = Bldgs
        self.platforms = platforms
        self.GND_LAYER()
        self.Plats = Plats
        self.Bricks = Bricks
        self.Cars = Cars


        # stage objects to display
        self.StageBlocks = pygame.sprite.Group()
        self.StageBlocks.add(self.Plats)
        self.StageBlocks.add(self.platforms)
        self.StageBlocks.add(self.Cars)
        self.StageBlocks.add(self.Bldgs)
        self.StageBlocks.add(self.Bricks)

        self.bgimg = pygame.image.load("images/bg_level.png").convert()
        self.bgimg1 = pygame.transform.flip(self.bgimg, True, False)

        self.stagesurf = pygame.Surface([self.num_bg * self.bgimg.get_width(),\
                                         self.bgimg.get_height()]).convert()


        for i in range(0, self.num_bg, 1):
            if i % 2 == 0:
                left_corner = (i * self.bgimg.get_width(), 0)
                self.stagesurf.blit(self.bgimg, left_corner)
            else:
                left_corner = (i * self.bgimg1.get_width(), 0)
                self.stagesurf.blit(self.bgimg1, left_corner)

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





    def draw(self, screen, SB_SW):
        screen.fill(setting.bg_color)
        screen.blit(self.stagesurf, (self.scroll, 0))
        for block in self.Bricks:
            screen.blit(block.surf, block.rect)
        if SB_SW:
            for block in self.StageBlocks:
                screen.blit(block.surf, block.rect)



ST1 = Stage()
