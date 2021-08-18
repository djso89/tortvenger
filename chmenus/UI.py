#!/usr/bin/env python3
import pygame
import sys
from character_menu import Ch_Menu

class Ch_Sel_UI(Ch_Menu):
    def __init__(self):
        super().__init__()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()
            if (event.type == pygame.KEYDOWN):
                if event.key == pygame.K_q:
                    pygame.display.quit()
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_LEFT:
                    self.go_bl = True
                if event.key == pygame.K_RIGHT:
                    self.go_br = True


    def _update_screen(self):
        self.show_menu()
        pygame.display.flip()
        self.clock.tick(60)

    def run_ch_sel(self):
        """ run the character selection menu """
        while self.run_display:
            self._check_events()
            self._update_screen()
