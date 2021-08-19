#!/usr/bin/env python3
from display import *
import pygame
from spritesheet import SpriteSheet


black = (0, 0, 0)

class Ani_Frame(pygame.sprite.Sprite):
    """class Animated Frames """
    def __init__(self):
        """default constructor """
        super().__init__()
        self.cnt_0 = 0
        self.cnt_1 = 0
        self.cnt_2 = 0

        self.index_0 = 0
        self.index_1 = 0

        self.frame_0 = []
        self.frame_1 = []


        self.img0 = pygame.Surface\
            ((286, 160), pygame.SRCALPHA, 32).convert_alpha()
        self.img1 = pygame.Surface\
            ((286, 160), pygame.SRCALPHA, 32).convert_alpha()

        self.pos_0 = vec((0, 0))
        self.pos_1 = vec((0, 0))


    def load_frame0(self, path, fr_tot):
        """ load the images from spritesheet for frame0 """
        sprite_sheet = SpriteSheet(path, black)
        for i in range(0, fr_tot):
            ss = sprite_sheet.sprite_sheet
            width = ss.get_width()
            height = ss.get_height()
            image = sprite_sheet.get_image\
                (i * width // fr_tot, 0, width // fr_tot, height)
            self.frame_0.append(image)

    def load_frame1(self, path, fr_tot):
        """ load the images from spritesheet for frame1"""
        sprite_sheet = SpriteSheet(path, black)
        for i in range(0, fr_tot):
            ss = sprite_sheet.sprite_sheet
            width = ss.get_width()
            height = ss.get_height()
            image = sprite_sheet.get_image\
                (i * width // fr_tot, 0, width // fr_tot, height)
            self.frame_1.append(image)

    def ani_frame0(self, period):
        """animate the profile pic0 """
        max_index = (len(self.frame_0) - 1)
        if (self.cnt_0 >= period):
            self.img0 = self.frame_0[self.index_0]
            if self.index_0 < max_index:
                self.index_0 += 1
            else:
                self.index_0 = 0
            self.cnt_0 = 0
        else:
            self.cnt_0 += 1

    def ani_frame1(self, period):
        """animate the profile pic1 """
        max_index = (len(self.frame_1) - 1)
        if (self.cnt_1 >= period):
            self.img1 = self.frame_1[self.index_1]
            if self.index_1 < max_index:
                self.index_1 += 1
            else:
                self.index_1 = 0
            self.cnt_1 = 0
        else:
            self.cnt_1 += 1

    def set_frame_pos0(self, x, y):
        self.pos_0.x = x
        self.pos_0.y = y

    def set_frame_pos1(self, x, y):
        self.pos_1.x = x
        self.pos_1.y = y

    def display_0(self):
        """ display the animating frame_0 for profile """
        w = self.img0.get_width()
        h = self.img0.get_height()
        screen.blit(self.img0, self.pos_0, (0, 0, w, h))

    def display_1(self):
        """ display the animating frame_1 for profile """
        w = self.img1.get_width()
        h = self.img1.get_height()
        screen.blit(self.img1, self.pos_1, (0, 0, w, h))

    def show_frame(self, period0, period1):
        """animate all the profile pics and display
        on the screen
        """
        self.ani_frame0(period0)
        self.ani_frame1(period1)

        self.set_frame_pos0(self.pos_0.x, self.pos_0.y)
        self.set_frame_pos1(self.pos_1.x, self.pos_1.y)

        self.display_0()
        self.display_1()
