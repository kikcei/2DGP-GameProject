from pico2d import *

import logo_mode
import play_mode


WIDTH, HEIGHT = 800, 600

def main():
    open_canvas(WIDTH, HEIGHT)
    logo_mode.init()
    play_mode.reset_world()

    while play_mode.running:
        clear_canvas()
        play_mode.handle_events()
        play_mode.update_world()
        play_mode.render_world()
        delay(0.03)

    logo_mode.finish()
    close_canvas()


if __name__ == '__main__':
    main()
