#!/usr/bin/env python3
import pygame
import sys
from pygame.locals import *
from display import *
from stage import ST1
from spritesheet import SpriteSheet



class Kuppa(pygame.sprite.Sprite):


    def loadimages(self):
        """ load all the kuppa action frames """
        sprite_sheet = SpriteSheet("images/troopakuppa19/krdy.png", (0, 0, 0))
        sprite_sheetjmp = SpriteSheet("images/troopakuppa19/kjmp.png", (0, 0, 0))

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
            width = ss_jmp.get_width()
            height = ss_jmp.get_height()
            image = sprite_sheetjmp.get_image(width/11 * i, 0,
                                               width/11, height)
            self.OnGround_r.append(image)
            image = pygame.transform.flip(image, True, False)
            self.OnGround_l.append(image)


    def __init__(self):
        """ initialize player """
        super().__init__()

        #counter for animating jumping
        self.cnt = 0
        #counter for animating sword drawing
        self.cnt_swrd_draw = 0
        # counter for damage
        self.cnt_dmg = 0

        # counter for animating get off
        self.cnt_get_off = 0
        # action frames
        self.ready_r = []
        self.ready_l = []
        self.OnGround_l = []
        self.OnGround_r = []


        # load the image
        self.loadimages()


        # kinematic factors
        self.pos = vec((0, 0))
        self.steps = 0
        self.battlesteps = 0
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

        # flag to get off the platform
        self.go_get_off  = False
        self.get_off = False

        # set the image the player start with
        self.image = self.ready_r[0]
        self.rect = self.image.get_rect(topleft=self.pos)

        # orientation and movement status
        self.orientation = 'right'
        self.OnGround = True
        self.OnVeryBottom = False

        # action flags for drawing swords
        self.swd_on = False
        self.swd_drwn = False

        # collision flag for cell attacking kuppa
        self.cell_atk_k = False
        self.dmg_blinking = False
        self.n_blinks = 0

    def jmp_dwn_plat(self):
        """turn on get off the platform """
        if self.OnVeryBottom == False:
            self.go_get_off = True
        else:
            self.go_get_off = False
            self.get_off = False


    def no_swd_dmg_blink(self):
        period = 2
        if self.cell_atk_k:
            if self.cnt_dmg >= period:
                self.image = pygame.Surface((self.rect.width, self.rect.height), flags = SRCALPHA)
                self.image.fill((0, 0, 0, 0))
                self.dmg_blinking = True
                self.cnt_dmg = 0
                if self.n_blinks == 15:
                    self.cell_atk_k = False
                    self.dmg_blinking = False
                    self.n_blinks = 0
                else:
                    self.n_blinks += 1
            else:
                self.cnt_dmg += 1


    def get_rect(self):
        return self.image.get_rect()

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
        self.acc = vec(0, 2.5)
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT]:
            if not pressed_keys[K_a]:
                self.acc.x = -ACC
                self.orientation = 'left'
                self.steps += 1
            if pressed_keys[K_a] and not self.swd_on:
                self.acc.x = -ACC
                self.orientation = 'left'
                self.steps += 1
            if pressed_keys[K_a] and self.swd_on:
                self.acc.x = 0
                self.steps = 0
        if pressed_keys[K_RIGHT]:
            if not pressed_keys[K_a]:
                self.acc.x = ACC
                self.orientation = 'right'
                self.steps += 1
            if pressed_keys[K_a] and not self.swd_on:
                self.acc.x = ACC
                self.orientation = 'right'
                self.steps += 1
            if pressed_keys[K_a] and self.swd_on:
                self.acc.x = 0
                self.steps = 0

    def jump(self):
        """ jump action """
        if self.OnGround == True:
            self.vel.y = -43
            self.OnGround = False

    def touchYU_UP(self, hits):
        """touch collision when player jump up
        and touch the downside of the object,
        move the player just above the downside"""
        for block in hits:
            if self.vel.y > 0:
                self.OnGround = True
                self.cnt = 0
                self.vel.y = 0
                self.rect.bottom = block.rect.bottom
            self.pos.y = self.rect.y

    def touchYUD(self, hits):
        """ when player jump up and touch the
        downside of the object, go through the
        list of collided sprites in Y direction
        and block the player from moving up"""
        for block in hits:
            self.OnVeryBottom = False
            if self.vel.y > 0:
                if self.get_off:
                    self.get_off = False
                    self.cnt_get_off = 0
                    self.rect.top = block.rect.bottom
                    self.vel.y = 0
                else:
                    self.OnGround = True
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
                self.OnGround = True
                self.OnVeryBottom = True
                self.cnt = 0
                self.vel.y = 0
                self.rect.bottom = block.rect.top
            self.pos.y = self.rect.y


    def collisionY(self):
        """ check the collision in Y direction """
        #touch Cars
        hitC = pygame.sprite.spritecollide(self, ST1.Cars, False)
        self.touchYU(hitC)

        #touch ground platforms
        hits = pygame.sprite.spritecollide(self, ST1.platforms, False)
        self.touchYU(hits)


        # touch Bricks
        hitB = pygame.sprite.spritecollide(self, ST1.Bricks, False)
        self.touchYUD(hitB)

        #touch Plats
        hitP = pygame.sprite.spritecollide(self, ST1.Plats, False)
        self.touchYUD(hitP)

        #touch Bldgs
        hitBldg = pygame.sprite.spritecollide(self, ST1.Bldgs, False)
        self.touchYU_UP(hitBldg)



    """ animation functions """


    def ani_move(self):
        """ animate the left right movement"""
        if self.orientation == 'right' and self.OnGround == True:
            frame = (self.steps // 10) % len(self.ready_r)
            self.image = self.ready_r[int(frame)]


        elif self.orientation == 'left' and self.OnGround == True:
            frame = (self.steps // 10) % len(self.ready_l)
            self.image = self.ready_l[int(frame)]



    def ani_jump(self):
        """ animate the jump """
        period = 2
        if self.OnGround == False:
            if (self.cnt >= period * (len(self.OnGround_r) -1 )):
                self.cnt = period * (len(self.OnGround_r) -1 )
            else:
                self.cnt += 1
            if self.orientation == 'right':
                self.image = self.OnGround_r[self.cnt//period]
            if self.orientation == 'left':
                self.image = self.OnGround_l[self.cnt//period]

    def ani_get_off(self):
        period = 2
        if self.go_get_off:
            if self.cnt_get_off >= period * (len(self.OnGround_r) - 1):
                self.cnt_get_off = period * (len(self.OnGround_r) - 1)
                self.get_off = True
                self.go_get_off = False
            else:
                self.cnt_get_off += 1
            if self.orientation == 'right':
                self.image = self.OnGround_r[self.cnt_get_off//period]
            if self.orientation == 'left':
                self.image = self.OnGround_l[self.cnt_get_off//period]



    def animate(self):
        """animate the player. """
        self.ani_move()
        self.ani_jump()
        self.ani_get_off()
        self.no_swd_dmg_blink()

    def render(self):
        """ paste the player object into screen """
        self.animate()
        w = self.image.get_width()
        h = self.image.get_height()
        # check for action flags
        if not self.swd_drwn:
            screen.blit(self.image, self.pos, (0, 0, w ,h))
        # screen.blit(self.image, self.pos,
           # (0, 0, self.image.get_width(), self.image.get_height()))
