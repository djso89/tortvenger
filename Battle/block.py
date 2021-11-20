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
        self.surf.set_alpha(100)
        self.surf.fill((0, 0, 0))
        self.rect = self.surf.get_rect(topleft = (0, HEIGHT - 20))

    def newBlock(self, x, y, w, h, a):
        self.surf = pygame.Surface((w, h))
        self.surf.set_alpha(a)
        self.surf.fill((0, 0, 0))
        self.rect = self.surf.get_rect(topleft = (x, y))


    def loadBrick(self, x, y, color='brown'):
        if color == 'brown':
            ob = pygame.image.load('images/blocks/block1.png').convert()
        if color == 'grey':
            ob = pygame.image.load('images/blocks/block2.png').convert()
        if color == 'whitegrey':
            ob = pygame.image.load('images/blocks/block3.png').convert()
        self.surf = pygame.Surface([ob.get_width(), ob.get_height()])
        self.surf.blit(ob, (0, 0), (0, 0, ob.get_width(), ob.get_height()))
        #self.surf.set_colorkey((0, 0, 0))
        self.rect = self.surf.get_rect(topleft=(x, y))

    def loadobject(self, x, y, img_path):
        ob = pygame.image.load(img_path)
        self.surf = pygame.Surface([ob.get_width(), ob.get_height()], \
                                   pygame.SRCALPHA, 32).convert_alpha()
        self.surf.blit(ob, (0, 0), (0, 0, ob.get_width(), ob.get_height()))
        self.rect = self.surf.get_rect(topleft=(x, y))


    def expand_brick(self, x, y, col, row, color='brown'):
        if color == 'brown':
            ob = pygame.image.load('images/blocks/block1.png').convert()
        if color == 'grey':
            ob = pygame.image.load('images/blocks/block2.png').convert()
        w = col * ob.get_width()
        h = row * ob.get_height()
        self.surf = pygame.Surface([w, h])
        for i in range(0, col, 1):
            for j in range(0, row, 1):
                self.surf.blit(ob, (i * ob.get_width(), j * ob.get_height()), (0, 0, ob.get_width(), ob.get_height()))
        #self.surf.set_colorkey((0, 0, 0))
        self.rect = self.surf.get_rect(topleft=(x, y))
