#!/usr/bin/env python3
import sys
import pygame
from display import *
import time as t
from tortoise_lettuce.le_battle import *

from covid19 import *
from stage import *

class Game:
    """ Game Class """
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.run = True
        self.a_key_cnt = 0

    def Key_a_delay(self, cnt_h, cnt_btnM_h, cnt_btnM_l):
        """Key release Key_a mechanism """
        self.a_key_cnt = pygame.time.get_ticks() - self.a_key_cnt
        if P1.wand_on:
            P1.ATK = True

    def shoot_event(self):
        self.Key_a_delay(100, 90, 34)


    def run_game(self):
        while self.run:
            self._check_events()
            self._update_screen()

        t.sleep(3)
        pygame.quit()
        sys.exit()

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
                    P1.draw_the_wand()
                if event.key == pygame.K_a:
                    self.shoot_event()
                if event.key == pygame.K_UP:
                    P1.jump()
            if (event.type == pygame.KEYUP):
                if event.key == pygame.K_a:
                    self.a_key_cnt = pygame.time.get_ticks()


    def move_camera_x(self, x_range):
        """
        set the boundary for player
        in horizontal direction
        """
        # if the P1 gets near the right, shift the word left
        if P1.pos.x >= x_range - P1.rect.width:
            diff = (P1.pos.x + P1.rect.width) - x_range
            ST1.move_stage(-diff)
            move_cell(-diff, ST1.cells)
            P1.pos.x = x_range - P1.rect.width

        # check position boundary for player
        if P1.pos.x < 0:
            P1.pos.x = 0



    def _update_screen(self):
        """this function updates
        objects on the screen"""

        # do the Player 1 routines
        self.player_stuff()
        self.move_camera_x(700)

        # do the COVID19 routines
        for cell in Cells:
            cell.move()
            cell.hp_show()

        for orb in magic_orbs:
            orb.move()


        """ drawing routines """
        # draw the Stage
        ST1.draw(screen, True)

        # draw the cells and player
        self.cell_draw()
        self.player_draw()

        for orb in magic_orbs:
            orb.animate()
            orb.render()



        """refresh the page per (1000/FPS) ms """
        # tick the clock at 60Hz rate
        pygame.display.update()
        self.clock.tick(FPS)

    def cell_draw(self):
        #draw the cells
        for cell in Cells:
            cell.animate()
            cell.render()

    def player_draw(self):
        #draw the player
#        P1.render()
        P1.render_a()


    def player_stuff(self):
        P1.move()
        P1.update()
