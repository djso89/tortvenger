#!/usr/bin/env python3
from display import *
from fonts.bordertext import Borderline_Txt

class Ch_Sel_Profile():
    def __init__(self, name, bio_txt, Ch_info):
        self.bio_text = bio_txt
        self.name = name
        self.ch_info = Ch_info


    def load_profile_img(self, path):
        self.profile_img = pygame.image.load(path).convert_alpha()
