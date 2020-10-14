#!/usr/bin/env python3
import pygame
from display import *

cnt = 0

class Player():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 192
        self.height = 104
        self.velocity = 0
        self.falling = True
        self.onGround = False
        self.images = pygame.image.load('images/krdy.png')
        self.numImages=2
        self.cImage = 0

        self.cnt = 0

    def jump(self):
        if (self.onGround == False):
            return

        self.velocity=8
        self.onGround=False

    def detectCollision(self, x1, y1, w1, h1, x2, y2, w2, h2):
        if (x2+w2 >= x1 >= x2 and y2 + h2 >= y1 >=y2):
            return True
        elif (x2+w2>=x1+w1 >=x2 and y2+h2>=y1>=y2):
            return True
        elif (x2+w2>=x1>=x2 and y2+h2>=y1+h1>=y2):
            return True
        elif (x2+w2>=x1+w1>=x2 and y2+h2>=y1+h1>=y2):
            return True
        else:
            return False

    def update(self, gravity, blocklist):
        if (self.velocity < 0):
            self.falling = True

        collision = False
        blockX, blockY = 0, 0
        for block in blocklist:
            collision = self.detectCollision(self.x, self.y, self.width,
                                             self.height, block.x, block.y,
                                             block.width, block.height)
            if (collision==True):
                blockX = block.x
                blockY = block.y
                break

        if (collision == True):
            if (self.falling == True):
                self.falling = False
                self.onGround = True
                self.velocity = 0
                self.y = blockY - self.height

        if (self.onGround == False):
            self.velocity+=gravity

        self.y -= self.velocity

        if (self.cnt >= 10):
            self.cnt = 0
            if (self.cImage >= self.numImages-1):
                self.cImage=0
            else:
                self.cImage+=1
        self.cnt += 1

    def render(self, window):
        #pygame.draw.rect(window,(0,0,0), (self.x, self.y, self.width, self.height))
        screen.blit(self.images, (self.x, self.y),
                    (self.cImage*self.width, 0, self.width, self.height))
