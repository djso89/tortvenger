#!/usr/bin/env python3
import sys
import pygame
from display import *
from player import Player
from player import P1
from block import *




class Game:

    def __init__(self):
  #      self.settings = Settings()
        pygame.init()
        self.clock = pygame.time.Clock()
        self.bg = pygame.image.load("images/bg_level.png").convert()
        self.prd = 0
#        self.screen = pygame.display.set_mode(
 #          (self.settings.screen_width, self.settings.screen_height))

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()


    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if (event.type == pygame.KEYDOWN):
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_UP:
                    P1.jump()
            if (event.type == pygame.KEYDOWN):
                if event.key == pygame.K_UP:
                    P1.jump()


    def _update_screen(self):
        screen.fill(setting.bg_color)
        P1.update()
        screen.blit(self.bg, (0, 0))
        for block in platforms:
           screen.blit(block.surf, block.rect)

        P1.render(screen)
        P1.move()
        # if (self.prd >= 100):
        #     self.prd = 0;
        #     print("playerX: {}, Y: {}".format(P1.pos.x, P1.pos.y))
        #     print("playerRect midbottom: {}".format(P1.rect.midbottom))

        # self.prd += 1
        pygame.display.flip()
        self.clock.tick(60)
