#!/usr/bin/env python3
import pygame
import sys
from pygame.locals import *
from display import *
from stage import *
from spritesheet import SpriteSheet



green = (0, 255, 0)
black = (0, 0, 0)
class Gooster(pygame.sprite.Sprite):
    """Gooster Class """
    def loadimages(self):
        """ load all the kuppa action frames """
        sprite_sheet = SpriteSheet("images/gst_rdy.png", black)
        #sprite_sheet_envk = SpriteSheet("images/gst_env_k.png", black)
        sprite_sheet_flap = SpriteSheet('images/gst_flap.png')

        ss = sprite_sheet.sprite_sheet
        ss_flap = sprite_sheet_flap.sprite_sheet
        #ss_envk = sprite_sheet_envk.sprite_sheet

        # load all right facing ready images
        for i in range(0, 2, 1):
            width = ss.get_width()
            height = ss.get_height()
            image = sprite_sheet.get_image(i * width / 2, 0,
                                           width / 2, height)
            image.set_colorkey((0, 0, 0))
            self.ready_r.append(image)
            image = pygame.transform.flip(image, True, False)
            image.set_colorkey((0, 0, 0))
            self.ready_l.append(image)

        # load all right facing ready images
        for i in range(0, 4, 1):
            width = ss_flap.get_width()
            height = ss_flap.get_height()
            image = sprite_sheet_flap.get_image(i * width / 4, 0,
                                           width / 4, height)
            image.set_colorkey((0, 0, 0))
            self.flap_r.append(image)
            image = pygame.transform.flip(image, True, False)
            image.set_colorkey((0, 0, 0))
            self.flap_l.append(image)



    def __init__(self):
        """ initialize player """
        super().__init__()

        # counter for animating jumping
        self.cnt = 0
        self.num_jmp = 0
        # counter for damage blinking
        self.cnt_dmg = 0

        # action frames
        self.ready_r = []
        self.ready_l = []
        self.flap_l = []
        self.flap_r = []

        # load the image
        self.loadimages()


        # kinematic factors
        self.steps = 0
        self.pos = vec((0, 0))
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

        # set the image the player start with
        self.image = self.ready_r[0]
        self.rect = self.image.get_rect(topleft=self.pos)

        # orientation and movement status
        self.orientation = 'right'
        self.OnGround = True
        self.go_flap = False

        # cell attack and damage blinking
        self.cell_atk_g = False
        self.dmg_blinking = False
        self.n_blinks = 0


    def get_rect(self):
        return self.image.get_rect()

    def no_atk_dmg_blink(self):
        period = 2
        if self.cell_atk_g:
            if self.cnt_dmg >= period:
                self.image = Surface((self.rect.width, self.rect.height),\
                                     flags = SRCALPHA)
                self.image.fill((0, 0, 0, 0))
                self.dmg_blinking = True
                self.cnt_dmg = 0
                if self.n_blinks == 15:
                    self.cell_atk_g = False
                    self.dmg_blinking = False
                    self.n_blinks = 0
                else:
                    self.n_blinks += 1
            else:
                self.cnt_dmg += 1



    def move(self):
        """
        player move function
        this just simply sets acceleration
        according to the key presses
        """
        self.acc = vec(0, 2)
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT]:
            self.acc.x = -ACC
            self.orientation = 'left'
            self.steps += 1
        if pressed_keys[K_RIGHT]:
            self.acc.x = ACC
            self.orientation = 'right'
            self.steps += 1

    def jump(self):
        """ jump action """
        if self.OnGround == True:
            self.num_jmp += 1
            if self.num_jmp <= 7:
                self.vel.y = -20
                self.go_flap = True
            else:
                self.num_jmp = 0
                self.OnGround = False
                self.go_flap = False
        #    self.OnGround = False

    # gooster touching the stage objects
    def touchXR(self, hits):
        #touch hits coming from right side
        for block in hits:
            if self.vel.x > 0:
                self.rect.right = block.rect.left
            self.pos.x = self.rect.x

    def touchXL(self, hits):
        #touch hits coming from left side
        for block in hits:
            if self.vel.x < 0:
                self.rect.left = block.rect.right
            self.pos.x = self.rect.x


    def touchYUD(self, hits):
        """ go through the list of collided sprites
        in Y direction"""
        for block in hits:
            if self.vel.y > 0:
                self.OnGround = True
                self.go_flap = False
                self.cnt = 0
                self.vel.y = 0
                self.rect.bottom = block.rect.top
            elif self.vel.y < 0:
                self.rect.top = block.rect.bottom
                self.vel.y = 0
                self.cnt = 0
                self.go_flap = False
            self.pos.y = self.rect.y

    def touchYU(self, hits):
        """ check just for falling direction """
        for block in hits:
            if self.vel.y > 0:
                self.OnGround = True
                self.go_flap = False
                self.cnt = 0
                self.vel.y = 0
                self.rect.bottom = block.rect.top
            self.pos.y = self.rect.y




    def collisionY(self):

        """ check the collision in Y direction """

        #touch ground platforms
        hits = pygame.sprite.spritecollide(self, platforms, False)
        self.touchYU(hits)

        #touch Cars
        hitC = pygame.sprite.spritecollide(self, Cars, False)
        self.touchYUD(hitC)

        # touch Bricks
        hitB = pygame.sprite.spritecollide(self, Bricks, False)
        self.touchYUD(hitB)

        #touch Plats
        hitP = pygame.sprite.spritecollide(self, Plats, False)
        self.touchYUD(hitP)

        #touch Bldgs
        hitBldg = pygame.sprite.spritecollide(self, Bldgs, False)
        self.touchYUD(hitBldg)

        #touch Steps
        hitSt = pygame.sprite.spritecollide(self, Steps, False)
        self.touchYUD(hitSt)


    """ animation functions """


    def ani_move(self):
        """ animate the left right movement"""
        if self.orientation == 'right' and self.OnGround == True:
            frame = (self.steps // 10) % len(self.ready_r)
            self.image = self.ready_r[int(frame)]


        elif self.orientation == 'left' and self.OnGround == True:
            frame = (self.steps // 10) % len(self.ready_l)
            self.image = self.ready_l[int(frame)]

    def ani_flap(self):
        period = 4
        if self.go_flap:
            if (self.cnt >= period * len(self.flap_r)):
                self.cnt = 0
                self.go_flap = False
            else:
                if self.orientation == 'right':
                    self.image = self.flap_r[self.cnt // period]
                if self.orientation == 'left':
                    self.image = self.flap_l[self.cnt // period]
                self.cnt += 1
        else:
            self.cnt = 0
