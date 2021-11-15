#!/usr/bin/env python3
"""Stage 1-0 objects"""
from block import *
from display import *



alph = 68

Ground = Block()


Bricks = pygame.sprite.Group()
Brick1 = Block()
Brick1.loadBrick(411, 237)

Brick1_1 = Block()
Brick1_1.expand_brick(5411, 237, 33, 3)

Bricks.add(Brick1_1)

Brick1_2 = Block()
Brick1_2.loadBrick(6711, 337)

Bricks.add(Brick1_2)

Brick2 = Block()
Brick2.expand_brick(616, 408, 15, 1)
Bricks.add(Brick2)


Cars = pygame.sprite.Group()
Car1 = Block()
Car2 = Block()

#Car1.newBlock(193, 400, 65, 50, alph)
Car1.loadobject(123, 390, 'images/cars/Car1R.png')
Car2.loadobject(938, 340, 'images/cars/Car2.png')
Cars.add(Car1)
Cars.add(Car2)



Steps = pygame.sprite.Group()




Plats = pygame.sprite.Group()

Plat = Block()
Plat.expand_brick(0, 442, 10, 1, 'grey')
Plats.add(Plat)

Plat_1 = Block()
Plat_1.expand_brick(6300, 442, 10, 1, 'grey')
Plats.add(Plat_1)

Plat_2 = Block()
Plat_2.expand_brick(6700, 242, 20, 2, 'grey')
Plats.add(Plat_2)

Plat1 = Block()
Plat1.expand_brick(503, 190, 10, 1, 'grey')
Plats.add(Plat1)

Plat2 = Block()
Plat2.expand_brick(990, 52, 5, 1)
Plats.add(Plat2)

Plat2_1 = Block()
Plat2_1.expand_brick(4100, 300, 3, 1, 'grey')
Plats.add(Plat2_1)

Plat3 = Block()
Plat3.expand_brick(4430, 100, 10, 2)
Plats.add(Plat3)

Plat4 = Block()
Plat4.expand_brick(5200, 410, 8, 1)
Plats.add(Plat4)


Bldgs = pygame.sprite.Group()
Bldg1 = Block()
Bldg1.loadobject(2000, 94, 'images/buildings/hotel.png')


Bldg2 = Block()
Bldg2.loadobject(1300, 245, 'images/buildings/petsmart.png')

Bldg3 = Block()
Bldg3.loadobject(2520, 253, 'images/buildings/tjoes.png')

Bldg4 = Block()
Bldg4.loadobject(3320, 175, 'images/buildings/24hrFitness.png')

Bldgs.add(Bldg1)
Bldgs.add(Bldg2)
Bldgs.add(Bldg3)
Bldgs.add(Bldg4)


platforms = pygame.sprite.Group()
