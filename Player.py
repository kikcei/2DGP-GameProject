from pico2d import *
from state_machine import StateMachine



def down_a(eve):
    return eve[0] =='INPUT' and eve[1].type == SDL_KEYDOWN and eve[1].key == SDLK_a

def up_a(eve):
    return eve[0] == 'INPUT' and eve[1].type == SDL_KEYUP and eve[1].key == SDLK_a


def right_down(eve):
    return eve[0] =='INPUT' and eve[1].type == SDL_KEYDOWN and eve[1].key == SDLK_RIGHT
def right_up(eve):
    return eve[0] =='INPUT' and eve[1].type == SDL_KEYUP and eve[1].key == SDLK_RIGHT
def left_down(eve):
    return eve[0] =='INPUT' and eve[1].type == SDL_KEYDOWN and eve[1].key == SDLK_LEFT
def left_up(eve):
    return eve[0] =='INPUT' and eve[1].type == SDL_KEYUP and eve[1].key == SDLK_LEFT

def up_down(eve):
    return eve[0] == 'INPUT' and eve[1].type == SDL_KEYDOWN and eve[1].key == SDLK_UP
def up_up(eve):
    return eve[0] == 'INPUT' and eve[1].type == SDL_KEYUP and eve[1].key == SDLK_UP
def down_down(eve):
    return eve[0] == 'INPUT' and eve[1].type == SDL_KEYDOWN and eve[1].key == SDLK_DOWN
def down_up(eve):
    return eve[0] == 'INPUT' and eve[1].type == SDL_KEYUP and eve[1].key == SDLK_DOWN


class Idle:

    def __init__(self, player):
        self.player = player

    def enter(self, e):
        pass
    def exit(self, e):
        pass

    def do(self):
        self.player.frame_players_stop_body = (self.player.frame_players_stop_body + 1) % 11
        self.player.frame_players_stop_leg = (self.player.frame_players_stop_leg + 1) % 11

    def draw(self):
        self.player.image_players_stop_leg.draw(self.player.x - 3, self.player.y - 56)  # Adjust y position for leg
        self.player.image_players_stop_body[self.player.frame_players_stop_body].draw(self.player.x, self.player.y)



class Walk:

    def __init__(self, player):
        self.keys = {'left': False, 'right': False, 'up': False, 'down': False}
        self.player = player

        # enter 함수는 해당 상태로 진입했을때 한번만 호출된다.
    def enter(self, e):
        pass

    def exit(self, e):
       pass

       #방향키를 갱신할때마다 호출된다.
    def handle_event(self, e):
        evt = e[1]  # ('INPUT', event)
        if evt.type == SDL_KEYDOWN:
            if evt.key == SDLK_LEFT: self.keys['left'] = True
            if evt.key == SDLK_RIGHT: self.keys['right'] = True
            if evt.key == SDLK_UP: self.keys['up'] = True
            if evt.key == SDLK_DOWN: self.keys['down'] = True
        elif evt.type == SDL_KEYUP:
            if evt.key == SDLK_LEFT: self.keys['left'] = False
            if evt.key == SDLK_RIGHT: self.keys['right'] = False
            if evt.key == SDLK_UP: self.keys['up'] = False
            if evt.key == SDLK_DOWN: self.keys['down'] = False

    def do(self):
        self.player.dirx = int(self.keys['right']) - int(self.keys['left'])
        self.player.face_dir = int(self.keys['right']) - int(self.keys['left']) + int(self.keys['up']) - int(self.keys['down'])
        self.player.diry = int(self.keys['up']) - int(self.keys['down'])

        # 모든 키가 떨어졌을 때 IDLE 상태로 전환
        if self.keys['left'] == False and self.keys['right'] == False \
                and self.keys['up'] == False and self.keys['down'] == False:
            self.player.state_machine.cur_state.exit(None)
            self.player.state_machine.cur_state = self.player.IDLE
            self.player.state_machine.cur_state.enter(None)
            self.keys = {'left': False, 'right': False, 'up': False, 'down': False}

        if self.player.dirx != 0 or self.player.diry != 0:
            self.player.frame_players_walk = (self.player.frame_players_walk + 1) % 10

        elif self.player.dirx == 0 and self.player.diry == 0:
            self.player.frame_players_stop_body = (self.player.frame_players_stop_body + 1) % 11
            self.player.frame_players_stop_leg = (self.player.frame_players_stop_leg + 1) % 11

        self.player.x += self.player.dirx * 5
        self.player.y += self.player.diry * 5


    def draw(self):
        if self.player.face_dir >= 1:
            self.player.image_players_walk[self.player.frame_players_walk].draw(self.player.x, self.player.y)

        elif self.player.face_dir <= -1:
            self.player.image_players_walk[self.player.frame_players_walk].draw(self.player.x, self.player.y)

        elif self.player.face_dir == 0 and self.keys['left'] == True and self.keys['up'] == True:
            self.player.image_players_walk[self.player.frame_players_walk].draw(self.player.x, self.player.y)

        elif self.player.face_dir == 0 and self.keys['right'] == True and self.keys['down'] == True:
            self.player.image_players_walk[self.player.frame_players_walk].draw(self.player.x, self.player.y)

        elif self.player.face_dir == 0 :
            self.player.image_players_stop_leg.draw(self.player.x - 3, self.player.y - 56)
            self.player.image_players_stop_body[self.player.frame_players_stop_body].draw(self.player.x, self.player.y)




