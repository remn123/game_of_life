import pygame as pg
import pandas as pd
import numpy as np


class Map:
    
    def __init__(self, game):
        self.game = game
        self.settings = game.settings
        self.scale = int(self.settings.get('scale'))
        J, I = self.settings.get('resolution')
        self.I, self.J = I // self.scale, J // self.scale
        self.mini_map = []
        self.world_map = {}
        self.dt = 1
        self._running = False
        self._has_changed = False
        self._status = ''
        self._make_initial_map()
        self.get_map()
        
    def _make_initial_map(self):
        data = np.zeros((self.I, self.J), dtype=int)
        df = pd.DataFrame(data)
        self.mini_map = df.to_numpy()
        #print(self.mini_map)
        
    def get_map(self):
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                self.world_map[(i, j)] = value
    
    def update(self):
        timestep = int(self.settings.get('timestep'))
        self.dt += self.game.dt
        if self._running and self.dt >= timestep:
            self.mini_map = self.game.conway.step(self.mini_map)
            self.dt = 0
            self._has_changed = True
        if self._has_changed:
            self.get_map()
            self._has_changed = False
            
    def draw(self):
        for pos in self.world_map:
            value = int(1-self.world_map[pos])
            if not value:
                color = self.settings.get('live_color')
                pg.draw.rect(
                    self.game.screen, 
                    color,
                    (pos[0]*self.scale, pos[1]*self.scale, self.scale, self.scale), 
                    value
                )
            # Draw borders
            pg.draw.rect(
                self.game.screen, 
                self.settings.get('border_color'),
                (pos[0]*self.scale, pos[1]*self.scale, self.scale, self.scale), 
                1
            )
            
        if self._status == 'RUNNING':
            pg.draw.circle(self.game.screen, 'green', (self.J*self.scale-50, 25), 15)
        elif self._status == 'PAUSED':
            pg.draw.rect(self.game.screen, 'red', (self.J*self.scale-65, 5, 30, 30), 0)
        
    def on_events(self, event):
        # TODO: Transcript into a better Design Pattern
        keys = pg.key.get_pressed()
        if not self._running:
            if event.type == pg.MOUSEBUTTONUP:
                if event.button == 1: # left
                    y, x = pg.mouse.get_pos()
                    x = x // self.scale
                    y = y // self.scale
                    self.mini_map[x, y] = 1
                    print(f'self.mini_map[({x}, {y})] = {self.mini_map[x, y]}')
                    self._has_changed = True
                if event.button == 3: # right
                    y, x = pg.mouse.get_pos()
                    x = x // self.scale
                    y = y // self.scale
                    self.mini_map[x, y] = 0 
                    print(f'self.mini_map[({x}, {y})] = {self.mini_map[x, y]}')
                    self._has_changed = True
            
            if keys[pg.K_KP_ENTER] or keys[pg.K_RETURN]:
                print("Running Conway's Algorithm...")
                self._running = True
                self._status = 'RUNNING'
                
        else:
            if keys[pg.K_SPACE]:
                print("Stop Conway's Algorithm...")
                self._running = False
                self._status = 'STOPPED'
                
            if keys[pg.K_KP_ENTER] or keys[pg.K_RETURN]:
                print("Pause Conway's Algorithm...")
                self._running = False
                self._status = 'PAUSED'
        