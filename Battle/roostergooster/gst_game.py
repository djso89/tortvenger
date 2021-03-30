#!/usr/bin/env python3
import sys
import pygame
from display import *
from roostergooster.gst_action import *
from roostergooster.envkunai import *
from roostergooster.expkage import *

from covid19 import *
from stage import *




class Game:
    """ Game class """
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.prd = 0
        self.cnt_show_comb = False
        self.frames = 0

        # toggle flag for displaying Stage Objects
        self.SB_toggle = False

        # release counter for measing how long the a key is let go after it's pressed
        self.a_key_cnt = 0

    def Key_a_delay(self, cnt_h, cnt_btnM_h, cnt_btnM_l):
        """Key release Key_a mechanism """
        self.a_key_cnt = pygame.time.get_ticks() - self.a_key_cnt
        # print("you release key a for " + str(self.a_key_cnt) + "ms")
        P1.go_env_k = True



    def attack_event(self):
        """attacking routine of player """
        envk_period = envk_frame_period * (envk_frame_num)
        envk_len = (envk_period * 1000) / FPS
        self.Key_a_delay(envk_len + 100, 90 ,34)

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()

    def print_key(self, key):
        print(key)

    def _check_events(self):
        """ this function checks the events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()
            if (event.type == pygame.KEYDOWN):
                if event.key == pygame.K_q:
                    pygame.display.quit()
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_d:
                    P1.go_exp_k = True
                    # P1.draw_the_swrd()
                if event.key == pygame.K_a:
                     self.attack_event()
                if event.key == pygame.K_UP:
                    P1.jump()
            if (event.type == pygame.KEYUP):
                if event.key == pygame.K_a:
                    self.a_key_cnt = pygame.time.get_ticks()


    def _update_screen(self):
        """this function updates
        objects on the screen"""

        # do the Player 1 routines
        self.player_stuff()
        self.show_info()

        # do the COVID19 routines
        for cell in Cells:
            cell.move()
            
        for bullet in envk_bullets:
            bullet.move()
        
        for bullet in expk_bullets:
            bullet.move()


        """ drawing routines """
        # draw the Stage
        ST1.draw(screen, self.SB_toggle)

        # draw the cells and player
        
        self.cell_draw()
        self.player_draw()
        
        for bullet in envk_bullets:
            bullet.animate()
            bullet.render()
            
        for bullet in expk_bullets:
            bullet.animate()
            bullet.render()
        """refresh the page per (1000/FPS) ms """
        # tick the clock at 60Hz rate
        pygame.display.flip()
        self.clock.tick(FPS)

    def cell_draw(self):
        #draw the cells
        for cell in Cells:
            cell.animate()
            cell.pause()
            cell.render()

    def player_draw(self):
        #draw the player
        P1.render()


    def player_stuff(self):
        P1.move()
        P1.update()











    def get_coord(self):
        m1, m2, m3 = pygame.mouse.get_pressed()
        if m1 == 1:
            print("Point 1: {}".format(pygame.mouse.get_pos()))
                
    def show_info(self):
        if (self.prd >= 13):
            self.get_coord()
        self.prd += 1

        
    def print_stat(self):
        if (P1.ATK):
            act_rect = P1.rect_a
            print("action rect's image is {}".format(act_rect))
            print("frames: {}".format(self.frames))
            print("combo: {} Atack: {}".format(P1.atk_comb, P1.ATK))
            self.frames += 1
            print("------------------------------------")
        else:
            self.frames = 0
