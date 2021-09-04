#!/usr/bin/env python3
import pygame
from fonts.bordertext import Borderline_Txt

black = (0, 0, 0)
white = (255, 255, 255)

class Profile_ATTR():
    """ Class Profile attribute """
    def __init__(self):
        """attributes for printing 'ATK:' on attribute window"""
        self.attr_font = pygame.font.Font("fonts/aileron_regular.otf", 40)
        self.attr_atk_name = Borderline_Txt\
            ("ATK:", self.attr_font, black, white, 2)
        self.attr_atk_name_rect = self.attr_atk_name.get_rect()
        self.attr_atk_name_rect.topleft = ((845, 300))

        """ attributes for printing 'DEF:' on attribute window"""
        self.attr_def_name = Borderline_Txt\
            ("DEF:", self.attr_font, black, white, 2)
        self.attr_def_name_rect = self.attr_def_name.get_rect()
        self.attr_def_name_rect.topleft = ((845, 345))

        """ attributes for printing 'DEX:' on attribute window"""
        self.attr_dex_name = Borderline_Txt\
            ("DEX:", self.attr_font, black, white, 2)
        self.attr_dex_name_rect = self.attr_dex_name.get_rect()
        self.attr_dex_name_rect.topleft = ((845, 390))

        """ attributes for printing 'LUK:' on attribute window"""
        self.attr_luk_name = Borderline_Txt\
            ("LUK:", self.attr_font, black, white, 2)
        self.attr_luk_name_rect = self.attr_luk_name.get_rect()
        self.attr_luk_name_rect.topleft = ((845, 435))
