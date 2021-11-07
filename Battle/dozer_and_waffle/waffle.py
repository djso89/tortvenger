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
        sprite_sheet_sb = SpriteSheet("images/wf_sb_rdy.png", (0, 0, 0))
        sprite_sheet_sb_drw = SpriteSheet('images/wf_draw.png', (0, 0, 0))



        ss = sprite_sheet.sprite_sheet
        ss_sb = sprite_sheet_sb.sprite_sheet
        ss_frame = sp_sheet_frame.sprite_sheet
        ss_sb_draw = sprite_sheet_sb_drw.sprite_sheet

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

            width = ss_sb.get_width()
            height = ss_sb.get_height()
            image = sprite_sheet_sb.get_image(i * width/2, 0,
                                           width/2, height)
            self.sb_rdy_r.append(image)
            image = pygame.transform.flip(image, True, False)
            self.sb_rdy_l.append(image)


        # load all drawing light-saber images
        for i in range(0, 17, 1):
            width = ss_sb_draw.get_width()
            height = ss_sb_draw.get_height()
            image = sprite_sheet_sb_drw.get_image(i * width / 17, 0,
                                                   width / 17, height)
            self.sber_draw_r.append(image)
            image = pygame.transform.flip(image, True, False)
            self.sber_draw_l.append(image)

    def __init__(self):
        """ initialize player """
        pygame.sprite.Sprite.__init__(self)
        #WF_Attr.__init__(self)

        #counter for animating jumping
        self.cnt = 0
        self.cnt_sber_draw = 0
        self.cnt_dmg = 0

        self.cnt_a = 0

        # action frames
        self.wfframe = []
        self.ready_r = []
        self.ready_l = []
        self.sb_rdy_r = []
        self.sb_rdy_l = []

        self.jmp_l = []
        self.jmp_r = []

        self.sb_cut_r = []
        self.sb_cut_l = []

        self.sb_jmp_l = []
        self.sb_jmp_r = []
        self.sber_draw_r = []
        self.sber_draw_l = []

        # load the image
        self.loadimages()


        # kinematic factors
        self.steps = 0
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

        # flag switch for drawing sb
        self.sb_on = False
        # flag for process of drawing sb
        self.sb_drawing = False

        # flag for attack
        self.ATK = False
        self.ATK_DONE = False


        self.cut_period = 0
        self.cnt_sb_cut = 0

        self.cnt_hold = 0


        self.clock = pygame.time.Clock()

        # Darth light saber swing
        self.swing_number = 1
        #self.cell_atk_k = False
        self.dmg_blinking = False
        self.n_blinks = 0

    def no_sb_dmg_blink(self):
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

    def draw_the_sber(self):
        """ draw the sber function.
        the function gets the key press reading
        and toggles sb_on flaf to True to False """
        self.sb_on = not self.sb_on


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
                self.steps += 1
                self.orientation = 'left'
            if pressed_keys[K_a] and not self.sb_on:
                self.acc.x = -ACC
                self.steps += 1
                self.orientation = 'left'
            if pressed_keys[K_a] and self.sb_on:
                self.acc.x = 0
                self.steps = 0
        if pressed_keys[K_RIGHT]:
            if not pressed_keys[K_a]:
                self.steps += 1
                self.acc.x = ACC
                self.orientation = 'right'
            if pressed_keys[K_a] and not self.sb_on:
                self.acc.x = ACC
                self.steps += 1
                self.orientation = 'right'
            if pressed_keys[K_a] and self.sb_on:
                self.acc.x = 0
                self.steps = 0

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
            frame = (self.steps // 10) % len(self.ready_r)
            if self.sb_on and not self.sb_drawing:
                self.image_wf = self.sb_rdy_r[int(frame)]
            else:
                self.image_wf = self.ready_r[int(frame)]
            self.pos_a.x = self.pos.x - 10
            self.pos_a.y = self.pos.y - 60
        elif self.orientation == 'left':# and self.OnGround == True:
            frame = (self.steps // 10) % len(self.ready_l)
            if self.sb_on and not self.sb_drawing:
                self.image_wf = self.sb_rdy_l[int(frame)]
            else:
                self.image_wf = self.ready_l[int(frame)]
            self.pos_a.x = self.pos.x - 80
            self.pos_a.y = self.pos.y - 60




    def ani_sb_out(self):
        """ animate pulling out swords"""
        period = 7
        max_period = period * (len(self.sber_draw_r) - 1)
        if (self.cnt_sber_draw >= max_period):
            self.cnt_sber_draw = max_period
            self.sb_drawing = False
        else:
            self.sb_drawing = True
            if (self.orientation == 'right'):
                self.image_wf = self.sber_draw_r[self.cnt_sber_draw // period]
                self.pos_a.x = self.pos.x - 10
                self.pos_a.y = self.pos.y - 60
            if (self.orientation == 'left'):
                self.image_wf = self.sber_draw_l[self.cnt_sber_draw // period]
                self.pos_a.x = self.pos.x - 80
                self.pos_a.y = self.pos.y - 60
            self.cnt_sber_draw += 1

    def ani_sb_in(self):
        """animate drawing the saber staff """
        period = 7
        max_period = period * (len(self.sber_draw_l) - 1)
        if (self.cnt_sber_draw <= 0):
            self.cnt_sber_draw = 0
            self.sb_drawing = False
        else:
            self.sb_drawing = True
            self.cnt_sber_draw -= 1
            if (self.orientation == 'right'):
                self.image_wf = self.sber_draw_r[self.cnt_sber_draw // period]
                self.pos_a.x = self.pos.x - 10
                self.pos_a.y = self.pos.y - 60
            if self.orientation == 'left':
                self.image_wf = self.sber_draw_l[self.cnt_sber_draw // period]
                self.pos_a.x = self.pos.x - 80
                self.pos_a.y = self.pos.y - 60




    def ani_sb_draw(self):
        if self.sb_on == True:
            self.ani_sb_out()
        elif self.sb_on == False:
            self.ani_sb_in()


    def animate(self):
        """animate the player. """
        self.ani_move()
        self.ani_sb_draw()



    def render(self):
        """ paste the player object into screen """
        self.animate()
        self.rect_wf = self.image_wf.get_rect(topleft=self.pos_a)
        screen.blit(self.image_wf, self.pos_a)
#        screen.blit(self.image, self.pos)



P1 = Waffle()
