import game_framework
from resource_load import PlayerResourceLoad
from state_machine import StateMachine
import random
import math

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 25.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.2
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8
FRAMES_PER_SECOND = FRAMES_PER_ACTION * ACTION_PER_TIME

class Idle:
    def __init__(self,boos,player):
        self.boos = boos
        self.player = player

        if self.player.x <= self.boos.x:
            self.boos.face_dir = -1
        else:
            self.boos.face_dir = 1

    def enter(self,e):
        pass

    def exit(self,e):
        pass

    def do(self):
        self.boos.frame_boos_walk = (self.boos.frame_boos_walk + FRAMES_PER_SECOND * game_framework.frame_time) % 9
        # --- 플레이어 방향으로 이동하는 로직 ---

        dx = self.player.x - self.boos.x
        dy = self.player.y - self.boos.y
        rad = math.atan2(dy, dx)  # 각도 계산

        distance = math.sqrt(dx * dx + dy * dy)

        if abs(dx) >= 100:
            self.boos.x += math.cos(rad) * RUN_SPEED_PPS * game_framework.frame_time
        elif abs(dx) < 95:
            self.boos.x -= math.cos(rad) * RUN_SPEED_PPS * game_framework.frame_time
        self.boos.y += math.sin(rad) * RUN_SPEED_PPS * game_framework.frame_time

        # --- 방향 결정 ---
        if self.player.x <= self.boos.x:
            self.boos.face_dir = -1
        else:
            self.boos.face_dir = 1

        if abs(dy) < 20 and abs(dx) <= 100:
            num = random.choice([1, 2, 3])
            next_state = self.boos.IDLE
            if num == 1:
                next_state = self.boos.ATTACK1
            elif num == 2:
                next_state = self.boos.ATTACK2
            elif num == 3:
                next_state = self.boos.ATTACK3
            self.boos.state_machine.cur_state.exit(None)
            self.boos.state_machine.cur_state = next_state
            self.boos.state_machine.cur_state.enter(None)


def draw(self):
    if self.boos.face_dir == 1:
        self.boos.image_boos_walk[int(self.boos.frame_boos_walk)].draw(self.boos.x, self.boos.y - 4)

    else:
        self.boos.image_boos_walk_left[int(self.boos.frame_boos_walk)].draw(self.boos.x - 6, self.boos.y - 4)



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

class Attack_Gun:
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

    def __init__(self,resource_loader: PlayerResourceLoad,player):
        self.player = player

        self.image_boos_shadow = resource_loader.get('shadow')
        self.image_boos_walk = resource_loader.get('boos_walk')
        self.image_boos_walk_left = resource_loader.get('boos_walk_left')
        self.image_boos_attack1 = resource_loader.get('boos_attack1')
        self.image_boos_attack1_left = resource_loader.get('boos_attack1_left')
        self.image_boos_attack2 = resource_loader.get('boos_attack2')
        self.image_boos_attack2_left = resource_loader.get('boos_attack2_left')
        self.image_boos_attack_gun = resource_loader.get('boos_attack_gun')
        self.image_boos_attack_gun_left = resource_loader.get('boos_attack_gun_left')

        self.x = 600
        self.y = 300

        self.frame_boos_walk = 0
        self.frame_boos_attack1 = 0
        self.frame_boos_attack2 = 0
        self.frame_boos_attack_gun = 0

        self.IDLE = Idle(self,player)
        self.ATTACK1 = Attack1()
        self.ATTACK2 = Attack2()
        self.ATTACK_Gun = Attack_Gun()
        self.skill = Skill()

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
