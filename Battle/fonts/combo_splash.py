#!/usr/bin/env python3
import pygame
from k_action import KuppaAct, P1
from display import screen
# define the RGB value for white,
#  green, blue colour .
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
orange_red = (255,69,0)



class K_Comb():
    def __init__(self):
        self.ComboFont = pygame.font.Font('fonts/atk_comb.ttf',48)
        self.Txtclr = green
        self.ComboTxt = self.ComboFont.render('', True, self.Txtclr)
        self.ComboRect = self.ComboTxt.get_rect()
        self.ComboRect.center = (500, 500)
        self.ComboNum = str(KuppaAct.atk_comb)
            
        
    def change_color(self, color):
        self.Txtclr = color

    def update_combo(self, cnum):
        self.ComboNum = str(cnum)
        text = "Combo " + self.ComboNum
        self.ComboTxt = self.ComboFont.render(text, True, self.Txtclr)
        screen.blit(self.ComboTxt, self.ComboRect)

pygame.font.init()
KuppaCombo = K_Comb()
KuppaCombo.change_color(orange_red)
