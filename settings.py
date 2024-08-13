import pygame as pg

pg.init()

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700

FPS = 60

font = pg.font.Font(None, 40)

player_high = 400
player_width = 200
player_color = [255, 0, 0]
player_size = [50, 50]
player_xy = pg.mouse.get_pos()

def text_render(text):
    return font.render(str(text), True, "black")

