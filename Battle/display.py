#!/usr/bin/python3
""" display module """
import pygame
from settings import *
vec = pygame.math.Vector2

ACC = 0.5
FRIC = -0.12

setting = Settings()
setting.flags = pygame.SCALED #| pygame.FULLSCREEN
screen = pygame.display.set_mode((setting.screen_width, setting.screen_height), 
    setting.flags)
