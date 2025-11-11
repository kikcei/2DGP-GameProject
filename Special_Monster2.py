from resource_load import PlayerResourceLoad
from state_machine import StateMachine
import math
import random


class Idle:
    def __init__(self, special_monster2,player):
        self.special_monster2 = special_monster2
        self.player = player

    def enter(self,e):
        pass

    def exit(self,e):
        pass

    def do(self):
       pass

    def draw(self):
        if self.special_monster2.face_dir == 1:
            self.special_monster2.image_special_monster2_walk[self.special_monster2.frame_special_monster2_walk].draw(self.special_monster2.x - 7, self.special_monster2.y - 20)
        else:
            self.special_monster2.image_special_monster2_walk_left[self.special_monster2.frame_special_monster2_walk].draw(self.special_monster2.x + 2, self.special_monster2.y - 20)


class Attack:
    def __init__(self, special_monster2):
        self.special_monster2 = special_monster2


    def enter(self, e):
        pass

    def exit(self, e):
        pass

    def do(self):
        pass

    def draw(self):
        if self.special_monster2.face_dir == 1:
            self.special_monster2.image_special_monster2_walk[self.special_monster2.frame_special_monster2_walk].draw(
                self.special_monster2.x - 7, self.special_monster2.y - 20)
        else:
            self.special_monster2.image_special_monster2_walk_left[
                self.special_monster2.frame_special_monster2_walk].draw(self.special_monster2.x + 2,
                                                                        self.special_monster2.y - 20)


class Special_Monster2:

    def __init__(self,resource_loader: PlayerResourceLoad,player):
        self.player = player

        self.image_special_monster2_shadow = resource_loader.get('shadow')

        self.image_special_monster2_walk = resource_loader.get('special_monster2_walk')
        self.image_special_monster2_walk_left = resource_loader.get('special_monster2_walk_left')
        self.image_special_monster2_attack = resource_loader.get('special_monster2_attack')
        self.image_special_monster2_attack_left = resource_loader.get('special_monster2_attack_left')
        self.image_special_monster2_ammo = resource_loader.get('special_monster2_ammo')
        self.image_special_monster2_ammo_left = resource_loader.get('special_monster2_ammo_left')


        self.x = 800
        self.y = 100

        self.face_dir = random.choice([-1, 1])

        self.frame_special_monster2_walk = 0
        self.frame_special_monster2_attack = 0

        self.IDLE = Idle(self,player)
        self.ATTACK = Attack(self)


        self.state_machine = StateMachine(
            self.IDLE,
            {
                self.IDLE:{},
            }
        )


    def update(self):
        self.state_machine.update()

    def draw(self):
        self.image_special_monster2_shadow.draw(self.x - 2, self.y - 74)
        self.state_machine.draw()
