#!/usr/bin/env python3
import pygame
import sys
from pygame.locals import *
from display import *
from stage import *
from spritesheet import SpriteSheet



cut_frame_period = 5
cut_frame_num = 7


class Gregg(pygame.sprite.Sprite):#, WF_Attr):
    """ Gregg class """

    def loadimages(self):
        """ load all the kuppa action frames """
        sprite_sheet = SpriteSheet("images/Gregg_rdy.png", (0, 0, 0))
        sp_sheet_frame = SpriteSheet("images/Gregg_frame.png", (0, 0, 0))
        sprite_sheet_gd = SpriteSheet("images/Gregg_gd_rdy.png", (0, 0, 0))
        sprite_sheet_gd_drw = SpriteSheet('images/Gregg_draw.png', (0, 0, 0))



        ss = sprite_sheet.sprite_sheet
        ss_gd = sprite_sheet_gd.sprite_sheet
        ss_frame = sp_sheet_frame.sprite_sheet
        ss_gd_draw = sprite_sheet_gd_drw.sprite_sheet

        # load the frame
        for i in range(0, 1, 1):
            width = ss_frame.get_width()
            height = ss_frame.get_height()
            image = sp_sheet_frame.get_image(0, 0, width, height)
            self.Greggframe.append(image)

        # load all right facing ready images
        for i in range(0, 2, 1):
            width = ss.get_width()
            height = ss.get_height()
            image = sprite_sheet.get_image(i * width/2, 0,
                                           width/2, height)
            self.ready_l.append(image)
            image = pygame.transform.flip(image, True, False)
            self.ready_r.append(image)

            width = ss_gd.get_width()
            height = ss_gd.get_height()
            image = sprite_sheet_gd.get_image(i * width/2, 0,
                                           width/2, height)
            self.gd_rdy_l.append(image)
            image = pygame.transform.flip(image, True, False)
            self.gd_rdy_r.append(image)


        # load all drawing Guan Dao images
        for i in range(0, 8, 1):
            width = ss_gd_draw.get_width()
            height = ss_gd_draw.get_height()
            image = sprite_sheet_gd_drw.get_image(i * width / 8, 0,
                                                   width / 8, height)
            self.gder_draw_l.append(image)
            image = pygame.transform.flip(image, True, False)
            self.gder_draw_r.append(image)


    def __init__(self):
        """ initialize player """
        pygame.sprite.Sprite.__init__(self)
        #GREGG_Attr.__init__(self)

        #counter for animating jumping
        self.cnt = 0
        self.cnt_gder_draw = 0
        self.cnt_dmg = 0

        self.cnt_a = 0

        # action frames
        self.Greggframe = []
        self.ready_r = []
        self.ready_l = []
        self.gd_rdy_r = []
        self.gd_rdy_l = []

        self.jmp_l = []
        self.jmp_r = []

        self.gd_cut_r = []
        self.gd_cut_l = []

        self.gd_jmp_l = []
        self.gd_jmp_r = []
        self.gder_draw_r = []
        self.gder_draw_l = []

        # load the image
        self.loadimages()


        # kinematic factors
        self.pos = vec((0, 0))
        self.steps = 0
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

        # action frame position
        self.pos_a = vec((0, 0))

        # set the image the player start with
        self.image = self.Greggframe[0]
        self.image_Gregg = self.ready_r[0]
        self.rect = self.image.get_rect(topleft=self.pos)
        self.rect_Gregg = self.image_Gregg.get_rect(topleft=self.pos_a)

        # orientation and movement status
        self.orientation = 'right'
        self.OnGround = True

        # flag switch for drawing gd
        self.gd_on = False
        # flag for process of drawing gd
        self.gd_drawing = False

        # flag for attack
        self.ATK = False
        self.ATK_DONE = False


        self.cut_period = 0
        self.cnt_gd_cut = 0

        self.cnt_hold = 0


        self.clock = pygame.time.Clock()

        # Darth light saber swing
        self.swing_number = 1
        #self.cell_atk_k = False
        self.dmg_blinking = False
        self.n_blinks = 0

    def no_gd_dmg_blink(self):
        period = 2
        if self.cell_atk_k:
            if self.cnt_dmg >= period:
                self.image_Gregg = Surface((self.rect.width, self.rect.height), flags = SRCALPHA)
                self.image_Gregg.fill((0, 0, 0, 0))
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

    def draw_the_gder(self):
        """ draw the gder function.
        the function gets the key press reading
        and toggles gd_on flaf to True to False """
        self.gd_on = not self.gd_on


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
            if pressed_keys[K_a] and not self.gd_on:
                self.acc.x = -ACC
                self.orientation = 'left'
                self.steps += 1
            if pressed_keys[K_a] and self.gd_on:
                self.acc.x = 0
        if pressed_keys[K_RIGHT]:
            if not pressed_keys[K_a]:
                self.acc.x = ACC
                self.orientation = 'right'
                self.steps += 1
            if pressed_keys[K_a] and not self.gd_on:
                self.acc.x = ACC
                self.orientation = 'right'
                self.steps += 1
            if pressed_keys[K_a] and self.gd_on:
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
            frame = (self.steps // 10) % len(self.ready_r)
            if self.gd_on:
                self.image_Gregg = self.gd_rdy_r[int(frame)]
            else:
                self.image_Gregg = self.ready_r[int(frame)]
            self.pos_a.x = self.pos.x - 40
            self.pos_a.y = self.pos.y - 300
        elif self.orientation == 'left':# and self.OnGround == True:
            frame = (self.steps // 10) % len(self.ready_l)
            if self.gd_on:
                self.image_Gregg = self.gd_rdy_l[int(frame)]
            else:
                self.image_Gregg = self.ready_l[int(frame)]
            self.pos_a.x = self.pos.x - 170
            self.pos_a.y = self.pos.y - 300




    def ani_gd_out(self):
        """ animate pulling out swords"""
        period = 7
        max_period = period * (len(self.gder_draw_r) - 1)
        if (self.cnt_gder_draw >= max_period):
            self.cnt_gder_draw = max_period
            self.gd_drawing = False
        else:
            self.gd_drawing = True
            if (self.orientation == 'right'):
                self.image_Gregg = self.gder_draw_r[self.cnt_gder_draw // period]
                self.pos_a.x = self.pos.x - 40
                self.pos_a.y = self.pos.y - 300
            if (self.orientation == 'left'):
                self.image_Gregg = self.gder_draw_l[self.cnt_gder_draw // period]
                self.pos_a.x = self.pos.x - 170
                self.pos_a.y = self.pos.y - 300
            self.cnt_gder_draw += 1

    def ani_gd_in(self):
        """animate drawing the saber staff """
        period = 7
        max_period = period * (len(self.gder_draw_l) - 1)
        if (self.cnt_gder_draw <= 0):
            self.cnt_gder_draw = 0
            self.gd_drawing = False
        else:
            self.gd_drawing = True
            self.cnt_gder_draw -= 1
            if (self.orientation == 'right'):
                self.image_Gregg = self.gder_draw_r[self.cnt_gder_draw // period]
                self.pos_a.x = self.pos.x - 40
                self.pos_a.y = self.pos.y - 300
            if self.orientation == 'left':
                self.image_Gregg = self.gder_draw_l[self.cnt_gder_draw // period]
                self.pos_a.x = self.pos.x - 170
                self.pos_a.y = self.pos.y - 300




    def ani_gd_draw(self):
        if self.gd_on == True:
            self.ani_gd_out()
        elif self.gd_on == False:
            self.ani_gd_in()


    def animate(self):
        """animate the player. """
        self.ani_move()
        self.ani_gd_draw()



    def render(self):
        """ paste the player object into screen """
        self.animate()
        self.rect_Gregg = self.image_Gregg.get_rect(topleft=self.pos_a)
#        screen.blit(self.image, self.pos)
        screen.blit(self.image_Gregg, self.pos_a)




P1 = Gregg()
