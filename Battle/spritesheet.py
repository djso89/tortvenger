#!/usr/bin/env python3
import pygame

class SpriteSheet(object):
    """ class used to grab the image from spritesheet """
    def __init__(self, filename, bck_drop_clr):
        """ constructor """

        # load the spritesheet
        self.sprite_sheet = pygame.image.load(filename).convert()
        self.bck_drop_clr = bck_drop_clr

    def get_image(self, x, y, width, height):
        """ grab a single image from (x, y) location of spritesheet
        and capture rectangle frame (cutout of spritesheet) width
        and height """
        image = pygame.Surface([width, height]).convert()
        # copy the sprite to the image surface
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))

        # if background has backdrop color, set it transparant
        image.set_colorkey(self.bck_drop_clr)

        # return the image
        return image
