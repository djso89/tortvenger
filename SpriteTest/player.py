#!/usr/bin/env python3
import pygame
import sys
from pygame.locals import *
from display import *
from block import *
import random

vec = pygame.math.Vector2

ACC = 0.5
FRIC = -0.12


class Player(pygame.sprite.Sprite):

    def __init__(self):
        """ initialize player """
        super().__init__()
        # load the image
        self.images = pygame.image.load('images/krdy.png')

        #frame set up
        self.numImages = 2
        self.cImage = 0
        self.cnt = 0

        #rectangle dimension
        self.width = self.images.get_width() / self.numImages
        self.height = self.images.get_height()
        self.rect = self.images.get_rect()

        # kinematic factors
        self.pos = vec((300, 350))
        self.vel = vec(0,0)
        self.acc = vec(0, 0)


    def move(self):
        self.acc = vec(0, 0.5)

        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_LEFT]:
            self.acc.x = -ACC
        if pressed_keys[K_RIGHT]:
            self.acc.x = ACC

        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        self.rect.midtop = self.pos
        #self.rect.midbottom = self.pos + (0, self.height)

    def jump(self):
        """ jump action """
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if hits:
            self.vel.y = -15



    def update(self):
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if self.vel.y > 0:
            if hits:
                self.vel.y = 0
                self.pos.y = hits[0].rect.top - self.height - 1
                # print("playerY: {}".format(self.pos.y))
                # print("platTop{} platbottom: {}".format(hits[0].rect.top, hits[0].rect.bottom))




    def render(self, window):
        """ paste the player object into screen """
        screen.blit(self.images, (self.pos.x, self.pos.y),
                    (self.cImage*self.width, 0, self.width, self.height))

        # animation loop: each counter (cnt) is equivalent to (1/FPS) seconds
        if (self.cnt >= 10):
            self.cnt = 0
            if (self.cImage >= self.numImages-1):
                self.cImage=0
            else:
                self.cImage+=1
        self.cnt += 1

P1 = Player()
