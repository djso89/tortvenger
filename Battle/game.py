#!/usr/bin/env python3
import sys
import pygame
from display import *
from action import P1, KuppaAct

from covid19 import *
from stage import *




class Game:
    """ Game class """
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.prd = 0

        # release counter for measing how long the a key is let go after it's pressed
        self.a_key_cnt = 0

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()


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
                if event.key == pygame.K_a:
                    self.a_key_cnt = pygame.time.get_ticks() - self.a_key_cnt
                    print("you release key a for " + str(self.a_key_cnt) + "ms")
                    if P1.swd_on:
                        KuppaAct.ATK = True
                        # combo routine
                        if self.a_key_cnt >= 192:
                            KuppaAct.atk_comb = 1
                        elif self.a_key_cnt <= 191:
                            print("combo up!!")
                            KuppaAct.atk_comb += 1
                        if KuppaAct.atk_comb == 3: #Max combo up to 2
                            KuppaAct.atk_comb = 1
                        print("Combo #: {}".format(KuppaAct.atk_comb))
                        
                if event.key == pygame.K_UP:
                    P1.jump()

            if (event.type == pygame.KEYUP):
                if event.key == pygame.K_a:
                    self.a_key_cnt = pygame.time.get_ticks()
                    #P1.acc.x = 0



    def _update_screen(self):
        """this function updates
        objects on the screen"""
        
        # do the Player 1 routines
        self.player_stuff()
        #self.show_info()

        # do the COVID19 routines
        C19.move()
        C19.update()


        """ drawing routines """
        # draw the Stage
        ST1.draw(screen)

        #draw the cells
        C19.ani_move()
        C19.render()


        #draw the player
        P1.animate()
        P1.render()
        KuppaAct.render()

        # tick the clock at 60Hz rate
        pygame.display.flip()
        self.clock.tick(60)

    def player_stuff(self):
        P1.move()
        #KuppaAct.attack()
        P1.update()













    def show_info(self):

        if (self.prd >= 10):
            # print("combo # = {}".format(self.atk_comb))
            m1, m2, m3 = pygame.mouse.get_pressed()
            if m1 == 1:
                print("Point 1: {}".format(pygame.mouse.get_pos()))
            self.prd = 0;

        self.prd += 1
