#!/usr/bin/env python3
import pygame
from moviepy.editor import *



def play_cutscene_1_1():
    # Create a VideoCapture object and read from input file
#    pygame.init()
    clip = VideoFileClip('videos/1_1.mp4')

    clipresized = clip.resize(height=600)
    clip.preview()
#    pygame.quit()
