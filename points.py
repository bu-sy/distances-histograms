import math

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_from(self, point):
        return math.sqrt((point.x-self.x) ** 2 + (point.y-self.y) ** 2)

    def equals(self, point):
        return (self.x == point.x) and (self.y == point.y)


if __name__ == "__main__":
    print("TEST")
    print("TEST EQUALS")
    assert Point(1, 2).equals(Point(1, 2))
    assert not Point(1, 2).equals(Point(2, 1))
    print("TEST DISTANCE")
    assert Point(0, 3).distance_from(Point(4, 0)) == 5
    assert Point(0, 3).distance_from(Point(0, 5)) == 2
    assert Point(7, 7).distance_from(Point(7, 7)) == 0
    print("TEST SUCCEEDED")
