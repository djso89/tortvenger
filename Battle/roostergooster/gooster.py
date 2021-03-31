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


    def loadimages(self):
        """ load all the kuppa action frames """
        sprite_sheet = SpriteSheet("images/gst_rdy.png", black)
        #sprite_sheet_envk = SpriteSheet("images/gst_env_k.png", black)

        ss = sprite_sheet.sprite_sheet
        #ss_envk = sprite_sheet_envk.sprite_sheet

        # load all right facing ready images
        for i in range(0, 2, 1):
            width = ss.get_width()
            height = ss.get_height()
            image = sprite_sheet.get_image(i * width / 2, 0,
                                           width / 2, height)
            self.ready_r.append(image)
            image = pygame.transform.flip(image, True, False)
            self.ready_l.append(image)



    def __init__(self):
        """ initialize player """
        super().__init__()

        #counter for animating jumping
        self.cnt = 0

        # action frames
        self.ready_r = []
        self.ready_l = []
        self.jmp_l = []
        self.jmp_r = []

        # load the image
        self.loadimages()


        # kinematic factors
        self.pos = vec((0, 0))
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

        # set the image the player start with
        self.image = self.ready_r[0]
        self.rect = self.image.get_rect(topleft=self.pos)

        # orientation and movement status
        self.orientation = 'right'
        self.OnGround = True
        

        
    def get_rect(self):
        return self.image.get_rect()
        



    def move(self):
        """
        player move function
        this just simply sets acceleration
        according to the key presses
        """
        self.acc = vec(0, 2.5)
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT]:
            self.acc.x = -ACC
            self.orientation = 'left'
        if pressed_keys[K_RIGHT]:
            self.acc.x = ACC
            self.orientation = 'right'

    def jump(self):
        """ jump action """
        if self.OnGround == True:
            self.vel.y = -25
            self.OnGround = False
            
    # def update(self):
        # """
        # function that calculates position
        # and check collision
        # """
        # # move along the x direction
        # self.acc.x += self.vel.x * FRIC
        # self.vel.x += self.acc.x
        # self.pos.x += self.vel.x + 0.5 * self.acc.x

        # #left Most boundary of stage. Block the player from
        # #moving further
        # if self.pos.x < 0:
            # self.pos.x = 0

        # if self.pos.x > WIN_W - self.rect.width:
            # self.pos.x = WIN_W - self.rect.width

        # self.rect.x = self.pos.x
        # self.collisionX()
        # #moving along the y direction
        # self.vel.y += self.acc.y
        # self.pos.y += self.vel.y + 0.5 * self.acc.y
        # # assign the y coordinate to frame's y
        # self.rect.y = self.pos.y

        # self.collisionY()
        
    # def touchX(self, hits):
        # #touch hits
        # for block in hits:
            # if self.vel.x > 0: #moving right
                # self.rect.right = block.rect.left
            # if self.vel.x < 0: #moving left
                # self.rect.left = block.rect.right
            # # set the x coordinate
            # self.pos.x = self.rect.x
            
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
                self.cnt = 0
                self.vel.y = 0
                self.rect.bottom = block.rect.top
            elif self.vel.y < 0:
                self.rect.top = block.rect.bottom
                self.vel.y = 0
            self.pos.y = self.rect.y

    def touchYU(self, hits):
        """ check just for falling direction """
        for block in hits:
            if self.vel.y > 0:
                self.OnGround = True
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
            frame = (self.pos.x // 30) % len(self.ready_r)
            self.image = self.ready_r[int(frame)]


        elif self.orientation == 'left' and self.OnGround == True:
            frame = (self.pos.x // 30) % len(self.ready_l)
            self.image = self.ready_l[int(frame)]
    
    

            


    # def ani_jump(self):
        # """ animate the jump """
        # period = 2
        # if self.OnGround == False:
            # if (self.cnt >= period * (len(self.OnGround_r) -1 )):
                # self.cnt = period * (len(self.OnGround_r) -1 )
            # else:
                # self.cnt += 1
            # if self.orientation == 'right':
                # self.image = self.OnGround_r[self.cnt//period]
            # if self.orientation == 'left':
                # self.image = self.OnGround_l[self.cnt//period]




