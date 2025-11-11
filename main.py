from pico2d import *
from Maps import *
from Player import *
from Basic_Monster import *
from resource_load import PlayerResourceLoad

WIDTH, HEIGHT = 800, 600


def handle_events(player):  # player를 인자로 받음
    global running

    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
            player.handle_event(event)  # 기존 player 객체에 이벤트 전달


def main():
    open_canvas(WIDTH, HEIGHT)

    resource_load = PlayerResourceLoad()
    resource_load.load()

    map = Maps()

    player = Player(resource_load)

    monsters = Basic_Monster(resource_load)

    global running
    running = True

    while running:
        clear_canvas()

        map.draw()
        player.update()
        handle_events(player)  # player 전달
        player.draw()

        monsters.update()
        monsters.draw()

        update_canvas()
        delay(0.03)

    close_canvas()


if __name__ == '__main__':
    main()
