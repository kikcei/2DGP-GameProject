from pico2d import *

class Player:
    def __init__(self):

        for i in range(1, 12):
            path = f'resources/Player/sprites/DefineSprite_60/{i}.png'
            image = load_image(path)
            self.image_players_stop_body.append(image)

        self.image_players_stop_leg = load_image('resources/Player/sprites/DefineSprite_124/1.png')
        self.x, self.y = 400, 300



        self.frame_players_stop_body = 0
        self.frame_players_stop_leg = 0

    def update(self):
        self.frame_players_stop_body = (self.frame_players_stop_body + 1) % 11
        self.frame_players_stop_leg = (self.frame_players_stop_leg + 1) % 1  # Assuming only one frame for leg

    def draw(self):
        self.image_players_stop_body[self.frame_players_stop_body].draw(self.x, self.y)
        self.image_players_stop_leg.draw(self.x, self.y - 50)  # Adjust y position for leg


class All_Player:
    def __init__(self):
        self.player = Player()

    def update(self):
        self.player.update()

    def draw(self):
       self.player.draw()
