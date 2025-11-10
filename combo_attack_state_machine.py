from pico2d import *
from state_machine import StateMachine

def down_a(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_a

def down_s(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_s

class Attack_A:
    def __init__(self, player):
        self.player = player  # 여기서 Player 저장

    def enter(self, e):
        self.player.frame_players_attack_a = 0
        self.image = self.player.image_players_attack_a if self.player.face_dir==1 else self.player.image_players_attack_a_left

    def do(self):
        self.player.frame_players_attack_a = (self.player.frame_players_attack_a + 1) % 8

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

