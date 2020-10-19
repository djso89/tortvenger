#!/usr/bin/env python3
import pygame
from pygame import *
from pygame.locals import *
from display import *
WIDTH = setting.screen_width
HEIGHT = setting.screen_height

class Block(pygame.sprite.Sprite):
    def __init__(self, w, h):
        super().__init__()
        self.surf = pygame.Surface((w, 40))
        self.surf.set_alpha(12)
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect(center = (w/2, h - 20))



Ground = Block(WIDTH, HEIGHT)
platforms = pygame.sprite.Group()
platforms.add(Ground)
