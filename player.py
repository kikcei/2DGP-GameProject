from pico2d import *

class Player:
    def __init__(self):
        self.image = load_image('resources/player/images/Player.png')
        self.x, self.y = 400, 300
        self.frame = 0

    def update(self):
        self.frame = (self.frame + 1) % 8  # Assuming there are 8 frames in the sprite sheet

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)  # Adjust according to sprite size