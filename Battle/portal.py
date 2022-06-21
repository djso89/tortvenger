#!/usr/bin/env python3
import pygame
from display import screen, vec
from spritesheet import SpriteSheet



class Portal(pygame.sprite.Sprite):
    """Portal Class """
    def __init__(self, x=0, y=0):
        pygame.sprite.Sprite.__init__(self)
        sprite_sheet = SpriteSheet('images/portal/warp_door.png')

        ss = sprite_sheet.sprite_sheet
        self.cnt = 0

        self.pos = vec((x, y))

        self.glow = []

        for i in range(0, 30, 1):
            width = ss.get_width()
            height = ss.get_height()
            image = sprite_sheet.get_image((width / 30) * i, 0, (width / 30), height)
            self.glow.append(image)

        self.image = self.glow[0]
        self.rect = self.image.get_rect()
        self.pos

    def glow_now(self):
        """animate the glowing portal """
        period = 5
        tot_cnt = period * 30
        if self.cnt >= tot_cnt:
            self.image = self.glow[29]
            self.cnt = 0
        else:
            self.image = self.glow[self.cnt // period]
            self.image.set_alpha(230)
            self.cnt += 1


    def render(self):
        """draw the portal on screen """
        self.glow_now()
        w = self.image.get_width()
        h = self.image.get_height()
        screen.blit(self.image, self.pos, (0, 0, w, h))
