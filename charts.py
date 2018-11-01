import numpy as np

from actor import Actor
from transform import Transform
from tween import TweenableValue


class Bar(Actor):

    def __init__(self, width, height, max_value, value, color=None, transform=None):
        self.width = TweenableValue(width)
        self.height = TweenableValue(height)
        self.max_value = TweenableValue(max_value)
        self.value = TweenableValue(value)
        self.color = color or  (0, 127, 127)
        super().__init__(transform)

    def step(self, dt):
        self.width.step(dt)
        self.height.step(dt)
        self.max_value.step(dt)
        self.value.step(dt)

    def render(self):
        height = int(self.height.get_value())
        width = int(self.width.get_value())
        value = self.value.get_value()
        max_value = self.max_value.get_value()
        bar = np.ones((height, width, 3), dtype=np.uint8) * 255
        top = height * value // max_value
        print(top, height)
        bar[top:height, 0:width] = self.color
        return bar

class BarGraph(Actor):

    def __init__(self, labels, values, height=240, width=320, padding=20, show_labels=True):
        min_val = min(values)
        max_val = max(values)
        num_bars = len(labels)

        self.bars = []

        bar_width = (width - (num_bars + 1) * padding) / num_bars
        bar_height = height - padding * 2
        if show_labels:
            bar_height -= 25

        for label, value in zip(labels, values):
            transform = Transform()
            transform.x = self.transform.x +
            transform.y = self.transform.y +
            self.bars.append(Bar(bar_width, transform=transform))

    def step(self, dt):
        for bar in self.bars:
            bar.step(dt)

    def render(self):
        for bar in self.bars:
