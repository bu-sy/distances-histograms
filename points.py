import math


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_from(self, point):
        return math.sqrt((point.x-self.x) ** 2 + (point.y-self.y) ** 2)

    def equals(self, point):
        return (self.x == point.x) and (self.y == point.y)

    def combine(self, point):
        return Point(
            self.x + point.x,
            self.y + point.y,
        )

    def __str__(self):
        return f"POINT({self.x, self.y})"


class Range(object):
    def __init__(self, valueStart, valueEnd):
        self.valueStart = valueStart
        self.valueEnd = valueEnd

    def getDivide(self, point_number):
        def getWeightedValue(first, second, percent):
            return second * percent + (1-percent) * first

        assert point_number >= 2
        for a in range(0, point_number):
            percentage = a / (point_number-1)
            yield getWeightedValue(self.valueStart, self.valueEnd, percentage)


class Grid(object):
    def __init__(self, points):
        self.points = points

    def distance_from(self, point):
        return min([grid_point.distance_from(point) for grid_point in self.points])


if __name__ == "__main__":
    print("TEST POINT EQUALS")
    assert Point(1, 2).equals(Point(1, 2))
    assert not Point(1, 2).equals(Point(2, 1))
    print("TEST POINT DISTANCE")
    assert Point(0, 3).distance_from(Point(4, 0)) == 5
    assert Point(0, 3).distance_from(Point(0, 5)) == 2
    assert Point(7, 7).distance_from(Point(7, 7)) == 0
    print("TEST POINT ADD")
    assert Point(3, 7).combine(Point(4, 5)).equals(Point(7, 12))
    print("TEST GRID DISTANCE")
    grid = Grid([
        Point(0, 0),
        Point(0, 2),
        Point(2, 0)
    ])
    assert grid.distance_from(Point(2, 2)) == 2
    assert grid.distance_from(Point(0, 1)) == 1
    assert grid.distance_from(Point(0, 1.5)) == 0.5
    print("TESTS RANGE DIVIDE")
    myRange = Range(0, 20)
    assert list(myRange.getDivide(5)) == [0, 5, 10, 15, 20]
    print("TESTS SUCCEEDED")
