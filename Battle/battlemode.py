#!/usr/bin/env python3
"""Battle mode functions """
from display import WIN_W
from covid19 import move_cell


def move_camera_x(player, stage, x_range):
    """
    set the boundary for player
    in horizontal direction
    """
    # player reached the end of the stage
    # lock the camera
    if abs(stage.scroll) >= (stage.num_bg - 1) * WIN_W:
        stage.scroll = -1 * (stage.num_bg - 1) * WIN_W
        player.battlesteps = 0
        if player.pos.x < 0:
            player.pos.x = 0
        if player.pos.x >= WIN_W - player.rect.width:
            player.pos.x = WIN_W - player.rect.width
    else:
        if player.pos.x < 0:
            player.pos.x = 0
        if player.pos.x >= x_range - player.rect.width:
            diff = (player.pos.x + player.rect.width) - x_range
            stage.move_stage(-diff)
            move_cell(-diff, stage.cells)
            player.pos.x = x_range - player.rect.width
            if player.vel.x >= 4 and player.vel.x < 5:
                player.battlesteps += 1


def lock_camera_x(player, stage):
    if player.pos.x < 0:
        player.pos.x = 0
    if player.pos.x >= WIN_W - player.rect.width:
        player.pos.x = WIN_W - player.rect.width
    if not stage.cells:
        stage.battlemode = False
        stage.cell_plats.empty()
