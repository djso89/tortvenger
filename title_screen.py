#!/usr/bin/env python3

import pygame
import sys
from pygame.locals import *
pygame.init()

#size = width, height = 2048, 1536
black = 0, 0, 0
white = 255, 255, 255

pygame.display.set_caption('Tortvenger - Main Menu')
info = pygame.display.Info()
flags = pygame.RESIZABLE
screen = pygame.display.set_mode((info.current_w, info.current_h), flags)

font = pygame.font.Font('AmericanTypewriter.ttc', 36)
bg = pygame.image.load('titlemockup.png')
bg = pygame.transform.scale(bg, (info.current_w, info.current_h))

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, 1, white)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)

def main_menu():
    while True:
        screen.blit(bg, (0, 0))
        #screen.fill(black)
        text = 'press any key to start'
        draw_text(text, font, white, screen, info.current_w / 2,
                  info.current_h / 1.25)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                screen.fill(black)

        pygame.display.update()

main_menu()
