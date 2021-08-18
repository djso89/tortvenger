#!/usr/bin/env python3
from stageobject import *



class Stage(pygame.sprite.Sprite):
    """ class Stage """

    def __init__(self):
        """initialize the Stage """
        self.num_bg = 20
        self.scroll = 0
        self.Bldgs = Bldgs
        self.platforms = platforms
        self.Plats = Plats
        self.Steps = Steps
        self.Bricks = Bricks
        self.Cars = Cars


        # stage objects to show
        self.StageBlocks = pygame.sprite.Group()
        self.StageBlocks.add(self.Plats)
        self.StageBlocks.add(self.platforms)
        self.StageBlocks.add(self.Cars)
        self.StageBlocks.add(self.Steps)
        self.StageBlocks.add(self.Bldgs)

        self.bgimg = pygame.image.load("images/bg_level.png").convert()
        self.bgimg1 = pygame.transform.flip(self.bgimg, True, False)
        self.stagesurf = pygame.Surface([self.num_bg * self.bgimg.get_width(),\
                                         self.bgimg.get_height()]).convert()


        for i in range(0, self.num_bg, 1):
            if i % 2 == 0:
                self.stagesurf.blit(self.bgimg, (i * self.bgimg.get_width(), 0))
            else:
                self.stagesurf.blit(self.bgimg1, (i * self.bgimg1.get_width(), 0))

        #self.rect = self.bgimg.get_rect(topleft=(0,0))

    def change_background(self, pic):
        self.bgimg = pygame.image.load(pic).convert()
        self.rect = self.bgimg.get_rect(topleft=(0,0))

    def draw(self, screen, SB_SW):
        screen.fill(setting.bg_color)
        screen.blit(self.stagesurf, (0, 0),\
                    (self.scroll, 0, self.bgimg.get_width(), self.bgimg.get_height()))
        for block in self.Bricks:
            screen.blit(block.surf, block.rect)
        if SB_SW:
            for block in self.StageBlocks:
                screen.blit(block.surf, block.rect)


ST1 = Stage()
#Bldgs = ST1.Bldgs
#platforms = ST1.platforms
#Plats = ST1.Plats
#Steps = ST1.Steps
#Bricks = ST1.Bricks
#Cars = ST1.Cars
#BackDrop = pygame.sprite.Group()




Stage1Blocks = pygame.sprite.Group()
Stage1Blocks.add(platforms)
Stage1Blocks.add(Bricks)
#Stage1Blocks.add(BackDrop)
Stage1Blocks.add(Plats)
