#!/usr/bin/env python3
import pygame
import sys
from pygame.locals import *
from display import *
from stage import *
from spritesheet import SpriteSheet


class Character:
    pass


class Kuppa(pygame.sprite.Sprite):


    def loadimages(self):
        """ load all the kuppa action frames """
        sprite_sheet = SpriteSheet("images/krdy.png")
        sprite_sheetjmp = SpriteSheet("images/kjmp.png")

        ss = sprite_sheet.sprite_sheet
        ss_jmp = sprite_sheetjmp.sprite_sheet




        # load all right facing ready images
        for i in range(0, 2, 1):
            width = ss.get_width()
            height = ss.get_height()
            image = sprite_sheet.get_image(i * width/2, 0,
                                           width/2, height)
            self.ready_r.append(image)
            image = pygame.transform.flip(image, True, False)
            self.ready_l.append(image)


        # load all the right facing jmp images
        for i in range(0, 11, 1):
            width1 = ss_jmp.get_width()
            height1 = ss_jmp.get_height()
            image1 = sprite_sheetjmp.get_image(width1/11 * i, 0,
                                               width1/11, height1)
            self.jmp_r.append(image1)
            image1 = pygame.transform.flip(image1, True, False)
            self.jmp_l.append(image1)


    def __init__(self):
        """ initialize player """
        super().__init__()

        #counter for animating jumping
        self.cnt = 0
        self.cnt_swrd_draw = 0

        # action frames
        self.ready_r = []
        self.ready_l = []
        self.jmp_l = []
        self.jmp_r = []

        self.swrd_off = []

        # load the image
        self.loadimages()


        # kinematic factors
        self.pos = vec((0, 350))
        self.vel = vec(0,0)
        self.acc = vec(0, 0)

        # set the image the player start with
        self.image = self.ready_r[0]
        self.rect = self.image.get_rect(topleft=self.pos)

        # orientation and movement status
        self.orientation = 'right'
        self.jmp = True

        self.swd_on = False
        self.swd_drwn = False

    def draw_the_swrd(self):
        """ draw the swrd function.
        the function gets the key press reading
        and toggles swrd_on flaf to True to False """
        self.swd_on = not self.swd_on

    def move(self):
        """
        player move function
        this just simply sets acceleration
        according to the key presses
        """
        self.acc = vec(0, 3)
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT] and not pressed_keys[K_a]:
            self.acc.x = -ACC
            self.orientation = 'left'
        if pressed_keys[K_RIGHT] and not pressed_keys[K_a]:
            self.acc.x = ACC
            self.orientation = 'right'


    def jump(self):
        """ jump action """
        if self.jmp == True:
            self.vel.y = -40
            self.jmp = False

    def touchX(self, hits):
        #touch hits
        for block in hits:
            if self.vel.x > 0: #moving right
                self.rect.right = block.rect.left
            elif self.vel.x < 0:
                self.rect.left = block.rect.right
            self.pos.x = self.rect.x

    def touchXR(self, hits):
        #touch hits coming from right side
        for block in hits:
            if self.vel.x > 0:
                self.rect.right = block.rect.left
            self.pos.x = self.rect.x

    def touchXL(self, hits):
        #touch hits coming from right side
        for block in hits:
            if self.vel.x < 0:
                self.rect.left = block.rect.right
            self.pos.x = self.rect.x

    def touchYUD(self, hits):
        """ go through the list of collided sprites
        in Y direction"""
        for block in hits:
            if self.vel.y > 0:
                self.jmp = True
                self.cnt = 0
                self.vel.y = 0
                self.rect.bottom = block.rect.top
            elif self.vel.y < 0:
                self.rect.top = block.rect.bottom
                self.vel.y = 0
            self.pos.y = self.rect.y

    def touchYU(self, hits):
        """ check just for falling direction """
        for block in hits:
            if self.vel.y > 0:
                self.jmp = True
                self.cnt = 0
                self.vel.y = 0
                self.rect.bottom = block.rect.top
            self.pos.y = self.rect.y


    def collisionX(self):
        """check the collision in X direction """

        # touch bricks
        hitB = pygame.sprite.spritecollide(self, Bricks, False)
        self.touchX(hitB)

        #touch Cars
        hitC = pygame.sprite.spritecollide(self, Cars, False)
        self.touchX(hitC)




    def collisionY(self):
        """ check the collision in Y direction """

        #touch ground platforms
        hits = pygame.sprite.spritecollide(self, platforms, False)
        self.touchYU(hits)

        #touch Cars
        hitC = pygame.sprite.spritecollide(self, Cars, False)
        self.touchYU(hitC)

        # touch Bricks
        hitB = pygame.sprite.spritecollide(self, Bricks, False)
        self.touchYUD(hitB)

        #touch Plats
        hitP = pygame.sprite.spritecollide(self, Plats, False)
        self.touchYUD(hitP)

        #touch Bldgs
        hitBldg = pygame.sprite.spritecollide(self, Bldgs, False)
        self.touchYUD(hitBldg)

        #touch Steps
        hitSt = pygame.sprite.spritecollide(self, Steps, False)
        self.touchYUD(hitSt)


    def update(self):
        """
        function that calculates position
        and check collision
        """
        # move along the x direction
        self.acc.x += self.vel.x * FRIC
        self.vel.x += self.acc.x
        self.pos.x += self.vel.x + 0.5 * self.acc.x

        #left Most boundary of stage. Block the player from
        #moving further
        if self.pos.x < 0:
            self.pos.x = 0
        self.rect.x = self.pos.x

        if self.pos.x > WIDTH - self.rect.width:
            self.pos.x = WIDTH - self.rect.width
        self.rect.x = self.pos.x

        self.collisionX()

        #moving along the y direction
        self.vel.y += self.acc.y
        self.pos.y += self.vel.y + 0.5 * self.acc.y
        # assign the y coordinate to frame's y
        self.rect.y = self.pos.y

        self.collisionY()


    """ animation functions """


    def ani_move(self):
        """ animate the left right movement"""
        if self.orientation == 'right' and self.jmp == True:
            frame = (self.pos.x // 30) % len(self.ready_r)
            self.image = self.ready_r[int(frame)]


        elif self.orientation == 'left' and self.jmp == True:
            frame = (self.pos.x // 30) % len(self.ready_l)
            self.image = self.ready_l[int(frame)]



    def ani_jump(self):
        """ animate the jump """
        period = 2

        if self.jmp == False:
            if (self.cnt >= period * (len(self.jmp_r) -1 )):
                self.cnt = period * (len(self.jmp_r) -1 )
            else:
                self.cnt += 1
            if self.orientation == 'right':
                self.image = self.jmp_r[self.cnt//period]
            if self.orientation == 'left':
                self.image = self.jmp_l[self.cnt//period]



    def animate(self):
        """animate the player. """
        self.ani_move()
        self.ani_jump()

    def render(self):
        """ paste the player object into screen """

        # check for action flags
        if not self.swd_drwn:
            screen.blit(self.image, self.pos,
                        (0, 0, self.image.get_width(),
                         self.image.get_height()))



# initialize the player 1 object P1
P1 = Kuppa()
