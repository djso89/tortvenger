from attr import K_Attr
import pygame
from fonts.bordertext import Borderline_Txt
from display import screen
from troopakuppa19.kuppabattle import P1
from gauge_imgs import *

class K_Gauge(K_Attr):
    def __init__(self):
        super().__init__()
        self.image_pf = pygame.image.load(pf_dir)
        self.image_hp = pygame.image.load(hp_dir).convert()
        self.image_ki = pygame.image.load(ki_dir).convert()
        self.image_kp = pygame.image.load(kp_dir)
        self.image_keh = pygame.image.load(keh_dir).convert()

        self.surf = pygame.Surface((1000, 600), pygame.SRCALPHA, 32).convert_alpha()

        self.fonth = pygame.font.Font('fonts/aileron_regular.otf', 80)
        self.fontk = pygame.font.Font('fonts/aileron_regular.otf', 80)

        self.pf = pygame.Surface((453, 500), pygame.SRCALPHA, 32).convert_alpha()
        self.pf.blit(self.image_pf, (0, 0))
        self.pf.blit(self.image_kp, (0, 0))



        self.surf.blit(self.image_keh, (453, 100))
        self.hp_bar_w = self.image_hp.get_width()
        self.width_per_hp = self.hp_bar_w / self.HP

        self.surf.blit(self.image_hp, (485, 133), (0, 0, (self.curr_hp / self. HP)* self.hp_bar_w, self.image_hp.get_height()))

        self.hpstring = 'H P :  ' + str(self.curr_hp) + "  /  " + str(self.HP)
        self.hp_text = Borderline_Txt(self.hpstring, self.fonth, (0, 0, 0), (255, 255, 255), 5)
        self.surf.blit(self.hp_text, (500, 0))



        self.surf.blit(self.image_keh, (453, 328))
        self.ki_bar_w = self.image_ki.get_width()
        self.width_per_ki = self.ki_bar_w / self.KI
        self.surf.blit(self.image_ki, (485, 363), (0, 0, self.ki_bar_w, self.image_ki.get_height()))



        self.kistring = 'K I :  ' + str(self.curr_ki) +'  /  ' + str(self.KI)
        self.ki_text = Borderline_Txt(self.kistring, self.fontk, (0, 0, 0), (255, 255, 255), 5)
        self.surf.blit(self.ki_text, (500, 220))


    def show_profile(self):
        self.pf = pygame.transform.scale(self.pf, (140, 150))

    def update_bars(self):
        self.surf = pygame.Surface((1000, 600), pygame.SRCALPHA, 32)
        self.surf = self.surf.convert_alpha()
        self.surf.blit(self.image_keh, (453, 100))
        self.hp_bar_w = self.image_hp.get_width()
        self.width_per_hp = self.hp_bar_w / self.HP

        self.surf.blit(self.image_hp, (485, 133), (0, 0, (self.curr_hp / self. HP)* self.hp_bar_w, self.image_hp.get_height()))

        self.hpstring = 'H P :  ' + str(self.curr_hp) + "  /  " + str(self.HP)
        self.hp_text = Borderline_Txt(self.hpstring, self.fonth, (0, 0, 0), (255, 255, 255), 5)
        self.surf.blit(self.hp_text, (500, 0))

        self.surf.blit(self.image_keh, (453, 328))
        self.ki_bar_w = self.image_ki.get_width()
        self.width_per_ki = self.ki_bar_w / self.KI
        self.surf.blit(self.image_ki, (485, 363), (0, 0, self.ki_bar_w, self.image_ki.get_height()))



        self.kistring = 'K I :  ' + str(self.curr_ki) +'  /  ' + str(self.KI)
        self.ki_text = Borderline_Txt(self.kistring, self.fontk, (0, 0, 0), (255, 255, 255), 5)
        self.surf.blit(self.ki_text, (500, 220))


    def show_bars(self):
        if P1.cell_atk_k:
            self.update_bars()
        self.surf.convert()
        self.surf = pygame.transform.scale(self.surf,(300, 150))



    def show_gauge(self):
        self.show_profile()
        #self.show_bars()

        screen.blit(self.pf, (20, 20))
        #screen.blit(self.surf, (20, 20))


pygame.font.init()
kuppainfo = K_Gauge()
