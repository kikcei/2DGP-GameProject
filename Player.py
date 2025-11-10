from pico2d import *
from state_machine import StateMachine
from resource_load import PlayerResourceLoad
import time

DOUBLE_TAP_RUN_TIME = 0.2

def down_a(eve):
    return eve[0] =='INPUT' and eve[1].type == SDL_KEYDOWN and eve[1].key == SDLK_a

def up_a(eve):
    return eve[0] == 'INPUT' and eve[1].type == SDL_KEYUP and eve[1].key == SDLK_a


def right_down(eve):
    return eve[0] =='INPUT' and eve[1].type == SDL_KEYDOWN and eve[1].key == SDLK_RIGHT
def right_up(eve):
    return eve[0] =='INPUT' and eve[1].type == SDL_KEYUP and eve[1].key == SDLK_RIGHT
def left_down(eve):
    return eve[0] =='INPUT' and eve[1].type == SDL_KEYDOWN and eve[1].key == SDLK_LEFT
def left_up(eve):
    return eve[0] =='INPUT' and eve[1].type == SDL_KEYUP and eve[1].key == SDLK_LEFT

def up_down(eve):
    return eve[0] == 'INPUT' and eve[1].type == SDL_KEYDOWN and eve[1].key == SDLK_UP
def up_up(eve):
    return eve[0] == 'INPUT' and eve[1].type == SDL_KEYUP and eve[1].key == SDLK_UP
def down_down(eve):
    return eve[0] == 'INPUT' and eve[1].type == SDL_KEYDOWN and eve[1].key == SDLK_DOWN
def down_up(eve):
    return eve[0] == 'INPUT' and eve[1].type == SDL_KEYUP and eve[1].key == SDLK_DOWN


class Idle:

    def __init__(self, player):
        self.player = player

    def enter(self, e):
        pass
    def exit(self, e):
        pass

    def do(self):
        self.player.frame_players_stop_body = (self.player.frame_players_stop_body + 1) % 11
        self.player.frame_players_stop_leg = (self.player.frame_players_stop_leg + 1) % 11

    def draw(self):
        if self.player.face_dir == 1:
            self.player.image_players_stop_leg.draw(self.player.x - 3, self.player.y - 56)  # Adjust y position for leg
            self.player.image_players_stop_body[self.player.frame_players_stop_body].draw(self.player.x, self.player.y)
        else:
            self.player.image_players_stop_leg_left.draw(self.player.x - 3, self.player.y - 56)  # Adjust y position for leg
            self.player.image_players_stop_body_left[self.player.frame_players_stop_body].draw(self.player.x, self.player.y)


class Walk:

    def __init__(self, player):
        self.player = player

    def enter(self, e):
        pass

    def exit(self, e):
        pass

    def do(self):
        # 이동 방향 계산
        self.player.dirx = int(self.player.keys['right']) - int(self.player.keys['left'])
        self.player.diry = int(self.player.keys['up']) - int(self.player.keys['down'])
        self.player.face_dir = self.player.dirx + self.player.diry

        # 모든 키가 떨어졌을 때 IDLE 상태로 전환
        if (not self.player.keys['left'] and not self.player.keys['right']
                and not self.player.keys['up'] and not self.player.keys['down']):
            self.player.state_machine.cur_state.exit(None)
            self.player.state_machine.cur_state = self.player.IDLE
            self.player.state_machine.cur_state.enter(None)

        # 프레임 갱신
        if self.player.dirx != 0 or self.player.diry != 0:
            self.player.frame_players_walk = (self.player.frame_players_walk + 1) % 10
        else:
            self.player.frame_players_stop_body = (self.player.frame_players_stop_body + 1) % 11
            self.player.frame_players_stop_leg = (self.player.frame_players_stop_leg + 1) % 11

        # 위치 갱신
        self.player.x += self.player.dirx * 5
        self.player.y += self.player.diry * 5

    def draw(self):
        # 방향에 따라 그리기
        if self.player.face_dir == 1:
            self.player.image_players_walk[self.player.frame_players_walk].draw(self.player.x, self.player.y)
        else:
            self.player.image_players_walk_left[self.player.frame_players_walk].draw(self.player.x, self.player.y)




class  Run:

    def __init__(self, player):
        self.player = player

    def enter(self, e):
        pass

    def exit(self, e):
        pass

    def do(self):
        self.player.dirx = int(self.player.keys['right']) - int(self.player.keys['left'])
        self.player.diry = int(self.player.keys['up']) - int(self.player.keys['down'])
        self.player.face_dir = self.player.dirx + self.player.diry
        # 모든 키가 떨어졌을 때 IDLE 상태로 전환
        if (not self.player.keys['left'] and not self.player.keys['right']
                and not self.player.keys['up'] and not self.player.keys['down']):
            self.player.state_machine.cur_state.exit(None)
            self.player.state_machine.cur_state = self.player.IDLE
            self.player.state_machine.cur_state.enter(None)

        # 프레임 갱신
        if self.player.dirx != 0 or self.player.diry != 0:
            self.player.frame_players_run = (self.player.frame_players_run + 1) % 5
        else:
            self.player.frame_players_stop_body = (self.player.frame_players_stop_body + 1) % 11
            self.player.frame_players_stop_leg = (self.player.frame_players_stop_leg + 1) % 11

        # 위치 갱신
        self.player.x += self.player.dirx * 10
        self.player.y += self.player.diry * 10

    def draw(self):
        # 방향에 따라 그리기
        if self.player.face_dir == 1:
            self.player.image_players_run[self.player.frame_players_run].draw(self.player.x, self.player.y - 10)
        else:
            self.player.image_players_run_left[self.player.frame_players_run].draw(self.player.x, self.player.y - 10)


