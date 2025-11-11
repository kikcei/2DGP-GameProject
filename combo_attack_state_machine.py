from pico2d import *
from state_machine import StateMachine

def down_a(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_a

def down_s(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_s

class Attack_A:
    def __init__(self, player):
        self.player = player
        self.can_receive_input = False
        self.next_input = None

    def enter(self, e):
        self.player.frame_players_attack_a = 0
        self.image = self.player.image_players_attack_a if self.player.face_dir == 1 else self.player.image_players_attack_a_left
        self.can_receive_input = False
        self.next_input = None

    def do(self):
        # 프레임 진행
        self.player.frame_players_attack_a += 1

        if self.player.frame_players_attack_a >= 7:  # 마지막 프레임 도달
            self.player.frame_players_attack_a = 7
            self.can_receive_input = True

            # 버퍼링된 입력이 있으면 처리
            if self.next_input is not None:
                self.handle_event(self.next_input)
            else:
                # 입력 없으면 Idle로 전환
                self.player.state_machine.cur_state.exit(None)
                self.player.state_machine.cur_state = self.player.IDLE
                self.player.state_machine.cur_state.enter(None)

    def handle_event(self, event):
        if not self.can_receive_input:
            # 프레임이 끝나기 전이면 입력 버퍼링
            self.next_input = event
            return

        if event[0] == 'INPUT' and event[1].type == SDL_KEYDOWN:
            key = event[1].key
            if key == SDLK_a:
                next_state = Attack_A_A(self.player)
            elif key == SDLK_s:
                next_state = Attack_A_S(self.player)
            else:
                next_state = self.player.IDLE

            self.player.state_machine.cur_state.exit(None)
            self.player.state_machine.cur_state = next_state
            self.player.state_machine.cur_state.enter(None)

    def draw(self):
        if self.player.face_dir == 1:
            self.player.image_players_attack_a[self.player.frame_players_attack_a].draw(self.player.x+22, self.player.y-8)
        else:
            self.player.image_players_attack_a_left[self.player.frame_players_attack_a].draw(self.player.x-29, self.player.y-8)

class Attack_A_A:
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

