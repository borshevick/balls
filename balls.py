import pygame as pg
import random
from settings import *
pg.init()


class enemy():
    def __init__(self):
        self.xspeed = 5
        self.yspeed = 5
        self.color1 = random.randint(1, 255)
        self.color2 = random.randint(1, 255)
        self.color3 = random.randint(1, 255)
        self.x = random.randint(1, SCREEN_WIDTH)
        self.y = random.randint(1, SCREEN_HEIGHT)
        self.size = random.randint(1, 100)
        self.hitbox = pg.rect.Rect([self.x, self.y], [self.size, self.size])
        
    def draw(self, screen):
        pg.draw.ellipse(screen, [self.color1, self.color2, self.color3], self.hitbox)
    
    def move(self):
        self.hitbox.x = self.hitbox.x+self.xspeed
        if self.hitbox.right > SCREEN_WIDTH:
            self.xspeed = random.randint(-5, -1)
            self.ballcolor3 = random.randint(0, 255)
            self.ballcolor2 = random.randint(0, 255)
            self.ballcolor1 = random.randint(0, 255)
        if self.hitbox.left <= 0:
            self.xspeed = random.randint(1, 5)
            self.ballcolor3 = random.randint(0, 255)
            self.ballcolor2 = random.randint(0, 255)
            self.ballcolor1 = random.randint(0, 255)
            self.hitbox.y = self.hitbox.y+self.yspeed
        if self.hitbox.top <= 0:
            self.self.yspeed = random.randint(1, 5)
            if self.xspeed < 0:
                self.xspeed = random.randint(-5, -1)
            else:
                self.xspeed = random.randint(1, 5)
            self.ballcolor3 = random.randint(0, 255)
            self.ballcolor2 = random.randint(0, 255)
            self.ballcolor1 = random.randint(0, 255)
        if self.hitbox.bottom >= 600:
            if self.xspeed > 0:
                self.xspeed = random.randint(1, 10)
            else:
                self.xspeed = random.randint(-10, -1)
            self.yspeed = random.randint(-10, -1)
            self.ballcolor3 = random.randint(0, 255)
            self.ballcolor2 = random.randint(0, 255)
            self.ballcolor1 = random.randint(0, 255)