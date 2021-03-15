import pygame
from k_action import *
from covid19 import Cells

class K_Battle(K_Act):
    def __init__(self):
        super().__init__()
        self.gotHit = False
        
    def update(self):
        """
        function that calculates position
        and check collision
        """
        
        
        # move along the x direction
        self.acc.x += self.vel.x * FRIC
        self.vel.x += self.acc.x
        self.pos.x += self.vel.x + 0.5 * self.acc.x

        self.touch_cell_X()
        #left Most boundary of stage. Block the player from
        #moving further
        if self.pos.x < 0:
            self.pos.x = 0
        #self.rect.x = self.pos.x

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
        
    def check_dir(self, cell):
        if self.vel.x > 0 and cell.direction == 1:
            # check for intersection area
            if self.rect.right >= cell.rect.left + 55:
                self.pos.x -= 60
                #print("Player facing right and cell facing left")
        if self.vel.x > 0 and cell.direction == 0:
            # check for intersection area
            if self.rect.right >= cell.rect.left + 80:
                self.pos.x -= 100
                #print("Player facing right and cell facing right")
        if self.vel.x < 0 and cell.direction == 0:
            if self.rect.left <= cell.rect.right - 55:
                self.pos.x += 60
                print("touched from left")
        if self.vel.x < 0 and cell.direction == 1:
            if self.rect.left <= cell.rect.right - 80:
                self.pos.x += 100

    def touch_cell_X(self):
        """ detecting collision between player and cells"""
        hitCells = pygame.sprite.spritecollide(self, Cells, False)
        
        for cell in hitCells:
            self.check_dir(cell)
            
        

P1 = K_Battle()