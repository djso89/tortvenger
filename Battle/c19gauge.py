#!/usr/bin/env python3
from attr import C19_Attr
from fonts.bordertext import Borderline_Txt
from display import screen
import pygame

black = (0, 0, 0)
white = (255, 255, 255)

ehb_dir = 'images/cell_gauge/cell_hp_gauge.png'
hp_dir = 'images/cell_gauge/cell_hpbar.png'
font_dir = 'fonts/aileron_regular.otf'

class C19_Gauge(C19_Attr):
    def __init__(self):
        super(C19_Gauge, self).__init__()
        self.img_ehb = pygame.image.load(ehb_dir).convert()
        self.img_hp = pygame.image.load(hp_dir).convert()
        self.show_hp = False
        self.cnt_show_hp = 0

        self.hp_stat = self.img_ehb
        self.font = pygame.font.Font(font_dir, 90)
        self.hp_bar_w = self.img_hp.get_width()
        self.hp_bar_h = self.img_hp.get_height()
        self.hp_stat.blit(self.img_hp, (25, 25), \
                       (0, 0, (self.curr_hp / self.HP) * self.hp_bar_w, self.hp_bar_h))

        self.hpstring = 'H P :  ' + str(self.curr_hp) + ' / ' + str(self.HP)
        self.hptxt = Borderline_Txt(self.hpstring, self.font, black, white, 10)
        self.hp_stat.blit(self.hptxt, (100, 10))


    def show_gauge(self):
        """transform the updated hp bar of C19 to show """
        self.hp_stat = pygame.transform.scale(self.hp_stat, (140, 30))

    def hp_show(self):
        if self.show_hp:
            if self.cnt_show_hp >= 20:
                self.show_hp = False
                self.cnt_show_hp = 0
            else:
                self.cnt_show_hp += 1


    def __str__(self):
        return "LV: {} ATK: {} DEF: {} DEX:{} LUK: {}"\
            .format(self.LV, self.attack, \
                    self.defense, self.dexterity, self.luck)

pygame.font.init()
