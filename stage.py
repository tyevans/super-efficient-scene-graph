from actor import Actor


class Stage(Actor):

    def __init__(self, transform=None):
        super().__init__(transform)
        self.actors = []

    def add_actor(self, actor):
        self.actors.append(actor)

    def remove_actor(self, actor):
        self.actors.remove(actor)

    def step(self, dt):
        for actor in self.actors:
            actor.step(dt)

    def draw(self, viewport):
        for actor in self.actors:
            actor.draw(viewport)