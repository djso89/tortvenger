from attr import GST_Attr
import pygame
from fonts.bordertext import Borderline_Txt
from display import screen
from gauge_imgs import *

black = (0, 0, 0)
white = (255, 255, 255)


class GST_Gauge(GST_Attr):
    def __init__(self):
        super().__init__()
        self.update_bar = False
        self.image_pf = pygame.image.load(gst_pf_dir).convert_alpha()
        self.image_hp = pygame.image.load(gst_hp_dir).convert_alpha()
        self.image_pkg = pygame.image.load(gst_pkg_dir).convert_alpha()


        self.surf = pygame.Surface((1000, 600), pygame.SRCALPHA, 32)\
                          .convert_alpha()

        self.surf.blit(self.image_pf, (0, 0))

        #initialize the hp bar
        hp_bar_w = self.image_hp.get_width()
        hp_h = self.image_hp.get_height()
        self.hp_surf = pygame.Surface((hp_bar_w, hp_h), pygame.SRCALPHA, 32)\
                             .convert_alpha()
        hp_len =  (self.curr_hp / self.HP) * hp_bar_w
        self.hp_surf.blit(self.image_hp, (0, 0))
        self.surf.blit(self.hp_surf, (395, 190),(0, 0, hp_len, hp_h))

        self.fonth = pygame.font.Font('fonts/aileron_regular.otf', 70)

        self.hpstring = 'H P :  ' + str(self.curr_hp) + "  /  " + str(self.HP)
        self.hp_text = Borderline_Txt(self.hpstring, self.fonth, black, white, 10)
        self.surf.blit(self.hp_text, (465, 180))



        #initialize Packages gauges
        pkg_bar_w = self.image_pkg.get_width()
        pkg_h = self.image_pkg.get_height()
        self.pkg_surf = pygame.Surface((pkg_bar_w, pkg_h), pygame.SRCALPHA, 32)\
                             .convert_alpha()
        pkg_len = (self.curr_pkgs / self.PKGS) * pkg_bar_w
        self.pkg_surf.blit(self.image_pkg, (0, 0))
        self.surf.blit(self.pkg_surf, (345, 410), (0, 0, pkg_len, pkg_h))

        self.fontpkg = pygame.font.Font('fonts/aileron_regular.otf', 55)

        self.pkgstring =  'Pkgs :  ' + str(self.curr_pkgs) + '  /  ' + str(self.PKGS)
        self.pkgs_text = Borderline_Txt(self.pkgstring, self.fontpkg, black, white, 10)
        self.surf.blit(self.pkgs_text, (435, 395))
        self.surf = pygame.transform.scale(self.surf,(300, 150))
        self.surf.convert()

    def update_bars(self):
        self.surf = pygame.Surface((1000, 600), pygame.SRCALPHA, 32)\
                          .convert_alpha()
        self.surf.blit(self.image_pf, (0, 0))
        #update the hp bar
        hp_bar_w = self.image_hp.get_width()
        hp_h = self.image_hp.get_height()
        self.hp_surf = pygame.Surface((hp_bar_w, hp_h), pygame.SRCALPHA, 32)\
                             .convert_alpha()
        self.hp_surf.blit(self.image_hp, (0, 0))
        hp_len =  (self.curr_hp / self.HP) * hp_bar_w
        self.surf.blit(self.hp_surf, (395, 190),(0, 0, hp_len, hp_h))
        self.hpstring = 'H P :  ' + str(self.curr_hp) + "  /  " + str(self.HP)
        self.hp_text = Borderline_Txt(self.hpstring, self.fonth, black, white, 10)
        self.surf.blit(self.hp_text, (465, 180))

        #initialize Packages gauges
        pkg_bar_w = self.image_pkg.get_width()
        pkg_h = self.image_pkg.get_height()
        self.pkg_surf = pygame.Surface((pkg_bar_w, pkg_h), pygame.SRCALPHA, 32)\
                             .convert_alpha()
        pkg_len = (self.curr_pkgs / self.PKGS) * pkg_bar_w
        self.pkg_surf.blit(self.image_pkg, (0, 0))
        self.surf.blit(self.pkg_surf, (345, 410), (0, 0, pkg_len, pkg_h))


        self.pkgstring = 'Pkgs :  ' + str(self.curr_pkgs) + '  /  ' + str(self.PKGS)
        self.pkgs_text = Borderline_Txt(self.pkgstring, self.fontpkg, black, white, 10)
        self.surf.blit(self.pkgs_text, (435, 395))
        self.surf = pygame.transform.scale(self.surf,(300, 150))
        self.surf.convert()

    def show_gauge(self):
        if self.update_bar:
            self.update_bars()
            self.update_bar = False
        screen.blit(self.surf, (20, 20))


pygame.font.init()
goosterinfo = GST_Gauge()
