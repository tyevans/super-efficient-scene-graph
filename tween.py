import uuid


class LinearTransition(object):

    def __init__(self, starting_value, destination_value, transition_time):
        self.starting_value = starting_value
        self.destination_value = destination_value
        self.transition_time = transition_time
        self.travel_distance = destination_value - starting_value
        self.runtime = 0
        self._current_value = starting_value

    def current_value(self):
        return self._current_value

    def step(self, dt):
        if self.runtime <= self.transition_time:
            self.runtime += dt
            completed = self.runtime / self.transition_time
            self._current_value = self.travel_distance * completed + self.starting_value
        elif self._current_value != self.destination_value:
            self._current_value = self.destination_value
        else:
            return False
        return True


class TweenableValue(object):

    def __init__(self, value, transition_class=LinearTransition, transition_time=10.0):
        self.value = value
        self.transition_class = transition_class
        self.transition_time = transition_time
        self.in_transit = False
        self.transition = None

    def get_value(self):
        return self.value

    def set_value(self, value):
        if self.value == value:
            return

        self.in_transit = True
        self.transition = self.transition_class(self.value, value, self.transition_time)

    def step(self, dt):
        if self.in_transit:
            moving = self.transition.step(dt)
            self.value = self.transition.current_value()
            if not moving:
                self.in_transit = False
                self.transition = None
