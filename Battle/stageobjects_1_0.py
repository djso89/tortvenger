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
#Bricks.add(Cars)


Steps = pygame.sprite.Group()




Plats = pygame.sprite.Group()

Plat = Block()
Plat.expand_brick(0, 442, 10, 1, 'grey')
Plats.add(Plat)

Plat1 = Block()
Plat1.expand_brick(503, 190, 10, 1, 'grey')
Plats.add(Plat1)





Bldgs = pygame.sprite.Group()
Bldg1 = Block()
Bldg1.loadobject(1700, 103, 'images/buildings/hotel.png')


Bldg2 = Block()
Bldg2.loadobject(1300, 253, 'images/buildings/petsmart.png')

Bldg3 = Block()
Bldg3.loadobject(2020, 273, 'images/buildings/tjoes.png')

Bldgs.add(Bldg1)
Bldgs.add(Bldg2)
Bldgs.add(Bldg3)

platforms = pygame.sprite.Group()



cell_plats = pygame.sprite.Group()
cell_plats.add(Plat1)
cell_plats.add(Ground)
cell_plats.add(Brick2)
