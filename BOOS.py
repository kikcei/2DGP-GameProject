import game_framework
from resource_load import PlayerResourceLoad
from state_machine import StateMachine
import random
import math

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 12.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.3
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


        dx = self.player.x - self.boos.x
        dy = self.player.y - self.boos.y
        rad = math.atan2(dy, dx)  # 각도 계산

        if abs(dx) < 400:
            self.boos.x -= math.cos(rad)  * RUN_SPEED_PPS * game_framework.frame_time

        elif 300 < abs(dx) <= 400:
            self.boos.x = self.boos.x
            self.boos.y += math.sin(rad) * RUN_SPEED_PPS * game_framework.frame_time
        else:
            self.boos.x += math.cos(rad)  * RUN_SPEED_PPS * game_framework.frame_time
        self.boos.y += math.sin(rad) * 2 * RUN_SPEED_PPS * game_framework.frame_time

        if self.player.x <= self.boos.x:
            self.boos.face_dir = -1
        else:
            self.boos.face_dir = 1

        if abs(dy) < 20 and 100 >= abs(dx) > 80:
            next_state = self.boos.ATTACK1
            self.boos.state_machine.cur_state.exit(None)
            self.boos.state_machine.cur_state = next_state
            self.boos.state_machine.cur_state.enter(None)

        elif abs(dy) < 20 and abs(dx) < 80:
            next_state = self.boos.ATTACK2
            self.boos.state_machine.cur_state.exit(None)
            self.boos.state_machine.cur_state = next_state
            self.boos.state_machine.cur_state.enter(None)

        elif abs(dy) < 20 and 400> abs(dx) > 300:
            next_state = self.boos.ATTACK_Gun
            self.boos.state_machine.cur_state.exit(None)
            self.boos.state_machine.cur_state = next_state
            self.boos.state_machine.cur_state.enter(None)
        else:
            if random.random() < 0.001:
                next_state = self.boos.ATTACK_SKILL
                self.boos.state_machine.cur_state.exit(None)
                self.boos.state_machine.cur_state = next_state
                self.boos.state_machine.cur_state.enter(None)

    def draw(self):
        if self.boos.face_dir == 1:
            self.boos.image_boos_walk[int(self.boos.frame_boos_walk)].draw(self.boos.x, self.boos.y - 4)

        else:
            self.boos.image_boos_walk_left[int(self.boos.frame_boos_walk)].draw(self.boos.x - 6, self.boos.y - 4)


class Attack1:
    def __init__(self,boos):
        self.boos = boos

    def enter(self,e):
        self.boos.frame_boos_attack1 = 0

    def exit(self,e):
        pass

    def do(self):
        self.boos.frame_boos_attack1 = self.boos.frame_boos_attack1 + FRAMES_PER_SECOND * game_framework.frame_time
        self.boos.x += self.boos.face_dir* RUN_SPEED_PPS * game_framework.frame_time
        if self.boos.frame_boos_attack1 >= 15:
            self.boos.state_machine.cur_state.exit(None)
            self.boos.state_machine.cur_state = self.boos.IDLE
            self.boos.state_machine.cur_state.enter(None)

    def draw(self):
        if self.boos.face_dir == 1:
            self.boos.image_boos_attack1[int(self.boos.frame_boos_attack1)].draw(self.boos.x - 14, self.boos.y +19)
        else:
            self.boos.image_boos_attack1_left[int(self.boos.frame_boos_attack1)].draw(self.boos.x + 9, self.boos.y +19)


class Attack2:
    def __init__(self,boos):
        self.boos = boos

    def enter(self,e):
        self.boos.frame_boos_attack2 = 0

    def exit(self,e):
        pass

    def do(self):
        self.boos.frame_boos_attack2 = self.boos.frame_boos_attack2 + FRAMES_PER_SECOND * 1.5 * game_framework.frame_time
        if self.boos.frame_boos_attack2 >= 31:
            self.boos.state_machine.cur_state.exit(None)
            self.boos.state_machine.cur_state = self.boos.IDLE
            self.boos.state_machine.cur_state.enter(None)

    def draw(self):
        if self.boos.face_dir == 1:
            self.boos.image_boos_attack2[int(self.boos.frame_boos_attack2)].draw(self.boos.x, self.boos.y + 28)
        else:
            self.boos.image_boos_attack2_left[int(self.boos.frame_boos_attack2)].draw(self.boos.x , self.boos.y + 28)


