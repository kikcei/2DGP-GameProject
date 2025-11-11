from resource_load import PlayerResourceLoad
from state_machine import StateMachine
import random

class Basic_Monster:

    def __init__(self,resource_loader: PlayerResourceLoad):

        self.image_basic_monster_shadow = resource_loader.get('shadow')

        self.image_basic_monster_walk = resource_loader.get('basic_monster')
        self.image_basic_monster_walk_left = resource_loader.get('basic_monster_left')

        self.frame_basic_monster_walk = 0


        self.IDLE = None
        self.state_machine = StateMachine(
            self.IDLE,
            {
                self.IDLE:{},
            }
        )


    def update(self):
        pass

    def draw(self):
        pass
