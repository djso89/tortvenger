import pygame
from troopakuppa19.k_action import *
from covid19 import Cells
from kuppagauge import kuppainfo


class K_Battle(K_Act):
    def __init__(self):
        super().__init__()
        self.gotHit = False
        self.show_comb = False
        self.btn_mash = 0
        self.num_cells = 0

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

        # touch Plat
        hitP = pygame.sprite.spritecollide(self, Plats, False)
        self.touchX(hitP)

    def gotHit_reset(self):
        # reset gotHit flag
        self.gotHit = False
        self.gotHitBack = False

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
            self.num_cells += 1
            self.check_dir_x(cell)
            # check for maximum number of cells to hit
            # for specific combo
            if self.atk_comb < 3:
                #just hit one cell
                break
            elif self.atk_comb == 3:
                if self.num_cells == 2:
                    break
            elif self.atk_comb == 5:
                #attack up to 3 cells
                if self.num_cells == 4:
                    break
            elif self.atk_comb >= 6 and self.atk_comb < 9:
                if self.num_cells == 5:
                    break
        self.num_cells = 0

    def cell_do_dmg_x(self, cell, knock_back):
        kuppainfo.hit_hp(cell.get_dmg(kuppainfo.defense, kuppainfo.luck))
        self.pos.x += knock_back
        self.cell_atk_k = True
        kuppainfo.update_bar = True


    def cell_hit_player_xl(self, cell):
        """
        function that checks for collision between
        player facing left and cell when player is not attacking
        """
        if cell.direction == 0: # cell direction right
            if self.pos.x + 80  <= (cell.pos.x + cell.rect.width):
                if not self.dmg_blinking:
                    self.cell_do_dmg_x(cell, 200)
                    self.gotHit = True
        if cell.direction == 1:  # cell direction left
            if self.pos.x < cell.pos.x: # the cell is behind the player
                if cell.pos.x <= (self.pos.x + self.rect.width) - 80:
                    if not self.dmg_blinking:
                        self.cell_do_dmg_x(cell, -100)
            else: # the cell is front of the player
                if self.pos.x <= (cell.pos.x + cell.rect.width - 80):
                    if not self.dmg_blinking:
                        self.cell_do_dmg_x(cell, 100)
                        self.gotHit = True


    def cell_hit_player_xr(self, cell):
        """
        function that checks for collision between player
        facing right and cell when player is not attacking
        """
        if cell.direction == 1:
            if (self.pos.x + self.rect.width - 80) >= cell.pos.x:
                if not self.dmg_blinking:
                    self.cell_do_dmg_x(cell, -200)
                    self.gotHit = True
        if cell.direction == 0:
            if self.pos.x > cell.pos.x:
                if self.pos.x + 80 <= (cell.pos.x + cell.rect.width):
                    if not self.dmg_blinking:
                        self.cell_do_dmg_x(cell, 100)
            else:
                if self.pos.x + self.rect.width >= cell.pos.x + 80:
                    if not self.dmg_blinking:
                        self.cell_do_dmg_x(cell, -100)
                        self.gotHit = True

    def player_dmg(self, cell, knock_back):
        """player damage function """
        combo_dmg = round((self.atk_comb / 3) * kuppainfo.get_dmg(cell.defense, cell.luck))
        cell.hit_hp(combo_dmg)
        cell.pos.x += knock_back
        cell.hitCell = True
        cell.update_hp()
        cell.show_hp = True

    def first_combo_mash_check(self, cell, knock_back):
        cut_finish = cut_frame_num * cut_frame_period - 1
        if self.atk_comb < 2:
            self.show_comb = True
            if (self.btn_mash >= 3):
                self.pos.x -= 50 * knock_back
                self.gotHit = True
                self.btn_mash = 0
            else:
                if self.cnt_swd_cut == cut_finish:
                    self.player_dmg(cell, knock_back)

    def player_attack(self, cell, knock_back, combo_knock_back, shadow_cut_dash):
        """
        function that executes cell getting knock_back
        when player attacks cell
        """
        cut_finish = cut_frame_num * cut_frame_period - 1
        self.first_combo_mash_check(cell, knock_back)
        if self.atk_comb >= 2 and self.cnt_swd_cut == cut_finish:
            self.btn_mash = 0
            self.show_comb = True
            if self.atk_comb == 11:
                self.pos.x += shadow_cut_dash
            self.player_dmg(cell, combo_knock_back)

    def player_combo_routine_xl(self, cell):
        """this is where how cells will be attacked from
        combo 1 through 9 when player is facing left"""
        cut_finish = cut_frame_num * cut_frame_period - 1
        if self.atk_comb >= 1 and self.atk_comb <= 9:
            if cell.direction == 0:
                if self.pos_a.x <= (cell.pos.x + cell.rect.width) - 0:
                    self.player_attack(cell, -2, -50, -400)
            if cell.direction == 1:
                if self.pos_a.x <= (cell.pos.x + cell.rect.width) - 0:
                    if self.pos.x > cell.pos.x: # you are behind cell
                        self.player_attack(cell, -2, -50, -400)
                    else: # cell is behind you
                        if self.atk_comb == 4: #when combo4 is executed, go away
                            if self.cnt_swd_cut == cut_finish:
                                self.show_comb = True
                                self.player_dmg(cell, 400)
                        else:
                            if not self.dmg_blinking:
                                self.cell_do_dmg_x(cell, 400)

    def player_combo_routine_xr(self, cell):
        """this is where how cells will be attacked from
        combo 1 through 9 when player is facing right"""
        cut_finish = cut_frame_num * cut_frame_period - 1
        if self.atk_comb >= 1 and self.atk_comb <= 9:
            if cell.direction == 1:
                if self.atk_comb >= 1 and self.atk_comb <= 9:
                    if self.pos_a.x + self.rect_a.width - 0 >= cell.pos.x:
                        self.player_attack(cell, 2, 50, 400)
            if cell.direction == 0:
                if self.rect_a.left + self.rect_a.width >= (cell.rect.left + 0):
                    if self.pos.x < cell.pos.x:
                        self.player_attack(cell, 2, 50, 500)
                    else:
                        #cell do the damage so watch your back
                        #cell knocks you back to the left
                        if self.atk_comb == 4:
                            if self.cnt_swd_cut == cut_finish:
                                self.show_comb = True
                                self.player_dmg(cell, -400)
                        else:
                            if not self.dmg_blinking:
                                self.cell_do_dmg_x(cell, -400)


    def player_hit_cell_xl(self, cell):
        """
        function that checks for collision between player
        facing left and cell when player is attacking
        """
        self.player_combo_routine_xl(cell)
        if self.atk_comb == 10:
            if cell.direction == 0:
                self.player_dmg(cell, -50)
            if cell.direction == 1:
                if self.pos.x > cell.pos.x:
                    self.player_dmg(cell, -50)
                else:
                    self.player_dmg(cell, 50)


    def player_hit_cell_xr(self, cell):
        """
        function that checks for collision between player
        facing right and cell when player is attacking
        """
        self.player_combo_routine_xr(cell)
        if self.atk_comb == 10:
            if cell.direction == 1:
                self.player_dmg(cell, 50)
            if cell.direction == 0:
                if self.pos.x > cell.pos.x:
                    self.player_dmg(cell, -50)
                else:
                    self.player_dmg(cell, 50)


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
