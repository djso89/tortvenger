#!/usr/bin/env python3
import pygame
from fonts.bordertext import Borderline_Txt


black =(0, 0, 0)
white = (255, 255, 255)

class ATTR_BAR():
    """ Attribute Bar Class """
    def __init__(self):
        """ constructor """
        empty_bar_path = \
            'images/attr_bars/empty_bar.png'
        self.empty_bar = pygame.\
            image.load(empty_bar_path).convert_alpha()
        atk_bar_path = \
            'images/attr_bars/atk_bar.png'
        self.atk_bar = pygame.\
            image.load(atk_bar_path).convert_alpha()
        def_bar_path = \
            'images/attr_bars/def_bar.png'
        self.def_bar = pygame.\
            image.load(def_bar_path).convert_alpha()
        dex_bar_path = \
            'images/attr_bars/dex_bar.png'
        self.dex_bar = pygame.\
            image.load(dex_bar_path).convert_alpha()
        luk_bar_path = \
            'images/attr_bars/luk_bar.png'
        self.luk_bar = pygame.\
            image.load(luk_bar_path).convert_alpha()

        self.bar_img = pygame.Surface((200, 213), pygame.SRCALPHA, 32).convert_alpha()
        self.bar_img_rect = self.bar_img.get_rect()

    def set_bars(self, ch_info):
        bars_surf = pygame.Surface((200, 213), pygame.SRCALPHA, 32).convert_alpha()
        atk_w = self.atk_bar.get_width() * (ch_info.attack / 999)
        atk_h = self.atk_bar.get_height()

        def_w = self.def_bar.get_width() * (ch_info.defense / 999)
        def_h = self.def_bar.get_height()

        dex_w = self.dex_bar.get_width() * (ch_info.dexterity / 999)
        dex_h = self.dex_bar.get_height()

        luk_w = self.luk_bar.get_width() * (ch_info.luck / 999)
        luk_h = self.luk_bar.get_height()

        attr_font = pygame.font.Font("fonts/aileron_regular.otf", 20)
        # add the empty bars and attribute bars
        bars_surf.blit(self.empty_bar, (0, 0))
        bars_surf.blit(self.atk_bar, (1, 2),(0, 0, \
                                             atk_w,\
                                             atk_h))

        attr_value = Borderline_Txt\
            (str(ch_info.attack), attr_font, black, white, 2)
        bars_surf.blit(attr_value, (3, 2))

        bars_surf.blit(self.empty_bar, (0, 43))
        bars_surf.blit(self.def_bar, (1, 45), (0, 0, def_w, def_h))
        attr_value = Borderline_Txt\
            (str(ch_info.defense), attr_font, black, white, 2)
        bars_surf.blit(attr_value, (3, 45))

        bars_surf.blit(self.empty_bar, (0, 86))
        bars_surf.blit(self.dex_bar, (2, 88), (0, 0, dex_w, dex_h))
        attr_value = Borderline_Txt\
            (str(ch_info.dexterity), attr_font, black, white, 2)
        bars_surf.blit(attr_value, (3, 88))

        bars_surf.blit(self.empty_bar, (0, 132))
        bars_surf.blit(self.luk_bar, (2, 134), (0, 0, luk_w, luk_h))
        attr_value = Borderline_Txt\
            (str(ch_info.luck), attr_font, black, white, 2)
        bars_surf.blit(attr_value, (3, 134))

        self.bar_img = bars_surf
