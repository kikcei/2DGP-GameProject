import game_framework
from resource_load import PlayerResourceLoad
from state_machine import StateMachine
import math
import random

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.25
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8
FRAMES_PER_SECOND = FRAMES_PER_ACTION * ACTION_PER_TIME

class Idle:
    def __init__(self, special_monster1,player):
        self.special_monster1 = special_monster1
        self.player = player

    def enter(self,e):
        pass


    def exit(self,e):
        pass


    def do(self):


        self.special_monster1.frame_special_monster1_walk = (self.special_monster1.frame_special_monster1_walk + FRAMES_PER_SECOND * game_framework.frame_time)%8
        # --- 플레이어 방향으로 이동하는 로직 ---

        dx = self.player.x - self.special_monster1.x
        dy = self.player.y - self.special_monster1.y
        rad = math.atan2(dy, dx)  # 각도 계산

        distance = math.sqrt(dx * dx + dy * dy)

        if abs(dx) >= 100:
            self.special_monster1.x += math.cos(rad) * RUN_SPEED_PPS * game_framework.frame_time
        elif abs(dx) < 95:
            self.special_monster1.x -= math.cos(rad) * RUN_SPEED_PPS * game_framework.frame_time
        self.special_monster1.y += math.sin(rad)  * RUN_SPEED_PPS * game_framework.frame_time

        # --- 방향 결정 ---
        if self.player.x <= self.special_monster1.x:
            self.special_monster1.face_dir = -1
        else:
            self.special_monster1.face_dir = 1

        if  abs(dy) <20 and abs(dx) <= 100:
            num=random.choice([1,2,3])
            next_state = self.special_monster1.IDLE
            if num == 1:
                next_state = self.special_monster1.ATTACK1
            elif num == 2:
                next_state = self.special_monster1.ATTACK2
            elif num == 3:
                next_state = self.special_monster1.ATTACK3
            self.special_monster1.state_machine.cur_state.exit(None)
            self.special_monster1.state_machine.cur_state = next_state
            self.special_monster1.state_machine.cur_state.enter(None)


    def draw(self):
        if self.special_monster1.face_dir == 1:
            self.special_monster1.image_special_monster1_walk[int(self.special_monster1.frame_special_monster1_walk)].draw(self.special_monster1.x , self.special_monster1.y -4 )
        else:
            self.special_monster1.image_special_monster1_walk_left[int(self.special_monster1.frame_special_monster1_walk)].draw(self.special_monster1.x-6 , self.special_monster1.y -4)


class Attack1:
    def __init__(self, special_monster1):
        self.special_monster1 = special_monster1


    def enter(self,e):
        self.special_monster1.frame_special_monster1_attack1 = 0


    def exit(self,e):
        pass

    def do(self):
        self.special_monster1.frame_special_monster1_attack1 = self.special_monster1.frame_special_monster1_attack1 + FRAMES_PER_SECOND * game_framework.frame_time

        if self.special_monster1.frame_special_monster1_attack1 >=13:
            self.special_monster1.state_machine.cur_state.exit(None)
            self.special_monster1.state_machine.cur_state = self.special_monster1.IDLE
            self.special_monster1.state_machine.cur_state.enter(None)


    def draw(self):
        if self.special_monster1.face_dir == 1:
            self.special_monster1.image_special_monster1_attack1[int(self.special_monster1.frame_special_monster1_attack1)].draw(self.special_monster1.x + 4, self.special_monster1.y - 9)
        else:
            self.special_monster1.image_special_monster1_attack1_left[int(self.special_monster1.frame_special_monster1_attack1)].draw(self.special_monster1.x - 6,self.special_monster1.y - 9)


class Attack2:
    def __init__(self, special_monster1):
        self.special_monster1 = special_monster1

    def enter(self, e):
        self.special_monster1.frame_special_monster1_attack2 = 0

    def exit(self, e):
        pass

    def do(self):
        self.special_monster1.frame_special_monster1_attack2 = self.special_monster1.frame_special_monster1_attack2 + FRAMES_PER_SECOND * game_framework.frame_time

        if self.special_monster1.frame_special_monster1_attack2 >= 12:
            self.special_monster1.state_machine.cur_state.exit(None)
            self.special_monster1.state_machine.cur_state = self.special_monster1.IDLE
            self.special_monster1.state_machine.cur_state.enter(None)

    def draw(self):
        if self.special_monster1.face_dir == 1:
            self.special_monster1.image_special_monster1_attack2[int(self.special_monster1.frame_special_monster1_attack2)].draw(self.special_monster1.x-2,
                                                                           self.special_monster1.y +13)
        else:
            self.special_monster1.image_special_monster1_attack2_left[int(
                self.special_monster1.frame_special_monster1_attack2)].draw(self.special_monster1.x - 4,
                                                                           self.special_monster1.y +13)


class Attack3:
    def __init__(self, special_monster1):
        self.special_monster1 = special_monster1

    def enter(self, e):
        self.special_monster1.frame_special_monster1_attack3 = 0

    def exit(self, e):
        pass

    def do(self):
        self.special_monster1.frame_special_monster1_attack3 = self.special_monster1.frame_special_monster1_attack3 + FRAMES_PER_SECOND * game_framework.frame_time


        if self.special_monster1.frame_special_monster1_attack3 >= 13:
            self.special_monster1.state_machine.cur_state.exit(None)
            self.special_monster1.state_machine.cur_state = self.special_monster1.IDLE
            self.special_monster1.state_machine.cur_state.enter(None)

    def draw(self):
        if self.special_monster1.face_dir == 1:
            self.special_monster1.image_special_monster1_attack3[int(
                self.special_monster1.frame_special_monster1_attack3)].draw(self.special_monster1.x+13,
                                                                           self.special_monster1.y - 11)
        else:
            self.special_monster1.image_special_monster1_attack3_left[int(
                self.special_monster1.frame_special_monster1_attack3)].draw(self.special_monster1.x - 19,
                                                                           self.special_monster1.y - 11)


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
