#!/usr/bin/env python3
import pygame
from display import screen, vec
from spritesheet import SpriteSheet
import random

black = (0, 0, 0)

class M_Orb(pygame.sprite.Sprite):
    """ class Magic Orb class for Lettuce """
    def empty_frames(self):
        self.m_orb_r = []
        self.m_orb_l = []

    def load_images(self):
        sprite_sheet = SpriteSheet('images/magic_orb.png', black)
        ss = sprite_sheet.sprite_sheet
        for i in range(0, 10, 1):
            width = ss.get_width()
            height = ss.get_height()
            image = sprite_sheet.get_image(i * width / 10, 0, width / 10, height)
            self.m_orb_r.append(image)
            image = pygame.transform.flip(image, True, False)
            self.m_orb_l.append(image)

    def __init__(self, x, y, orientation):
        """initialize magic orb objects """
        super().__init__()
        self.empty_frames()
        self.load_images()

        self.pos = vec((x, y))
        self.reach = random.randint(320, 510)
        self.endpt_xr = self.pos.x + self.reach
        self.endpt_xl = self.pos.x - self.reach
        self.vel = vec(20, 0)
        self.image = self.m_orb_r[0]
        self.rect = self.image.get_rect(topleft=self.pos)
        self.orientation = orientation
        self.hitlanded = False

    def move(self):
        if self.orientation == 'right':
            self.pos.x += self.vel.x
            if self.pos.x >= self.endpt_xr:
                self.kill()
            if self.hitlanded:
                self.hitlanded = False
                self.kill()
        if self.orientation == 'left':
            self.pos.x -= self.vel.x
            if self.pos.x <= self.endpt_xl:
                self.kill()
            if self.hitlanded:
                self.hitlanded = False
                self.kill()
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y

    def ani_move(self):
        frame = (self.pos.x // 10) % len(self.m_orb_r)
        if self.orientation == 'left':
            self.image = self.m_orb_l[int(frame)]
        if self.orientation == 'right':
            self.image = self.m_orb_r[int(frame)]

    def animate(self):
        self.ani_move()

    def render(self):
        width = self.image.get_width()
        height = self.image.get_height()
        screen.blit(self.image, self.pos, (0, 0, width, height))

magic_orbs = pygame.sprite.Group()
