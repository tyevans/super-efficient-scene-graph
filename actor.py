import numpy as np

from transform import Transform


class Actor(object):

    def __init__(self, transform=None, input_handler=None):
        self.transform = transform or Transform(0, 0, 1.0, 1.0, 0)
        self.input_handler = input_handler

    def draw(self, viewport):
        viewport.draw(self.transform, self.render())

    def set_input_handler(self, input_handler):
        self.input_handler = input_handler

    def step(self, dt):
        pass

    def render(self):
        pass

class SquareActor(Actor):

    def __init__(self, transform=None, input_handler=None):
        self.transform = transform or Transform(0, 0, 1.0, 1.0, 0)
        self.speed = 0
        self.max_speed = 10
        self.gravity = -9.2
        self.input_handler = input_handler

    def step(self, dt):
        self.speed += self.gravity * dt
        self.transform.x += self.speed * dt
        self.transform.y += self.speed * dt

    def draw(self, viewport):
        viewport.draw(self.transform, self.render())

    def render(self):
        content = np.ones((10, 10, 3), dtype=np.uint8) * 255
        content[2:8, 2:8] = 0
        return content

    def set_input_handler(self, input_handler):
        self.input_handler = input_handler
