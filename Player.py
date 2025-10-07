from pico2d import *

class Player:
    def __init__(self):
        self.image_players_stop_body = []
        self.image_players_walk = []

        self.state = 'stop'
        self.dirx = 0
        self.diry = 0
        self.speed = 5
        self.x, self.y = 400, 300


        for i in range(1, 12):
            path = f'resources/Players/sprites/DefineSprite_60/{i}.png'
            image = load_image(path)
            self.image_players_stop_body.append(image)

        for i in range(1, 11):
            path = f'resources/Players/sprites/DefineSprite_79/{i}.png'
            image = load_image(path)
            self.image_players_walk.append(image)

        self.image_players_stop_leg = load_image('resources/Players/sprites/DefineSprite_124/1.png')


        self.stop_frame_w, self.stop_frame_h = 64, 96  # 프레임 크기
        self.walk_frame_w, self.walk_frame_h = 64, 96

        self.stop_body_frame = 11
        self.stop_leg_frame = 11
        self.walk_frame = 11

        self.frame_players_stop_body = 0
        self.frame_players_stop_leg = 0
        self.frame_players_walk = 0

    def handle_events(self):
        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                exit(0)
            elif event.type == SDL_KEYDOWN:
                if event.key == SDLK_RIGHT:
                    self.dirx = 1
                    self.state = 'walk'
                elif event.key == SDLK_LEFT:
                    self.dirx = -1
                    self.state = 'walk'
                elif event.key == SDLK_UP:
                    self.diry = 1
                    self.state = 'walk'
                elif event.key  == SDLK_DOWN:
                    self.diry = -1
                    self.state = 'walk'
                elif event.key == SDLK_ESCAPE:
                    exit(0)

            elif event.type == SDL_KEYUP:
                if event.key == SDLK_RIGHT:
                    self.dirx = 0
                    self.state = 'stop'
                elif event.key == SDLK_LEFT:
                    self.dirx = 0
                    self.state = 'stop'
                elif event.key == SDLK_UP:
                    self.diry = 0
                    self.state = 'stop'
                elif event.key == SDLK_DOWN:
                    self.diry = 0
                    self.state = 'stop'

    def update(self):
        self.x += self.dirx * self.speed
        self.y += self.diry * self.speed

        if self.state == 'stop':
            self.frame_players_stop_body = (self.frame_players_stop_body + 1) % 11
            self.frame_players_stop_leg = (self.frame_players_stop_leg + 1) % 1

        elif self.state == 'walk':
            self.frame_players_walk = (self.frame_players_walk + 1) % 10

    def draw(self):
        if(self.state == 'stop'):
            self.image_players_stop_leg.draw(self.x - 3, self.y - 56)  # Adjust y position for leg
            self.image_players_stop_body[self.frame_players_stop_body].draw(self.x, self.y)
        elif(self.state == 'walk'):
            self.image_players_walk[self.frame_players_walk].draw(self.x, self.y)



class All_Player:
    def __init__(self):
        self.player = Player()

    def handle_events(self):
        self.player.handle_events()

    def update(self):
        self.player.update()

    def draw(self):
       self.player.draw()
