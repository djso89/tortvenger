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
        self.images = pygame.image.load('images/krdy.png').convert_alpha()

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

        # orientation and movement status
        self.orientation = 'right'
        self.jmp = False


    def move(self):
        self.acc = vec(0, 3)

        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_LEFT]:
            self.acc.x = -ACC
            self.orientation = 'left'
        if pressed_keys[K_RIGHT]:
            self.acc.x = ACC
            self.orientation = 'right'



        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc


        if self.pos.x < 0:
            self.pos.x = 0

        self.rect.midtop = self.pos


    def jump(self):
        """ jump action """
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if hits:
            self.vel.y = -45
            self.jmp = True



    def update(self):
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if self.vel.y > 0:
            if hits:
                self.jmp = False
                self.vel.y = 0
                self.pos.y = hits[0].rect.top - self.height - 1
                # print("playerY: {}".format(self.pos.y))
                # print("platTop{} platbottom: {}".format(hits[0].rect.top, hits[0].rect.bottom))


    def reset(self, numWin):
        #frame set up
        self.numImages = numWin

        #rectangle dimension
        self.width = self.images.get_width() / self.numImages
        self.height = self.images.get_height()
        self.rect = self.images.get_rect()



    def animate_once(self, pic, counter):
        """animate just once """
        if (self.cnt >= counter):
            self.cnt = 0
            if (self.cImage >= self.numImages-1):
                self.cImage = self.numImages - 1
            else:
                self.cImage+=1

        self.cnt += 1

        screen.blit(self.images, self.pos,
                    (self.cImage*self.width, 0, self.width, self.height))


    def animate(self, pic, counter):
        """animate the player. The counter is the delay """
        if (self.cnt >= counter):
            self.cnt = 0
            if (self.cImage >= self.numImages-1):
                self.cImage=0
            else:
                self.cImage+=1

        self.cnt += 1
        screen.blit(pic, self.pos,
                (self.cImage*self.width, 0, self.width, self.height))


    def render(self, window):
        """ paste the player object into screen """
        if self.orientation == "right":
            if self.jmp == True:
                self.images = pygame.image.load('images/kjmp.png').convert_alpha()
                self.reset(11)
                if self.cImage == self.numImages - 1:
                    self.images = pygame.image.load('images/krdy.png').convert_alpha()
                    self.reset(2)
                # animation once: changes the cImage per period
                if (self.cnt >= 1):
                    self.cnt = 0
                    if (self.cImage >= self.numImages-1):
                        self.cImage = self.numImages - 1
                    else:
                        # counter the tick
                        screen.blit(self.images, self.pos,
                            (self.cImage*self.width, 0, self.width, self.height))
                        if (self.cImage <= self.numImages - 1):
                            self.cImage+=1
                self.cnt += 1


            self.images = pygame.image.load('images/krdy.png').convert_alpha()
            self.reset(2)
            self.animate(self.images,10)

        if self.orientation == "left":
            if self.jmp == True:
                # load the image
                jmpLPic = pygame.image.load('images/kjmpL.png')
                self.images = jmpLPic.convert_alpha()
                self.reset(11)
                self.animate_once(self.images, 1)

            self.images = pygame.image.load('images/krdy.png').convert_alpha()
            self.reset(2)
            new_images = pygame.transform.flip(self.images, True, False)
            self.animate(new_images, 10)


P1 = Player()
