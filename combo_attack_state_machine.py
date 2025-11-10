from pico2d import *
from state_machine import StateMachine

def down_a(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_a

def down_s(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_s

class Attack_A:
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
