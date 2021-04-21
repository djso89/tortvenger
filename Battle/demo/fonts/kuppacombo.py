#!/usr/bin/env python3
import pygame
from troopakuppa19.kuppabattle import *
from display import screen
from fonts.bordertext import Borderline_Txt

# color codes
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
orange_red = (255,69,0)
dark_red = (139,0,0)
dark_orange = (255,140,0)
black = (0, 0, 0)


class K_Comb(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.Txtclr = green
        self.ComboNum = str(P1.atk_comb)
        
        self.Txtclr = black
        self.ComboFont = pygame.font.Font('fonts/atk_comb.ttf', 36)
        self.ComboTxt = self.ComboFont.render('', True, self.Txtclr)
        self.ComboRect = self.ComboTxt.get_rect()
        
        

    def change_color(self, color):
        self.Txtclr = color


    def update_combo(self, cnum):
        self.ComboNum = str(cnum)
        # concatenate Combo and the atk_comb
        text = "Combo " + self.ComboNum
        
        self.ComboTxt = Borderline_Txt(text, self.ComboFont, self.Txtclr, black, 4)
        # check the player frame's orientation
        if P1.orientation == 'left':
            self.ComboRect.center = (P1.pos.x - 70, P1.pos.y - 30)
            self.ComboTxt = pygame.transform.rotate(self.ComboTxt, -45)    
        if P1.orientation == 'right':
            self.ComboRect.center = (P1.pos.x + 70, P1.pos.y - 30)
            self.ComboTxt = pygame.transform.rotate(self.ComboTxt, 45)
        

        screen.blit(self.ComboTxt, self.ComboRect)
        

pygame.font.init()
KuppaCombo = K_Comb()
KuppaCombo.change_color(dark_red)
