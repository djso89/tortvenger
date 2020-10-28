#!/usr/bin/env python3
from player import *

OFF_SET_X = 2
OFF_SET_Y = 5


class K_Act(pygame.sprite.Sprite):
    """ Kuppa action class
    this is where K_Act reads P1 action flags
    to display the action
    """
    def load_images(self):
        """ load the images from sprite sheets """
        sprite_sheet_swd_draw = SpriteSheet("images/k_swd_d.png")
        sprite_sheet_swd_rdy = SpriteSheet("images/k_swd_rdy.png")

        for i in range(0, 12, 1):
            ss_swd_draw = sprite_sheet_swd_draw.sprite_sheet
            width = ss_swd_draw.get_width()
            height = ss_swd_draw.get_height()
            image = sprite_sheet_swd_draw.get_image(i * width // 12, 0, width // 12, height)
            self.swrd_draw_r.append(image)

        for i in range(0, 12, 1):
            ss_swd_draw = sprite_sheet_swd_draw.sprite_sheet
            width = ss_swd_draw.get_width()
            height = ss_swd_draw.get_height()
            image = sprite_sheet_swd_draw.get_image(i * width // 12, 0, width // 12, height)
            image = pygame.transform.flip(image, True, False)
            self.swrd_draw_l.append(image)


        # load all right facing images - swd_rdy
        for i in range(0, 2, 1):
            ss_swd_rdy = sprite_sheet_swd_rdy.sprite_sheet
            width = ss_swd_rdy.get_width()
            height = ss_swd_rdy.get_height()
            image = sprite_sheet_swd_rdy.get_image(i * width // 2, 0, width // 2, height)
            self.swrd_rdy_r.append(image)

        # load all left facing ready images - swd_rdy
        for i in range(0, 2, 1):
            width = ss_swd_rdy.get_width()
            height = ss_swd_rdy.get_height()
            image = sprite_sheet_swd_rdy.get_image(width/2 * i, 0,
                                           width/2, height)
            image = pygame.transform.flip(image, True, False)
            self.swrd_rdy_l.append(image)


    def __init__(self):
        super().__init__()
        self.swrd_draw_r = []
        self.swrd_draw_l = []
        
        self.swrd_rdy_r = []
        self.swrd_rdy_l = []

        self.load_images()

        self.image = self.swrd_draw_r[0]
        self.rect = self.image.get_rect()

        # frame counter
        self.cnt_swrd_draw = 0

        # position of the Action Frames
        self.pos = vec((0, 0))

    def ani_turn_off(self):
        self.image = Surface((self.rect.width, self.rect.height), flags = SRCALPHA)
        self.image.fill((0, 0, 0, 0))

    def ani_move(self):
        if P1.orientation == 'right' and self.cnt_swrd_draw // 4 == 11:
            frame = (self.pos.x // 30) % len(self.swrd_rdy_r)
            self.image = self.swrd_rdy_r[int(frame)]
        if P1.orientation == 'left' and self.cnt_swrd_draw // 4 == 11:
            frame = (self.pos.x // 30) % len(self.swrd_rdy_l)
            self.image = self.swrd_rdy_l[int(frame)]



    def ani_swd_draw(self):
        period = 4
        max_period = period * (len(self.swrd_draw_r) - 1)
        if P1.orientation == 'right':
            if P1.swd_on == True:
                P1.swd_drwn = True  # turn the Player frame off
                if (self.cnt_swrd_draw >= max_period):
                    self.cnt_swrd_draw = max_period
                else:
                    self.cnt_swrd_draw += 1
                self.image = self.swrd_draw_r[self.cnt_swrd_draw//period]

            elif P1.swd_on == False:
                if (self.cnt_swrd_draw <= 0):
                    self.cnt_swrd_draw = 0
                    self.ani_turn_off()
                    P1.swd_drwn = False # turn the Player frame on
                else:
                    self.cnt_swrd_draw -= 1
                    self.image = self.swrd_draw_r[self.cnt_swrd_draw//period]

        if P1.orientation == 'left':
            if P1.swd_on == True:
                P1.swd_drwn = True  # turn the Player frame off
                if (self.cnt_swrd_draw >= max_period):
                    self.cnt_swrd_draw = max_period
                else:
                    self.cnt_swrd_draw += 1
                self.image = self.swrd_draw_l[self.cnt_swrd_draw//period]

            elif P1.swd_on == False:
                if (self.cnt_swrd_draw <= 0):
                    self.cnt_swrd_draw = 0
                    self.ani_turn_off()
                    P1.swd_drwn = False # turn the Player frame on
                else:
                    self.cnt_swrd_draw -= 1
                    self.image = self.swrd_draw_l[self.cnt_swrd_draw//period]





    def animate(self):
        self.ani_swd_draw()
        self.ani_move()


    def render(self):
        self.animate()
        if P1.orientation == 'right':
            self.pos.x = P1.pos.x - OFF_SET_X
            self.pos.y = P1.pos.y - P1.rect.height - OFF_SET_Y

        if P1.orientation == 'left':
            self.pos.x = P1.pos.x  - OFF_SET_X - 51
            self.pos.y = P1.pos.y - P1.rect.height - OFF_SET_Y

        screen.blit(self.image, self.pos, self.rect)


#     def ani_swrd_draw(self):
#         """animate the swrd draw movement """
#         period = 2
# #        cnt_swrd_draw
#         if self.swrd_on == True:
#             if (self.cnt_swrd_draw >= period * (len(self.swrd_draw) - 1)):
#                 self.cnt_swrd_draw = period * (len(self.swrd_draw) - 1)
#             else:
#                 self.cnt_swrd_draw += 1

#             self.image = self.swrd_draw[self.cnt_swrd_draw//period]
#         else:
#             self.cnt_swrd_draw = 0




KuppaAct = K_Act()
