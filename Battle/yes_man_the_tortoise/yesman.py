#!/usr/bin/env python3
import pygame
import sys
from pygame.locals import *
from display import *
from stage import *
from spritesheet import SpriteSheet

cut_frame_period = 5
cut_frame_num = 7


class Yesman(pygame.sprite.Sprite):
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



        ss = sprite_sheet.sprite_sheet
        ss_swd = sprite_sheet_swd.sprite_sheet
        ss_frame = sp_sheet_frame.sprite_sheet
        ss_jmp = sprite_sheetjmp.sprite_sheet
        ss_swd_draw = sprite_sheet_swd_drw.sprite_sheet
        ss_swd_cut1 = sprite_sheet_swd_cut1.sprite_sheet


        # load first 3 sword cutting images
        for i in range(0, 7, 1):
            width = ss_swd_cut1.get_width()
            height = ss_swd_cut1.get_height()
            image = sprite_sheet_swd_cut1.get_image(i * width / 7, 0,
                                           width / 7, height)
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
        super().__init__()

        #counter for animating jumping
        self.cnt = 0
        self.cnt_swrd_draw = 0
        self.cnt_dmg = 0

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
        self.atk_comb = 1
        self.cnt_swd_cut = 0

        self.cell_atk_k = False
        self.dmg_blinking = False
        self.n_blinks = 0

    def no_swd_dmg_blink(self):
        period = 2
        if self.cell_atk_k:
            if self.cnt_dmg >= period:
                self.image = Surface((self.rect.width, self.rect.height), flags = SRCALPHA)
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

    def attack(self):
        """game logic for attack if ATK flag is triggered """
        if self.ATK:
            self.ani_cut()
        elif not self.ATK:
            self.cnt_swd_cut = 0


    def update(self):
        """
        function that calculates position
        and check collision
        """
        # move along the x direction
        self.acc.x += self.vel.x * FRIC
        self.vel.x += self.acc.x
        self.pos.x += self.vel.x + 0.5 * self.acc.x


        # routine when player didn't touch cells
        #left Most boundary of stage. Block the player from
        #moving further
        if self.pos.x < 0:
            self.pos.x = 0

        if self.pos.x > WIN_W - self.rect.width:
            self.pos.x = WIN_W - self.rect.width

        self.rect.x = self.pos.x
        self.collisionX()

        #moving along the y direction
        self.vel.y += self.acc.y
        self.pos.y += self.vel.y + 0.5 * self.acc.y
        # assign the y coordinate to frame's y
        self.rect.y = self.pos.y

        self.collisionY()

    # Kuppa touching the stage objects
    def touchXR(self, hits):
        #touch hits coming from right side
        for block in hits:
            if self.vel.x > 0:
                self.rect.right = block.rect.left
            self.pos.x = self.rect.x



    def collisionX(self):
        """check the collision in X direction """
        # touch bricks
        hitB = pygame.sprite.spritecollide(self, Bricks, False)
        self.touchX(hitB)

        #touch Cars
        hitC = pygame.sprite.spritecollide(self, Cars, False)
        self.touchX(hitC)

        # touch Plat
        hitP = pygame.sprite.spritecollide(self, Plats, False)
        self.touchX(hitP)

    def touchX(self, hits):
        #touch hits
        for block in hits:
            if self.vel.x > 0: #moving right
                self.rect.right = block.rect.left
            if self.vel.x < 0: #moving left
                self.rect.left = block.rect.right
            # set the x coordinate
            self.pos.x = self.rect.x

    def touchXL(self, hits):
        #touch hits coming from left side
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
        elif self.orientation == 'left' and self.OnGround == True:
            frame = (self.pos.x // 30) % len(self.ready_l)
            if self.swd_on == True and self.swd_drawing == False:
                self.image_ym = self.swd_rdy_l[int(frame)]
            else:
                self.image_ym = self.ready_l[int(frame)]


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
            if self.orientation == 'left':
                if self.swd_on:
                    self.image_ym = self.swd_jmp_l[self.cnt//period]
                else:
                    self.image_ym = self.jmp_l[self.cnt//period]


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
            if (self.orientation == 'left'):
                self.image_ym = self.swrd_draw_l[self.cnt_swrd_draw // period]
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
            if self.orientation == 'left':
                self.image_ym = self.swrd_draw_l[self.cnt_swrd_draw // period]


    def ani_swd_draw(self):
        if self.swd_on == True:
            self.ani_swd_out()
        elif self.swd_on == False:
            self.ani_swd_in()

    def ani_cut(self):
        """ animate the sword cutting"""
        cut_period = cut_frame_period * cut_frame_num
        if self.cnt_swd_cut >= cut_period:
            self.cnt_swd_cut = 0
            self.ATK = False
            self.ATK_DONE = True
        else:
            self.ATK_DONE = False
            combo_i = (self.atk_comb *cut_frame_num) - cut_frame_num
            frame_atk = combo_i + (self.cnt_swd_cut // cut_frame_period)
            if self.orientation == 'right':
                self.image_ym = self.swd_cut_r[frame_atk]
            if self.orientation == 'left':
                self.image_ym = self.swd_cut_l[frame_atk]
            self.cnt_swd_cut += 1

    def animate(self):
        """animate the player. """
        self.ani_move()
        self.ani_jump()
        self.ani_swd_draw()
        self.attack()
        self.no_swd_dmg_blink()

    def ani_frame_adj(self):
        """adjust the frame according to action flags """
        if self.orientation == 'left':
            if self.swd_drawing == True:
                self.pos_a.x = self.pos.x - 50
                self.pos_a.y = self.pos.y - 50
            else:
                if self.ATK:
                    self.pos_a.x = self.pos.x - 50
                    self.pos_a.y = self.pos.y - 60
                else:
                    self.pos_a.x = self.pos.x - 33
                    self.pos_a.y = self.pos.y
        elif self.orientation == 'right':
            if self.swd_drawing == True:
                self.pos_a.x = self.pos.x - 15
                self.pos_a.y = self.pos.y - 50
            else:
                if self.ATK:
                    self.pos_a.x = self.pos.x - 15
                    self.pos_a.y = self.pos.y - 60
                else:
                    self.pos_a.x = self.pos.x
                    self.pos_a.y = self.pos.y

    def render(self):
        """ paste the player object into screen """
        self.animate()
        w = self.image.get_width()
        h = self.image.get_height()
        self.ani_frame_adj()
        screen.blit(self.image_ym, self.pos_a)
        #screen.blit(self.image, self.pos)



P1 = Yesman()
