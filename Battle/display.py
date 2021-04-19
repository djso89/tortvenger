#!/usr/bin/python3
""" display module """
import pygame
from settings import *
vec = pygame.math.Vector2

setting = Settings()

ACC = 0.6
FRIC = -0.12
FPS = 70

WIN_W = setting.screen_width
WIN_H = setting.screen_height


setting.flags = pygame.SCALED | pygame.RESIZABLE
screen = pygame.display.set_mode((WIN_W, WIN_H),
    setting.flags)
