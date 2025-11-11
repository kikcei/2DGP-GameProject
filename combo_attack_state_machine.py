from pico2d import *
from state_machine import StateMachine

def down_a(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_a

def down_s(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_s

class Attack_A:
    def __init__(self, player):
        self.player = player
        self.pressed_key = None  # 어떤 키가 눌렸는지만 기록

    def enter(self, e):
        self.player.frame_players_attack_a = 0
        self.image = (
            self.player.image_players_attack_a
            if self.player.face_dir == 1
            else self.player.image_players_attack_a_left
        )
        self.pressed_key = None

    def do(self):
        self.player.frame_players_attack_a += 1

        # 프레임 끝나면 입력 확인 후 상태 전환
        if self.player.frame_players_attack_a >= 7:
            self.player.frame_players_attack_a = 7

            # 입력 판정
            if self.pressed_key == SDLK_a:
                next_state = Attack_A_A(self.player)
            elif self.pressed_key == SDLK_s:
                next_state = Attack_A_S(self.player)
            else:
                next_state = self.player.IDLE

            # 상태 전환
            self.player.state_machine.cur_state.exit(None)
            self.player.state_machine.cur_state = next_state
            self.player.state_machine.cur_state.enter(None)

    def handle_event(self, event):
        if event[0] == 'INPUT' and event[1].type == SDL_KEYDOWN:
            key = event[1].key
            # 키를 “즉시 반응”하지 않고 기록만 해둔다
            if key in (SDLK_a, SDLK_s):
                self.pressed_key = key

    def draw(self):
        if self.player.face_dir == 1:
            self.player.image_players_attack_a[self.player.frame_players_attack_a].draw(self.player.x + 22, self.player.y - 8)
        else:
            self.player.image_players_attack_a_left[self.player.frame_players_attack_a].draw(self.player.x - 29, self.player.y - 8)

class Attack_A_A:
    def __init__(self, player):
        self.player = player

    def enter(self, player, e):
        self.player.frame_players_attack_a_a = 0

    def exit(self, e):
        pass

    def do(self, player):
        pass

    def handle_event(self, player, e):
        pass

    def draw(self, player):
        if self.player.face_dir == 1:
            self.player.image_players_attack_a_a[self.player.frame_players_attack_a].draw(self.player.x + 22,self.player.y - 8)

        else:
            self.player.image_players_attack_a_a_left[self.player.frame_players_attack_a].draw(self.player.x - 29,self.player.y - 8)


class Attack_A_S:
    def __init__(self, player):
        self.player = player

    def enter(self, player, e):
        pass

    def exit(self, e):
        pass

    def do(self, player):
        pass

    def handle_event(self, player, e):
        pass

    def draw(self, player):
       pass

class Attack_A_S_A:
    def enter(self, player, e):
        pass

    def exit(self, e):
        pass

    def do(self, player):
        pass

    def handle_event(self, player, e):
        pass

    def draw(self, player):
       pass

class Attack_S:
    def enter(self, player, e):
        pass

    def exit(self, e):
        pass

    def do(self, player):
        pass

    def handle_event(self, player, e):
        pass

    def draw(self, player):
       pass

class Attack_S_S:
    def enter(self, player, e):
        pass

    def exit(self, e):
        pass

    def do(self, player):
        pass

    def handle_event(self, player, e):
        pass

    def draw(self, player):
       pass

