#!/usr/bin/env python3
import sys


character = input("Enter the characte's name: ")
if character == 'Kuppa':
    from troopakuppa19.kuppagame import *
elif character == 'Gooster':
    from roostergooster.gst_game import *
elif character == 'Lettuce':
    from tortoise_lettuce.le_game import *
else:
    print('Error: character name is either empty or does not exist')
    sys.exit()
