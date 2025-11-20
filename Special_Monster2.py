import game_framework
import game_world
from resource_load import PlayerResourceLoad
from state_machine import StateMachine
import math
import random

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 7.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.3
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8
FRAMES_PER_SECOND = FRAMES_PER_ACTION * ACTION_PER_TIME

class Idle:
    def __init__(self, special_monster2,player):
        self.special_monster2 = special_monster2
        self.player = player

    def enter(self,e):
        pass

    def exit(self,e):
        pass

    def do(self):
        self.special_monster2.frame_special_monster2_body=(self.special_monster2.frame_special_monster2_body + FRAMES_PER_SECOND * game_framework.frame_time) % 8

        dx = self.player.x - self.special_monster2.x
        dy = self.player.y - self.special_monster2.y
        rad = math.atan2(dy, dx)  # 각도 계산

        if abs(dx)<340:
            self.special_monster2.x -= math.cos(rad) * 1.3 * RUN_SPEED_PPS * game_framework.frame_time

        elif 340 < abs(dx) <= 350:
            self.special_monster2.x = self.special_monster2.x
            self.special_monster2.y += math.sin(rad) * 2 * RUN_SPEED_PPS * game_framework.frame_time
        else:
            self.special_monster2.x += math.cos(rad) * 1.5 * RUN_SPEED_PPS * game_framework.frame_time
        self.special_monster2.y += math.sin(rad) * 2 * RUN_SPEED_PPS * game_framework.frame_time

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
            self.special_monster2.image_special_monster2_body[int(self.special_monster2.frame_special_monster2_body)].draw(self.special_monster2.x - 7, self.special_monster2.y - 20)
            self.special_monster2.image_special_monster2_walk[int(self.special_monster2.frame_special_monster2_walk)].draw(self.special_monster2.x-1 , self.special_monster2.y  -31)
        else:
            self.special_monster2.image_special_monster2_body_left[int(self.special_monster2.frame_special_monster2_body)].draw(self.special_monster2.x + 2, self.special_monster2.y - 20)
            self.special_monster2.image_special_monster2_walk_left[int(self.special_monster2.frame_special_monster2_walk)].draw(self.special_monster2.x - 3, self.special_monster2.y - 31)

class Attack:
    def __init__(self, special_monster2,player):
        self.special_monster2 = special_monster2
        self.player = player

    def enter(self, e):
        self.special_monster2.frame_special_monster2_attack = 0

    def exit(self, e):
        pass

    def do(self):
        prev = int(self.special_monster2.frame_special_monster2_attack)
        self.special_monster2.frame_special_monster2_attack += FRAMES_PER_SECOND * game_framework.frame_time
        curr = int(self.special_monster2.frame_special_monster2_attack)

        if prev < 14 <= curr:
            ammo = Attack_Ammo(self.special_monster2)
            ammo.enter(None)
            game_world.add_object(ammo, 1)
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
            self.special_monster2.image_special_monster2_attack[int(self.special_monster2.frame_special_monster2_attack)].draw(self.special_monster2.x + 70, self.special_monster2.y - 27)
        else:
            self.special_monster2.image_special_monster2_attack_left[int(self.special_monster2.frame_special_monster2_attack)].draw(self.special_monster2.x - 70 ,self.special_monster2.y - 27)

class Attack_Ammo:
    def __init__(self, special_monster2):
        self.special_monster2 = special_monster2
        self.face_dir = 1
        self.x = special_monster2.x
        self.y = special_monster2.y
        self.speed = 9

    def enter(self, e):
        self.face_dir = self.special_monster2.face_dir

    def do(self):
        # 방향에 따라 이동
        self.x += self.speed * self.face_dir * -1 * RUN_SPEED_PPS * game_framework.frame_time

    def update(self):
        self.do()
        if not (100 <= self.x <= 1280 and 0 <= self.y <= 720):
            game_world.remove_object(self)

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

    def draw(self):
        self.image_special_monster2_shadow.draw(self.x - 2, self.y - 74)
        self.state_machine.draw()


