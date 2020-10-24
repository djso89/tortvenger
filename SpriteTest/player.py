#!/usr/bin/env python3
import pygame
import sys
from pygame.locals import *
from display import *
from block import *
from spritesheet import SpriteSheet
from collections import namedtuple
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
            width = ss.get_width()
            height = ss.get_height()
            image = sprite_sheet.get_image(i * width/2, 0,
                                           width/2, height)
            self.ready_r.append(image)


        # load all left facing ready images
        for i in range(0, 2, 1):
            width = ss.get_width()
            height = ss.get_height()
            image = sprite_sheet.get_image(width/2 * i, 0,
                                           width/2, height)
            image = pygame.transform.flip(image, True, False)
            self.ready_l.append(image)


        # load all the right facing jmp images
        for i in range(0, 11, 1):
            width1 = ss_jmp.get_width()
            height1 = ss_jmp.get_height()
            image1 = sprite_sheetjmp.get_image(width1/11 * i, 0,
                                               width1/11, height1)
            self.jmp_r.append(image1)

        # load all the left facing jmp images
        for i in range(0, 11, 1):
            width1 = ss_jmp.get_width()
            height1 = ss_jmp.get_height()
            image1 = sprite_sheetjmp.get_image(width1/11 * i, 0,
                                               width1/11, height1)
            image1 = pygame.transform.flip(image1, True, False)
            self.jmp_l.append(image1)

        # kinematic factors
        self.pos = vec((0, 350))
        self.vel = vec(0,0)
        self.acc = vec(0, 0)

        # set the image the player start with
        self.image = self.ready_r[0]
        self.rect = self.image.get_rect()

        # orientation and movement status
        self.orientation = 'right'
        self.jmp = True


    def move(self):
        self.acc = vec(0, 3)
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT]:
            self.acc.x = -ACC
            self.orientation = 'left'
        if pressed_keys[K_RIGHT]:
            self.acc.x = ACC
            self.orientation = 'right'


    def jump(self):
        """ jump action """
        if self.jmp == True:
            self.vel.y = -45
            self.jmp = False
#            self.cnt = 0



    def update(self):
        # move along the x direction
        self.acc.x += self.vel.x * FRIC
        self.vel.x += self.acc.x
        self.pos.x += self.vel.x + 0.5 * self.acc.x

        #left Most boundary of stage. Block the player from
        #moving further
        if self.pos.x < 0:
            self.pos.x = 0
        self.rect.x = self.pos.x

        #moving along the y direction
        self.vel.y += self.acc.y
        self.pos.y += self.vel.y + 0.5 * self.acc.y


        self.rect.y = self.pos.y

        """ check the collisions """
        hits = pygame.sprite.spritecollide(self, platforms, False)
        for block in hits:
            if self.vel.y > 0:
                self.jmp = True
                self.cnt = 0
                self.vel.y = 0
                self.pos.y = block.rect.top - self.rect.height - 1





    def ani_move(self):
        """ animate the left right movement"""
        if self.orientation == 'right' and self.jmp == True:
            frame = (self.pos.x // 30) % len(self.ready_r)
            self.image = self.ready_r[int(frame)]
        elif self.orientation == 'left' and self.jmp == True:
            frame = (self.pos.x // 30) % len(self.ready_l)
            self.image = self.ready_l[int(frame)]


    def ani_jump(self):
        """ animate the jump """
        if self.jmp == False:
            if (self.cnt >= 10):
                self.cnt = 10
            else:
                self.cnt += 1
            if self.orientation == 'right':
                self.image = self.jmp_r[self.cnt]
            if self.orientation == 'left':
                self.image = self.jmp_l[self.cnt]


    def animate(self):
        """animate the player. """
        self.ani_move()
        self.ani_jump()

    def render(self):
        """ paste the player object into screen """
        screen.blit(self.image, self.pos,
                (0, 0, self.image.get_width(),
                 self.image.get_height()))



Kuppa = pygame.sprite.Group()
P1 = Player()
Kuppa.add(P1)
