import pygame
from k_action import *
from covid19 import Cells

class K_Battle(K_Act):
    def __init__(self):
        super().__init__()
        
    def update(self):
        """
        function that calculates position
        and check collision
        """
        # move along the x direction
        self.acc.x += self.vel.x * FRIC
        self.vel.x += self.acc.x
        self.pos.x += self.vel.x + 0.5 * self.acc.x

        #left Most boundary of stage. Block the player from
        #moving further
        if self.pos.x < 0:
            self.pos.x = 0
        #self.rect.x = self.pos.x

        if self.pos.x > WIN_W - self.rect.width:
            self.pos.x = WIN_W - self.rect.width
        self.rect.x = self.pos.x

        self.collisionX()
        self.touch_cell_X()

        #moving along the y direction
        self.vel.y += self.acc.y
        self.pos.y += self.vel.y + 0.5 * self.acc.y
        # assign the y coordinate to frame's y
        self.rect.y = self.pos.y

        self.collisionY()
        
    def touch_cell_X(self):
        """ detecting collision between player and cells"""
        hitCells = pygame.sprite.spritecollide(self, Cells, False)
        
        for cell in hitCells:
            if self.vel.x > 0 and cell.direction == 1:
                if self.rect.right >= cell.rect.left + 50:
                    self.pos.x -= 50
                    print("touched from right")
                    cell.direction = 0

            elif self.vel.x < 0:
                print("touched from left")

        

P1 = K_Battle()