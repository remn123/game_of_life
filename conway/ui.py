import pygame as pg
import pygame_gui as pgui

#from pygame_gui.core import ObjectID
from pygame_gui.elements import UIButton, UILabel, UIImage

class UserInterface:
    
    def __init__(self, game):
        self.game = game
        self.settings = game.settings
        W, H = self.settings.get('resolution')
        theme = self.settings.get('theme')
        self.manager = pgui.UIManager((W, H), theme)
        self.widgets = self._make_widgets(W, H)
        
    def update(self):
        dt = self.game.dt
        self.manager.update(dt)
    
    def draw(self):
        self.manager.draw_ui(self.game.screen)
        
    def on_events(self, event):
        self.manager.process_events(event)
    
    def _make_widgets(self, width, height):
        image_path = self.settings.get('image')
        image_surface = pg.image.load(image_path).convert()
        img_w, img_h = image_surface.get_size()
        scale = 2
        img_w, img_h = scale*img_w, scale*img_h
        ratio = width / height
        w = 200
        h = int(w//ratio)
        
        
        widgets = dict(
            label = UILabel(
                relative_rect=pg.Rect(
                    (475, 70),
                    (-1, -1)
                ),
                text="Conway's Game of Life",
                manager=self.manager
            ),
            button = UIButton(
                relative_rect=pg.Rect(
                    ((width-w)//2, (height-h)//2),
                    (-1, -1)
                ),
                text='Start Game',
                manager=self.manager
            ),
            image = UIImage(
                relative_rect=pg.Rect(
                    (width-500, (height-400)//2),
                    (img_w, img_h)
                ),
                image_surface=image_surface,
                manager=self.manager
            )
        )
        return widgets