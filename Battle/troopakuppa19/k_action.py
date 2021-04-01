#!/usr/bin/env python3
"""
Action Class - K_Act
animating attacks and actions that involve when
swords are drawn
"""
import pygame
from troopakuppa19.kuppa import *

black = (0, 0, 0)

# number of maximum combo you can perform
MaxCombo = 10
# show one frame per 33ms = cut_frame_period * (1000 / FPS)
cut_frame_period = 2
# number of frames for one cut
cut_frame_num = 7

OFF_SET_X = 2
OFF_SET_Y = 5


class K_Act(Kuppa):
    """ Kuppa action class
    this is where K_Act reads self action flags
    to display the action
    """
    def empty_frames(self):
        """initialize all the action frames """

        # drawing sword frames
        self.swrd_draw_r = []
        self.swrd_draw_l = []

        # sword ready stance frames
        self.swrd_rdy_r = []
        self.swrd_rdy_l = []

        # sword cut frames
        self.swd_cut_r = []
        self.swd_cut_l = []

        # sword jump frames
        self.swd_jmp_r = []
        self.swd_jmp_l = []

    def load_images(self):
        """ load the images from sprite sheets """
        sprite_sheet_swd_draw = SpriteSheet("images/k_swd_d.png", black)
        sprite_sheet_swd_rdy = SpriteSheet("images/k_swd_rdy.png", black)
        sprite_sheet_swd_cuts = SpriteSheet('images/k_swd_cut.png', black)
        sprite_sheet_swd_cuts2 = SpriteSheet('images/k_swd_cut2.png', black)
        sprite_sheet_swd_cuts3 = SpriteSheet('images/k_swd_cut3.png', black)
        sprite_sheet_swd_cuts4 = SpriteSheet('images/k_swd_cut4.png', black)
        sprite_sheet_swd_cuts5 = SpriteSheet('images/k_swd_cut5.png', black)        
        sprite_sheet_swd_cuts6 = SpriteSheet('images/k_swd_cut6.png', black)
        sprite_sheet_swd_cuts7 = SpriteSheet('images/k_swd_cut7.png', black)        
        sprite_sheet_swd_jmp = SpriteSheet('images/k_swd_jmp.png', black)


        # load all the L/R frames for jumping with swords held
        for i in range(0, 7, 1):
            ss_swd_jmp = sprite_sheet_swd_jmp.sprite_sheet
            width = ss_swd_jmp.get_width()
            height = ss_swd_jmp.get_height()
            image = sprite_sheet_swd_jmp.get_image(i * width // 7, 0, width // 7, height)
            self.swd_jmp_r.append(image)
            image = pygame.transform.flip(image, True, False)
            self.swd_jmp_l.append(image)

        # load all the left and right facing for sword cutting
        # combo 1 ~ 2
        for i in range(0, 14, 1):
            ss_swd_cuts = sprite_sheet_swd_cuts.sprite_sheet
            width = ss_swd_cuts.get_width()
            height = ss_swd_cuts.get_height()
            image = sprite_sheet_swd_cuts.get_image(i * width // 14, 0, width // 14, height)
            self.swd_cut_r.append(image)
            image = pygame.transform.flip(image, True, False)
            self.swd_cut_l.append(image)
            
        # combo 3 - 4
        for i in range(0, 14, 1):
            ss_swd_cuts2 = sprite_sheet_swd_cuts2.sprite_sheet
            width = ss_swd_cuts2.get_width()
            height = ss_swd_cuts2.get_height()
            image = sprite_sheet_swd_cuts2.get_image(i * width // 14, 0, width // 14, height)
            self.swd_cut_r.append(image)
            image = pygame.transform.flip(image, True, False)
            self.swd_cut_l.append(image)
        
        # combo 5 - 6
        for i in range(0, 14, 1):
            ss_swd_cuts3 = sprite_sheet_swd_cuts3.sprite_sheet
            width = ss_swd_cuts3.get_width()
            height = ss_swd_cuts3.get_height()
            image = sprite_sheet_swd_cuts3.get_image(i * width // 14, 0, width // 14, height)
            self.swd_cut_r.append(image)
            image = pygame.transform.flip(image, True, False)
            self.swd_cut_l.append(image)
            
        # combo 7 - 8
        for i in range(0, 14, 1):
            ss_swd_cuts4 = sprite_sheet_swd_cuts4.sprite_sheet
            width = ss_swd_cuts4.get_width()
            height = ss_swd_cuts4.get_height()
            image = sprite_sheet_swd_cuts4.get_image(i * width // 14, 0, width // 14, height)
            self.swd_cut_r.append(image)
            image = pygame.transform.flip(image, True, False)
            self.swd_cut_l.append(image)
        
        # combo 9
        for i in range(0, 7, 1):
            ss_swd_cuts5 = sprite_sheet_swd_cuts5.sprite_sheet
            width = ss_swd_cuts5.get_width()
            height = ss_swd_cuts5.get_height()
            image = sprite_sheet_swd_cuts5.get_image(i * width // 7, 0, width // 7, height)
            self.swd_cut_r.append(image)
            image = pygame.transform.flip(image, True, False)
            self.swd_cut_l.append(image)       


        
        # combo 10
        for i in range(0, 7, 1):
            ss_swd_cuts6 = sprite_sheet_swd_cuts6.sprite_sheet
            width = ss_swd_cuts6.get_width()
            height = ss_swd_cuts6.get_height()
            image = sprite_sheet_swd_cuts6.get_image(i * width // 7, 0, width // 7, height)
            self.swd_cut_r.append(image)
            image = pygame.transform.flip(image, True, False)
            self.swd_cut_l.append(image)
            
        # combo 11
        for i in range(0, 7, 1):
            ss_swd_cuts7 = sprite_sheet_swd_cuts7.sprite_sheet
            width = ss_swd_cuts7.get_width()
            height = ss_swd_cuts7.get_height()
            image = sprite_sheet_swd_cuts7.get_image(i * width // 7, 0, width // 7, height)
            self.swd_cut_r.append(image)
            image = pygame.transform.flip(image, True, False)
            self.swd_cut_l.append(image)

        # load all the left and right facing for sword drawing
        for i in range(0, 12, 1):
            ss_swd_draw = sprite_sheet_swd_draw.sprite_sheet
            width = ss_swd_draw.get_width()
            height = ss_swd_draw.get_height()
            image = sprite_sheet_swd_draw.get_image(i * width // 12, 0, width // 12, height)
            self.swrd_draw_r.append(image)
            image = pygame.transform.flip(image, True, False)
            self.swrd_draw_l.append(image)


        # load all right facing images - swd_rdy
        for i in range(0, 2, 1):
            ss_swd_rdy = sprite_sheet_swd_rdy.sprite_sheet
            width = ss_swd_rdy.get_width()
            height = ss_swd_rdy.get_height()
            image = sprite_sheet_swd_rdy.get_image(i * width // 2, 0, width // 2, height)
            self.swrd_rdy_r.append(image)
            image = pygame.transform.flip(image, True, False)
            self.swrd_rdy_l.append(image)


    def __init__(self):
        super().__init__()
        self.empty_frames()

        self.load_images()


        # frame counter
        self.cnt_swrd_draw = 0
        self.cnt_swd_jmp = 0
        self.cnt_swd_cut = 0

        # sword cut flag and combo count
        self.ATK = False
        self.ATK_DONE = False
        self.atk_comb = 1
        self.frame_atk = 0

        # position of the Action Frames
        self.pos_a = vec((0, 0))
        self.image_a = self.swrd_draw_r[0]
        self.rect_a = self.image_a.get_rect(topleft=self.pos_a)


    def ani_turn_off(self):
        """ turn off the action frame """
        self.image_a = Surface((self.rect_a.width, self.rect_a.height), flags = SRCALPHA)
        self.image_a.fill((0, 0, 0, 0))


    def ani_cut(self):
        """ animate sword cutting combo 1 ~ 2 """
        # one cut length
        cut_period = cut_frame_period * ((cut_frame_num))
        """Combo Routine"""
        if (self.cnt_swd_cut  >= cut_period):
            # done cutting
            self.cnt_swd_cut = 0
            self.ATK = False
            self.ATK_DONE = True
            # print("combo#{} done cutting".format(self.atk_comb))
        else:
            self.ATK_DONE = False
            combo_i = (self.atk_comb * cut_frame_num) - cut_frame_num
            self.frame_atk = combo_i + (self.cnt_swd_cut // cut_frame_period)
            if (self.orientation == 'right'):
                self.image_a = self.swd_cut_r[self.frame_atk]
            if (self.orientation == 'left'):
                self.image_a = self.swd_cut_l[self.frame_atk]
            # print("cut frame index: {} combo: {}".format(self.frame_atk, self.atk_comb))
            # print("image rect is {}".format(self.rect_a))
            self.cnt_swd_cut += 1


    def attack(self):
        """ game logic for attack
        the ATK flag is triggered true. ATK is true when
        Key_a is pressed
        Go refer to game.py for keyboard mechanism for Key_a
        """
        if self.ATK:
            self.ani_cut()
        elif not self.ATK:
            self.cnt_swd_cut = 0


    def ani_swd_move(self):
        """animate the movement with holding the swords """
        # check the Player object's orientation and if sword_draw_counter
        # reached to last frame of sword_draw spritesheet
        # there are 11 frames (starting from 0) in sword
        if self.orientation == 'right' and self.cnt_swrd_draw // 2 == 11:
            frame = (self.pos_a.x // 30) % len(self.swrd_rdy_r)
            self.image_a = self.swrd_rdy_r[int(frame)]
        if self.orientation == 'left' and self.cnt_swrd_draw // 2 == 11:
            frame = (self.pos_a.x // 30) % len(self.swrd_rdy_l)
            self.image_a = self.swrd_rdy_l[int(frame)]

    def ani_swd_out(self):
        """ animate pulling out the sword """
        period = 2
        max_period = period * (len(self.swrd_draw_r) - 1)
        self.swd_drwn = True  # turn the Player frame off
        if (self.cnt_swrd_draw >= max_period):
            self.cnt_swrd_draw = max_period
        else:
            if (self.orientation == 'right'):
                self.image_a = self.swrd_draw_r[self.cnt_swrd_draw // period]
            if (self.orientation == 'left'):
                self.image_a = self.swrd_draw_l[self.cnt_swrd_draw // period]
            self.cnt_swrd_draw += 1

    def ani_swd_in(self):
        """ animate drawing back the sword """
        period = 2
        max_period = period * (len(self.swrd_draw_r) - 1)
        if (self.cnt_swrd_draw <= 0):
            self.cnt_swrd_draw = 0
            self.ani_turn_off() # turn off the action frame
            self.swd_drwn = False # turn the Player frame on
        else:
            self.cnt_swrd_draw -= 1
            if (self.orientation == 'right'):
                self.image_a = self.swrd_draw_r[self.cnt_swrd_draw // period]
            if (self.orientation == 'left'):
                self.image_a = self.swrd_draw_l[self.cnt_swrd_draw // period]


    def ani_swd_draw(self):
        """animate drawing the swords """
        if self.swd_on == True:
            self.ani_swd_out()
        elif self.swd_on == False:
            self.ani_swd_in()

    def ani_swd_jmp(self):
        """ animate jump with sword in hands"""
        period = 3
        if self.OnGround == False and self.swd_drwn:
            if (self.cnt_swd_jmp >= period * (len(self.swd_jmp_r) - 1)):
                self.cnt_swd_jmp = period * (len(self.swd_jmp_r) - 1)
            else:
                self.cnt_swd_jmp += 1
            if self.orientation == 'right':
                self.image_a = self.swd_jmp_r[self.cnt_swd_jmp // period]
            if self.orientation == 'left':
                self.image_a = self.swd_jmp_l[self.cnt_swd_jmp // period]
        else:
            self.cnt_swd_jmp = 0



    def ani_adj_offset(self, x_off, y_off):
        """adjust the action frame coordinate """
        if self.orientation == 'right':
            self.pos_a.x = self.pos.x - OFF_SET_X + x_off
            self.pos_a.y = self.pos.y + y_off - self.rect.height - OFF_SET_Y
        if self.orientation == 'left':
            self.pos_a.x = self.pos.x  -  (self.image_a.get_width()
                                     - self.image.get_width()) + x_off
            self.pos_a.y = self.pos.y  + y_off - self.rect.height - OFF_SET_Y
        self.rect_a = self.image_a.get_rect(topleft=self.pos_a)


    def combo_frame_adj_offset(self):
        if self.ATK == False:
            self.ani_adj_offset(0, 0)
        elif self.ATK == True and self.atk_comb <= 2:
            self.ani_adj_offset(2, -2)
        elif self.ATK == True and (self.atk_comb > 2 and self.atk_comb <= 4):
            self.ani_adj_offset(2, 20)
        elif self.ATK == True and (self.atk_comb > 4 and self.atk_comb <= MaxCombo):
            self.ani_adj_offset(2, -20)

    def ani_action(self):
        self.combo_frame_adj_offset()
        """animate all the action frames """
        self.ani_swd_draw()
        self.ani_swd_move()
        self.ani_swd_jmp()
        self.attack()

    def render_a(self):
        self.ani_action()
        w = self.image_a.get_width()
        h = self.image_a.get_height()
        screen.blit(self.image_a, self.pos_a, (0, 0, w, h))
