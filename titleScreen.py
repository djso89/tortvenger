#!/usr/bin/env python3
""" titleScreen module """

import pygame
import sys
from constants import *
from pygame.locals import *
pygame.init()


def drawText(text, font, color, surface, x, y):
    """ draws text onto a surface """
    textObj = font.render(text, 1, WHITE)
    textRect = textObj.get_rect()
    textRect.center = (x, y)
    surface.blit(textObj, textRect)


class TitleScreen:
    """ titleScreen class """
    def displayTitle(self):
        """ renders the title page onto the user's screen """
        while True:
            pygame.display.set_caption('Tortvenger')
            pygame.mixer.music.load('sound/titlescreen.ogg')
            pygame.mixer.music.play(-1)
            info = pygame.display.Info()
            flags = pygame.RESIZABLE
            screen = pygame.display.set_mode((info.current_w, info.current_h),
                                             flags)

            font = pygame.font.Font('AmericanTypewriter.ttc', 36)
            bg = pygame.image.load('titlemockup.png')
            bg = pygame.transform.scale(bg, (info.current_w, info.current_h))

            settingsButton = pygame.image.load('images/gear.png')
            settingsButton = pygame.transform.scale(settingsButton,
                                                    (int(info.current_w/50),
                                                     int(info.current_w/50)))

            screen.blit(bg, (0, 0))
            screen.blit(settingsButton, (info.current_w - 50,
                                         info.current_h - 50))
            text = 'press any key to start'
            drawText(text, font, WHITE, screen, info.current_w / 2,
                     info.current_h / 1.25)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    if info.current_w - 50 <= mouse[0] <= info.current_w - 50 + int(info.current_w/50) \
                    and info.current_h - 50 <= mouse[1] <= info.current_w - 50 + int(info.current_w/50):
                        pygame.quit()
                        sys.exit()
                if event.type == KEYDOWN:
                    screen.fill(BLACK)

            pygame.display.update()
            mouse = pygame.mouse.get_pos()

title = TitleScreen()
title.displayTitle()
