#!/usr/bin/env python3
import sys
import time as t
import pygame
from display import *
from roostergooster.gst_battle import *
from roostergooster.envkunai import *
from roostergooster.expkage import *
from goostergauge import *
from fonts.goostercombo import *

from covid19 import *
from stage import *




class Game:
    """ Game class """
    def __init__(self):
        #pygame.init()
        self.clock = pygame.time.Clock()
        self.run = True
        self.prd = 0
        self.cnt_show_comb = False
        self.frames = 0

        # toggle flag for displaying Stage Objects
        self.SB_toggle = False

        # release counter for measing how long
        # the a key is let go after it's pressed
        self.a_key_cnt = 0

    def Key_a_delay(self, cnt_h, cnt_btnM_h, cnt_btnM_l):
        """Key release Key_a mechanism """
        self.a_key_cnt = pygame.time.get_ticks() - self.a_key_cnt
        P1.go_env_k = True



    def attack_event(self):
        """attacking routine of player """
        envk_period = envk_frame_period * (envk_frame_num)
        envk_len = (envk_period * 1000) / FPS
        self.Key_a_delay(envk_len + 100, 90 ,34)

    def run_game(self):
        while self.run:
            self._check_events()
            self._update_screen()

        t.sleep(3)
        pygame.quit()
        sys.exit()

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
                if event.key == pygame.K_a:
                    self.attack_event()
                if event.key == pygame.K_UP:
                    P1.jump()
            if (event.type == pygame.KEYUP):
                if event.key == pygame.K_a:
                    self.a_key_cnt = pygame.time.get_ticks()
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    P1.steps = 0


    def move_camera_x(self, x_range):
        """
        set the boundary for player
        in horizontal direction
        """
        # player reached the end of the stage
        # lock the camera
        if abs(ST1.scroll) >= (ST1.num_bg - 1) * WIN_W:
            ST1.scroll = -1 * (ST1.num_bg - 1) * WIN_W
            P1.battlesteps = 0
            if P1.pos.x < 0:
                P1.pos.x = 0
            if P1.pos.x >= WIN_W - P1.rect.width:
                P1.pos.x = WIN_W - P1.rect.width
        else:
            if P1.pos.x < 0:
                P1.pos.x = 0
            if P1.pos.x >= x_range - P1.rect.width:
                diff = (P1.pos.x + P1.rect.width) - x_range
                ST1.move_stage(-diff)
                move_cell(-diff, ST1.cells)
                P1.pos.x = x_range - P1.rect.width


    def _update_screen(self):
        """this function updates
        objects on the screen"""

        # do the Player 1 routines
        self.player_stuff()
        self.show_info()

        #player boundary
        self.move_camera_x(700)


        # do the COVID19 routines
        for cell in Cells:
            cell.move()
            cell.hp_show()

        # gooster's bullet routines
        for bullet in envk_bullets:
            bullet.move()
        for bullet in expk_bullets:
            bullet.move()


        """ drawing routines """
        # draw the Stage
        ST1.draw(screen, True)
        goosterinfo.show_gauge()

        # draw the cells and player
        self.cell_draw()
        self.player_draw()

        for bullet in envk_bullets:
            bullet.animate()
            bullet.render()

        for bullet in expk_bullets:
            bullet.animate()
            bullet.render()

        # game over
        if goosterinfo.curr_hp == 0:
            font = pygame.font.Font('fonts/aileron_regular.otf', 40)
            g_over_txt = Borderline_Txt("Game Over", font, black, white, 5)
            screen.blit(g_over_txt, (WIN_W / 2, WIN_H /2))
            self.run = False

        """refresh the page per (1000/FPS) ms """
        # tick the clock at 60Hz rate
        pygame.display.update()
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

        if P1.show_comb:
            if self.cnt_show_comb >= 20:
                P1.show_comb = False
                self.cnt_show_comb = 0
            GoosterCombo.update_combo(P1.atk_comb)
            self.cnt_show_comb += 1



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
