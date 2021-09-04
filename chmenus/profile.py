#!/usr/bin/env python3
from display import *
from fonts.bordertext import Borderline_Txt
from profile_attr import Profile_ATTR
from profile_attr_bar import ATTR_BAR
from ani_frame import Ani_Frame
from gauge_import import *


black = (0, 0, 0)
green = (0, 216, 65)
white = (255, 255, 255)

def paragraph_text(surface, text, pos, \
                   font, color=pygame.Color('black')):
    """print out the long string from text file """
    words = [word.split(' ') for word in text.splitlines()]
    space = font.size(' ')[0]
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            word_surface = Borderline_Txt\
                (word, font, color, white, 2)
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.

class Ch_Sel_Profile():
    """Character Selection Profile Class """
    def __init__(self, name):
        """constructor """
        """displaying the name of character """
        self.name = name
        self.namefont = pygame.font.Font("fonts/CP-&-TRANS.ttf", 80)
        self.name_txt = self.namefont.render(self.name, True, black)
        self.name_txt = Borderline_Txt\
            (self.name, self.namefont, green, white, 3)
        self.name_rect = self.name_txt.get_rect()
        self.name_rect.topleft = ((402, 82))

        """period values for animated profile pics """
        self.period_0 = 1
        self.period_1 = 1

        """character biography """
        bio_path = "bio/" + "{}/{}_Bio.txt".\
            format(self.name, self.name)
        bio_txt_file = open(bio_path, "r")
        self.bio_text = bio_txt_file.read()
        bio_txt_file.close()

        self.bio_font = pygame.font.Font("fonts/aileron_regular.otf", 55)
        self.bio_title = self.bio_font.render("Bio", True, black)
        self.bio_title = Borderline_Txt\
            ("Bio", self.bio_font, black, white, 2)
        self.bio_title_rect = self.bio_title.get_rect()
        self.bio_title_rect.topleft = ((400, 180))

        self.bio_text_font = pygame.font.Font("fonts/aileron_regular.otf", 20)

        gauge_name = self.name + 'info'
        self.ch_info = eval(gauge_name)
        self.pos_info = vec((0, 0))
        self.pics = Ani_Frame()

        """profile_attribute """
        self.prof_attr = Profile_ATTR()
        self.attr_bars = ATTR_BAR()


    def load_profile_img(self, fr_tot0, fr_tot1, fr_tot2):
        """load the profile sprites based on character name """
        path = "images/profiles/"\
            + self.name + "/" + self.name +\
            "_0.png"
        self.pics.load_frame0(path, fr_tot0)
        path = "images/profiles/"\
            + self.name + "/" + self.name +\
            "_1.png"
        self.pics.load_frame1(path, fr_tot1)
        path = "images/profiles/"\
            + self.name + "/" + self.name +\
            "_2.png"
        self.pics.load_frame1(path, fr_tot2)

    def show_name(self):
        """show the character's name """
        screen.blit(self.name_txt, self.name_rect)

    def show_bio(self):
        """show the character's bio """
        screen.blit(self.bio_title, self.bio_title_rect)
        paragraph_text(screen, self.bio_text, (407, 246), self.bio_text_font)

    def show_attr(self):
        """display the Attribute names """
        screen.blit(self.prof_attr.attr_atk_name, \
                    self.prof_attr.attr_atk_name_rect)
        screen.blit(self.prof_attr.attr_def_name, \
                    self.prof_attr.attr_def_name_rect)
        screen.blit(self.prof_attr.attr_dex_name, \
                    self.prof_attr.attr_dex_name_rect)
        screen.blit(self.prof_attr.attr_luk_name, \
                    self.prof_attr.attr_luk_name_rect)
        """display the attribute bars along with its values"""
        self.attr_bars.set_bars(self.ch_info)
        screen.blit(self.attr_bars.bar_img, (942, 310))

    def show_pics(self):
        """animate the character profile pics """
        self.ch_info.show_gauge(self.pos_info)
        self.show_name()
        self.show_bio()
        self.show_attr()
        self.pics.show_frame(self.period_0, self.period_1)
