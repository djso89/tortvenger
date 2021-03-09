#!/usr/bin/env python3
import pygame


class Settings:

    def __init__(self):
        self.screen_width, self.screen_height = 1216, 640
        self.bg_color = (225, 225, 225)
        self.flags = pygame.SCALED
