#!/usr/bin/env python3

from objects import *

db_jump = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                P1.jump()


    displaysurface.fill((0, 0, 0))


    P1.update()
    for entity in all_sprites:
        displaysurface.blit(entity.surf, entity.rect)
        entity.move()
    # print(P1.pos)

    pygame.display.update()
    FramePerSec.tick(FPS)
