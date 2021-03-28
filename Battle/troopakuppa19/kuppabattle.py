import pygame
from troopakuppa19.k_action import *
from covid19 import Cells

class K_Battle(K_Act):
    def __init__(self):
        super().__init__()
        self.gotHit = False
        self.show_comb = False


    def touchX(self, hits):
        #touch hits
        for block in hits:
            if self.vel.x > 0: #moving right
                if self.gotHit:
                    self.rect.left = block.rect.right
                else:
                    self.rect.right = block.rect.left
            if self.vel.x < 0: #moving left
                if self.gotHit:
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
        #print("---------------------------------")
    
    def cell_hit_player_xl(self, cell):
        """
        function that checks for collision between
        player facing left and cell when player is not attacking
        """
        if cell.direction == 0:
            if self.pos.x + 80  <= (cell.pos.x + cell.rect.width):
                self.pos.x += 200
                self.gotHit = True
        if cell.direction == 1:
            if cell.pos.x >= (self.pos.x + self.rect.width) - 80:
                self.pos.x -= 100

    def cell_hit_player_xr(self, cell):
        """
        function that checks for collision between player
        facing right and cell when player is not attacking
        """
        if cell.direction == 1:
            if (self.pos.x + self.rect.width - 80) >= cell.pos.x:
                self.pos.x -= 200
                self.gotHit = True
        if cell.direction == 0:
            if self.pos.x + 80 >= (cell.pos.x + cell.rect.width):
                self.pos.x += 100
                
    def player_attack(self, cell,knock_back, combo_knock_back, combo_7):
        """ 
        function that executes cell getting knock_back
        when player attacks cell
        """
        if self.atk_comb < 2:
            self.show_comb = True
            cell.pos.x += knock_back
            cell.hitCell = True
        if self.atk_comb >= 2 and self.frame_atk == (self.atk_comb * 7) - 1:
            self.show_comb = True
            
            if self.atk_comb == 7:
                self.pos.x += combo_7
            cell.pos.x += combo_knock_back
            cell.hitCell = True
        
                
    def player_hit_cell_xl(self, cell):
        """
        function that checks for collision between player
        facing left and cell when player is attacking
        """
        if cell.direction == 0:
            if self.pos_a.x <= (cell.pos.x + cell.rect.width) - 40:
                self.player_attack(cell, -2, -50, -200)
                
        if cell.direction == 1:
            if self.pos_a.x <= (cell.pos.x + cell.rect.width) - 20:
                self.player_attack(cell, -2, -50, -200)
                    
    def player_hit_cell_xr(self, cell):
        """
        function that checks for collision between player
        facing right and cell when player is attacking
        """
        if cell.direction == 1:
            if self.pos_a.x + self.rect_a.width - 40 >= cell.pos.x:
                self.player_attack(cell, 2, 50, 400)
        if cell.direction == 0:
            if self.pos_a.x + self.rect_a.width - 20 >= (cell.pos.x): 
                self.player_attack(cell, 2, 50, 400)
        

    def check_dir_x(self, cell):
        """
        function that checks for player's direction
        and cell's direction for collision
        """
        if self.vel.x > 0:
            if not self.ATK:
                self.cell_hit_player_xr(cell)
            else:
                self.player_hit_cell_xr(cell)
        if self.vel.x < 0:
            if not self.ATK:
                self.cell_hit_player_xl(cell)
            else:
                self.player_hit_cell_xl(cell)
                            
        



P1 = K_Battle()
