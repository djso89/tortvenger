#!/usr/bin/python3
from __init__ import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((128, 255, 40))
        self.rect = self.surf.get_rect(center = (10, 450))

        self.pos = vec((15,430))
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def move(self):
        """ move the player """
        self.acc = vec(0,0)

        pressed_key = pygame.key.get_pressed()

        if pressed_key[K_LEFT]:
            self.acc.x = -ACC
        if pressed_key[K_RIGHT]:
            self.acc.x = ACC
        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        if self.pos.x > WIDTH:
            self.pos.x = WIDTH
        if self.pos.x < 0:
            self.pos.x = 0

        self.rect.midbottom = self.pos


class platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((WIDTH, 20))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(center = (WIDTH/2, HEIGHT - 10))
