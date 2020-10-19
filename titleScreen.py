#!/usr/bin/env python3

import pygame
import sys
from pygame.locals import *
pygame.init()


black = 0, 0, 0
white = 255, 255, 255


def drawText(text, font, color, surface, x, y):
    """draws text onto a surface"""
    textObj = font.render(text, 1, white)
    textRect = textObj.get_rect()
    textRect.center = (x, y)
    surface.blit(textObj, textRect)


class titleScreen:
    """ titleScreen class"""
    def displayTitle(self):
        """ renders the title page onto the user's screen"""
        while True:
            pygame.display.set_caption('Tortvenger')
            info = pygame.display.Info()
            flags = pygame.RESIZABLE
            screen = pygame.display.set_mode((info.current_w, info.current_h),
                                             flags)

            font = pygame.font.Font('AmericanTypewriter.ttc', 36)
            bg = pygame.image.load('titlemockup.png')
            bg = pygame.transform.scale(bg, (info.current_w, info.current_h))

            screen.blit(bg, (0, 0))
            text = 'press any key to start'
            drawText(text, font, white, screen, info.current_w / 2,
                     info.current_h / 1.25)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    screen.fill(black)

            pygame.display.update()

title = titleScreen()
title.displayTitle()
