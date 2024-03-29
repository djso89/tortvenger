#!/usr/bin/env python3
import pygame
import sys
from pygame.locals import *
from display import *
from stage import *
from spritesheet import SpriteSheet
from attr import YM_Attr
from yesmangauge import Yesmaninfo

cut_frame_period = 5
cut_frame_num = 7


class Yesman(pygame.sprite.Sprite, YM_Attr):
    """ Yesman class """

    def loadimages(self):
        """ load all the kuppa action frames """
        sprite_sheet = SpriteSheet("images/ym_rdy.png", (0, 0, 0))
        sprite_sheet_swd = SpriteSheet("images/ym_swd_rdy.png", (0, 0, 0))
        sp_sheet_frame = SpriteSheet("images/ym_frame.png", (0, 0, 0))
        sprite_sheetjmp = SpriteSheet("images/ym_jmp.png", (0, 0, 0))
        sprite_sheet_swd_drw = SpriteSheet('images/ym_swd_draw.png', (0, 0, 0))
        sprite_sheet_swdjmp = SpriteSheet("images/ym_swd_jmp.png", (0, 0, 0))
        sprite_sheet_swd_cut1 = SpriteSheet("images/ym_swd_combo1.png", (0, 0, 0))
        sprite_sheet_swd_cut2 = SpriteSheet("images/ym_swd_combo2.png",(0, 0, 0))
        sprite_sheet_swd_cut3 = SpriteSheet("images/ym_swd_combo3.png",(0, 0, 0))


        ss = sprite_sheet.sprite_sheet
        ss_swd = sprite_sheet_swd.sprite_sheet
        ss_frame = sp_sheet_frame.sprite_sheet
        ss_jmp = sprite_sheetjmp.sprite_sheet
        ss_swd_draw = sprite_sheet_swd_drw.sprite_sheet
        ss_swd_cut1 = sprite_sheet_swd_cut1.sprite_sheet
        ss_swd_cut2 = sprite_sheet_swd_cut2.sprite_sheet
        ss_swd_cut3 = sprite_sheet_swd_cut3.sprite_sheet

        # load combo 1-3 sword cutting images
        for i in range(0, 7, 1):
            width = ss_swd_cut1.get_width()
            height = ss_swd_cut1.get_height()
            image = sprite_sheet_swd_cut1.get_image(i * width / 7, 0,
                                           width / 7, height)
            self.swd_cut_r.append(image)
            image = pygame.transform.flip(image, True, False)
            self.swd_cut_l.append(image)

        #load combo 4 - 5 sword cutting images
        for i in range(0, 8, 1):
            width = ss_swd_cut2.get_width()
            height = ss_swd_cut2.get_height()
            image = sprite_sheet_swd_cut2.get_image(i * width / 8, 0,
                                           width / 8, height)
            self.swd_cut_r.append(image)
            image = pygame.transform.flip(image, True, False)
            self.swd_cut_l.append(image)

        #load combo 6 sword cutting images
        for i in range(0, 8, 1):
            width = ss_swd_cut3.get_width()
            height = ss_swd_cut3.get_height()
            image = sprite_sheet_swd_cut3.get_image(i * width / 8, 0,
                                           width / 8, height)
            self.swd_cut_r.append(image)
            image = pygame.transform.flip(image, True, False)
            self.swd_cut_l.append(image)

        # load all drawing sword images
        for i in range(0, 13, 1):
            width = ss_swd_draw.get_width()
            height = ss_swd_draw.get_height()
            image = sprite_sheet_swd_drw.get_image(i * width / 13, 0,
                                           width / 13, height)
            self.swrd_draw_r.append(image)
            image = pygame.transform.flip(image, True, False)
            self.swrd_draw_l.append(image)

        # load the frame
        for i in range(0, 1, 1):
            width = ss_frame.get_width()
            height = ss_frame.get_height()
            image = sp_sheet_frame.get_image(0, 0, width, height)
            self.ymframe.append(image)

        # load all right facing ready images
        for i in range(0, 2, 1):
            width = ss.get_width()
            height = ss.get_height()
            image = sprite_sheet.get_image(i * width/2, 0,
                                           width/2, height)
            self.ready_r.append(image)
            image = pygame.transform.flip(image, True, False)
            self.ready_l.append(image)

            width = ss_swd.get_width()
            height = ss_swd.get_height()
            image = sprite_sheet_swd.get_image(i * width/2, 0,
                                           width/2, height)
            self.swd_rdy_r.append(image)
            image = pygame.transform.flip(image, True, False)
            self.swd_rdy_l.append(image)


        # load all the right facing jmp images
        for i in range(0, 6, 1):
            width = ss_jmp.get_width()
            height = ss_jmp.get_height()
            image = sprite_sheetjmp.get_image(width/ 6 * i, 0,
                                               width/ 6, height)
            self.jmp_r.append(image)
            image = pygame.transform.flip(image, True, False)
            self.jmp_l.append(image)

            ss_swd_jmp = sprite_sheet_swdjmp.sprite_sheet
            width = ss_swd_jmp.get_width()
            height = ss_swd_jmp.get_height()
            image = sprite_sheet_swdjmp.get_image\
                (i * width // 6, 0, width // 6, height)
            self.swd_jmp_r.append(image)
            image = pygame.transform.flip(image, True, False)
            self.swd_jmp_l.append(image)


    def __init__(self):
        """ initialize player """
        pygame.sprite.Sprite.__init__(self)
        YM_Attr.__init__(self)

        #counter for animating jumping
        self.cnt = 0
        self.cnt_swrd_draw = 0
        self.cnt_dmg = 0

        self.cnt_a = 0

        # action frames
        self.ymframe = []
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
        self.image = self.ymframe[0]
        self.image_ym = self.ready_r[0]
        self.rect = self.image.get_rect(topleft=self.pos)
        self.rect_ym = self.image_ym.get_rect(topleft=self.pos)

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


        # slash number
        self.slash_number = 1

        self.cell_atk_k = False
        self.dmg_blinking = False
        self.n_blinks = 0

    def no_swd_dmg_blink(self):
        period = 2
        if self.cell_atk_k:
            if self.cnt_dmg >= period:
                self.image_ym = Surface((self.rect.width, self.rect.height), flags = SRCALPHA)
                self.image_ym.fill((0, 0, 0, 0))
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
        if self.orientation == 'right' and self.OnGround == True:
            frame = (self.pos.x // 30) % len(self.ready_r)
            if self.swd_on == True and self.swd_drawing == False:
                self.image_ym = self.swd_rdy_r[int(frame)]
            else:
                self.image_ym = self.ready_r[int(frame)]
            self.pos_a.x = self.pos.x
            self.pos_a.y = self.pos.y
        elif self.orientation == 'left' and self.OnGround == True:
            frame = (self.pos.x // 30) % len(self.ready_l)
            if self.swd_on == True and self.swd_drawing == False:
                self.image_ym = self.swd_rdy_l[int(frame)]
            else:
                self.image_ym = self.ready_l[int(frame)]
            self.pos_a.x = self.pos.x - 33
            self.pos_a.y = self.pos.y


    def ani_jump(self):
        """ animate the jump """
        period = 4
        if self.OnGround == False:
            if self.cnt >= (period * (len(self.jmp_r) -1 )):
                self.cnt = period * (len(self.jmp_r) -1 )
            else:
                self.cnt += 1
            if self.orientation == 'right':
                if self.swd_on:
                    self.image_ym = self.swd_jmp_r[self.cnt//period]
                else:
                    self.image_ym = self.jmp_r[self.cnt//period]
                self.pos_a.x = self.pos.x
                self.pos_a.y = self.pos.y
            if self.orientation == 'left':
                if self.swd_on:
                    self.image_ym = self.swd_jmp_l[self.cnt//period]
                else:
                    self.image_ym = self.jmp_l[self.cnt//period]
                self.pos_a.x = self.pos.x - 33
                self.pos_a.y = self.pos.y


    def ani_swd_out(self):
        """ animate pulling out swords"""
        period = 2
        max_period = period * (len(self.swrd_draw_r) - 1)
        if (self.cnt_swrd_draw >= max_period):
            self.cnt_swrd_draw = max_period
            self.swd_drawing = False
        else:
            self.swd_drawing = True
            if (self.orientation == 'right'):
                self.image_ym = self.swrd_draw_r[self.cnt_swrd_draw // period]
                self.pos_a.x = self.pos.x - 15
                self.pos_a.y = self.pos.y - 50
            if (self.orientation == 'left'):
                self.image_ym = self.swrd_draw_l[self.cnt_swrd_draw // period]
                self.pos_a.x = self.pos.x - 50
                self.pos_a.y = self.pos.y - 50
            self.cnt_swrd_draw += 1

    def ani_swd_in(self):
        """animate drawing the swords """
        period = 5
        max_period = period * (len(self.swrd_draw_l) - 1)
        if (self.cnt_swrd_draw <= 0):
            self.cnt_swrd_draw = 0
            self.swd_drawing = False
        else:
            self.swd_drawing = True
            self.cnt_swrd_draw -= 1
            if (self.orientation == 'right'):
                self.image_ym = self.swrd_draw_r[self.cnt_swrd_draw // period]
                self.pos_a.x = self.pos.x - 15
                self.pos_a.y = self.pos.y - 50
            if self.orientation == 'left':
                self.image_ym = self.swrd_draw_l[self.cnt_swrd_draw // period]
                self.pos_a.x = self.pos.x - 50
                self.pos_a.y = self.pos.y - 50


    def ani_swd_draw(self):
        if self.swd_on == True:
            self.ani_swd_out()
        elif self.swd_on == False:
            self.ani_swd_in()

    def get_slash_number(self, frame_atk):
        if frame_atk == 3:
            return 1
        if frame_atk == 4:
            return 2
        if frame_atk == 6:
            return 3
        if frame_atk == 10:
            return 4
        if frame_atk == 12:
            return 5
        if frame_atk == 21:
            return 6
        return 0

    def get_frame_atk(self, slash_num):
        if slash_num == 1:
            return 3
        if slash_num == 2:
            return 4
        if slash_num == 3:
            return 6
        if slash_num == 4:
            return 10
        if slash_num == 5:
            return 12
        if slash_num == 6:
            return 21
        return 0

    def get_cut_frame_period(self, slash_num):
        if slash_num >= 1 and slash_num <= 3:
            return 4
        if slash_num == 4 or slash_num == 5:
            return 5
        if slash_num == 6:
            return 4
        return 1

    def show_cut(self, frame_atk):
        """display the cut image according to frame_atk """
        if self.orientation == 'right':
            self.image_ym = self.swd_cut_r[frame_atk]
            self.pos_a.x = self.pos.x - 15
            self.pos_a.y = self.pos.y - 60
        if self.orientation == 'left':
            self.image_ym = self.swd_cut_l[frame_atk]
            self.pos_a.x = self.pos.x - 50
            self.pos_a.y = self.pos.y - 60
        #print(frame_atk)

    def ani_cut(self):
        """ animate the sword cutting
        according to slash number
        """
        cut_frame_period = self.get_cut_frame_period(self.slash_number)
        start_pt = self.get_frame_atk(self.slash_number - 1)
        end_pt = self.get_frame_atk(self.slash_number)
        frame_num = (end_pt - start_pt)

        self.cut_period = cut_frame_period * (frame_num)
        frame_atk = start_pt + (self.cnt_swd_cut // cut_frame_period)
        self.show_cut(frame_atk)
        if self.cnt_swd_cut >= self.cut_period:
            self.show_cut(end_pt)
            self.ATK_DONE = True
            self.go_hit = True
        else:
            self.ATK_DONE = False
            self.go_hit = False
            self.cnt_swd_cut += 1

    def atk_isDone(self):
        self.ATK_DONE = False
        self.ATK = False
        self.slash_number = 1
        self.cnt_hold = 0
        self.cnt_swd_cut = 0

    def go_combo(self):
        self.incr_slash()


    def cut_delay(self):
        cut_frame_period = self.get_cut_frame_period(self.slash_number)
        if (self.ATK_DONE):
            if (self.cnt_hold >=  3 * cut_frame_period):
                self.atk_isDone()
            else:
                self.cnt_hold += 1



    def incr_slash(self):
        if self.slash_number == 3:
            self.slash_number = 1
            self.ATK_DONE = False
            self.cnt_swd_cut = 0
        else:
            self.slash_number += 1
            self.ATK_DONE = False
            self.cnt_hold = 0
            self.cnt_swd_cut = 0




    def go_attack(self):
        """game logic for attack if ATK flag is triggered """
        if self.ATK:
            #print("slash #: {}".format(self.slash_number))
            combo_func = 'self.ani_cut'
            eval(combo_func)()
            self.cut_delay()
            #self.go_hit = False



    def animate(self):
        """animate the player. """
        self.ani_move()
        self.ani_jump()
        self.ani_swd_draw()
        self.no_swd_dmg_blink()
        self.go_attack()



    def render(self):
        """ paste the player object into screen """
        self.animate()
        w = self.image.get_width()
        h = self.image.get_height()
        self.rect_ym = self.image_ym.get_rect(topleft=self.pos_a)
        screen.blit(self.image_ym, self.pos_a)
#        screen.blit(self.image, self.pos)



P1 = Yesman()
