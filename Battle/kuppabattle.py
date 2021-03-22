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
                if self.gotHit:
                    self.rect.left = block.rect.right
                else:
                    self.rect.right = block.rect.left
            if self.vel.x < 0:
                if self.gotHit:
                    print("here")
                    self.rect.right = block.rect.left
                else:
                    self.rect.left = block.rect.right
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

    def gotHit_reset(self):
        # reset gotHit flag
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
        
        # routine when player didn't touch cells
        #left Most boundary of stage. Block the player from
        #moving further
        if self.pos.x < 0:
            self.pos.x = 0

        if self.pos.x > WIN_W - self.rect.width:
            self.pos.x = WIN_W - self.rect.width

        self.rect.x = self.pos.x
        self.collisionX()
        self.gotHit_reset()
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
            #print("made contact with cell")
            self.check_dir_x(cell)
        print("---------------------------------")
    

    
    def check_dir_x(self, cell):
        """
        function that checks for player's direction
        and cell's direction for collision
        """
        if self.vel.x < 0:
            if not self.ATK:
                if cell.direction == 0:
                    #print("player facing left and cell facing right")
                    if self.pos.x + 40  <= (cell.pos.x + cell.rect.width):
                        self.pos.x += 200
                        self.gotHit = True
                if cell.direction == 1:
                    #print("player facing left and cell facing left")
                    if cell.pos.x >= (self.pos.x + self.rect.width) - 40:
                        self.pos.x -= 100
                        #print("bam")
            else:
                if self.frame_atk == (self.atk_comb * 7) - 1:
                    cell.hitCell = True
                    print("cell got hit")
                    print("Combo#: {} frame attack: {}".format(self.atk_comb, self.frame_atk))
        if self.vel.x > 0:
            if cell.direction == 1:
                if cell.pos.x >= (self.pos.x + self.rect.width) - 40:
                    self.pos.x -= 200
                    self.gotHit = True
            if cell.direction == 0:
                if self.pos.x + 40 >= (cell.pos.x + cell.rect.width):
                    self.pos.x += 100



P1 = K_Battle()
