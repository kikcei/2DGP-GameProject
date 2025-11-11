from resource_load import PlayerResourceLoad
from state_machine import StateMachine
import math
from Player import Player
import random


class Idle:
    def __init__(self, special_monster1,player):
        self.special_monster1 = special_monster1
        self.player = player

    def enter(self,e):
        pass


    def exit(self,e):
        pass


    def do(self):

        self.special_monster1.frame_special_monster1_walk = (self.special_monster1.frame_special_monster1_walk + 1)%8
        # --- 플레이어 방향으로 이동하는 로직 ---
        dx = self.player.x - self.special_monster1.x
        dy = self.player.y - self.special_monster1.y
        rad = math.atan2(dy, dx)  # 각도 계산

        speed = 2  # 이동 속도 (원하면 special_monster1.speed 로 대체 가능)
        self.special_monster1.x += math.cos(rad) * speed
        self.special_monster1.y += math.sin(rad) * speed

        # --- 방향 결정 ---
        if self.player.x <= self.special_monster1.x:
            self.special_monster1.face_dir = -1
        else:
            self.special_monster1.face_dir = 1

        # --- 플레이어와의 거리 확인 (예: 일정 거리 이상이면 다른 상태로 전이) ---
        distance = math.sqrt(dx * dx + dy * dy)


    def draw(self):
        if self.special_monster1.face_dir == 1:
            self.special_monster1.image_special_monster1_walk[self.special_monster1.frame_special_monster1_walk].draw(self.special_monster1.x , self.special_monster1.y -4 )
        else:
            self.special_monster1.image_special_monster1_walk_left[self.special_monster1.frame_special_monster1_walk].draw(self.special_monster1.x-6 , self.special_monster1.y -4)


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

    def __init__(self,resource_loader: PlayerResourceLoad,player):
        self.player = player

        self.image_special_monster1_shadow = resource_loader.get('shadow')

        self.image_special_monster1_stop = resource_loader.get('special_monster1_stop')
        self.image_special_monster1_stop_left = resource_loader.get('special_monster1_stop_left')
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

        self.IDLE = Idle(self,player)
        self.ATTACK1 = Attack1(self)
        self.ATTACK2 = Attack2(self)
        self.ATTACK3 = Attack3(self)

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
