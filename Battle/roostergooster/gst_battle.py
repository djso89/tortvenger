import pygame
from covid19 import Cells
from roostergooster.gst_action import *
from roostergooster.expkage import expk_bullets
from roostergooster.envkunai import envk_bullets
from goostergauge import goosterinfo

class GST_Battle(GST_Act):
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

        hitP = pygame.sprite.spritecollide(self, Plats, False)
        self.touchX(hitP)

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
        self.envk_hit_cell()
        self.expk_hit_cell()
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

    def cell_do_dmg_x(self, cell, knock_back):
        goosterinfo.hit_hp(cell.get_dmg(goosterinfo.defense, goosterinfo.luck))
        self.pos.x += knock_back
        self.cell_atk_g = True
        goosterinfo.update_bar = True

    def cell_hit_player_xl(self, cell):
        """
        function that checks for collision between
        player facing left and cell when player is not attacking
        """
        if cell.direction == 0:
            if self.pos.x  <= (cell.pos.x + cell.rect.width) - 20:
                if not self.dmg_blinking:
                    self.cell_do_dmg_x(cell, 200)
                    self.gotHit = True
        if cell.direction == 1:
            if cell.pos.x >= (self.pos.x + self.rect.width) - 20:
                self.pos.x -= 100
                self.cell_atk_g = True

    def cell_hit_player_xr(self, cell):
        """
        function that checks for collision between player
        facing right and cell when player is not attacking
        """
        if cell.direction == 1:
            if (self.pos.x + self.rect.width - 20) >= cell.pos.x:
                self.pos.x -= 200
                self.gotHit = True
        if cell.direction == 0:
            if self.pos.x + 20 >= (cell.pos.x + cell.rect.width):
                self.pos.x += 100


    def envk_hit_cell(self):
        """
        function that checks collision between
        envelope kunai bullets and cells
        """
        for bullet in envk_bullets:
            hitCells = pygame.sprite.spritecollide(bullet, Cells, False)
            for cell in hitCells:
                bullet.hitlanded = True
                cell.hitCell_envk = True
                if bullet.orientation == 'right' and cell.direction == 0:
                    cell.pos.x += 20
                if bullet.orientation == 'right' and cell.direction == 1:
                    cell.pos.x += 20
                if bullet.orientation == 'left' and cell.direction == 0:
                    cell.pos.x -= 20
                if bullet.orientation == 'left' and cell.direction == 1:
                    cell.pos.x -= 20

    def expk_hit_cell(self):
        for bullet in expk_bullets:
            hitCells = pygame.sprite.spritecollide(bullet, Cells, False)
            for cell in hitCells:
                bullet.hitlanded = True
                cell.hitCell_expk = True
                if bullet.orientation == 'right' and cell.direction == 0:
                    cell.pos.x += 200
                if bullet.orientation == 'right' and cell.direction == 1:
                    cell.pos.x += 200
                if bullet.orientation == 'left' and cell.direction == 0:
                    cell.pos.x -= 200
                if bullet.orientation == 'left' and cell.direction == 1:
                    cell.pos.x -= 200


    def check_dir_x(self, cell):
        """
        function that checks for player's direction
        and cell's direction for collision
        """
        if self.vel.x > 0:
            self.cell_hit_player_xr(cell)
        if self.vel.x < 0:
            self.cell_hit_player_xl(cell)




P1 = GST_Battle()
