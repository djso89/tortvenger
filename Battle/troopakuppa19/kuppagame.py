#!/usr/bin/env python3
import sys
import random
import pygame
import time as t
from troopakuppa19.kuppabattle import *
from fonts.kuppacombo import *
from kuppagauge import kuppainfo
from battlemode import move_camera_x, lock_camera_x


from stage import *

from troopakuppa19.vid import *
from display import *


class Game:
    """ Game class """
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.run = True
        self.prd = 0
        self.cnt_show_comb = False
        self.cnt_sb = 0
        self.frames = 0

        # toggle flag for displaying Stage Objects
        # for the KuppaVision
        self.SB_toggle = False

        # release counter for measing how long the a key is let go after it's pressed
        self.a_key_cnt = 0


        # release counter for measing how long the w key is let go after it's pressed
        self.w_key_cnt = 0


    def Key_a_delay(self, cnt_h, cnt_btnM_h, cnt_btnM_l):
        """Key release Key_a mechanism """
        self.a_key_cnt = pygame.time.get_ticks() - self.a_key_cnt
        # print("you release key a for " + str(self.a_key_cnt) + "ms")
        if P1.swd_on:
            P1.ATK = True
            if self.a_key_cnt >= cnt_h:
                P1.atk_comb = 1
                P1.cnt_swd_cut = 0
            elif (self.a_key_cnt <= cnt_btnM_h and self.a_key_cnt > cnt_btnM_l):
                P1.atk_comb = 1
                P1.btn_mash += 1
            else:
                #check if current attack combo reached MaxCombo
                if P1.atk_comb == kuppainfo.MaxCombo:
                    # reset the combo to 1
                    P1.atk_comb = 1
                else:
                    if P1.ATK_DONE:
                        P1.atk_comb += 1

    def Key_w_delay(self):
        """Key release Key_a mechanism """
        if P1.swd_on:
            P1.start_field = True

    def attack_event(self):
        """attacking routine of player """
        cut_period = cut_frame_period * (cut_frame_num)
        cut_len = (cut_period * 1000) / FPS
        self.Key_a_delay(cut_len + 100, 90 ,34)

    def block_event(self):
        """blocking routine of player """
        self.Key_w_delay()


    def run_game(self):
        play_cutscene_1_1()
        pygame.init()
        pygame.display.init()
        full_screen()
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
                    print('q is pressed')
                if event.key == pygame.K_d:
                    P1.draw_the_swrd()
                if event.key == pygame.K_s:
                    if not P1.swd_on:
                        if kuppainfo.curr_ki > 0:
                            self.SB_toggle = True
                if event.key == pygame.K_w:
                    self.block_event()
                if event.key == pygame.K_a:
                    self.attack_event()
                if event.key == pygame.K_UP:
                    P1.jump()
                if event.key == pygame.K_DOWN:
                    P1.jmp_dwn_plat()
            if (event.type == pygame.KEYUP):
                if event.key == pygame.K_a:
                    self.a_key_cnt = pygame.time.get_ticks()
                if event.key == pygame.K_w:
                    self.w_key_cnt = pygame.time.get_ticks()
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    P1.acc.x = 0
                    P1.steps = 0
                if event.key == pygame.K_DOWN:
                    pass
                    #P1.get_off = False
                if event.key == pygame.K_s:
                    self.SB_toggle = False


    def cell_generate(self, num_cells):
        """choose the platform to place the cell
        and generate the cells"""
        print("Scroll value: {}".format(abs(ST1.scroll)))

        curr_stage = abs(ST1.scroll) // WIN_W
        shift_value = abs(ST1.scroll) - (curr_stage * WIN_W)
        print('shifted value: {}'.format(shift_value))

        # generate cells on the ground
        cells_on_ground(ST1.cells, num_cells, P1)



    def battlemode_switch(self):
        if not ST1.battlemode:
            step_encounter = random.randrange(300, 800, 20)
            if P1.battlesteps >= step_encounter:
                P1.battlesteps = 0
                ST1.battlemode = True
                self.cell_generate(7)

    def _update_screen(self):
        """this function updates
        objects on the screen"""

        # do the Player 1 routines
        self.player_stuff()
        self.show_info()


        # horizontal map scrolling
        self.battlemode_switch()
        if not ST1.battlemode:
            move_camera_x(P1, ST1, 700)
        else:
            lock_camera_x(P1, ST1)

        # do the COVID19 routines
        for cell in ST1.cells:
            cell.move()
            cell.hp_show()


        """ drawing routines """
        # draw the Stage
        ST1.draw(screen, True)

        # draw the cells and player
        self.cell_draw()
        self.player_draw()

        if kuppainfo.curr_hp == 0:
            font = pygame.font.Font('fonts/aileron_regular.otf', 40)
            g_over_txt = Borderline_Txt("Game Over", font, black, white, 5)
            screen.blit(g_over_txt, (WIN_W/2, WIN_H/2))
            self.run = False

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
        P1.render_a()
        # show combo
        if P1.show_comb:
            if self.cnt_show_comb >= 20:
                P1.show_comb = False
                self.cnt_show_comb = 0
            KuppaCombo.update_combo(P1.atk_comb)
            self.cnt_show_comb += 1
        kuppainfo.show_gauge()

    def player_stuff(self):
        P1.move()
        P1.update()





    """------------------------------------------------------------------------- """
    def get_coord(self):
        m1, m2, m3 = pygame.mouse.get_pressed()
        if m1 == 1:
            mouse_pt = pygame.mouse.get_pos()
            mouse_coord = (mouse_pt[0] + abs(ST1.scroll), mouse_pt[1])
            print("Point 1: {}".format(mouse_coord))

    def show_info(self):
        if (self.prd >= 13):
            self.get_coord()
        self.prd += 1
        #p_rect = P1.rect
        #if (self.prd >= 1):
        #    print("player1's image is {}".format(P1.rect))
        #    self.print_stat()
        #    self.prd = 0;

        #self.prd += 1

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
