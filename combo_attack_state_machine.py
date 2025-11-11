from pico2d import *
from state_machine import StateMachine

def down_a(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_a

def down_s(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_s

class Attack_A:
    def __init__(self, player):
        self.player = player
        self.input_queue = []  # 입력 큐

    def enter(self, e):
        self.player.frame_players_attack_a = 0
        self.input_queue.clear()
        self.image = (
            self.player.image_players_attack_a
            if self.player.face_dir == 1
            else self.player.image_players_attack_a_left
        )

    def exit(self, e):
        self.input_queue.clear()

    def do(self):
        self.player.frame_players_attack_a += 1

        if self.player.frame_players_attack_a >= 7:
            self.player.frame_players_attack_a = 7
            next_state = self.player.IDLE

            if self.input_queue:
                key = self.input_queue.pop(0)
                if key == SDLK_a:
                    next_state = Attack_A_A(self.player)
                elif key == SDLK_s:
                    next_state = Attack_A_S(self.player)

            # 상태 전환
            self.player.state_machine.cur_state.exit(None)
            self.player.state_machine.cur_state = next_state
            self.player.state_machine.cur_state.enter(None)

    def handle_event(self, e):
        if e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN:
            key = e[1].key
            if key in (SDLK_a, SDLK_s):
                self.input_queue.append(key)

    def draw(self):
        if self.player.face_dir == 1:
            self.player.image_players_attack_a[self.player.frame_players_attack_a].draw(self.player.x + 22, self.player.y - 8)
        else:
            self.player.image_players_attack_a_left[self.player.frame_players_attack_a].draw(self.player.x - 29, self.player.y - 8)

class Attack_A_A:
    def __init__(self, player):
        self.player = player
        self.input_queue = []

    def enter(self, e):
        self.player.frame_players_attack_a_a = 0
        self.input_queue.clear()
        self.image = (
            self.player.image_players_attack_a_a
            if self.player.face_dir == 1
            else self.player.image_players_attack_a_a_left
        )

    def do(self):
        self.player.frame_players_attack_a_a += 1

        if self.player.frame_players_attack_a_a >= 11:
            self.player.frame_players_attack_a_a = 11
            next_state = self.player.IDLE

            if self.input_queue:
                key = self.input_queue.pop(0)
                if key == SDLK_a:
                    next_state = Attack_A_A(self.player)
                elif key == SDLK_s:
                    next_state = Attack_A_S(self.player)

            self.player.state_machine.cur_state.exit(None)
            self.player.state_machine.cur_state = next_state
            self.player.state_machine.cur_state.enter(None)

    def handle_event(self, e):
        if e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN:
            key = e[1].key
            if key in (SDLK_a, SDLK_s):
                self.input_queue.append(key)

    def draw(self):
        if self.player.face_dir == 1:
            self.player.image_players_attack_a_a[self.player.frame_players_attack_a_a].draw(self.player.x + 22, self.player.y - 8)
        else:
            self.player.image_players_attack_a_a_left[self.player.frame_players_attack_a_a].draw(self.player.x - 29, self.player.y - 8)
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

