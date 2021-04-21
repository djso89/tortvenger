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
        self.surf.blit(self.image_hp, (395, 190),(0, 0, (self.curr_hp / self.HP) * hp_bar_w, self.image_hp.get_height()))

        self.fonth = pygame.font.Font('fonts/aileron_regular.otf', 60)
        
        self.hpstring = 'HP :  ' + str(self.curr_hp) + "  /  " + str(self.HP)
        self.hp_text = Borderline_Txt(self.hpstring, self.fonth, (0, 0, 0), (255, 255, 255), 5)
        self.surf.blit(self.hp_text, (495, 185))
        
        #initialize Packages gauges
        pkg_bar_w = self.image_pkg.get_width()
        self.surf.blit(self.image_pkg, (345, 410), (0, 0, (self.curr_pkgs / self.PKGS) * pkg_bar_w, self.image_pkg.get_height()))
        
        self.fontpkg = pygame.font.Font('fonts/aileron_regular.otf', 50)

        self.pkgstring =  'Pkgs :  ' + str(self.curr_pkgs) + '  /  ' + str(self.PKGS)
        self.pkgs_text = Borderline_Txt(self.pkgstring, self.fontpkg, (0, 0, 0), (255, 255, 255), 5)
        self.surf.blit(self.pkgs_text, (435, 395))
        self.surf = pygame.transform.scale(self.surf,(300, 150))
        self.surf.convert()

    def show_bars(self):
        self.surf = pygame.transform.scale(self.surf,(300, 150))
        self.surf.convert()



    def show_gauge(self):
        screen.blit(self.surf, (20, 20))


pygame.font.init()
goosterinfo = GST_Gauge()