class  Run:

    def __init__(self, player):
        self.player = player

    def enter(self, e):
        pass

    def exit(self, e):
        pass

    def do(self):
        pass

    def draw(self):
        pass


class Attack:

    def __init__(self, player):
        self.player = player

    def enter(self, e):
        pass

    def exit(self, e):
        pass

    def do(self):
        self.player.frame_players_attack_a = (self.player.frame_players_attack_a + 1) % 8

    def draw(self):
        self.player.image_players_attack_a[self.player.frame_players_attack_a].draw(self.player.x + 22, self.player.y - 8)



class Player:

    def __init__(self):
        self.image_players_stop_body = []
        self.image_players_walk = []
        self.image_players_run = []
        self.image_players_attack_a = []
        self.dirx = 0
        self.diry = 0

        self.state = 'stop'
        self.face_dir = 1
        self.x, self.y = 400, 300

        # stop
        for i in range(1, 12):
            path = f'resources/Players/sprites/stop/DefineSprite_60/{i}.png'
            image = load_image(path)
            self.image_players_stop_body.append(image)
        # walk
        for i in range(1, 11):
            path = f'resources/Players/sprites/walk/DefineSprite_79/{i}.png'
            image = load_image(path)
            self.image_players_walk.append(image)
        # run
        for i in range(1, 6):
            path = f'resources/Players/sprites/run/DefineSprite_91/{i}.png'
            image = load_image(path)
            self.image_players_run.append(image)
        # attack_a
        for i in range(1, 9):
            path = f'resources/Players/sprites/attack_a/DefineSprite_97/{i}.png'
            image = load_image(path)
            self.image_players_attack_a.append(image)

        self.image_players_shadow = load_image('resources/Players/sprites/shadow/DefineSprite_45/1.png')
        self.image_players_stop_leg = load_image('resources/Players/sprites/stop/DefineSprite_124/1.png')

        self.player_stop_body_frame_max = 11
        self.player_stop_leg_frame_max = 11
        self.player_walk_frame_max = 11
        self.player_run_frame_max = 6
        self.player_attack_a_frame_max = 9


        self.frame_players_stop_body = 0
        self.frame_players_stop_leg = 0
        self.frame_players_walk = 0
        self.frame_players_run = 0
        self.frame_players_attack_a = 0

        self.IDLE = Idle(self)
        self.WALK = Walk(self)
        self.RUN = Run(self)
        self.ATTACK = Attack(self)
        self.state_machine = StateMachine(
            self.IDLE,
            {
                self.IDLE: {right_down: self.WALK, left_down: self.WALK, right_up: self.IDLE, left_up: self.IDLE,
                            up_down: self.WALK, up_up: self.IDLE, down_down: self.WALK, down_up: self.IDLE, down_a: self.ATTACK},

                self.WALK: {  right_down: self.WALK, left_down: self.WALK,
                             up_down: self.WALK,  down_down: self.WALK, down_a: self.ATTACK},

                self.ATTACK: {up_a: self.IDLE,}
            }
        )



    def handle_event(self,event):
        self.state_machine.handle_state_event(('INPUT', event))

        if self.state_machine.cur_state == self.WALK:
            self.WALK.handle_event(('INPUT', event))

    def update(self):
        self.state_machine.update()

    def draw(self):
        self.image_players_shadow.draw(self.x - 5, self.y - 74)
        self.state_machine.draw()