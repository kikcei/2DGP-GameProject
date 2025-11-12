from resource_load import PlayerResourceLoad
from state_machine import StateMachine
import random


class Idle:
    def __init__(self):
        pass
    def enter(self,e):
        pass

    def exit(self,e):
        pass

    def do(self):
        pass

    def draw(self):
        pass

class Attack1:
    def __init__(self):
        pass
    def enter(self,e):
        pass

    def exit(self,e):
        pass

    def do(self):
        pass

    def draw(self):
        pass

class Attack2:
    def __init__(self):
        pass
    def enter(self,e):
        pass

    def exit(self,e):
        pass

    def do(self):
        pass

    def draw(self):
        pass

class Skill:
    def __init__(self):
        pass
    def enter(self,e):
        pass

    def exit(self,e):
        pass

    def do(self):
        pass

    def draw(self):
        pass

class Boos:

    def __init__(self,resource_loader: PlayerResourceLoad):

        self.image_boos_shadow = resource_loader.get('shadow')

        self.image_boos_walk = resource_loader.get('basic_monster')
        self.image_boos_walk_left = resource_loader.get('basic_monster_left')


        self.x = 600
        self.y = 300

        self.face_dir = random.choice([-1, 1])

        self.frame_basic_monster_walk = 0


        self.IDLE = Idle(self)
        self.state_machine = StateMachine(
            self.IDLE,
            {
                self.IDLE:{},
            }
        )


    def update(self):
        self.state_machine.update()

    def draw(self):
        self.image_boos_shadow.draw(self.x - 2, self.y - 74)
        self.state_machine.draw()
