#!/usr/bin/env python3
"""Stage 1-0 objects"""
from block import *
from display import *



alph = 68

Ground = Block()

Bricks = pygame.sprite.Group()
Brick1 = Block()
Brick1.loadBrick(411, 237)

Bricks.add(Brick1)
#Bricks.add(Brick2)

Cars = pygame.sprite.Group()
Car1 = Block()
Car2 = Block()

Car1.newBlock(193, 400, 65, 50, alph)
Car2.newBlock(938, 359, 105, 50, alph)

Cars.add(Car1)
Cars.add(Car2)


Steps = pygame.sprite.Group()

Step0 = Block()
Step1 = Block()
Step2 = Block()
Step3 = Block()


Step0.newBlock(486, 508, 35, 4, alph)
Step1.newBlock(547, 455, 80, 10, alph)
Step2.newBlock(572, 443, 40, 6, alph)
Step3.newBlock(616, 408, 600, 4, alph)


Steps.add(Step3)

Plats = pygame.sprite.Group()

Plat = Block()
Plat.newBlock(0, 452, 253, 10, alph)
Plats.add(Plat)

Plat1 = Block()
Plat1.newBlock(503, 250, 233, 8, alph)
Plats.add(Plat1)

Plat2 = Block()
Plat2.newBlock(145, 534, 100, 50, alph)



Bldgs = pygame.sprite.Group()
Bldg1 = Block()
Bldg1.newBlock(840, 85, 166, 10, alph)
Bldgs.add(Bldg1)



platforms = pygame.sprite.Group()
platforms.add(Ground)
platforms.add(Step0)
platforms.add(Step1)
platforms.add(Step2)

cell_plats = pygame.sprite.Group()
cell_plats.add(Bldgs)
cell_plats.add(Plat1)
cell_plats.add(Ground)
cell_plats.add(Step3)
