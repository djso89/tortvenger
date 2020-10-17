#!/usr/bin/env python3
import sys
import pygame
from display import *
from player import Player
from block import *



player = Player(300, 350)

class Game:

    def __init__(self):
  #      self.settings = Settings()
        self.clock = pygame.time.Clock()
#        self.screen = pygame.display.set_mode(
 #          (self.settings.screen_width, self.settings.screen_height))
        self.movex = 0
        self.movey = 0

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()


    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if (event.type == pygame.KEYDOWN):
                if event.key == pygame.K_q:
                    sys.exit()
                elif event.key == pygame.K_RIGHT:
                    self.movex = 5

                elif event.key == pygame.K_LEFT:
                    self.movex = -5
                elif event.key == pygame.K_UP:
                    player.jump()
            if (event.type == pygame.KEYUP):
                if event.key == pygame.K_RIGHT:
                    self.movex = 0
                elif event.key == pygame.K_LEFT:
                    self.movex = 0

    def _update_screen(self):
        screen.fill(setting.bg_color)

        for block in platforms:
            block.render(screen)
        player.pos.x += self.movex

        player.update()
        player.render(screen)
        self.clock.tick(60)
        pygame.display.flip()
