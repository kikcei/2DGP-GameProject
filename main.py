from pico2d import *
from Maps import *
WIDTH, HEIGHT = 800,600

def main():
    open_canvas(WIDTH, HEIGHT)

    map = Maps()
    while True:
        clear_canvas()  # 이전 프레임 지움

        map.draw()  # 지도

        update_canvas()  # 그린 걸 실제로 화면에 표시

        delay(0.03)

    close_canvas()

if __name__ == '__main__':
    main()