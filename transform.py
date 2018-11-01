class Transform(object):

    def __init__(self, x, y, scale_x, scale_y, rotation):
        self.x = x
        self.y = y
        self.scale_x = scale_x
        self.scale_y = scale_y
        self.rotation = rotation

    def to_world(self, local_transform):
        return Transform(
            local_transform.x + self.x,
            local_transform.y + self.y,
            local_transform.scale_x * self.scale_x,
            local_transform.scale_y * self.scale_y,
            local_transform.rotation + self.rotation
        )

    def from_world(self, world_transform):
        return Transform(
            world_transform.x - self.x,
            world_transform.y - self.y,
            world_transform.scale_x / self.scale_x,
            world_transform.scale_y / self.scale_y,
            world_transform.rotation - self.rotation
        )