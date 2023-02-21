import pygame as pg
import sys

from conway.settings import *
from conway.map import *
from conway.algorithm import *


class Game:
    
    def __init__(self):
        pg.init()
        self.settings = Settings('resources/config.yaml')
        self.screen = pg.display.set_mode(self.settings.get('resolution'))
        self.clock = pg.time.Clock()
        self.dt = 1
        self.make_game()
    
    def make_game(self):
        self.map = Map(self)
        self.conway = Conway(self)
        
    def update(self):
        self.map.update()
        pg.display.flip()
        self.dt = self.clock.tick(self.settings.get('fps'))
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')
    
    def draw(self):
        self.screen.fill(self.settings.get('background_color'))
        self.map.draw()
    
    def on_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            self.map.on_events(event)
    
    def run(self):
        while True:
            self.on_events()
            self.update()
            self.draw()


    
        