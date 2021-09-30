#!/usr/bin/env python3
import sys
import pygame
from display import *
import time as t
from yes_man_the_tortoise.yesman import *




from covid19 import *
from stage import *




class Game:
    """ Game class """
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.run = True
        self.prd = 0
        self.cnt_show_comb = False
        self.cnt_sb = 0
        self.frames = 0


        # release counter for measing how long
        #the a key is let go after it's pressed
        self.a_key_cnt = 0




    def Key_a_delay(self, cnt_h, cnt_btnM_h, cnt_btnM_l):
        """Key release Key_a mechanism """
        self.a_key_cnt = pygame.time.get_ticks() - self.a_key_cnt
        self.pressed_a = True
        if P1.swd_on:
            if P1.ATK_DONE == False:
                P1.ATK = True


    def attack_event(self):
        """attacking routine of player """
        cut_len = int((P1.cut_period * 1000) / FPS)
        self.Key_a_delay(cut_len, 50 ,34)


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
                    P1.cnt_a += 1
                if event.key == pygame.K_d:
                    P1.draw_the_swrd()
                if event.key == pygame.K_UP:
                    P1.jump()
            if (event.type == pygame.KEYUP):
                if event.key == pygame.K_a:
                    self.a_key_cnt = pygame.time.get_ticks()
                    print("a key counter held: {}".format(P1.cnt_a))
                    P1.go_combo()






    def _update_screen(self):
        """this function updates
        objects on the screen"""

        # do the Player 1 routines
        self.player_stuff()

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


    def player_stuff(self):
        P1.move()
        P1.update()

    def get_coord(self):
        m1, m2, m3 = pygame.mouse.get_pressed()
        if m1 == 1:
            print("Point 1: {}".format(pygame.mouse.get_pos()))
