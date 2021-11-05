#!/usr/bin/env python3
from stageobject import Bldgs, platforms, Plats, Steps, Bricks, Cars
import pygame
from display import *
from block import *




class Stage(pygame.sprite.Sprite):
    """ class Stage """

    def __init__(self):
        """initialize the Stage """
        self.num_bg = 20
        self.scroll = 0
        self.Bldgs = Bldgs
        self.platforms = platforms
        self.Plats = Plats
        self.Steps = Steps
        self.Bricks = Bricks
        self.Cars = Cars


        # stage objects
        self.StageBlocks = pygame.sprite.Group()
        self.StageBlocks.add(self.Plats)
        self.StageBlocks.add(self.platforms)
        self.StageBlocks.add(self.Cars)
        self.StageBlocks.add(self.Steps)
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
        print('+++++++++++++++++++++++')
        print('scroll_x: {}'.format(self.scroll))


        """move the stage background and stage objects """
        for Plat in self.Plats:
            Plat.rect.x += round(shift)

        for car in self.Cars:
            car.rect.x += round(shift)

        """move the stage background and stage objects """
        for platform in self.platforms:
            platform.rect.x += round(shift)

        """move the Bricks """
        for brick in self.Bricks:
            brick.rect.x += round(shift)

        """move the Step """
        for step in self.Steps:
            step.rect.x += round(shift)

        """move the Bricks """
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
