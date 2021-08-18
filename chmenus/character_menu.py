#!/usr/bin/python3
from display import *
from fonts.bordertext import Borderline_Txt

white = (255, 255, 255)
turquise = (0, 108, 117)
transparent = (0, 0, 0, 0)

class Ch_Menu():
    def __init__(self):
        pygame.font.init()
        self.run_display = True
        self.clock = pygame.time.Clock()
        self.offset = -100
        self.bg_img = pygame.image.load("images/ch_sel_bg.png").convert()

        self.titlefont = pygame.font.Font("fonts/Serif_Bold_Italic.ttf", 55)

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
        self.crs_pos = vec((0, 0))
        self.bl_cnt = 0
        self.br_cnt = 0
        self.go_bl = False
        self.go_br = False

    def show_arrows_LR(self):
        screen.blit(self.arrows_LR, (0, 0))

    def blink_arrow_L(self):
        if self.go_bl:
            if self.bl_cnt >= 2:
                self.go_bl = False
                self.bl_cnt = 0
            self.arrow_LF.blit(self.arrows_L, (0, 0))
            self.bl_cnt += 1
        else:
            self.arrow_LF = pygame.Surface\
                ((150, 640), pygame.SRCALPHA, 32).convert_alpha()
        screen.blit(self.arrow_LF, (0, 0))

    def blink_arrow_R(self):
        if self.go_br:
            if self.br_cnt >= 2:
                self.go_br = False
                self.br_cnt = 0
            self.arrow_RF.blit(self.arrows_R, (0, 0))
            self.br_cnt += 1
        else:
            self.arrow_RF = pygame.Surface\
                ((1200, 640), pygame.SRCALPHA, 32).convert_alpha()
        screen.blit(self.arrow_RF, (0, 0))


    def bio_window(self):
        b_win = pygame.image.\
            load("images/windows/ch_sel_bio_win.png").convert_alpha()
        screen.blit(b_win, (0, 0))

    def attr_window(self):
        attr_win = pygame.image.\
            load('images/windows/ch_sel_attr_win.png').convert_alpha()
        screen.blit(attr_win, (0, 0))

    def title_name(self):
        title_txt = self.titlefont.render('', True, turquise)
        title_rect = title_txt.get_rect()
        title_rect.topleft = ((5, 5))
        title_txt = Borderline_Txt\
            ('Character', self.titlefont, turquise, white, 3)

        screen.blit(title_txt, title_rect)
        title_txt = Borderline_Txt\
            ('Selection', self.titlefont, turquise, white, 3)
        title_rect.topleft = ((55, 55))
        screen.blit(title_txt, title_rect)


    def move_cursor(self, x, y):
        self.crs_pos.x += x
        self.crs_pos.y += y


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
