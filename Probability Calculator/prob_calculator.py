import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, quantity in kwargs.items():
            self.contents += [color] * quantity
    
    def draw(self, num_balls):
        if num_balls > len(self.contents):
            return self.contents
        drawn_balls = random.sample(self.contents, num_balls)
        self.contents = [ball for ball in self.contents if ball not in drawn_balls]
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successes = 0
    for i in range(num_experiments):
        drawn_balls = hat.draw(num_balls_drawn)
        hat_copy = copy.copy(hat)
        if all([drawn_balls.count(color) >= expected_balls.get(color, 0) for color in expected_balls.keys()]):
            successes += 1
        hat.contents = hat_copy.contents
    return successes / num_experiments
