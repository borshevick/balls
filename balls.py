import pygame as pg
import random
from player import *
from settings import *
pg.init()


class Enemy():
    def __init__(self, size):
        self.color1 = random.randint(1, 255)
        self.color2 = random.randint(1, 255)
        self.color3 = random.randint(1, 255)
        self.s = random.randint(1, 4)
        if self.s == 1:
            self.x = random.randint(0, SCREEN_WIDTH)
            self.y= -100
            self.xspeed = random.randint(-1, 1)
            self.yspeed = random.randint(1, 5)
        if self.s == 2:
            self.x = SCREEN_WIDTH+100
            self.y= random.randint(0, SCREEN_HEIGHT)
            self.xspeed = random.randint(-5, -1)
            self.yspeed = random.randint(-1, 1)
        if self.s == 3:
            self.x = random.randint(0, SCREEN_WIDTH)
            self.y= SCREEN_HEIGHT+100
            self.xspeed = random.randint(-1, 1)
            self.yspeed = random.randint(1, 5)
        if self.s == 4:
            self.x = -100
            self.y= random.randint(0, SCREEN_HEIGHT)
            self.xspeed = random.randint(1, 5)
            self.yspeed = random.randint(-1, 1)
        self.size = size
        self.hitbox = pg.rect.Rect([self.x, self.y], [self.size, self.size])
        
    def draw(self, screen):
        pg.draw.ellipse(screen, [self.color1, self.color2, self.color3], self.hitbox)
    
    def move(self):
        self.hitbox.x = self.hitbox.x+self.xspeed
        self.hitbox.y = self.hitbox.y+self.yspeed