#!/usr/bin/python3
from __init__ import *


class Player(pygame.sprite.Sprite):
    def __init__(self):
        """ draw the player Sprite """
        super().__init__()
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((255, 255, 0))
        self.rect = self.surf.get_rect()
        self.jumping = False
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
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if self.vel.y > 0:
            if hits:
                if self.pos.y < hits[0].rect.bottom:
                    self.pos.y = hits[0].rect.top + 1
                    self.vel.y = 0
                    self.jumping = False

    def jump(self):
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if hits and not self.jumping:
            self.jumping = True
            self.vel.y = -15

    def cancel_jump(self):
        if self.jumping:
            if self.vel.y < -3:
                self.vel.y = -3


class platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((random.randint(50, 100), 12))
        self.surf.fill((0, 255, 0))
        self.rect = self.surf.get_rect(center = (random.randint(0, WIDTH - 10)
                                     ,random.randint(0, HEIGHT - 30)))


    def move(self):
        pass


def check(platform, groupies):
    """ check if platforms are too close """
    if pygame.sprite.spritecollideany(platform, groupies):
        return True
    else:
        for entity in groupies:
            if entity == platform:
                continue
            if (abs(platform.rect.top - entity.rect.bottom) < 40) \
               and (abs(platform.rect.bottom - entity.rect.top) < 40):
                return True
        C = False

def plat_gen():
    while len(platforms) < 7:
        width = random.randrange(50, 100)
        p = platform()
        C = True

        while C:
            p = platform()
            p.rect.center = (random.randrange(0, WIDTH - width),
                         random.randrange(-50, 0))
            C = check(p, platforms)
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
