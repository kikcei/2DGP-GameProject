from pico2d import load_image

class PlayerResourceLoad:
    def __init__(self):
        self.resources = {}

    def load(self):
        self.resources = {
            'shadow': load_image('resources/Players/sprites/shadow/DefineSprite_45/1.png'),
            'stop_body': self.load_sequence('resources/Players/sprites/stop/DefineSprite_60', 11),
            'stop_leg': load_image('resources/Players/sprites/stop/DefineSprite_124/1.png'),
            'stop_body_left': self.load_sequence('resources/Players/sprites/stop/DefineSprite_60_left', 11),
            'stop_leg_left': load_image('resources/Players/sprites/stop/DefineSprite_124_left/1.png'),

            'walk': self.load_sequence('resources/Players/sprites/walk/DefineSprite_79', 10),
            'walk_left': self.load_sequence('resources/Players/sprites/walk/DefineSprite_79_left', 10),
            'run': self.load_sequence('resources/Players/sprites/run/DefineSprite_91', 5),
            'run_left': self.load_sequence('resources/Players/sprites/run/DefineSprite_91_left', 5),

            'run_attack_a': self.load_sequence('resources/Players/sprites/run_attack/attack_a/DefineSprite_227', 23),
            'run_attack_a_left': self.load_sequence('resources/Players/sprites/run_attack/attack_a/DefineSprite_227_left', 23),
            'run_attack_s': self.load_sequence('resources/Players/sprites/run_attack/attack_s/DefineSprite_228', 15),
            'run_attack_s_left': self.load_sequence('resources/Players/sprites/run_attack/attack_s/DefineSprite_228_left', 15),

            'attack_a': self.load_sequence('resources/Players/sprites/attack/attack_a/DefineSprite_97', 8),
            'attack_a_left': self.load_sequence('resources/Players/sprites/attack/attack_a/DefineSprite_97_left', 8),
            'attack_a_a': self.load_sequence('resources/Players/sprites/attack/attack_a_a/DefineSprite_107', 11),
            'attack_a_a_left': self.load_sequence('resources/Players/sprites/attack/attack_a_a/DefineSprite_107_left', 11),
            'attack_a_s': self.load_sequence('resources/Players/sprites/attack/attack_a_s/DefineSprite_169', 17),
            'attack_a_s_left': self.load_sequence('resources/Players/sprites/attack/attack_a_s/DefineSprite_169_left', 17),
            'attack_a_s_a': self.load_sequence('resources/Players/sprites/attack/attack_a_s_a/DefineSprite_176', 21),
            'attack_a_s_a_left': self.load_sequence('resources/Players/sprites/attack/attack_a_s_a/DefineSprite_176_left', 21),
            'attack_s': self.load_sequence('resources/Players/sprites/attack/attack_s/DefineSprite_137', 17),
            'attack_s_left': self.load_sequence('resources/Players/sprites/attack/attack_s/DefineSprite_137_left', 17),
            'attack_s_s': self.load_sequence('resources/Players/sprites/attack/attack_s_s/DefineSprite_146', 18),
            'attack_s_s_left': self.load_sequence('resources/Players/sprites/attack/attack_s_s/DefineSprite_146_left', 18),

            'basic_monster': self.load_sequence('resources/Monster/Basic_monster/Walk/sprites/DefineSprite_707', 8),
            'basic_monster_left': self.load_sequence('resources/Monster/Basic_monster/Walk/sprites/DefineSprite_707_left',8),

            'special_monster1_walk': self.load_sequence('resources/Monster/Special_Monster/Monster1/Walk/sprites/DefineSprite_637', 8),
            'special_monster1_walk_left': self.load_sequence('resources/Monster/Special_Monster/Monster1/Walk/sprites/DefineSprite_637_left', 8),
            'special_monster1_attack1': self.load_sequence('resources/Monster/Special_Monster/Monster1/Attack/Attack_1/sprites/DefineSprite_672', 14),
            'special_monster1_attack1_left': self.load_sequence('resources/Monster/Special_Monster/Monster1/Attack/Attack_1/sprites/DefineSprite_672_left', 14),
            'special_monster1_attack2': self.load_sequence('resources/Monster/Special_Monster/Monster1/Attack/Attack_2/sprites/DefineSprite_679', 13),
            'special_monster1_attack2_left': self.load_sequence('resources/Monster/Special_Monster/Monster1/Attack/Attack_2/sprites/DefineSprite_679', 13),
            'special_monster1_attack3':self.load_sequence('resources/Monster/Special_Monster/Monster1/Attack/Attack_3/sprites/DefineSprite_687', 14),
            'special_monster1_attack3_left':self.load_sequence('resources/Monster/Special_Monster/Monster1/Attack/Attack_3/sprites/DefineSprite_687_left', 14),

            'special_monster2_walk': self.load_sequence('resources/Monster/Special_Monster/Monster2/Walk/sprites/DefineSprite_773', 1),
            'special_monster2_walk_left': self.load_sequence('resources/Monster/Special_Monster/Monster2/Walk/sprites/DefineSprite_773_left', 1),
            'special_monster2_attack': self.load_sequence('resources/Monster/Special_Monster/Monster2/Attack/sprites/Attack/DefineSprite_777', 24),
            'special_monster2_attack_left': self.load_sequence('resources/Monster/Special_Monster/Monster2/Attack/sprites/Attack/DefineSprite_777_left', 24),
            'special_monster2_attack_ammo': self.load_sequence('resources/Monster/Special_Monster/Monster2/Attack/sprites/ammo/sprites/DefineSprite_914', 1),
            'special_monster2_attack_ammo_left': self.load_sequence('resources/Monster/Special_Monster/Monster2/Attack/sprites/ammo/sprites/DefineSprite_914_left', 1),

            'boos_walk': self.load_sequence('resources/Monster/Boos/Walk/sprites/DefineSprite_390', 9),
            'boos_walk_left': self.load_sequence('resources/Monster/Boos/Walk/sprites/DefineSprite_390_left', 9),
            'boos_attack1': self.load_sequence('resources/Monster/Boos/Attack/Attack_1/sprites/DefineSprite_579', 9),
            'boos_attack1_left': self.load_sequence('resources/Monster/Boos/Attack/Attack_1/sprites/DefineSprite_579_left', 9),
            'boos_attack2': self.load_sequence('resources/Monster/Boos/Attack/Attack_2/sprites/DefineSprite_589_left', 24),
            'boos_attack2_left': self.load_sequence('resources/Monster/Boos/Attack/Attack_2/sprites/DefineSprite_589_left', 24),
        }

    def load_sequence(self, base_path, count):
        return [load_image(f"{base_path}/{i}.png") for i in range(1, count + 1)]

    def get(self, key):
        return self.resources.get(key)