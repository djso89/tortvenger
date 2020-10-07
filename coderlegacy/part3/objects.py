#!/usr/bin/python3
from __init__ import *


class Player(pygame.sprite.Sprite):
    def __init__(self):
        """ draw the player Sprite """
        super().__init__()
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((128, 255, 40))
        self.rect = self.surf.get_rect()
        self.db_jmp = 0
        self.pos = vec((10,385))
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def move(self):
        """ move the player """
        self.acc = vec(0,0.5)

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

    def update(self):
        hits = pygame.sprite.spritecollide(P1, platforms, False)
        if P1.vel.y > 0:
            if hits:
                self.pos.y = hits[0].rect.top + 1
                self.vel.y = 0

    def jump(self):
        hits = pygame.sprite.spritecollide(P1, platforms, False)
        if hits:
            self.vel.y = -15


class platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((random.randint(50, 100), 12))
        self.surf.fill((0, 255, 0))
        self.rect = self.surf.get_rect(center = (random.randint(0, WIDTH - 10)
                                     ,random.randint(0, HEIGHT - 30)))


    def move(self):
        pass

def plat_gen():
    while len(platforms) < 7:
        width = random.randrange(50, 100)
        p = platform()
        p.rect.center = (random.randrange(0, WIDTH - width),
                         random.randrange(-50, 0))
        platforms.add(p)
        all_sprites.add(p)

PT1 = platform()
P1 = Player()

PT1.surf = pygame.Surface((WIDTH, 20))
PT1.surf.fill((255,0, 0))
PT1.rect = PT1.surf.get_rect(center = (WIDTH/2, HEIGHT - 10))

all_sprites = pygame.sprite.Group()
all_sprites.add(PT1)
all_sprites.add(P1)

platforms = pygame.sprite.Group()
platforms.add(PT1)
