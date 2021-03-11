#!/usr/bin/env python3
import pygame
from k_action import KuppaAct, P1
from display import screen



_circle_cache = {}
def _circlepoints(r):
    r = int(round(r))
    if r in _circle_cache:
        return _circle_cache[r]
    x, y, e = r, 0, 1 - r
    _circle_cache[r] = points = []
    while x >= y:
        points.append((x, y))
        y += 1
        if e < 0:
            e += 2 * y - 1
        else:
            x -= 1
            e += 2 * (y - x) - 1
    points += [(y, x) for x, y in points if x > y]
    points += [(-x, y) for x, y in points if x]
    points += [(x, -y) for x, y in points if y]
    points.sort()
    return points
    
    

def Borderline_Txt(text, font, gfcolor=pygame.Color('dodgerblue'), ocolor=(0, 0, 0), opx=2):
    textsurface = font.render(text, True, gfcolor).convert_alpha()
    w = textsurface.get_width() + 2 * opx
    h = font.get_height()

    osurf = pygame.Surface((w, h + 2 * opx)).convert_alpha()
    osurf.fill((0, 0, 0, 0))

    surf = osurf.copy()

    osurf.blit(font.render(text, True, ocolor).convert_alpha(), (0, 0))

    for dx, dy in _circlepoints(opx):
        surf.blit(osurf, (dx + opx, dy + opx))

    surf.blit(textsurface, (opx, opx))
    return surf








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
        self.ComboNum = str(KuppaAct.atk_comb)
        self.cnt_lit = 0 #delay counter 
            
        # Text Layer 1 - Text border color
        self.Txtclr = black
        self.ComboFont = pygame.font.Font('fonts/atk_comb.ttf',48)
        self.ComboTxt = self.ComboFont.render('', True, self.Txtclr)
        self.ComboRect = self.ComboTxt.get_rect()
        
        #Text layer 2 - The text color
        self.Txtclr1 = dark_orange
        self.ComboFont1 = pygame.font.Font('fonts/atk_comb.ttf',36)
        self.ComboTxt1 = self.ComboFont1.render('', True, self.Txtclr1)
        self.ComboRect1 = self.ComboTxt1.get_rect()

    def change_color(self, color):
        self.Txtclr = color
        
    def outline_render(self, ocolor, opx):#(text, font, gfcolor=pygame.Color('dodgerblue'), ocolor=(255, 0, 255), opx=2):
        text = "Combo " + self.ComboNum
        textsurface = self.ComboFont.render(text, True, gfcolor).convert_alpha()
        w = textsurface.get_width() + 2 * opx
        h = font.get_height()

        osurf = pygame.Surface((w, h + 2 * opx)).convert_alpha()
        osurf.fill((0, 0, 0, 0))

        surf = osurf.copy()

        osurf.blit(font.render(text, True, ocolor).convert_alpha(), (0, 0))

        for dx, dy in _circlepoints(opx):
            surf.blit(osurf, (dx + opx, dy + opx))

        surf.blit(textsurface, (opx, opx))
        return surf

    def update_combo(self, cnum):
        self.ComboNum = str(cnum)
        # concatenate Combo and the atk_comb
        text = "Combo " + self.ComboNum
        
        
        # check the player frame's orientation
        if P1.orientation == 'left':
            self.ComboRect.center = (P1.pos.x - 170, P1.pos.y - 30)
            self.ComboTxt = self.ComboFont.render(text, True, self.Txtclr)
            self.ComboTxt = pygame.transform.rotate(self.ComboTxt, -45)
            
            
        if P1.orientation == 'right':
            self.ComboRect.center = (P1.pos.x + 170, P1.pos.y - 30)
            self.ComboTxt = self.ComboFont.render(text, True, self.Txtclr)
            self.ComboTxt = pygame.transform.rotate(self.ComboTxt, 45)
        

        screen.blit(self.ComboTxt, self.ComboRect)
        screen.blit(self.ComboTxt1, self.ComboRect1)
        

pygame.font.init()
KuppaCombo = K_Comb()
KuppaCombo.change_color(dark_red)
