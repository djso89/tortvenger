#!/usr/bin/env python3
""" TitleScreen module """

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


class TitleScreen:
    """ titleScreen class """
    def displayTitle(self):
        """ renders the title page onto the user's screen """
        pygame.display.se:t_caption('Tortvenger')
        info = pygame.display.Info()
        flags = pygame.RESIZABLE
        screen = pygame.display.set_mode((info.current_w, info.current_h),
                                         flags)
        pygame.mixer.music.load('sound/titlescreen.ogg')
        pygame.mixer.music.play(-1)

        font = pygame.font.Font('fonts/AmericanTypewriter.ttc', 36)
        bg = pygame.image.load('images/titlemockup.png')
        bg = pygame.transform.scale(bg, (info.current_w, info.current_h))

        settingsButton = pygame.image.load('images/gear.png')
        settingsButton = pygame.transform.scale(settingsButton,
                                                (int(info.current_w/50),
                                                 int(info.current_w/50)))

        screen.blit(bg, (0, 0))
        screen.blit(settingsButton, (info.current_w - 50,
                                     20))
        text = 'press enter to start'
        drawText(text, font, WHITE, screen, info.current_w / 2,
                     info.current_h / 1.25)

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    if info.current_w - 50 <= mouse[0] <= info.current_w - 50 + int(info.current_w/50) \
                    and 20 <= mouse[1] <= info.current_w - 50 + int(info.current_w/50):
                        settings = Settings()
                        settings.displayVolumeCtrl(screen, info.current_w, info.current_h)
                if event.type == KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        screen.fill(BLACK)
                        pygame.mixer.music.stop()
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key == pygame.K_BACKSPACE:
                        title = TitleScreen()
                        title.displayTitle() 

            pygame.display.update()
            mouse = pygame.mouse.get_pos()

title = TitleScreen()
title.displayTitle()