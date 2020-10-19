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
        self.surf = pygame.Surface((WIDTH, 40))
        self.surf.set_alpha(12)
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect(center = (WIDTH/2, HEIGHT - 20))

    def loadBrick(self, x, y):
        self.surf = pygame.image.load('images/block1.png').convert_alpha()
        self.surf.set_alpha(255)
        self.rect = self.surf.get_rect(center = (x, y))


Ground = Block()
Brick = Block()
Brick.loadBrick(WIDTH - 300, HEIGHT - 400)
platforms = pygame.sprite.Group()
platforms.add(Ground)
platforms.add(Brick)
