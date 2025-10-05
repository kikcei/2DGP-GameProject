from pico2d import *

class Sky:
    def __init__(self):
        self.image = load_image('resources/maps/images/1391.jpg')

    def update(self):
        pass

    def draw(self):
        self.image.draw(400, 300)
        pass

class Grass:
    def __init__(self):
        self.image = load_image('resources/maps/images/DefineSprite_1860.png')
    def update(self):    #객체의 상호 작용, 행위
        pass

    def draw(self):
        self.image.draw(400,30)
        pass

class Maps:
    def __init__(self):
        self.sky = Sky()
        self.grass = Grass()

    def update(self):
        self.sky.update()
        self.grass.update()

    def draw(self):
        self.sky.draw()
        self.grass.draw()