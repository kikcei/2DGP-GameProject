# world[0] : 가장 낮은 계층 layer
# world[1] : 그 위의 계층 layer

world = [[], [], []]

def add_object(o, depth):
    world[depth].append(o)

def add_objects(ol, depth):
    world[depth] += ol

def update_world():
    for layer in world:
        for o in layer:
            o.update()

def draw_world():
    for layer in world:
        for o in layer:
            o.draw()

def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return

def clear():
    for layer in world:
        layer.clear()

