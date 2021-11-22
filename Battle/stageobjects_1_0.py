#!/usr/bin/env python3
"""Stage 1-0 objects"""
from block import *
from display import *



alph = 68


Bricks = pygame.sprite.Group()
Cars = pygame.sprite.Group()
Plats = pygame.sprite.Group()
Steps = pygame.sprite.Group()
Bldgs = pygame.sprite.Group()
platforms = pygame.sprite.Group()

# objects located from 0 to 1200 in x axis
Brick1 = Block()
Brick1.loadBrick(411, 237)


Brick1_2 = Block()
Brick1_2.expand_brick(616, 408, 15, 1)
Bricks.add(Brick1_2)


Car1_1 = Block()
Car1_2 = Block()

Car1_1.loadobject(123, 390, 'images/cars/Car1R.png')
Car1_2.loadobject(938, 340, 'images/cars/Car2.png')
Cars.add(Car1_1)
Cars.add(Car1_2)

Plat1_1 = Block()
Plat1_1.expand_brick(0, 442, 10, 1, 'grey')
Plats.add(Plat1_1)

Plat1_2 = Block()
Plat1_2.expand_brick(503, 190, 10, 1, 'grey')
Plats.add(Plat1_2)

Plat1_3 = Block()
Plat1_3.expand_brick(990, 52, 5, 1)
Plats.add(Plat1_3)



# objects located in between 1200 - 2400 in x-axis
Bldg2_1 = Block()
Bldg2_1.loadobject(2000, 94, 'images/buildings/hotel.png')


PS2_1 = Block()
PS2_1.loadobject(1300, 245, 'images/buildings/petsmart.png')

Bldgs.add(Bldg2_1)
Bldgs.add(PS2_1)


# x-axis : 2400 - 3600
Bldg3_1 = Block()
Bldg3_1.loadobject(2520, 253, 'images/buildings/tjoes.png')
Bldgs.add(Bldg3_1)


Bldg3_2 = Block()
Bldg3_2.loadobject(3320, 175, 'images/buildings/24hrFitness.png')
Bldgs.add(Bldg3_2)

# x-axis 3600 - 4800
Brick4_1 = Block()
Brick4_1.loadBrick(3902, 410, 'whitegrey')
Bricks.add(Brick4_1)


Plat4_1 = Block()
Plat4_1.expand_brick(4123, 284, 3, 1, 'grey')
Plats.add(Plat4_1)

Plat4_2 = Block()
Plat4_2.expand_brick(4268, 194, 10, 2)
Plats.add(Plat4_2)


# x-axis 4800 - 6000
Plat5_1 = Block()
Plat5_1.expand_brick(4674, 289, 16, 1)
Plats.add(Plat5_1)


Brick5_1 = Block()
Brick5_1.expand_brick(5411, 221, 24, 3)
Bricks.add(Brick5_1)

Brick5_2 = Block()
Brick5_2.loadBrick(5333, 432)
Bricks.add(Brick5_2)


# x-axis 6000 - 7200
Brick6_1 = Block()
Brick6_1.loadBrick(6711, 337)
Bricks.add(Brick6_1)

Brick6_2 = Block()
Brick6_2.loadBrick(6424, 365, 'grey')
Bricks.add(Brick6_2)


Plat6_1 = Block()
Plat6_1.expand_brick(6914, 157, 20, 2, 'grey')
Plats.add(Plat6_1)

# x-axis 7200 - 8400
Plat7_1 = Block()
Plat7_1.expand_brick(7595, 388, 10, 1, 'grey')
Plats.add(Plat7_1)


Plat7_2 = Block()
Plat7_2.expand_brick(7966, 214, 23, 2)
Plats.add(Plat7_2)

# x-axis 8400 - 9600
Brick8_1 = Block()
Brick8_1.loadBrick(8910, 222, 'grey')
Bricks.add(Brick8_1)



Brick8_2 = Block()
Brick8_2.expand_brick(9019, 139, 5, 1)
Bricks.add(Brick8_2)

Brick8_3 = Block()
Brick8_3.expand_brick(9284, 352, 3, 2)
Bricks.add(Brick8_3)

Plat8_1 = Block()
Plat8_1.expand_brick(9530, 290, 10, 2)
Plats.add(Plat8_1)


# x-axis 9600 - 10800
Brick9_1 = Block()
Brick9_1.loadBrick(9996, 249, 'grey')
Bricks.add(Brick9_1)

Brick9_2 = Block()
Brick9_2.loadBrick(10155, 404, 'whitegrey')
Bricks.add(Brick9_2)

Brick9_3 = Block()
Brick9_3.loadBrick(10230, 157, 'grey')
Bricks.add(Brick9_3)

Plat9_1 = Block()
Plat9_1.expand_brick(10508, 363, 24, 2, 'grey')
Plats.add(Plat9_1)

Plat9_2 = Block()
Plat9_2.expand_brick(10501, 123, 24, 2, 'grey')
Plats.add(Plat9_2)

# x-axis 10800 - 12000
PS10_1 = Block()
PS10_1.loadobject(11760, 194, 'images/buildings/petsmart.png')
Bldgs.add(PS10_1)


Plat10_1 = Block()
Plat10_1.expand_brick(11684, 430, 10, 1, 'grey')
Plats.add(Plat10_1)


Brick10_1 = Block()
Brick10_1.loadBrick(11573, 250, 'grey')
Bricks.add(Brick10_1)


Brick10_2 = Block()
Brick10_2.loadBrick(11414, 150)
Bricks.add(Brick10_2)
