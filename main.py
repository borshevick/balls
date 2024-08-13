import pygame as pg
import player
import balls
from settings import *
pg.init()



class Game:
    def __init__(self):

        
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.player = player.player()
        self.enemies = []
        for i in range(0, 10):
            enemy = balls.enemy()
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
            if event.type == pg.MOUSEMOTION:
                self.player.xy = event.pos
            for i in self.enemies:
                if self.player.hitbox.colliderect(i.hitbox):
                    if self.player.hitbox.width > i.hitbox.width:
                        self.enemies.remove(i) 
                        self.player.hitbox.width =  self.player.hitbox.width + i.size//2 
                        self.player.hitbox.height =  self.player.hitbox.height + i.size//2 
                    else: 
                        self.game_over = True

    def update(self):
        for i in self.enemies:
                i.move()
        self.player.move()

    def draw(self):
        self.screen.fill([255, 255, 255])
        self.player.draw(self.screen)
        for i in self.enemies:
            i.draw(self.screen)
        pg.display.flip()


if __name__ == "__main__":
    Game()