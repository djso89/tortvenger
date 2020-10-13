#!/usr/bin/env python3

from objects import *

db_jump = 0

for x in range(random.randint(5, 6)):
    C = True
    pl = platform()
    while C:
        pl = platform()
        C = check(pl, platforms)
    platforms.add(pl)
    all_sprites.add(pl)

while True:
    P1.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                P1.jump()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                P1.cancel_jump()

    if P1.rect.top <= HEIGHT / 3:
        P1.pos.y += abs(P1.vel.y)
        for plat in platforms:
            plat.rect.y += abs(P1.vel.y)
            if plat.rect.top >= HEIGHT:
                plat.kill()

    plat_gen()
    displaysurface.fill((0, 0, 0))


    for entity in all_sprites:
        displaysurface.blit(entity.surf, entity.rect)
        entity.move()
    # print(P1.pos)

    pygame.display.update()
    FramePerSec.tick(FPS)
