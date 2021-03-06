#!/usr/bin/env python3

import pygame
import sys

class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, int(0.05 * self.game.DISPLAY_H), int(0.05 * self.game.DISPLAY_H))
        self.offset = - int(0.25 * self.game.DISPLAY_H)

    def draw_cursor(self):
        self.game.draw_text('*', int(0.035 * self.game.DISPLAY_H), self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
        self.startx, self.starty = self.mid_w, self.mid_h + int(0.250 * self.game.DISPLAY_H)
        self.optionsx, self.optionsy = self.mid_w, self.mid_h + int(0.300 * self.game.DISPLAY_H)
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + int(0.350 * self.game.DISPLAY_H)
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            self.bg = pygame.image.load('images/titlemockup.png')
            self.bg = pygame.transform.scale(self.bg, (self.game.DISPLAY_W , self.game.DISPLAY_H))
            self.game.display.blit(self.bg, (0, 0))
            #self.game.display.fill(self.game.BLACK)
            #self.game.draw_text('Main Menu', int(0.05 * self.game.DISPLAY_H), self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - int(0.15 * self.game.DISPLAY_H))
            self.game.draw_text("Start Game", int(0.04 * self.game.DISPLAY_H), self.startx, self.starty)
            self.game.draw_text("Options", int(0.04 * self.game.DISPLAY_H), self.optionsx, self.optionsy)
            self.game.draw_text("Credits", int(0.04 * self.game.DISPLAY_H), self.creditsx, self.creditsy)
            self.draw_cursor()
            self.blit_screen()


    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
        elif self.game.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.playing = True
            elif self.state == 'Options':
                self.game.curr_menu = self.game.options
            elif self.state == 'Credits':
                self.game.curr_menu = self.game.credits
            self.run_display = False

class OptionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Volume'
        self.volx, self.voly = self.mid_w, self.mid_h + int(0.05 * self.game.DISPLAY_H)
        self.controlsx, self.controlsy = self.mid_w, self.mid_h + int(0.10 * self.game.DISPLAY_H)
        self.cursor_rect.midtop = (self.volx + self.offset, self.voly)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('Options', int(0.05 * self.game.DISPLAY_H), self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - int(0.10 * self.game.DISPLAY_H))
            self.game.draw_text("Volume", int(0.035 * self.game.DISPLAY_H), self.volx, self.voly)
            self.game.draw_text("Controls", int(0.035 * self.game.DISPLAY_H), self.controlsx, self.controlsy)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == 'Volume':
                self.state = 'Controls'
                self.cursor_rect.midtop = (self.controlsx + self.offset, self.controlsy)
            elif self.state == 'Controls':
                self.state = 'Volume'
                self.cursor_rect.midtop = (self.volx + self.offset, self.voly)
        elif self.game.START_KEY:
            # TO-DO: Create a Volume Menu and a Controls Menu
            pass

class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Credits', int(0.05 * self.game.DISPLAY_H), self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - int(0.05 * self.game.DISPLAY_H))
            self.game.draw_text('Made by Nic Basilio and Daniel So', int(0.035 * self.game.DISPLAY_H), self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + int(0.10 * self.game.DISPLAY_H))
            self.blit_screen()