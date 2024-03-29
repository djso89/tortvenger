#!/usr/bin/env python3
"""
Lettuce Action Class - LE_Act
animating attacks and actions that involve
when the wand is drawn
"""
import pygame
from tortoise_lettuce.lettuce import *
from tortoise_lettuce.magic_orb import *

black = (0, 0, 0)


# show one frame per 33ms = sht_frame_period * (1000 / FPS)
shoot_frame_period = 4
# number of frames for one sht
shoot_frame_num = 7


OFF_SET_X = 0
OFF_SET_Y = 0


class LE_Act(Lettuce):
    """
    Lettuce action class:
    this is where LE_Act reads self action flags
    to display the action
    """
    def empty_frames(self):
        self.wand_draw_r = []
        self.wand_draw_l = []

        # wand ready stance frames
        self.wand_rdy_r = []
        self.wand_rdy_l = []

        # wand shoot frames
        self.wand_shoot_r = []
        self.wand_shoot_l = []



    def load_images(self):
        """ load the images from sprite sheets """
        sprite_sheet_wand_draw = SpriteSheet("images/le_draw.png", black)
        sprite_sheet_wand_rdy = SpriteSheet("images/le_wand_rdy.png", black)
        sprite_sheet_wand_shoot = SpriteSheet('images/le_shoot.png', black)

        # load all right facing images - le_wand_rdy
        for i in range(0, 2, 1):
            ss_wand_rdy = sprite_sheet_wand_rdy.sprite_sheet
            width = ss_wand_rdy.get_width()
            height = ss_wand_rdy.get_height()
            image = sprite_sheet_wand_rdy.get_image(i * width // 2, 0, width // 2, height)
            self.wand_rdy_r.append(image)
            image = pygame.transform.flip(image, True, False)
            self.wand_rdy_l.append(image)



        # load all action frames for shoot
        for i in range(0, 7, 1):
            ss_shoot = sprite_sheet_wand_shoot.sprite_sheet
            width = ss_shoot.get_width()
            height = ss_shoot.get_height()
            image = sprite_sheet_wand_shoot.get_image(i * width // 7, 0, width // 7, height)
            self.wand_shoot_r.append(image)
            image = pygame.transform.flip(image, True, False)
            self.wand_shoot_l.append(image)



        # load all the left and right facing for wand drawing
        for i in range(0, 8, 1):
            ss_swd_draw = sprite_sheet_wand_draw.sprite_sheet
            width = ss_swd_draw.get_width()
            height = ss_swd_draw.get_height()
            image = sprite_sheet_wand_draw.get_image(i * width // 8, 0, width // 8, height)
            self.wand_draw_r.append(image)
            image = pygame.transform.flip(image, True, False)
            self.wand_draw_l.append(image)

    def __init__(self):
        super().__init__()
        self.empty_frames()
        self.load_images()

        # frame counter
        self.cnt_wand_draw = 0
        self.cnt_wand_jmp = 0
        self.cnt_wand_shoot = 0
        self.frame_shoot = 0
        self.cnt_got_dmg = 0
        self.num_blinks = 0

        # wand shoot flag and combo count
        self.ATK = False
        self.ATK_DONE = False
        self.atk_comb = 0

        self.drawing_in = False

        # position of the Action Frames
        self.pos_a = vec((0, 0))
        self.image_a = self.wand_draw_r[0]
        self.rect_a = self.image_a.get_rect(topleft=self.pos_a)

    def ani_dmg_blink(self):
        period = 2
        if self.cell_atk_k:
            if self.cnt_got_dmg >= period:
                self.ani_turn_off()
                self.cnt_got_dmg = 0
                self.dmg_blinking = True
                if self.num_blinks == 15:
                    self.cell_atk_k = False
                    self.dmg_blinking = False
                    self.num_blinks = 0
                else:
                    self.num_blinks += 1
            else:
                self.cnt_got_dmg += 1

    def ani_adj_offset(self, x_off, y_off):
        if self.orientation == 'right':
            self.pos_a.x = self.pos.x + x_off
            self.pos_a.y = self.pos.y + y_off
        if self.orientation == 'left':
            self.pos_a.x = self.pos.x + x_off
            self.pos_a.y = self.pos.y + y_off
        self.rect_a = self.image_a.get_rect(topleft=self.pos_a)


    def ani_turn_off(self):
        """ turn off the action frame """
        self.image_a = Surface((self.rect_a.width, self.rect_a.height), flags = SRCALPHA)
        self.image_a.fill((0, 0, 0, 0))

    def shoot(self):
        if self.ATK:
            self.ani_shoot()
        elif not self.ATK:
            self.cnt_wand_shoot = 0

    def ani_move(self):
        """ animate the left right movement"""
        if self.orientation == 'right' and self.OnGround == True:
            frame = (self.pos_a.x // 30) % len(self.ready_r)
            self.image_a = self.ready_r[int(frame)]
        elif self.orientation == 'left' and self.OnGround == True:
            frame = (self.pos_a.x // 30) % len(self.ready_l)
            self.image_a = self.ready_l[int(frame)]


    def ani_wand_move(self):
        """animate the movement with holding the wand """
        # check the Player object's orientation and if sword_draw_counter
        # reached to last frame of sword_draw spritesheet
        # there are 7 frames (starting from 0) in sword
        if self.orientation == 'right' and self.cnt_wand_draw // 5 == 7:
            frame = (self.pos_a.x // 30) % len(self.wand_rdy_r)
            self.image_a = self.wand_rdy_r[int(frame)]
        if self.orientation == 'left' and self.cnt_wand_draw // 5 == 7:
            frame = (self.pos_a.x // 30) % len(self.wand_rdy_l)
            self.image_a = self.wand_rdy_l[int(frame)]

    def ani_wand_out(self):
        period = 5
        max_period = period * (len(self.wand_draw_r) - 1)
        self.wand_drwn = True
        if self.cnt_wand_draw >= max_period:
            self.cnt_wand_draw = max_period
        else:
            if self.orientation == 'right':
                self.image_a = self.wand_draw_r[self.cnt_wand_draw // period]
            if self.orientation == 'left':
                self.image_a = self.wand_draw_l[self.cnt_wand_draw // period]
            self.cnt_wand_draw += 1

    def ani_wand_in(self):
        period = 10
        max_period = period * (len(self.wand_draw_r) - 1)
        if self.cnt_wand_draw <= 0:
            self.cnt_wand_draw = 0
            #self.ani_turn_off()
            self.wand_drwn = False
        else:
            #self.drawing_in = True
            self.cnt_wand_draw -= 1
            if self.orientation == 'right':
                self.image_a = self.wand_draw_r[self.cnt_wand_draw // period]
            if self.orientation == 'left':
                self.image_a = self.wand_draw_l[self.cnt_wand_draw // period]

    def ani_wand_draw(self):
        if self.wand_on == True:
            self.ani_wand_out()
        elif self.wand_on == False:
            self.ani_wand_in()

    def shoot_orbs(self):
        if self.orientation == 'right':
            start_x = self.pos.x + self.rect.width
            start_y = self.pos.y
            orb = M_Orb(start_x, start_y, self.orientation)
        if self.orientation == 'left':
            start_x = self.pos.x
            start_y = self.pos.y
            orb = M_Orb(start_x, start_y, self.orientation)
        magic_orbs.add(orb)



    def ani_shoot(self):
        if self.cnt_wand_shoot >= 3:
            if self.frame_shoot >= len(self.wand_shoot_r) - 1:
                self.frame_shoot = 0
                self.ATK = False
                #self.ATK_DONE = True
                self.cnt_wand_shoot = 0
            else:
                self.frame_shoot += 1
            self.cnt_wand_shoot = 0
        else:
           self.cnt_wand_shoot += 1
        #self.ATK_DONE = False
        if self.orientation == 'right':
            self.image_a = self.wand_shoot_r[self.frame_shoot]
        if self.orientation == 'left':
            self.image_a = self.wand_shoot_l[self.frame_shoot]
        if self.frame_shoot == 5:
            self.shoot_orbs()

        """ animation functions """



    def animate(self):
        """animate the player. """
        self.ani_move()
        self.no_swd_dmg_blink()

    def render(self):
        """ paste the player object into screen """
        #self.animate()
        w = self.image.get_width()
        h = self.image.get_height()
        pos = (self.pos.x, self.pos.y)
        screen.blit(self.image, pos, (0, 0, w ,h))



    def ani_action(self):
        if self.wand_drwn == True:
            if self.orientation == 'left':
                if self.ATK == False:
                    self.ani_adj_offset(-40, -30)
                else:
                    self.ani_adj_offset(-80, -30)
            if self.orientation == 'right':
                self.ani_adj_offset(-5, -30)
        else:
            self.ani_adj_offset(-5, -30)
        self.animate()
        self.ani_wand_draw()
        self.ani_wand_move()
        self.ani_dmg_blink()
        self.shoot()

    def render_a(self):
        self.ani_action()
#        self.render() # to show the player frame
        w = self.image_a.get_width()
        h = self.image_a.get_height()
        pos = (self.pos_a.x, self.pos_a.y)
        screen.blit(self.image_a, pos, (0, 0, w, h))
