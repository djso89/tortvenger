#!/usr/bin/env python3
import sys
import pygame
from display import *
from fonts.yesmancombo import *
import time as t
from yes_man_the_tortoise.yesmanbattle import *




from covid19 import *
from stage import *




class Game:
    """ Game class """
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.run = True
        self.prd = 0
        self.cnt_show_comb = 0
        self.cnt_sb = 0
        self.frames = 0


        # release counter for measing how long
        #the a key is let go after it's pressed
        self.a_key_cnt = 0
        self.a_stamp = 0
        self.cut_len = 0



    def Key_a_delay(self):
        """Key release Key_a mechanism """
        self.a_stamp = pygame.time.get_ticks() - self.a_key_cnt
        if P1.swd_on:
            if P1.ATK_DONE == False:
                P1.ATK = True




    def attack_event(self):
        """attacking routine of player """
        self.Key_a_delay()


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
                if event.key == pygame.K_a:
                    self.attack_event()
                if event.key == pygame.K_d:
                    P1.draw_the_swrd()
                if event.key == pygame.K_UP:
                    P1.jump()
            if (event.type == pygame.KEYUP):
                if event.key == pygame.K_a:
                    self.cut_len = int((P1.cut_period * 1000) / FPS)
                    self.a_key_cnt = pygame.time.get_ticks()
                    if self.a_stamp >= 3 * self.cut_len:
                        P1.slash_number = 1
                    else:
                        P1.go_combo()

    def player_boundary_x(self, x_range):
        """
        set the boundary for player
        in horizontal direction
        """
        # if the P1 gets near the right, shift the word left
        if P1.pos.x >= x_range - P1.rect.width:
            diff = (P1.pos.x + P1.rect.width) - x_range
            print(diff)
            ST1.move_stage(-diff)
            P1.pos.x = x_range - P1.rect.width

        # check position boundary for player
        if P1.pos.x < 0:
            P1.pos.x = 0



    def _update_screen(self):
        """this function updates
        objects on the screen"""

        # do the Player 1 routines
        self.player_stuff()
        self.player_boundary_x(700)

        # do the COVID19 routines
        for cell in Cells:
            cell.move()
            cell.hp_show()


        """ drawing routines """
        # draw the Stage
        ST1.draw(screen, False)
        # draw the gauge
        Yesmaninfo.show_gauge()

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
        if P1.show_comb:
            if self.cnt_show_comb >= 20:
                P1.show_comb = False
                self.cnt_show_comb = 0
            YesmanCombo.update_combo(P1.slash_number)
            self.cnt_show_comb += 1



    def player_stuff(self):
        P1.move()
        P1.update()

    def get_coord(self):
        m1, m2, m3 = pygame.mouse.get_pressed()
        if m1 == 1:
            print("Point 1: {}".format(pygame.mouse.get_pos()))
