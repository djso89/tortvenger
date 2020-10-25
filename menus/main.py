#!/usr/bin/env python3
import pygame
from game import Game

g = Game()
pygame.mixer.music.load('sounds/titlescreen.ogg')
pygame.mixer.music.play(-1)

while g.running:
    #pygame.mixer.music.load('sounds/titlescreen.ogg')
    #pygame.mixer.music.play(-1)
    g.curr_menu.display_menu()
    g.game_loop()
