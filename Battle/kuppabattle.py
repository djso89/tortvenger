import pygame
from k_action import *
from covid19 import Cells

class K_Battle(K_Act):
    def __init__(self):
        super().__init__()
        
        self.gotHit = False
        self.gotHitBack = False
        

    def touchX(self, hits):
        #touch hits
        for block in hits:
            if self.vel.x > 0: #moving right
                self.rect.right = block.rect.left
                

            elif self.vel.x < 0:
                if self.gotHit:
                    self.rect.right = block.rect.left
                else:
                    self.rect.left = block.rect.right
            # reset the gotHit flag
            self.gotHit = False
            self.gotHitBack = False
            # set the x coordinate
            self.pos.x = self.rect.x



    def collisionX(self):
        """check the collision in X direction """
        # touch bricks
        hitB = pygame.sprite.spritecollide(self, Bricks, False)
        self.touchX(hitB)

        #touch Cars
        hitC = pygame.sprite.spritecollide(self, Cars, False)
        self.touchX(hitC)
        
        
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
        
    def check_dir_x(self, cell):
        """
        function that checks for player's direction
        and cell's direction for collision
        """
        Bounds = pygame.sprite.Group()
        Bounds.add(Bricks)
        Bounds.add(Cars)
        
        hitBounds = pygame.sprite.spritecollide(self, Bounds, False)
        # player facing right direction
        if self.vel.x > 0 and cell.direction == 1:
            # check for intersection area
            if self.rect.right >= cell.rect.left + 20:
                self.pos.x -= 40
                self.gotHit = True
                if self.pos.x < 0:
                    self.pos.x = 0
        # Player facing right and cell facing right
        if self.vel.x > 0 and cell.direction == 0:
            if self.pos.x > cell.pos.x:
                if self.rect.left <= cell.rect.right + 20:
                    self.gotHitBack = True
                    self.pos.x += 40
                    if self.pos.x > WIN_W - self.rect.width:
                        self.pos.x = WIN_W - self.rect.width
            else:
                # check for intersection area
                if self.rect.right >= cell.rect.left + 20:
                    self.gotHit = True
                    self.pos.x -= 40
                    if self.pos.x < 0:
                        self.pos.x = 0
                #print("")
        if self.vel.x < 0 and cell.direction == 0:
            if self.rect.left <= cell.rect.right - 20:
                self.gotHit = True
                self.pos.x += 40
                if self.pos.x > WIN_W - self.rect.width:
                    self.pos.x = WIN_W - self.rect.width
                #print("touched from left")
        if self.vel.x < 0 and cell.direction == 1:
            if self.pos.x < cell.pos.x:
                self.gotHitBack = True
                if self.rect.right >= cell.rect.left - 20:
                    self.pos.x -= 40
                    if self.pos.x < 0:
                        self.pos.x = 0
            else:
                if self.rect.left <= cell.rect.right - 20: 
                    self.pos.x += 40
                    self.gotHit = True
                    if self.pos.x > WIN_W - self.rect.width:
                        self.pos.x = WIN_W - self.rect.width
            

    def touch_cell_X(self):
        """ detecting collision between player and cells"""
        hitCells = pygame.sprite.spritecollide(self, Cells, False)
        
        
        
        for cell in hitCells:
            #self.gotHit = True
            self.check_dir_x(cell)
            #break
        
        #self.gotHit = False
        

P1 = K_Battle()