import pygame as pg
import pygame.freetype as pgtype
import player
import balls
import random
from settings import *
pg.init()



class Game:
    def __init__(self):
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.player = player.Player()
        self.enemies = []
        self.enemyevent = pg.USEREVENT
        self.menu= True
        self.truy = 0
        self.win = None
        self.text_font = pgtype.Font("font/Acumin-ItPro_RUS.ttf", 20)
        pg.time.set_timer(self.enemyevent, 500)
        for i in range(0, 10):
            enemy = balls.Enemy(random.randint(self.player.hitbox.width - 10, self.player.hitbox.width + 10))
            self.enemies.append(enemy)
        self.clock = pg.time.Clock()
        self.run()

    def run(self):
        while True:
            self.event()
            self.update()
            self.draw()
            self.clock.tick(FPS)

    def event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()
            if self.menu == False:
                if event.type == pg.MOUSEMOTION:
                    self.player.xy = event.pos
            if  event.type == self.enemyevent:
                enemy = balls.Enemy(random.randint(self.player.hitbox.width - 1, self.player.hitbox.width + 1))
                self.enemies.append(enemy)
            if self.menu == True:
                if event.type == pg.KEYDOWN:
                    self.menu = False
    def update(self):
        for i in self.enemies:
            i.move()
            if self.menu == False:
                if self.player.hitbox.colliderect(i.hitbox) and self.player.hitbox.size >= i.hitbox.size:
                    self.player.hitbox.width = self.player.hitbox.width + 50
                    self.player.hitbox.height = self.player.hitbox.height + 50
                    self.enemies.remove(i)
                if self.player.hitbox.colliderect(i.hitbox) and self.player.hitbox.size < i.hitbox.size:
                    self.menu = True
                    self.truy = 1
                    self.win = False
                    self.player.hitbox.w = 50
                    self.player.hitbox.h = 50
                self.player.move()
            if self.player.hitbox.w >= 500:
                self.win = True
                self.truy = 1 
                self.menu = True
                self.player.hitbox.w = 50
                self.player.hitbox.h = 50
    def draw(self):
        self.screen.fill([255, 255, 255])
        if self.menu == False:
            self.player.draw(self.screen)
        for i in self.enemies:
            i.draw(self.screen)
        if self.menu == True:
            if  self.truy <= 0:
                self.text_font.render_to(self.screen, [SCREEN_WIDTH//2, SCREEN_HEIGHT//2], "press any to start")
            if self.truy > 0:
                self.text_font.render_to(self.screen, [SCREEN_WIDTH//2, SCREEN_HEIGHT//2], "press any to restart")
                if self.win == True:
                    self.text_font.render_to(self.screen, [SCREEN_WIDTH//3, SCREEN_HEIGHT//3], "YOU WIN")
                elif self.win == False: 
                    self.text_font.render_to(self.screen, [SCREEN_WIDTH//3, SCREEN_HEIGHT//3], "YOU LOSE")
        
        pg.display.flip()


if __name__ == "__main__":
    Game()