class Attack:

    def __init__(self, player):
        self.player = player

    def enter(self, e):
        pass

    def exit(self, e):
        pass

    def do(self):
        if self.player.frame_players_attack_a == 7:
            # 공격 애니메이션 끝나면 IDLE로 복귀
            self.player.state_machine.cur_state.exit(None)
            self.player.state_machine.cur_state = self.player.IDLE
            self.player.state_machine.cur_state.enter(None)

        self.player.frame_players_attack_a = (self.player.frame_players_attack_a + 1) % 8

    def draw(self):
        if self.player.face_dir == 1:
            self.player.image_players_attack_a[self.player.frame_players_attack_a].draw(self.player.x + 22,self.player.y - 8)
        else:
            self.player.image_players_attack_a_left[self.player.frame_players_attack_a].draw(self.player.x + 22,self.player.y - 8)



class Player:

    def __init__(self,resource_loader: PlayerResourceLoad):
        self.image_players_shadow = resource_loader.get('shadow')

        # 정지 상태
        self.image_players_stop_body = resource_loader.get('stop_body')
        self.image_players_stop_leg = resource_loader.get('stop_leg')
        self.image_players_stop_body_left = resource_loader.get('stop_body_left')
        self.image_players_stop_leg_left = resource_loader.get('stop_leg_left')

        # 걷기
        self.image_players_walk = resource_loader.get('walk')
        self.image_players_walk_left = resource_loader.get('walk_left')

        # 달리기
        self.image_players_run = resource_loader.get('run')
        self.image_players_run_left = resource_loader.get('run_left')

        # 공격 (A)
        self.image_players_attack_a = resource_loader.get('attack_a')
        self.image_players_attack_a_left = resource_loader.get('attack_a_left')

        # 공격 (A+A)
        self.image_players_attack_a_a = resource_loader.get('attack_a_a')
        self.image_players_attack_a_a_left = resource_loader.get('attack_a_a_left')

        # 공격 (A+S)
        self.image_players_attack_a_s = resource_loader.get('attack_a_s')
        self.image_players_attack_a_s_left = resource_loader.get('attack_a_s_left')

        # 공격 (A+S+A)
        self.image_players_attack_a_s_a = resource_loader.get('attack_a_s_a')
        self.image_players_attack_a_s_a_left = resource_loader.get('attack_a_s_a_left')

        # 공격 (S)
        self.image_players_attack_s = resource_loader.get('attack_s')
        self.image_players_attack_s_left = resource_loader.get('attack_s_left')

        # 공격 (S+S)
        self.image_players_attack_s_s = resource_loader.get('attack_s_s')
        self.image_players_attack_s_s_left = resource_loader.get('attack_s_s_left')

        self.frame_players_stop_body = 0
        self.frame_players_stop_leg = 0
        self.frame_players_walk = 0
        self.frame_players_run = 0
        self.frame_players_attack_a = 0
        self.frame_players_attack_a_a = 0
        self.frame_players_attack_a_s = 0
        self.frame_players_attack_a_s_a = 0
        self.frame_players_attack_s = 0
        self.frame_players_attack_s_s = 0


        self.dirx = 0
        self.diry = 0

        self.keys = {'left': False, 'right': False, 'up': False, 'down': False}
        self.face_dir = 1
        self.x, self.y = 400, 300

        self.last_key_time = {'left': 0, 'right': 0, 'up': 0, 'down': 0}
        self.last_tap_time = 0


        self.IDLE = Idle(self)
        self.WALK = Walk(self)
        self.RUN = Run(self)
        self.ATTACK = Attack(self)
        self.state_machine = StateMachine(
            self.IDLE,
            {
                self.IDLE: {right_down: self.WALK, left_down: self.WALK, right_up: self.IDLE, left_up: self.IDLE,
                            up_down: self.WALK, up_up: self.IDLE, down_down: self.WALK, down_up: self.IDLE, down_a: self.ATTACK},

                self.WALK: {  right_down: self.WALK, left_down: self.WALK,
                             up_down: self.WALK,  down_down: self.WALK, down_a: self.ATTACK},

                self.ATTACK: {},

                self.RUN: {down_a: self.ATTACK}
            }
        )



    def handle_event(self,evt):
        now = time.time()

        if evt.type == SDL_KEYDOWN:
            if evt.key == SDLK_LEFT: self.keys['left'] = True
            self.face_dir = -1
            if evt.key == SDLK_RIGHT: self.keys['right'] = True
            self.face_dir = 1
            if evt.key == SDLK_UP: self.keys['up'] = True
            if evt.key == SDLK_DOWN: self.keys['down'] = True

        elif evt.type == SDL_KEYUP:
            if evt.key == SDLK_LEFT: self.keys['left'] = False
            if evt.key == SDLK_RIGHT: self.keys['right'] = False
            if evt.key == SDLK_UP: self.keys['up'] = False
            if evt.key == SDLK_DOWN: self.keys['down'] = False

        key_map = {SDLK_LEFT: 'left', SDLK_RIGHT: 'right'}

        if evt.type == SDL_KEYDOWN and evt.key in key_map:
            key = key_map[evt.key]
            if now - self.last_key_time[key] < DOUBLE_TAP_RUN_TIME:
                self.state_machine.cur_state.exit(None)
                self.state_machine.cur_state = self.RUN
                self.state_machine.cur_state.enter(None)
            self.last_key_time[key] = now
            self.keys[key] = True

        elif evt.type == SDL_KEYUP and evt.key in key_map:
            key = key_map[evt.key]
            self.keys[key] = False

        self.state_machine.handle_state_event(('INPUT', evt))





    def update(self):
        self.state_machine.update()

    def draw(self):
        self.image_players_shadow.draw(self.x - 5, self.y - 74)
        self.state_machine.draw()