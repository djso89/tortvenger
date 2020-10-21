#!/usr/bin/env python3
""" Settings module """

import pygame
import sys
from constants import *
from pygame.locals import *
pygame.init()


def drawText(text, font, color, surface, x, y):
    """ draws text onto a surface """
    textObj = font.render(text, 1, color)
    textRect = textObj.get_rect()
    textRect.center = (x, y)
    surface.blit(textObj, textRect)

class Settings:
    """ Settings class """
    def displayVolumeCtrl(self, surface, screenWidth, screenHeight):
        """ displays the settings menu """
        pygame.display.set_caption('Settings')

        bg = pygame.image.load('images/settings.png')
        bg = pygame.transform.scale(bg, (screenWidth, screenHeight))
        surface.blit(bg, (0, 0))

        font = pygame.font.Font('fonts/Aeronaves.ttf', 100)
        drawText('Settings', font, BLACK, surface, screenWidth/2, screenHeight/7)