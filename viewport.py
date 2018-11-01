import numpy as np

from transform import Transform


def overlay_image(bg, fg, transform):
    bg_height, bg_width = bg.shape[:2]
    fg_height, fg_width = fg.shape[:2]

    bg_left = int(transform.x)
    bg_top = int(transform.y)

    if bg_top < 0:
        fg_top = bg_top * -1
        bg_top = 0
    else:
        fg_top = 0

    shared_height = min(bg_height - bg_top, fg_height - fg_top)
    fg_bottom = fg_top + shared_height

    if bg_left < 0:
        fg_left = bg_left * -1
        bg_left = 0
    else:
        fg_left = 0

    shared_width = min(bg_width - bg_left, fg_width - fg_left)
    fg_right = fg_left + shared_width

    if shared_width > 0 and shared_height > 0:
        bg_right = bg_left + shared_width
        bg_bottom = bg_top + shared_height
        bg[bg_top:bg_bottom, bg_left:bg_right] = fg[fg_top:fg_bottom, fg_left:fg_right]


class ViewPort(object):

    def __init__(self, stage, width, height, transform=None):
        self.stage = stage
        self.width = width
        self.height = height
        self.transform = transform or Transform(0, 0, 1.0, 1.0, 0)
        self.canvas = np.zeros((height, width, 3), dtype=np.uint8)

    def clear(self):
        self.canvas[...] = 0

    def draw(self, transform, content):
        t = self.stage.transform.to_world(transform).from_world(self.transform)
        overlay_image(self.canvas, content, t)

    def center_on(self, actor):
        self.transform.x = actor.transform.x - self.width // 2
        self.transform.y = actor.transform.y - self.height // 2