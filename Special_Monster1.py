from resource_load import PlayerResourceLoad
from state_machine import StateMachine
import random


class Idle:
    def __init__(self, special_monster1):
        self.special_monster1 = special_monster1


    def enter(self,e):
        pass


    def exit(self,e):
        pass

    def do(self):
       pass


    def draw(self):
        if self.special_monster1.face_dir == 1:
            self.special_monster1.image_special_monster1_walk[self.special_monster1.frame_special_monster1_walk].draw(self.special_monster1.x - 7, self.special_monster1.y - 20)
        else:
            self.special_monster1.image_special_monster1_walk_left[self.special_monster1.frame_special_monster1_walk].draw(self.special_monster1.x + 2, self.special_monster1.y - 20)



class Attack1:
    def __init__(self, special_monster1):
        self.special_monster1 = special_monster1


    def enter(self,e):
        pass


    def exit(self,e):
        pass

    def do(self):
       pass


    def draw(self):
        pass


class Attack2:
    def __init__(self, special_monster1):
        self.special_monster1 = special_monster1


    def enter(self,e):
        pass


    def exit(self,e):
        pass

    def do(self):
       pass


    def draw(self):
        pass


class Attack3:
    def __init__(self, special_monster1):
        self.special_monster1 = special_monster1


    def enter(self,e):
        pass


    def exit(self,e):
        pass

    def do(self):
       pass


    def draw(self):
        pass


class Special_Monster1:

    def __init__(self,resource_loader: PlayerResourceLoad):

        self.image_special_monster1_shadow = resource_loader.get('shadow')

        self.image_special_monster1_walk = resource_loader.get('special_monster1_walk')
        self.image_special_monster1_walk_left = resource_loader.get('special_monster1_walk_left')
        self.image_special_monster1_attack1 = resource_loader.get('special_monster1_attack1')
        self.image_special_monster1_attack1_left = resource_loader.get('special_monster1_attack1_left')
        self.image_special_monster1_attack2 = resource_loader.get('special_monster1_attack2')
        self.image_special_monster1_attack2_left = resource_loader.get('special_monster1_attack2_left')
        self.image_special_monster1_attack3 = resource_loader.get('special_monster1_attack3')
        self.image_special_monster1_attack3_left = resource_loader.get('special_monster1_attack3_left')


        self.x = 400
        self.y = 500
        self.face_dir = random.choice([-1, 1])

        self.frame_special_monster1_walk = 0
        self.frame_special_monster1_attack1 = 0
        self.frame_special_monster1_attack2 = 0
        self.frame_special_monster1_attack3 = 0

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
        self.image_special_monster1_shadow.draw(self.x - 2, self.y - 74)
        self.state_machine.draw()
