#!/usr/bin/env python3
"""
Action Class - K_Act
animating attacks and actions that involve when
swords are drawn
"""
import pygame
from roostergooster.gooster import *
from roostergooster.envkunai import *
from roostergooster.expkage import *
import random

envk_frame_period = 2
envk_frame_num = 9
envk_max_combo = 1



class GST_Act(Gooster):
    """ Kuppa action class
    this is where K_Act reads self action flags
    to display the action
    """
    def empty_frames(self):
        self.env_k_l = []
        self.env_k_r = []

        self.exp_k_l = []
        self.exp_k_r = []
        """initialize all the action frames """

    def load_images(self):
        """ load the images from sprite sheets """
        sprite_sheet_envk = SpriteSheet("images/gst_env_k.png", black)
        ss_envk = sprite_sheet_envk.sprite_sheet

        sprite_sheet_expk = SpriteSheet("images/gst_exp_k.png", black)
        ss_expk = sprite_sheet_expk.sprite_sheet

        # load all the L/R frames for jumping with swords held
        for i in range(0, 9, 1):
            width = ss_envk.get_width()
            height = ss_envk.get_height()
            image = sprite_sheet_envk.get_image(i * width / 9, 0, width / 9, height)
            self.env_k_r.append(image)
            image = pygame.transform.flip(image, True, False)
            self.env_k_l.append(image)

        for i in range(0, 9, 1):
            width = ss_expk.get_width()
            height = ss_expk.get_height()
            image = sprite_sheet_expk.get_image(i * width / 9, 0, width / 9, height)
            self.exp_k_r.append(image)
            image = pygame.transform.flip(image, True, False)
            self.exp_k_l.append(image)

    def __init__(self):
        super().__init__()
        self.empty_frames()

        self.load_images()


        # attack: envelop kunai attack
        self.go_env_k = False
        self.done_envk = False
        self.envk_comb = 1
        self.cnt_envk = 0
        self.frame_env = 0
        
        # attack: explosive package attack
        self.go_exp_k = False
        self.done_expk = False
        self.expk_comb = 1
        self.cnt_expk = 0
        self.frame_expk = 0

        #position of the Action Frames
        self.pos_a = vec((0, 0))
        self.image_a = self.env_k_r[0]


    def atk_envk(self):
        if self.go_env_k:
            self.ani_envk()
        elif not self.go_env_k:
            self.cnt_envk = 0
            
    def atk_expk(self):
        if self.go_exp_k:
            self.ani_expk()
        elif not self.go_exp_k:
            self.cnt_expk = 0
            
          
    def ani_envk(self):
        if self.cnt_envk >= envk_frame_period:
            if self.orientation == 'right':
                self.image_a = self.env_k_r[self.frame_env]
            if self.orientation == 'left':
                self.image_a = self.env_k_l[self.frame_env]
            if (self.frame_env == 5):
                self.throw_envk()
            self.frame_env += 1

            if self.frame_env >= len(self.env_k_r):
                self.frame_env = 0
                self.go_env_k = False
                self.done_envk = True
            self.cnt_envk = 0
        else:
            self.done_envk = False
            self.cnt_envk += 1
    
    def ani_expk(self):
        if self.cnt_expk >= 2:
            if self.orientation == 'right':
                self.image_a = self.exp_k_r[self.frame_expk]
            if self.orientation == 'left':
                self.image_a = self.exp_k_l[self.frame_expk]
            if self.frame_expk == 5:
                # throw
                self.throw_expk()
            self.frame_expk += 1

            if self.frame_expk >= len(self.exp_k_r):
                self.frame_expk = 0
                self.go_exp_k = False
                self.done_expk = True
            self.cnt_expk = 0
        else:
            self.done_expk = False
            self.cnt_expk += 1

    def envk_frame_adj(self):
        if self.go_env_k:
            if self.orientation == 'left':
                self.ani_adj_offset(-20, 0)
            if self.orientation == 'right':
                self.ani_adj_offset(0, 0)


    def expk_frame_adj(self):
        if self.go_exp_k:
            if self.orientation == 'left':
                self.ani_adj_offset(-20, 0)
            if self.orientation == 'right':
                self.ani_adj_offset(0, 0)

    def ani_adj_offset(self, x_off, y_off):
        if self.orientation == 'right':
            self.pos_a.x = self.pos.x + x_off
            self.pos_a.y = self.pos.y + y_off
        if self.orientation == 'left':
            self.pos_a.x = self.pos.x + x_off
            self.pos_a.y = self.pos.y + y_off
        self.rect_a = self.image_a.get_rect(topleft=self.pos_a)

    def throw_envk(self):
        if self.orientation == 'right':
            start_x = self.pos.x + self.rect.width
            start_y = self.pos.y + 50 + random.randint(-50, 50)
            envk_bullet = ENV_K(start_x, start_y, self.orientation)
        if self.orientation == 'left':
            start_x = self.pos.x
            start_y = self.pos.y + 50 + random.randint(-50, 50)
            envk_bullet = ENV_K(start_x, start_y, self.orientation)
        envk_bullets.add(envk_bullet)

    def throw_expk(self):
        if self.orientation == 'right':
            start_x = self.pos.x + self.rect.width
            start_y = self.pos.y + 50 + random.randint(-100, 50)
            expk_bullet = EXP_K(start_x, start_y, self.orientation)
        if self.orientation == 'left':
            start_x = self.pos.x
            start_y = self.pos.y + 50 + random.randint(-100, 50)
            expk_bullet = EXP_K(start_x, start_y, self.orientation)
        expk_bullets.add(expk_bullet)



    def animate(self):
        """animate the player. """

        self.ani_move()
        self.no_atk_dmg_blink()
        self.atk_envk()
        self.atk_expk()

        self.envk_frame_adj()
        self.expk_frame_adj()

    def render(self):
        """ paste the player object into screen """
        self.animate()

        if (self.go_env_k or self.go_exp_k):
            w_a = self.image_a.get_width()
            h_a = self.image_a.get_height()
            screen.blit(self.image_a, self.pos_a, (0, 0, w_a , h_a))
        else:
            w = self.image.get_width()
            h = self.image.get_height()
            screen.blit(self.image, self.pos, (0, 0,w ,h))
