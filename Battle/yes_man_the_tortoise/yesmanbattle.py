import pygame
from yes_man_the_tortoise.yesman import *
from covid19 import Cells



class YM_Battle(Yesman):
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

    def touch_cell_X(self):
        """ detecting collision between player and cells"""
        hitCells = pygame.sprite.spritecollide(self, Cells, False)
        for cell in hitCells:
            self.num_cells += 1
            self.check_dir_x(cell)
            if self.slash_number <= 3:
                break
        self.num_cells = 0



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


    def gotHit_reset(self):
        # reset gotHit flag
        self.gotHit = False



    def cell_do_dmg_x(self, cell, knock_back):
         Yesmaninfo.hit_hp(cell.get_dmg(Yesmaninfo.defense, Yesmaninfo.luck))
         self.pos.x += knock_back
         self.cell_atk_k = True
         Yesmaninfo.update_bar = True



    def cell_hit_player_xl(self, cell):
        """
        function that checks for collision between
        player facing left and cell when player is not attacking
        """
        if cell.direction == 0: # cell direction right
            if self.pos.x + 1  <= (cell.pos.x + cell.rect.width):
                if not self.dmg_blinking:
                    self.cell_do_dmg_x(cell, 200)
                    self.gotHit = True
        if cell.direction == 1:  # cell direction left
            if self.pos.x < cell.pos.x: # the cell is behind the player
                if cell.pos.x <= (self.pos.x + self.rect.width) - 1:
                    if not self.dmg_blinking:
                        self.cell_do_dmg_x(cell, -100)
            else: # the cell is front of the player
                if self.pos.x <= (cell.pos.x + cell.rect.width - 1):
                    if not self.dmg_blinking:
                        self.cell_do_dmg_x(cell, 100)
                        self.gotHit = True


    def cell_hit_player_xr(self, cell):
        """
        function that checks for collision between player
        facing right and cell when player is not attacking
        """
        if cell.direction == 1:
            if (self.pos.x + self.rect.width - 1) >= cell.pos.x:
                if not self.dmg_blinking:
                    self.cell_do_dmg_x(cell, -200)
                    self.gotHit = True
        if cell.direction == 0:
            if self.pos.x > cell.pos.x:
                if self.pos.x + 1 <= (cell.pos.x + cell.rect.width):
                    if not self.dmg_blinking:
                        self.cell_do_dmg_x(cell, 100)
            else:
                if self.pos.x + self.rect.width >= cell.pos.x + 1:
                    if not self.dmg_blinking:
                        self.cell_do_dmg_x(cell, -100)
                        self.gotHit = True


    def player_dmg(self, cell, knock_back):
        """player damage function """
        combo_dmg = round((self.slash_number / 3) * Yesmaninfo.get_dmg(cell.defense, cell.luck))
        print("go atk: {}".format(self.go_hit))
        print("slash#: {} dmg: {}".format(self.slash_number, combo_dmg))
        cell.hit_hp(combo_dmg)
        cell.pos.x += knock_back
        cell.hitCell = True
        cell.update_hp()
        cell.show_hp = True
        print('------------------------')

    def player_attack(self, cell, combo_knock_back):
        """
        function that executes cell getting knock_back
        when player attacks cell
        """
        if not self.dmg_blinking:
            if self.go_hit:
                print(self.get_cut_frame_period(self.slash_number))
                if self.cnt_hold == self.get_cut_frame_period(self.slash_number):
                    self.player_dmg(cell, combo_knock_back)
                    self.show_comb = True


    def player_combo_routine_xl(self, cell):
        """this is where how cells will be attacked from
        combo 1 through 9 when player is facing left"""
        if cell.direction == 0:
            if self.pos_a.x <= (cell.pos.x + cell.rect.width) - 1:
                self.player_attack(cell, -50)
        if cell.direction == 1:
            if self.pos_a.x <= (cell.pos.x + cell.rect.width) - 1:
                if self.pos.x > cell.pos.x: # you are behind cell
                    self.player_attack(cell, -50)
                else: # cell is behind you
                    self.cell_do_dmg_x(cell, 50)


    def player_combo_routine_xr(self, cell):
        """
        this is where how cells will be attacked from
        combo 1 through 9 when player is facing right
        """
        if cell.direction == 1:
            if self.pos_a.x + self.rect_ym.width - 1 >= cell.pos.x:
                self.player_attack(cell, 50)
        if cell.direction == 0:
            if self.rect_ym.left + self.rect_ym.width >= (cell.rect.left + 1):
                if self.pos.x < cell.pos.x:
                    self.player_attack(cell, 50)
                else:
                    self.cell_do_dmg_x(cell, -50)


    def player_hit_cell_xl(self, cell):
        """
        function that checks for collision between player
        facing left and cell when player is attacking
        """
        self.player_combo_routine_xl(cell)


    def player_hit_cell_xr(self, cell):
        """
        function that checks for collision between player
        facing right and cell when player is attacking
        """
        self.player_combo_routine_xr(cell)


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




P1 = YM_Battle()
