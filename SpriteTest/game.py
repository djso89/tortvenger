#!/usr/bin/env python3
import sys
import pygame
from display import *
from player import Player
from player import P1
from block import *




class Game:

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.bg = pygame.image.load("images/bg_level.png").convert()
        self.prd = 0

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
        # draw the background
        screen.blit(self.bg, (0, 0))

        #draw the platforms
        for block in platforms:
           screen.blit(block.surf, block.rect)

        P1.move()
        P1.animate()
        P1.render()


        if (self.prd >= 1):
            self.prd = 0;
            print("player Jump: {}".format(P1.jmp))
            print("PlayerY vel: {}".format(P1.vel.y))
            print("PlayerPos: {}".format(P1.pos))
            print("Player image: {}".format(P1.image))

        self.prd += 1
#        print("x and y: {}".format(pygame.mouse.get_pos()))
#        print("brick rect: {}".format(Brick.rect))
        pygame.display.flip()
        self.clock.tick(60)