from pico2d import *
from Maps import *
from Player import *

WIDTH, HEIGHT = 800,600

def main():
    open_canvas(WIDTH, HEIGHT)

    map = Maps()
    player = Player()

    while True:
        clear_canvas()  # 이전 프레임 지움

        map.draw()  # 지도
        player.handle_events()
        player.update()  # 플레이어 상태 업데이트
        player.draw()  # 플레이어 그리기

        update_canvas()  # 그린 걸 실제로 화면에 표시

        delay(0.03)

    close_canvas()

if __name__ == '__main__':
    main()