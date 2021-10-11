#!/usr/bin/env python3
import pygame
import sys
from pygame.locals import *
from display import *
from stage import *
from spritesheet import SpriteSheet
#from attr import WF_Attr
#from yesmangauge import Yesmaninfo
cut_frame_period = 5
cut_frame_num = 7


class Waffle(pygame.sprite.Sprite):#, WF_Attr):
    """ Waffle class """

    def loadimages(self):
        """ load all the kuppa action frames """
        sprite_sheet = SpriteSheet("images/wf_rdy.png", (0, 0, 0))
        sp_sheet_frame = SpriteSheet("images/wf_frame.png", (0, 0, 0))



        ss = sprite_sheet.sprite_sheet
        ss_frame = sp_sheet_frame.sprite_sheet

        # load the frame
        for i in range(0, 1, 1):
            width = ss_frame.get_width()
            height = ss_frame.get_height()
            image = sp_sheet_frame.get_image(0, 0, width, height)
            self.wfframe.append(image)

        # load all right facing ready images
        for i in range(0, 2, 1):
            width = ss.get_width()
            height = ss.get_height()
            image = sprite_sheet.get_image(i * width/2, 0,
                                           width/2, height)
            self.ready_r.append(image)
            image = pygame.transform.flip(image, True, False)
            self.ready_l.append(image)

    def __init__(self):
        """ initialize player """
        pygame.sprite.Sprite.__init__(self)
        #WF_Attr.__init__(self)

        #counter for animating jumping
        self.cnt = 0
        self.cnt_swrd_draw = 0
        self.cnt_dmg = 0

        self.cnt_a = 0

        # action frames
        self.wfframe = []
        self.ready_r = []
        self.ready_l = []
        self.swd_rdy_r = []
        self.swd_rdy_l = []

        self.jmp_l = []
        self.jmp_r = []

        self.swd_cut_r = []
        self.swd_cut_l = []

        self.swd_jmp_l = []
        self.swd_jmp_r = []
        self.swrd_draw_r = []
        self.swrd_draw_l = []

        # load the image
        self.loadimages()


        # kinematic factors
        self.pos = vec((0, 0))
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

        # action frame position
        self.pos_a = vec((0, 0))

        # set the image the player start with
        self.image = self.wfframe[0]
        self.image_wf = self.ready_r[0]
        self.rect = self.image.get_rect(topleft=self.pos)
        self.rect_wf = self.image_wf.get_rect(topleft=self.pos_a)

        # orientation and movement status
        self.orientation = 'right'
        self.OnGround = True

        # flag switch for drawing swd
        self.swd_on = False
        # flag for process of drawing swd
        self.swd_drawing = False

        # flag for attack
        self.ATK = False
        self.ATK_DONE = False
        self.go_hit = False

        self.cut_period = 0
        self.cnt_swd_cut = 0

        self.cnt_hold = 0


        self.clock = pygame.time.Clock()

        # Darth light saber swing
        self.swing_number = 1
        #self.cell_atk_k = False
        self.dmg_blinking = False
        self.n_blinks = 0

    def no_swd_dmg_blink(self):
        period = 2
        if self.cell_atk_k:
            if self.cnt_dmg >= period:
                self.image_wf = Surface((self.rect.width, self.rect.height), flags = SRCALPHA)
                self.image_wf.fill((0, 0, 0, 0))
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
        """get the rectangle object from image """
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
            if pressed_keys[K_a] and not self.swd_on:
                self.acc.x = -ACC
                self.orientation = 'left'
            if pressed_keys[K_a] and self.swd_on:
                self.acc.x = 0
        if pressed_keys[K_RIGHT]:
            if not pressed_keys[K_a]:
                self.acc.x = ACC
                self.orientation = 'right'
            if pressed_keys[K_a] and not self.swd_on:
                self.acc.x = ACC
                self.orientation = 'right'
            if pressed_keys[K_a] and self.swd_on:
                self.acc.x = 0

    def jump(self):
        """ jump action """
        if self.OnGround == True:
            self.vel.y = -40
            self.OnGround = False



    # Kuppa touching the stage objects
    def touchXR(self, hits):
        """
        touch hits coming from right side
        """
        for block in hits:
            if self.vel.x > 0:
                self.rect.right = block.rect.left
            self.pos.x = self.rect.x


    def touchXL(self, hits):
        """touch hits coming from left side """
        for block in hits:
            if self.vel.x < 0:
                self.rect.left = block.rect.right
            self.pos.x = self.rect.x


    def touchYUD(self, hits):
        """ go through the list of collided sprites
        in Y direction"""
        for block in hits:
            if self.vel.y > 0:
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
                self.cnt = 0
                self.vel.y = 0
                self.rect.bottom = block.rect.top
            self.pos.y = self.rect.y


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


    """ animation functions """
    def ani_move(self):
        """ animate the left right movement"""
        if self.orientation == 'right':# and self.OnGround == True:
            frame = (self.pos.x // 30) % len(self.ready_r)
            self.image_wf = self.ready_r[int(frame)]
            self.pos_a.x = self.pos.x - 10
            self.pos_a.y = self.pos.y - 60
        elif self.orientation == 'left':# and self.OnGround == True:
            frame = (self.pos.x // 30) % len(self.ready_l)
            self.image_wf = self.ready_l[int(frame)]
            self.pos_a.x = self.pos.x - 80
            self.pos_a.y = self.pos.y - 60


    def animate(self):
        """animate the player. """
        self.ani_move()



    def render(self):
        """ paste the player object into screen """
        self.animate()
        self.rect_wf = self.image_wf.get_rect(topleft=self.pos_a)
        screen.blit(self.image_wf, self.pos_a)
#        screen.blit(self.image, self.pos)



P1 = Waffle()
