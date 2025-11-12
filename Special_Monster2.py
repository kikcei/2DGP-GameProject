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
        self.special_monster2.frame_special_monster2_body=(self.special_monster2.frame_special_monster2_body + 1) % 8

        dx = self.player.x - self.special_monster2.x
        dy = self.player.y - self.special_monster2.y
        rad = math.atan2(dy, dx)  # 각도 계산

        distance = math.sqrt(dx * dx + dy * dy)

        speed = 2  # 이동 속도 (원하면 special_monster1.speed 로 대체 가능)
        if abs(dx)<340:
            self.special_monster2.x -= math.cos(rad) * 2
        elif 340 < abs(dx) <= 350:
            self.special_monster2.x = self.special_monster2.x
            self.special_monster2.y += math.sin(rad) * 3
        else:
            self.special_monster2.x += math.cos(rad) * 1.5
        self.special_monster2.y += math.sin(rad) * 3

        if self.player.x <= self.special_monster2.x:
            self.special_monster2.face_dir = 1
        else:
            self.special_monster2.face_dir = -1


        if  abs(dy) <5 and 185 <= abs(dx) <= 350 :
            next_state = self.special_monster2.ATTACK
            self.special_monster2.state_machine.cur_state.exit(None)
            self.special_monster2.state_machine.cur_state = next_state
            self.special_monster2.state_machine.cur_state.enter(None)

    def draw(self):
        if self.special_monster2.face_dir == -1:
            self.special_monster2.image_special_monster2_body[self.special_monster2.frame_special_monster2_body].draw(self.special_monster2.x - 7, self.special_monster2.y - 20)
            self.special_monster2.image_special_monster2_walk[self.special_monster2.frame_special_monster2_walk].draw(self.special_monster2.x-1 , self.special_monster2.y  -31)
        else:
            self.special_monster2.image_special_monster2_body_left[self.special_monster2.frame_special_monster2_body].draw(self.special_monster2.x + 2, self.special_monster2.y - 20)
            self.special_monster2.image_special_monster2_walk_left[self.special_monster2.frame_special_monster2_walk].draw(self.special_monster2.x - 3, self.special_monster2.y - 31)

class Attack:
    def __init__(self, special_monster2,player):
        self.special_monster2 = special_monster2
        self.player = player

    def enter(self, e):
        self.special_monster2.frame_special_monster2_attack = 0

    def exit(self, e):
        pass

    def do(self):
        self.special_monster2.frame_special_monster2_attack = self.special_monster2.frame_special_monster2_attack+1
        if self.special_monster2.frame_special_monster2_attack == 14:
            ammo = Attack_Ammo(self.special_monster2)
            ammo.enter(None)
            self.special_monster2.ammo.append(ammo)
        if self.special_monster2.frame_special_monster2_attack >= 23:
            dx = self.player.x - self.special_monster2.x
            dy = self.player.y - self.special_monster2.y

            if 185 <= abs(dx) <= 350 and abs(dy) < 5:
                next_state = self.special_monster2.ATTACK
            else:
                next_state = self.special_monster2.IDLE


            self.special_monster2.state_machine.cur_state.exit(None)
            self.special_monster2.state_machine.cur_state = next_state
            self.special_monster2.state_machine.cur_state.enter(None)

    def draw(self):
        if self.special_monster2.face_dir == -1:
            self.special_monster2.image_special_monster2_attack[self.special_monster2.frame_special_monster2_attack].draw(self.special_monster2.x + 70, self.special_monster2.y - 27)
        else:
            self.special_monster2.image_special_monster2_attack_left[self.special_monster2.frame_special_monster2_attack].draw(self.special_monster2.x - 70 ,self.special_monster2.y - 27)

class Attack_Ammo:
    def __init__(self, special_monster2):
        self.special_monster2 = special_monster2
        self.face_dir = 1
        self.x = special_monster2.x
        self.y = special_monster2.y
        self.speed = 15

    def enter(self, e):
        self.face_dir = self.special_monster2.face_dir

    def do(self):
        # 방향에 따라 이동
        self.x += self.speed * self.face_dir * -1

    def draw(self):
        if self.face_dir == -1:
            self.special_monster2.image_special_monster2_ammo[self.special_monster2.frame_special_monster2_ammo].draw(self.x+63, self.y-17)
        else:
            self.special_monster2.image_special_monster2_ammo_left[self.special_monster2.frame_special_monster2_ammo].draw(self.x-63, self.y-17)

class Special_Monster2:

    def __init__(self,resource_loader: PlayerResourceLoad,player):
        self.player = player

        self.image_special_monster2_shadow = resource_loader.get('shadow')

        self.image_special_monster2_body = resource_loader.get('basic_monster')
        self.image_special_monster2_body_left = resource_loader.get('basic_monster_left')
        self.image_special_monster2_walk = resource_loader.get('special_monster2_walk')
        self.image_special_monster2_walk_left = resource_loader.get('special_monster2_walk_left')
        self.image_special_monster2_attack = resource_loader.get('special_monster2_attack')
        self.image_special_monster2_attack_left = resource_loader.get('special_monster2_attack_left')
        self.image_special_monster2_ammo = resource_loader.get('special_monster2_attack_ammo')
        self.image_special_monster2_ammo_left = resource_loader.get('special_monster2_attack_ammo_left')


        self.x = 450
        self.y = 200

        self.face_dir = random.choice([-1, 1])

        self.ammo = []

        self.frame_special_monster2_body = 0
        self.frame_special_monster2_walk = 0
        self.frame_special_monster2_attack = 0
        self.frame_special_monster2_ammo = 0

        self.IDLE = Idle(self,player)
        self.ATTACK = Attack(self,player)


        self.state_machine = StateMachine(
            self.IDLE,
            {
                self.IDLE:{},
            }
        )


    def update(self):
        self.state_machine.update()
        for ammo in self.ammo:
            ammo.do()
        self.ammo = [ammo for ammo in self.ammo if 100 <= ammo.x <= 1280 and 0 <= ammo.y <= 720]

    def draw(self):
        self.image_special_monster2_shadow.draw(self.x - 2, self.y - 74)
        self.state_machine.draw()


        for ammo in self.ammo:
            ammo.draw()
