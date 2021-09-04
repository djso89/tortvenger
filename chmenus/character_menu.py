#!/usr/bin/python3
from display import *
from profile import Ch_Sel_Profile
from profile_list import character_profiles
from fonts.bordertext import Borderline_Txt


black = (0, 0, 0)
white = (255, 255, 255)
turquise = (0, 108, 117)
transparent = (0, 0, 0, 0)

class Ch_Menu():
    def __init__(self):
        pygame.font.init()
        self.run_display = True
        self.clock = pygame.time.Clock()

        self.bg_img = pygame.image.load("images/ch_sel_bg.png").convert()
        self.b_win = pygame.image.\
            load("images/windows/ch_sel_bio_win.png").convert_alpha()
        self.attr_win = pygame.image.\
            load('images/windows/ch_sel_attr_win.png').convert_alpha()

        """character selection text title on upper left corner """
        self.titlefont = pygame.font.Font("fonts/Serif_Bold_Italic.ttf", 55)
        self.title_txt = self.titlefont.render('', True, turquise)
        self.title_rect = self.title_txt.get_rect()
        self.title_rect.topleft = ((5, 5))
        self.title_txt = Borderline_Txt\
            ('Character', self.titlefont, turquise, white, 3)
        """ selection string  """
        self.title_txt1 = self.titlefont.render('', True, turquise)
        self.title_rect1 = self.title_txt1.get_rect()
        self.title_rect1.topleft = ((55, 55))
        self.title_txt1 = Borderline_Txt\
            ('Selection', self.titlefont, turquise, white, 3)

        """blinking arrow """
        self.arrows_LR = pygame.image.\
            load("images/arrows/ch_sel_arrows.png").convert_alpha()
        self.arrows_L = pygame.image.\
            load("images/arrows/ch_sel_l_arrow.png").convert_alpha()
        self.arrows_R = pygame.image.\
            load("images/arrows/ch_sel_r_arrow.png").convert_alpha()
        self.arrow_LF = pygame.Surface\
            ((150, 640), pygame.SRCALPHA, 32).convert_alpha()
        self.arrow_RF = pygame.Surface\
            ((1200, 640), pygame.SRCALPHA, 32).convert_alpha()

        self.bl_cnt = 0
        self.br_cnt = 0
        self.go_bl = False
        self.go_br = False

        """character profile """
        """list of data for single character profile """
        self.index_prof = 0
        self.num_prof_tot = len(character_profiles)
        self.curr_prof = character_profiles[self.index_prof]

    def show_arrows_LR(self):
        """display the both arrows """
        screen.blit(self.arrows_LR, (0, 0))

    def blink_arrow_L(self):
        """left arrow blinking animation
        when pressed left arrow
        """
        if self.go_bl:
            if self.bl_cnt >= 2:
                self.go_bl = False
                if self.index_prof == 0:
                    self.index_prof = 0
                else:
                    self.index_prof -= 1
                self.curr_prof = character_profiles[self.index_prof]
                self.bl_cnt = 0
            if self.index_prof != 0:
                self.arrow_LF.blit(self.arrows_L, (0, 0))
            self.bl_cnt += 1
        else:
            self.arrow_LF = pygame.Surface\
                ((150, 640), pygame.SRCALPHA, 32).convert_alpha()
        screen.blit(self.arrow_LF, (0, 0))

    def blink_arrow_R(self):
        """
        right arrow blinking animation
        when pressed right arrow key
        """
        if self.go_br:
            if self.br_cnt >= 2:
                self.go_br = False
                if self.index_prof == self.num_prof_tot - 1:
                    self.index_prof = self.num_prof_tot - 1
                else:
                    self.index_prof += 1
                self.curr_prof = character_profiles[self.index_prof]
                self.br_cnt = 0
            if self.index_prof != self.num_prof_tot - 1:
                self.arrow_RF.blit(self.arrows_R, (0, 0))
            self.br_cnt += 1
        else:
            self.arrow_RF = pygame.Surface\
                ((1200, 640), pygame.SRCALPHA, 32).convert_alpha()
        screen.blit(self.arrow_RF, (0, 0))


    def bio_window(self):
        """ show the transparent bio window"""
        screen.blit(self.b_win, (0, 0))

    def attr_window(self):
        """ show the transparent attribute window """
        screen.blit(self.attr_win, (0, 0))

    def title_name(self):
        """display the title name of menu """
        screen.blit(self.title_txt, self.title_rect)
        screen.blit(self.title_txt1, self.title_rect1)


    def show_menu(self):
        """
        display the menu items
        on the screen
        """
        # background image and title font
        screen.blit(self.bg_img, (0, 0))
        self.title_name()

        # show the arrows
        self.show_arrows_LR()
        # blinking arrows when user presses keys
        self.blink_arrow_L()
        self.blink_arrow_R()

        # show the bio and attribute windows
        self.bio_window()
        self.attr_window()

        # show the character roster
        self.curr_prof.show_pics() # period0 and period1
