#!/usr/bin/env python3
import pygame
from pygame import *
from pygame.locals import *
from display import *
WIDTH = setting.screen_width
HEIGHT = setting.screen_height

class Block(pygame.sprite.Sprite):
    def __init__(self):
        """initialize the block. By default,
        the ground is established """
        super().__init__()
        self.surf = pygame.Surface((WIDTH, 20))
        self.surf.set_alpha(17)
        self.surf.fill((0, 0, 0))
        self.rect = self.surf.get_rect(center = (WIDTH/2, HEIGHT - 10))

    def newBlock(self, x, y, w, h, a):
        self.surf = pygame.Surface((w, h))
        self.surf.set_alpha(a)
        self.surf.fill((0, 0, 0))
        self.rect = self.surf.get_rect(topleft = (x, y))


    def loadBrick(self, x, y):
        self.surf = pygame.image.load('images/block1.png').convert()
        self.surf.set_alpha(190)
        self.rect = self.surf.get_rect(topleft=(x, y))
