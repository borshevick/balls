import pygame as pg
from settings import *
pg.init()


class Player():
    def __init__(self):
        self.color = player_color
        self.xy = player_xy
        self.size = [player_size, player_size]
        self.hitbox = pg.rect.Rect(self.xy, self.size)
        
    def draw(self, screen):
        pg.draw.ellipse(screen, self.color, self.hitbox)
        
    def move(self):
        self.hitbox.center = pg.mouse.get_pos()
