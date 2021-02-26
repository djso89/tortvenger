#!/usr/bin/env python3
from player import *

OFF_SET_X = 2
OFF_SET_Y = 5


class K_Act(pygame.sprite.Sprite):
    """ Kuppa action class
    this is where K_Act reads P1 action flags
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
        sprite_sheet_swd_draw = SpriteSheet("images/k_swd_d.png")
        sprite_sheet_swd_rdy = SpriteSheet("images/k_swd_rdy.png")
        sprite_sheet_swd_cuts = SpriteSheet('images/k_swd_cut.png')
        sprite_sheet_swd_jmp = SpriteSheet('images/k_swd_jmp.png')


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
        for i in range(0, 14, 1):
            ss_swd_cuts = sprite_sheet_swd_cuts.sprite_sheet
            width = ss_swd_cuts.get_width()
            height = ss_swd_cuts.get_height()
            image = sprite_sheet_swd_cuts.get_image(i * width // 14, 0, width // 14, height)
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

        self.image = self.swrd_draw_r[0]
        self.rect = self.image.get_rect()

        # frame counter
        self.cnt_swrd_draw = 0
        self.cnt_swd_jmp = 0
        self.cnt_swd_cut = 0

        # sword cut flag and combo count
        self.ATK = False
        self.ATK_DONE = False
        self.atk_comb = 1

        # position of the Action Frames
        self.pos = vec((0, 0))

    def ani_turn_off(self):
        """ turn off the action frame """
        self.image = Surface((self.rect.width, self.rect.height), flags = SRCALPHA)
        self.image.fill((0, 0, 0, 0))

    def ani_cut(self):
        period = 2
        #            check the combo number
        if self.ATK:
            if self.atk_comb == 1:
                if (self.cnt_swd_cut >= period * 6):
                    self.cnt_swd_cut = 6 * period
                    #print("here")
                    # done cutting
                    self.ATK = False

                self.cnt_swd_cut += 1
                if (P1.orientation == 'right'):
                    self.image = self.swd_cut_r[self.cnt_swd_cut // period]

                if (P1.orientation == 'left'):
                    self.image = self.swd_cut_l[self.cnt_swd_cut // period]

        else:
            self.cnt_swd_cut = 0


    def ani_move(self):
        if P1.orientation == 'right' and self.cnt_swrd_draw // 2 == 11:
            frame = (self.pos.x // 30) % len(self.swrd_rdy_r)
            self.image = self.swrd_rdy_r[int(frame)]
        if P1.orientation == 'left' and self.cnt_swrd_draw // 2 == 11:
            frame = (self.pos.x // 30) % len(self.swrd_rdy_l)
            self.image = self.swrd_rdy_l[int(frame)]

    def ani_swd_out(self):
        """ animate pulling out the sword """
        period = 2
        max_period = period * (len(self.swrd_draw_r) - 1)
        P1.swd_drwn = True  # turn the Player frame off
        if (self.cnt_swrd_draw >= max_period):
            self.cnt_swrd_draw = max_period
        else:
            self.cnt_swrd_draw += 1
        if (P1.orientation == 'right'):
            self.image = self.swrd_draw_r[self.cnt_swrd_draw//period]
        if (P1.orientation == 'left'):
            self.image = self.swrd_draw_l[self.cnt_swrd_draw//period]

    def ani_swd_in(self):
        """ animate drawing back the sword """
        period = 4
        max_period = period * (len(self.swrd_draw_r) - 1)
        if (self.cnt_swrd_draw <= 0):
            self.cnt_swrd_draw = 0
            self.ani_turn_off()
            P1.swd_drwn = False # turn the Player frame on
        else:
            self.cnt_swrd_draw -= 1
            if (P1.orientation == 'right'):
                self.image = self.swrd_draw_r[self.cnt_swrd_draw//period]
            if (P1.orientation == 'left'):
                self.image = self.swrd_draw_l[self.cnt_swrd_draw//period]


    def ani_swd_draw(self):
        """animate drawing the swords """
        if P1.swd_on == True:
            self.ani_swd_out()
        elif P1.swd_on == False:
            self.ani_swd_in()

    def ani_swd_jmp(self):
        """ animate jump with sword in hands"""
        period = 2
        if P1.jmp == False and P1.swd_drwn:
            if (self.cnt_swd_jmp >= period * (len(self.swd_jmp_r) - 1)):
                self.cnt_swd_jmp = period * (len(self.swd_jmp_r) - 1)
            else:
                self.cnt_swd_jmp += 1
            if P1.orientation == 'right':
                self.image = self.swd_jmp_r[self.cnt_swd_jmp // period]
            if P1.orientation == 'left':
                self.image = self.swd_jmp_l[self.cnt_swd_jmp // period]
        else:
            self.cnt_swd_jmp = 0



    def ani_adj_offset(self, x_off, y_off):
        """adjust the action frame coordinate """
        if P1.orientation == 'right':
            self.pos.x = P1.pos.x - OFF_SET_X + x_off
            self.pos.y = P1.pos.y - P1.rect.height - OFF_SET_Y + y_off
        if P1.orientation == 'left':
            self.pos.x = P1.pos.x  -  (self.image.get_width()
                                       - P1.image.get_width()) + x_off
            self.pos.y = P1.pos.y - P1.rect.height - OFF_SET_Y + y_off


    def animate(self):
        """animate all the action frames """
        self.ani_swd_draw()
        self.ani_move()
        self.ani_swd_jmp()
        self.ani_cut()
        if self.ATK == False:
            self.ani_adj_offset(0, 0)
        elif self.ATK == True:
            self.ani_adj_offset(-2, 2)

    def render(self):
        self.animate()
        screen.blit(self.image, self.pos, self.rect)

KuppaAct = K_Act()
