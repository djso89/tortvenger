#!/usr/bin/env python3
import pygame
from gregg_the_tunisian_tortoise.gregg import *
from covid19 import Cells



class GRG_Battle(Gregg):
    def __init__(self):
        super().__init__()
        self.gotHit = False
        self.show_comb = False
        self.hold_frame = 0
        self.num_cells = 0

    def collisionX(self):
        """check the collision in X direction """
        # touch bricks
        hitB = pygame.sprite.spritecollide(self, Bricks, False)
        self.touchX(hitB)

        #touch Cars
        hitC = pygame.sprite.spritecollide(self, Cars, False)
        self.touchX(hitC)

        # touch Plat
        hitP = pygame.sprite.spritecollide(self, Plats, False)
        self.touchX(hitP)

    def touchX(self, hits):
        #touch hits
        for block in hits:
            if self.vel.x > 0: #moving right
                self.rect.right = block.rect.left
            if self.vel.x < 0: #moving left
                self.rect.left = block.rect.right
            # set the x coordinate
            self.pos.x = self.rect.x


    def update(self):
        """
        function that calculates position
        and check collision
        """
        # move along the x direction
        self.acc.x += self.vel.x * FRIC
        self.vel.x += self.acc.x
        self.pos.x += self.vel.x + 0.5 * self.acc.x


        # routine when player didn't touch cells
        #left Most boundary of stage. Block the player from
        #moving further
        if self.pos.x < 0:
            self.pos.x = 0

        if self.pos.x > WIN_W - self.rect.width:
            self.pos.x = WIN_W - self.rect.width

        self.rect.x = self.pos.x
        self.collisionX()
        #moving along the y direction
        self.vel.y += self.acc.y
        self.pos.y += self.vel.y + 0.5 * self.acc.y
        # assign the y coordinate to frame's y
        self.rect.y = self.pos.y

        self.collisionY()



P1 = GRG_Battle()
