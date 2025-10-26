from pico2d import *
from state_machine import StateMachine

class Player:
    def __init__(self):
        self.image_players_stop_body = []
        self.image_players_walk = []
        self.image_players_run = []
        self.image_players_attack_a = []

        self.state = 'stop'
        self.dirx = 0
        self.diry = 0
        self.speed = 5
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

    )
    def handle_events(self):
        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                exit(0)
            elif event.type == SDL_KEYDOWN:
                if event.key == SDLK_RIGHT:
                    self.dirx += 1
                elif event.key == SDLK_LEFT:
                    self.dirx += -1
                elif event.key == SDLK_UP:
                    self.diry += 1
                elif event.key  == SDLK_DOWN:
                    self.diry += -1
                elif event.key == SDLK_a:
                    state = self.state = 'attack_a'
                    self.frame_players_attack_a = 0
                elif event.key == SDLK_s:
                    state = self.state = 'attack_s'
                elif event.key == SDLK_ESCAPE:
                    exit(0)

            elif event.type == SDL_KEYUP:
                if event.key == SDLK_RIGHT:
                    self.dirx += -1
                elif event.key == SDLK_LEFT:
                    self.dirx += 1
                elif event.key == SDLK_UP:
                    self.diry += -1
                elif event.key == SDLK_DOWN:
                    self.diry += 1

        if self.state != 'attack_a':
            if self.dirx == 0 and self.diry == 0:
                self.state = 'stop'
            else:
                self.state = 'walk'



    def update(self):
        self.x += self.dirx * self.speed
        self.y += self.diry * self.speed

        if self.state == 'stop':
            self.frame_players_stop_body = (self.frame_players_stop_body + 1) % 11
            self.frame_players_stop_leg = (self.frame_players_stop_leg + 1) % 1

        elif self.state == 'walk':
            self.frame_players_walk = (self.frame_players_walk + 1) % 10

        elif self.state == 'run':
            self.frame_players_run = (self.frame_players_run + 1) % 5

        elif self.state == 'attack_a':
            self.frame_players_attack_a = (self.frame_players_attack_a + 1) % 8
            if self.frame_players_attack_a == 0:
                self.state = 'stop'

    def draw(self):
        self.image_players_shadow.draw(self.x - 5, self.y - 74)

        if(self.state == 'stop'):
            self.image_players_stop_leg.draw(self.x - 3, self.y - 56)  # Adjust y position for leg
            self.image_players_stop_body[self.frame_players_stop_body].draw(self.x, self.y)
        elif(self.state == 'walk'):
            self.image_players_walk[self.frame_players_walk].draw(self.x, self.y)
        elif(self.state == 'run'):
            self.image_players_run[self.frame_players_run].draw(self.x, self.y)
        elif(self.state == 'attack_a'):
            self.image_players_attack_a[self.frame_players_attack_a].draw(self.x + 22, self.y - 8)


class Idle:
    def __init__(self, player):
        self.player = player

class Attack:
    def __init__(self, player):
        self.player = player

class Walk:
    def __init__(self, player):
        self.player = player

class run:
    def __init__(self, player):
        self.player = player




class All_Player:
    def __init__(self):
        self.player = Player()

    def handle_events(self):
        self.player.handle_events()

    def update(self):
        self.player.update()

    def draw(self):
       self.player.draw()
