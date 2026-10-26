# Week 1.5, Session 1: Task 3

class Point:
    """
    A Point in 2D space.
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y
        

    def distance(self):
        total = self.x + self.y
        return total

    def distance_to(self, z):
        total = self.x + self.y + z




p = Point(1.5, 2.0)
print(p.distance())
