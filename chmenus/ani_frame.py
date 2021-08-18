#!/usr/bin/env python3
from display import *
import pygame
from spritesheet import SpriteSheet


black = (0, 0, 0)

class Ani_Frame(pygame.sprite.Sprite):
    """class Animated Frames """
    def __init__(self):
        """default constructor """
        super.__init__()
        self.cnt_0 = 0
        self.cnt_1 = 0
        self.cnt_2 = 0
        self.frame_0 = []
        self.frame_1 = []
        self.frame_2 = []

        self.img0 = pygame.Surface\
            ((286, 160), pygame.SRCALPHA, 32).convert_alpha()
        self.img1 = pygame.Surface\
            ((286, 160), pygame.SRCALPHA, 32).convert_alpha()
        self.img2 = pygame.Surface\
            ((286, 160), pygame.SRCALPHA, 32).convert_alpha()



    def load_frame0(self, path, fr_tot):
        """ load the images from spritesheet for frame0 """
        sprite_sheet = SpriteSheet(path, black)
        for i in range(0, fr_tot):
            ss = sprite_sheet.sprite_sheet
            width = ss.get_width()
            height = ss.get_height()
            image = sprite_sheet.get_image\
                (i * width // fr_tot, 0, width // fr_tot, height)
            self.frame0.append(image)

    def load_frame1(self, path, fr_tot):
        """ load the images from spritesheet for frame1"""
        sprite_sheet = SpriteSheet(path, black)
        for i in range(0, fr_tot):
            ss = sprite_sheet.sprite_sheet
            width = ss.get_width()
            height = ss.get_height()
            image = sprite_sheet.get_image\
                (i * width // fr_tot, 0, width // fr_tot, height)
            self.frame1.append(image)

    def load_frame2(self, path, fr_tot):
        """ load the images from spritesheet for frame1"""
        sprite_sheet = SpriteSheet(path, black)
        for i in range(0, fr_tot):
            ss = sprite_sheet.sprite_sheet
            width = ss.get_width()
            height = ss.get_height()
            image = sprite_sheet.get_image\
                (i * width // fr_tot, 0, width // fr_tot, height)
            self.frame2.append(image)

    def ani_frame0(self, period):
        """animate the profile pic0 """
        max_period = period * (len(self.frame_0) - 1)
        if (self.cnt_0 >= max_period):
            self.cnt_0 = 0
        else:
            self.img_0 = self.frame_0[self.cnt_0 // period]
            self.cnt_0 += 1

    def ani_frame1(self, period):
        """animate the profile pic1 """
        max_period = period * (len(self.frame_1) - 1)
        if (self.cnt_1 >= max_period):
            self.cnt_1 = 0
        else:
            self.img_1 = self.frame_1[self.cnt_1 // period]
            self.cnt_1 += 1

    def ani_frame2(self, period):
        """animate the profile pic2 """
        max_period = period * (len(self.frame_2) - 1)
        if (self.cnt_2 >= max_period):
            self.cnt_2 = 0
        else:
            self.img_2 = self.frame_2[self.cnt_2 // period]
            self.cnt_2 += 1
