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
        }

    def load_sequence(self, base_path, count):
        return [load_image(f"{base_path}/{i}.png") for i in range(1, count + 1)]

    def get(self, key):
        return self.resources.get(key)