#!/usr/bin/env python3
from UI import Ch_Sel_UI

Ch_Menu = Ch_Sel_UI()

if __name__ == 'runChMenu':
    while Ch_Menu.running:
        Ch_Menu.run()
