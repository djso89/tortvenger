#!/usr/bin/env python3
""" mainMenu module """

import pygame
import sys
from constants import *
from pygame.locals import *
from settings import *
pygame.init()

def drawText(text, font, color, surface, x, y):
    """ draws text onto a surface """
    textObj = font.render(text, 1, color)
    textRect = textObj.get_rect()
    textRect.center = (x, y)
    surface.blit(textObj, textRect)

class MainMenu:
    """ MainMenu class """
    def displayOptions(self):
        """ displays the options on the main menu """
        pygame.display.set_caption('Main Menu')
        info = pygame.display.Info()
        flags = pygame.RESIZABLE
        screen = pygame.display.set_mode((info.current_w, info.current_h),
                                         flags)
        screen.fill(BLACK)
        #pygame.mixer.music.load('sound/titlescreen.ogg')
        #pygame.mixer.music.play(-1)

        font = pygame.font.Font('fonts/Aeronaves.ttf', 100)
        screenWidth = info.current_w
        screenHeight = info.current_h
        drawText('Main Menu', font, WHITE, screen, screenWidth/2, screenHeight/7)
        font = pygame.font.Font('fonts/Aeronaves.ttf', 50)
        drawText('New Game', font, WHITE, screen, screenWidth/2, screenHeight/2)
        drawText('Load Game', font, WHITE, screen, screenWidth/2, screenHeight/2 + 80)
        drawText('Settings', font, WHITE, screen, screenWidth/2, screenHeight/2 + 160)
        drawText('Exit', font, WHITE, screen, screenWidth/2, screenHeight/2 + 240)

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    if info.current_w/2 - 100 <= mouse[0] <= info.current_w/2 + 100 \
                    and info.current_h/2 - 15 <= mouse[1] <= info.current_h/2 +15:
                        print('New Game')
                    elif info.current_w/2 - 100 <= mouse[0] <= info.current_w/2 + 100 \
                    and info.current_h/2+65 <= mouse[1] <= info.current_h/2 +95:
                        print('Load Game')
                    elif info.current_w/2 - 100 <= mouse[0] <= info.current_w/2 + 100 \
                    and info.current_h/2+145 <= mouse[1] <= info.current_h/2 +175:
                        settings = Settings()
                        settings.displayVolumeCtrl(screen, info.current_w, info.current_h)
                    elif info.current_w/2 - 50 <= mouse[0] <= info.current_w/2 + 50 \
                    and info.current_h/2+225 <= mouse[1] <= info.current_h/2 +255:
                        pygame.quit()
                        sys.exit()
            pygame.display.update()
            mouse = pygame.mouse.get_pos()