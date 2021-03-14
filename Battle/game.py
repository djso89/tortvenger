#!/usr/bin/env python3
import sys
import pygame
from display import *
from k_action import P1, KuppaAct, MaxCombo, cut_frame_period, cut_frame_num
from fonts.combo_splash import KuppaCombo



from covid19 import *
from stage import *




class Game:
    """ Game class """
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.prd = 0
        self.frames = 0

        # toggle flag for displaying Stage Objects
        self.SB_toggle = False

        # release counter for measing how long the a key is let go after it's pressed
        self.a_key_cnt = 0

    def Key_a_delay(self, cnt_h, cnt_btnM_h, cnt_btnM_l):
        """Key release Key_a mechanism """
        self.a_key_cnt = pygame.time.get_ticks() - self.a_key_cnt
        # print("you release key a for " + str(self.a_key_cnt) + "ms")
        if P1.swd_on:
            KuppaAct.ATK = True
            if self.a_key_cnt >= cnt_h or (self.a_key_cnt <= cnt_btnM_h and self.a_key_cnt > cnt_btnM_l):
                KuppaAct.atk_comb = 1
                KuppaAct.cnt_swd_cut = 0
            else:
                #check if current attack combo reached MaxCombo
                if KuppaAct.atk_comb == MaxCombo:
                    # reset the combo to 1
                    KuppaAct.atk_comb = 1
                else:
                    if KuppaAct.ATK_DONE:
                        KuppaAct.atk_comb += 1

    def attack_event(self):
        cut_period = cut_frame_period * (cut_frame_num)
        cut_len = (cut_period * 1000) / FPS
        self.Key_a_delay(cut_len, 100 ,34)

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
                    P1.draw_the_swrd()
                if event.key == pygame.K_s:
                    self.SB_toggle = not self.SB_toggle
                if event.key == pygame.K_a:
                    self.attack_event()
                if event.key == pygame.K_UP:
                    P1.jump()
            if (event.type == pygame.KEYUP):
                if event.key == pygame.K_a:
                    self.a_key_cnt = pygame.time.get_ticks()
                    #KuppaAct.atk_comb = 1
                if event.key == pygame.K_s:
                    self.SB_toggle = not self.SB_toggle


    def _update_screen(self):
        """this function updates
        objects on the screen"""

        # do the Player 1 routines
        self.player_stuff()
        #self.show_info()

        # do the COVID19 routines
        for cell in Cells:
            cell.move()
            cell.update()

        """ drawing routines """
        # draw the Stage
        ST1.draw(screen, self.SB_toggle)

        # draw the cells and player
        self.cell_draw()
        self.player_draw()

        """refresh the page per (1000/FPS) ms """
        # tick the clock at 60Hz rate
        pygame.display.flip()
        self.clock.tick(FPS)

    def cell_draw(self):
        #draw the cells
        for cell in Cells:
            cell.animate()
            cell.render()

    def player_draw(self):
        #draw the player
        P1.render()
        KuppaAct.render()
        # show combo
        if KuppaAct.ATK:
            KuppaCombo.update_combo(KuppaAct.atk_comb)

    def player_stuff(self):
        P1.move()
        P1.update()











    def get_coord(self):
        m1, m2, m3 = pygame.mouse.get_pressed()
        if m1 == 1:
            print("Point 1: {}".format(pygame.mouse.get_pos()))
                
    def show_info(self):
        #self.get_coord()
        p_rect = P1.rect
        if (self.prd >= 1):
            print("player1's image is {}".format(P1.rect))
            self.print_stat()
            self.prd = 0;

        self.prd += 1
        
    def print_stat(self):
        if (KuppaAct.ATK):
            act_rect = KuppaAct.rect_a
            print("action rect's image is {}".format(act_rect))
            print("frames: {}".format(self.frames))
            print("combo: {} Atack: {}".format(KuppaAct.atk_comb, KuppaAct.ATK))
            self.frames += 1
            print("------------------------------------")
        else:
            self.frames = 0
