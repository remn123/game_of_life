import pygame as pg
import pygame_gui as pgui
import sys

from conway.settings import *
from conway.map import *
from conway.algorithm import *
from conway.ui import *

class Game:
    
    def __init__(self):
        pg.init()
        self.settings = Settings('resources/config.yaml')
        self.screen = pg.display.set_mode(self.settings.get('resolution'))
        self.clock = pg.time.Clock()
        self.dt = 1
        self.state = 'START_GAME'
        self.make_game()
    
    def make_game(self):
        self.map = Map(self)
        self.conway = Conway(self)
        self.ui = UserInterface(self)
        
    def update(self):
        self.ui.update()
        self.map.update()
        pg.display.flip()
        self.dt = self.clock.tick(self.settings.get('fps'))
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')
    
    def draw(self):
        
        
        if self.state == 'START_GAME':
            self.ui.draw()
            
        if self.state == 'LOAD_MAP':
            self.screen.fill(self.settings.get('background_color'))
            self.map.draw()
    
    def on_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            
            if event.type == pgui.UI_BUTTON_PRESSED:
              if event.ui_element == self.ui.widgets.get('button'):
                  print('Starting Game...')
                  self.state = 'LOAD_MAP'
            
            if self.state == 'START_GAME':
                self.ui.on_events(event)
                
            if self.state == 'LOAD_MAP':
                self.map.on_events(event)
    
    def run(self):
        while True:
            self.on_events()
            self.update()
            self.draw()


    
        