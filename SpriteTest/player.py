#!/usr/bin/env python3
import pygame
import sys
from pygame.locals import *
from display import *
from block import *
from spritesheet import SpriteSheet

import random

vec = pygame.math.Vector2

ACC = 0.5
FRIC = -0.12


class Player(pygame.sprite.Sprite):

    def __init__(self):
        """ initialize player """
        super().__init__()
        # load the image
        sprite_sheet = SpriteSheet("images/krdy.png")
        sprite_sheetjmp = SpriteSheet("images/kjmp.png")
        ss = sprite_sheet.sprite_sheet
        ss_jmp = sprite_sheetjmp.sprite_sheet


        #frame set up
        self.cnt = 0

        # action frames
        self.ready_r = []
        self.ready_l = []
        self.jmp_l = []
        self.jmp_r = []

        # cut out dimension


        # load all right facing ready images

        for i in range(0, 2, 1):
            self.width = ss.get_width()
            self.height = ss.get_height()
            image = sprite_sheet.get_image(i * self.width/2, 0,
                                           self.width/2, self.height)
            self.ready_r.append(image)


        # load all left facing ready images
        for i in range(0, 2, 1):
            self.width = ss.get_width()
            self.height = ss.get_height()
            image = sprite_sheet.get_image(self.width/2 * i, 0,
                                           self.width/2, self.height)
            image = pygame.transform.flip(image, True, False)
            self.ready_l.append(image)


        # load all the right facing jmp images
        for i in range(0, 11, 1):
            self.width1 = ss_jmp.get_width()
            self.height1 = ss_jmp.get_height()
            image1 = sprite_sheetjmp.get_image(self.width1/11 * i, 0,
                                               self.width1/11, self.height1)
            self.jmp_r.append(image1)

        # load all the left facing jmp images
        for i in range(0, 11, 1):
            width1 = ss_jmp.get_width()
            height1 = ss_jmp.get_height()
            image1 = sprite_sheetjmp.get_image(width1/11 * i, 0,
                                               width1/11, height1)
            image1 = pygame.transform.flip(image1, True, False)
            self.jmp_l.append(image1)


        # set the image the player start with
        self.image = self.ready_r[0]
        self.rect = self.image.get_rect()

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

        #left Most boundary of stage. Block the player from
        #moving further
        if self.pos.x < 0:
            self.pos.x = 0

        self.rect.topleft = self.pos


    def jump(self):
        """ jump action """
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if hits:
            self.vel.y = -45
            self.jmp = True



    def update(self):
        """ check the collisions """
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if self.vel.y > 0:
            if hits:
                self.jmp = False
                self.cnt = 0
                self.vel.y = 0
                self.pos.y = hits[0].rect.top - self.height - 1
                # print("playerY: {}".format(self.pos.y))
                # print("platTop{} platbottom: {}".format(hits[0].rect.top, hits[0].rect.bottom))


    def animate(self):
        """animate the player. """
        if self.orientation == 'right' and self.jmp == False:
            frame = (self.pos.x // 30) % len(self.ready_r)
            print(frame)
            self.image = self.ready_r[int(frame)]
        elif self.orientation == 'left' and self.jmp == False:
            frame = (self.pos.x // 30) % len(self.ready_l)
            self.image = self.ready_l[int(frame)]

        elif self.jmp == True:
            # frame = (self.pos.y // 2) % len(self.jmp_r)
            if (self.cnt >= 10):
                self.cnt = 10
            else:
                self.cnt += 1
            if self.orientation == 'right':
                self.image = self.jmp_r[self.cnt]
            if self.orientation == 'left':
                self.image = self.jmp_l[self.cnt]
    def render(self):
        """ paste the player object into screen """
        screen.blit(self.image, self.pos,
                (0, 0, self.image.get_width(),
                 self.image.get_height()))



Kuppa = pygame.sprite.Group()
P1 = Player()
Kuppa.add(P1)
