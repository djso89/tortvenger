#!/usr/bin/env python3

from objects import *

PT1 = platform()
P1 = Player()


all_sprites = pygame.sprite.Group()
all_sprites.add(PT1)
all_sprites.add(P1)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    displaysurface.fill((0, 0, 0))

    for entity in all_sprites:
        displaysurface.blit(entity.surf, entity.rect)
    P1.move()
    print(P1.pos)

    pygame.display.update()
    FramePerSec.tick(FPS)
