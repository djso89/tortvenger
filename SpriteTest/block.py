#!/usr/bin/env python3
import pygame
from pygame import *
from pygame.locals import *
from display import *


class Block(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((setting.screen_width, 40))
        self.surf.set_alpha(12)
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect(center = (setting.screen_width/2,
                                                 setting.screen_height - 20))



PT1 = Block()
platforms = pygame.sprite.Group()
platforms.add(PT1)
