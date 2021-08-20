#!/usr/bin/env python3
from profile import Ch_Sel_Profile
import pygame

vec = pygame.math.Vector2


character_data = {
    1: { 'name': 'Kuppa',
         'pos0': vec((50, 200)),
         'pos1': vec((50, 300)),
         'pos_info': vec((753, 71)),
         'frames0': 2,
         'frames1': 14,
         'frames2': 14,
         'period_0': 10,
         'period_1': 2
    },
    2: { 'name': 'Gooster',
         'pos0': vec((50, 200)),
         'pos1': vec((230, 350)),
         'pos_info': vec((780, 75)),
         'frames0': 2,
         'frames1': 9,
         'frames2': 9,
         'period_0': 10,
         'period_1': 3
    }
}

character_profiles = []

for data in character_data:
    prof = Ch_Sel_Profile(character_data[data]['name'])
    prof.pics.pos_0 = character_data[data]['pos0']
    prof.pics.pos_1 = character_data[data]['pos1']
    prof.pos_info = character_data[data]['pos_info']
    prof.load_profile_img(character_data[data]['frames0'],\
                          character_data[data]['frames1'],\
                          character_data[data]['frames2'])
    prof.period_0 = character_data[data]['period_0']
    prof.period_1 = character_data[data]['period_1']
    character_profiles.append(prof)
