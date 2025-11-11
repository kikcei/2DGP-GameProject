from resource_load import PlayerResourceLoad
from state_machine import StateMachine
import random


class Idle:
    def __init__(self, basic_monster):
        self.basic_monster = basic_monster
        self.min_x = 40
        self.min_y = 40
        self.max_x = 760
        self.max_y = 560

    def enter(self,e):
        self.basic_monster.face_dir = random.choice([-1, 1])
        if self.basic_monster.face_dir == 1:
            self.basic_monster.dirx = 1
        else:
            self.basic_monster.dirx = -1


    def exit(self,e):
        pass

    def do(self):
        speed = 3
        self.basic_monster.frame_basic_monster_walk=(self.basic_monster.frame_basic_monster_walk + 1) % 8

        if self.basic_monster.x <= self.min_x:  # 왼쪽 벽
            self.basic_monster.x = self.min_x
            self.basic_monster.dirx *= -1
            self.basic_monster.face_dir = 1  # 반대쪽으로 향하게
        elif self.basic_monster.x >= self.max_x:  # 오른쪽 벽
            self.basic_monster.x = self.max_x
            self.basic_monster.dirx *= -1
            self.basic_monster.face_dir = -1

        if self.basic_monster.y <= self.min_y:  # 아래 벽
            self.basic_monster.y = self.min_y
            self.basic_monster.diry *= -1
        elif self.basic_monster.y >= self.max_y:  # 위 벽
            self.basic_monster.y = self.max_y
            self.basic_monster.diry *= -1

        self.basic_monster.x += self.basic_monster.dirx * speed
        self.basic_monster.y += self.basic_monster.diry * speed


    def draw(self):
        if self.basic_monster.face_dir == 1:
            self.basic_monster.image_basic_monster_walk[self.basic_monster.frame_basic_monster_walk].draw(self.basic_monster.x - 7, self.basic_monster.y - 20)
        else:
            self.basic_monster.image_basic_monster_walk_left[self.basic_monster.frame_basic_monster_walk].draw(self.basic_monster.x + 2, self.basic_monster.y - 20)





class Basic_Monster:

    def __init__(self,resource_loader: PlayerResourceLoad):

        self.image_basic_monster_shadow = resource_loader.get('shadow')

        self.image_basic_monster_walk = resource_loader.get('basic_monster')
        self.image_basic_monster_walk_left = resource_loader.get('basic_monster_left')


        self.x = 600
        self.y = 300
        self.dirx = random.choice([-1, 1])
        self.diry = random.choice([-1, 1])
        self.face_dir = random.choice([-1, 1])

        self.frame_basic_monster_walk = 0


        self.IDLE = Idle(self)
        self.state_machine = StateMachine(
            self.IDLE,
            {
                self.IDLE:{},
            }
        )


    def update(self):
        self.state_machine.update()

    def draw(self):
        self.image_basic_monster_shadow.draw(self.x - 2, self.y - 74)
        self.state_machine.draw()
