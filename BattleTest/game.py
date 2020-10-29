#!/usr/bin/env python3
import sys
import pygame
from display import *
from action import P1, KuppaAct

from covid19 import *
from stage import *




class Game:

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        #self.bg = pygame.image.load("images/bg_level.png").convert()
        self.prd = 0
        self.delay_cnt = 0

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()


    def _check_events(self):
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
                    #only when the sword is on
                    if P1.swd_on:
                        KuppaAct.ATK = True
                if event.key == pygame.K_UP:
                    P1.jump()

            if (event.type == pygame.KEYUP):
                if event.key == pygame.K_a:
                    P1.acc.x = 0



    def _update_screen(self):
        """this function updates
        objects on the screen"""
        """do the Player 1 routines"""

        self.player_stuff()
        self.show_info()

        # do the COVID19 routines
        C19.move()
        C19.update()


        """ drawing routines """
        # draw the Stage
        ST1.draw(screen)

        #draw the cells
        C19.render()





        #draw the player
        P1.animate()
        P1.render()
        KuppaAct.render()


        pygame.display.flip()
        self.clock.tick(60)

    def player_stuff(self):
        P1.move()
        P1.update()













    def show_info(self):

        if (self.prd >= 10):
            m1, m2, m3 = pygame.mouse.get_pressed()
            if m1 == 1:
                print("Point 1: {}".format(pygame.mouse.get_pos()))
            self.prd = 0;

            print("KuppaAct's ATK flag: {}".format(KuppaAct.ATK))
#            print("C19Pos: {}".format(C19.pos))
#            print("C19vel: {}".format(C19.vel))
            # print("Player img: {}".format(P1.image))
            # print("Brick1 bottom {}".format(Brick1.rect.bottom))

        self.prd += 1
#        print("x and y: {}".format(pygame.mouse.get_pos()))
#        print("brick rect: {}".format(Brick.rect))
