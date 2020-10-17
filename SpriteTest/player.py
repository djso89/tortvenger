#!/usr/bin/env python3
import pygame
import sys
from pygame.locals import *
from display import *
from block import *
import random

vec = pygame.math.Vector2

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.pos = vec((x, y))
        #        self.width = 192
        #        self.height = 104
        self.velocity = vec(0,0)
        self.acceleration = vec(0, 0)
        self.jumping = False
        self.images = pygame.image.load('images/krdy.png')
        self.numImages=2
        self.cImage = 0
        self.cnt = 0

    def jump(self):
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if hits and (self.jumping == False):
            self.velocity.y = -8
            self.jumping=True

    def cancel_jump(self):
        if self.jumping:
            if self.vel.y < -3:
                self.vel.y = -3


    def update(self):
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if self.vel.y > 0:
            if hits:
                if self.pos.y < hits[0].rect.bottom:
                    self.pos.y = hits[0].rect.top + 1
                    self.velocity.y = 0
                    self.jumping = False


        if (self.cnt >= 10):
            self.cnt = 0
            if (self.cImage >= self.numImages-1):
                self.cImage=0
            else:
                self.cImage+=1
        self.cnt += 1

    def render(self, window):
        #pygame.draw.rect(window,(0,0,0), (self.x, self.y, self.width, self.height))
        screen.blit(self.images, (self.pos.x, self.pos.y),
                    (self.cImage*self.width, 0, self.width, self.height))
