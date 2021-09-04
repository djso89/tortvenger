from attr import LE_Attr
import pygame
from fonts.bordertext import Borderline_Txt
from display import screen
from gauge_imgs import *

black = (0, 0, 0)
white = (255, 255, 255)


class LE_Gauge(LE_Attr):
    def __init__(self):
        super().__init__()
        self.image_profile = pygame.image.load(le_pf_dir).convert_alpha()
        self.image_hp = pygame.image.load(le_hp_dir).convert()
        self.image_mp = pygame.image.load(le_mp_dir).convert()
        self.image_empty_bar = pygame.image.load(le_empty_dir).convert()
        self.image_bar_frame = pygame.image.load(le_bar_frame_dir).convert_alpha()

        self.surf = pygame.Surface((1000, 600), pygame.SRCALPHA, 32)\
                          .convert_alpha()

        self.fonth = pygame.font.Font('fonts/aileron_regular.otf', 50)
        self.fontm = pygame.font.Font('fonts/aileron_regular.otf', 50)

        self.surf.blit(self.image_profile, (0, 0))
        self.surf.blit(self.image_empty_bar, (433, 74))
        self.surf.blit(self.image_empty_bar, (440, 304))

        self.surf.blit(self.image_hp, (433, 74))
        self.surf.blit(self.image_bar_frame, (290, 43))

        self.surf.blit(self.image_mp, (440, 304))
        self.surf.blit(self.image_bar_frame, (290, 274))

        self.hp_bar_w = self.image_hp.get_width()
        self.hp_h = self.image_hp.get_height()
        self.width_per_hp = self.hp_bar_w / self.HP

        self.mp_bar_w = self.image_mp.get_width()

        self.chw = (self.curr_hp / self.HP) * self.hp_bar_w
        self.hpstring = 'HP: ' + str(self.curr_hp) + " / " + str(self.HP)
        self.hp_text = Borderline_Txt(self.hpstring, self.fonth,black, white, 5)
        self.mpstring = 'MP: ' + str(self.curr_mp) + " / " + str(self.MP)
        self.surf.blit(self.hp_text, (530, 90))
        self.mp_text = Borderline_Txt(self.mpstring, self.fontm,black, white, 5)
        self.surf.blit(self.hp_text, (530, 320))

    def show_bars(self):
        self.surf = pygame.transform.scale(self.surf,(432, 236))
        self.surf.convert()

    def show_gauge(self, pos):
        self.show_bars()
        screen.blit(self.surf, pos)


pygame.font.init()
Lettuceinfo = LE_Gauge()
