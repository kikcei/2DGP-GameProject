from pico2d import *

import game_framework
from BOOS import Boos
from Maps import *
from Player import *
from Basic_Monster import *
from Special_Monster1 import *
from Special_Monster2 import Special_Monster2
from resource_load import PlayerResourceLoad
import game_world

WIDTH, HEIGHT = 800, 600

def init():
    global running
    running = True
    reset_world()

def finish():
    game_world.clear()
    pass

def handle_events():  # player를 인자로 받음
    global running
    global player

    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            player.handle_event(event)  # 기존 player 객체에 이벤트 전달

def reset_world():
    global world
    global player
    resource_load = PlayerResourceLoad()
    resource_load.load()

    map = Maps()
    game_world.add_object(map, 0)

    player = Player(resource_load)
    game_world.add_object(player, 1)

    monsters = Basic_Monster(resource_load)
    game_world.add_object(monsters, 2)

    special_monster1 = Special_Monster1(resource_load,player)
    game_world.add_object(special_monster1, 2)

    special_monster2 = Special_Monster2(resource_load,player)
    game_world.add_object(special_monster2, 2)

    boos = Boos(resource_load,player)
    game_world.add_object(boos, 2)


def update():
   game_world.update_world()


def draw():
    clear_canvas()
    game_world.draw_world()
    update_canvas()


running = True
def main():
    open_canvas(WIDTH, HEIGHT)
    reset_world()

    while running:
        handle_events()
        update()
        render()


    close_canvas()


if __name__ == '__main__':
    main()

def pause():
    pass

def resume():
    pass