class Attack_Gun:
    def __init__(self,boos):
        self.boos = boos

    def enter(self,e):
        self.boos.frame_boos_attack_gun = 0

    def exit(self,e):
        pass

    def do(self):
        self.boos.frame_boos_attack_gun = self.boos.frame_boos_attack_gun + FRAMES_PER_SECOND * 1.5 * game_framework.frame_time
        if self.boos.frame_boos_attack_gun >= 23:
            self.boos.state_machine.cur_state.exit(None)
            self.boos.state_machine.cur_state = self.boos.IDLE
            self.boos.state_machine.cur_state.enter(None)

    def draw(self):
        if self.boos.face_dir == 1:
            self.boos.image_boos_attack_gun[int(self.boos.frame_boos_attack_gun)].draw(self.boos.x + 107, self.boos.y-1 )
        else:
            self.boos.image_boos_attack_gun_left[int(self.boos.frame_boos_attack_gun)].draw(self.boos.x - 112, self.boos.y-1 )


class Skill:
    def __init__(self, boos):
        self.boos = boos
        self.min_x = 40
        self.min_y = 40
        self.max_x = 760
        self.max_y = 560
        self.timer = 0

    def enter(self,e):
        self.boos.frame_boos_attack_skill = 0
        self.timer = 0
    def exit(self,e):
        pass

    def do(self):
        self.boos.frame_boos_attack_skill = (self.boos.frame_boos_attack_skill + FRAMES_PER_SECOND * 1.5 * game_framework.frame_time) % 12
        self.timer += game_framework.frame_time

        if self.timer >= 5:
            self.boos.state_machine.cur_state.exit(None)
            self.boos.state_machine.cur_state = self.boos.IDLE
            self.boos.state_machine.cur_state.enter(None)

        if self.boos.x <= self.min_x:  # 왼쪽 벽
            self.boos.x = self.min_x
            self.boos.dirx *= -1
            self.boos.face_dir = 1
        elif self.boos.x >= self.max_x:  # 오른쪽 벽
            self.boos.x = self.max_x
            self.boos.dirx *= -1
            self.boos.face_dir = -1

        if self.boos.y <= self.min_y:  # 아래 벽
            self.boos.y = self.min_y
            self.boos.diry *= -1
        elif self.boos.y >= self.max_y:  # 위 벽
            self.boos.y = self.max_y
            self.boos.diry *= -1

        self.boos.x += self.boos.dirx * RUN_SPEED_PPS * 3 * game_framework.frame_time
        self.boos.y += self.boos.diry * RUN_SPEED_PPS * 3 * game_framework.frame_time




    def draw(self):
        self.boos.image_boos_attack_skill[int(self.boos.frame_boos_attack_skill)].draw(self.boos.x , self.boos.y )


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
        self.image_boos_attack_skill = resource_loader.get('boos_attack_skill')

        self.x = 600
        self.y = 400
        self.dirx = random.choice([-1, 1])
        self.diry = random.choice([-1, 1])
        self.face_dir = random.choice([-1, 1])

        self.frame_boos_walk = 0
        self.frame_boos_attack1 = 0
        self.frame_boos_attack2 = 0
        self.frame_boos_attack_gun = 0
        self.frame_boos_attack_skill = 0

        self.IDLE = Idle(self,player)
        self.ATTACK1 = Attack1(self)
        self.ATTACK2 = Attack2(self)
        self.ATTACK_Gun = Attack_Gun(self)
        self.ATTACK_SKILL = Skill(self)

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
