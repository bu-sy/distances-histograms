import math

def triangle_area(pointA, pointB, pointC):
    #Shoelace formula
    return math.fabs((pointA.x - pointC.x) * (pointB.y - pointA.y) - (pointA.x - pointB.x) * (pointC.y - pointA.y)) / 2

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


class LineSegment(object):
    def __init__(self, pointA, pointB):
        self.pointA = pointA
        self.pointB = pointB
        self.segmentLength = self.pointA.distance_from(pointB)

    def distance_from(self, pointC):
        areaOfTriangle = triangle_area(self.pointA, self.pointB, pointC)
        distanceFromLine = areaOfTriangle / self.segmentLength * 2
        distanceFromA = self.pointA.distance_from(pointC)
        distanceFromB = self.pointB.distance_from(pointC)
        if max(distanceFromA, distanceFromB) ** 2 >= self.segmentLength ** 2 + distanceFromLine ** 2:
            return min(distanceFromA, distanceFromB)
        else:
            return distanceFromLine

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
    def __init__(self, points=None, lines=None):
        self.points = points or []
        self.lines = lines or []

    def distance_from(self, point):
        return min([grid_element.distance_from(point) for grid_element in self.points + self.lines])


if __name__ == "__main__":
    print("TEST TRIANGLE AREA")
    assert triangle_area(Point(0,0), Point(10, 0), Point(0, 7)) == 35
    assert triangle_area(Point(100, 400), Point(110, 400), Point(100, 407)) == 35
    print("TEST LINE DISTANCE")
    line = LineSegment(Point(0, 0), Point(3, 0))
    assert line.distance_from(Point(2, 2)) == 2
    assert line.distance_from(Point(6, 4)) == 5
    assert line.distance_from(Point(-4, -3)) == 5
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
    grid = Grid(points=[
        Point(0, 0),
        Point(0, 2),
        Point(2, 0)
    ], lines=[LineSegment(Point(10, 10), Point(11, 10))])
    assert grid.distance_from(Point(2, 2)) == 2
    assert grid.distance_from(Point(0, 1)) == 1
    assert grid.distance_from(Point(0, 1.5)) == 0.5
    assert grid.distance_from(Point(11, 11)) == 1
    print("TESTS RANGE DIVIDE")
    myRange = Range(0, 20)
    assert list(myRange.getDivide(5)) == [0, 5, 10, 15, 20]
    print("TESTS SUCCEEDED")
