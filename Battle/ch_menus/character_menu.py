import pygame
from display import screen
from bordertext import *

class Ch_Menu():
    def __init__(self):
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = -100

    def draw_cursor(self, x, y):
        font = pygame.font.Font('fonts/aileron_regular.otf', 15)
        text_surface = font.render('*', True, white)
        text_rect = text_surface.get_rect()
        text_rect.left = (x, y)
        screen.blit(text_surface, text_rect)

    def show_menu(self):
        screen.blit(self.menu_display, (0, 0))


class MainMenu(Menu):
    def __init__(self):
        Menu.__init__(self)
        self.state = "Start"
