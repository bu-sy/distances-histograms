from points import Point, Range, Grid
import yaml
import bisect


class Loader(object):
    def __init__(self, yamlDefinition):
        self._grid = None
        definition = yaml.safe_load(yamlDefinition)['definition']
        self.pixelResolution = definition['board']['pixel_resolution']
        range = definition['board']['square']['range']
        self.range = list(Range(range[0], range[1]).getDivide(self.pixelResolution))

        points = []
        for pointDefinition in definition['distance_points']:
            assert len(pointDefinition) == 2
            points.append(
                Point(*pointDefinition)
            )
        self._grid = Grid(points)

    def getGrid(self):
        return self._grid

    def tranlatePoint(self, point):
        def translateCoordinate(coordinate):
            return bisect.bisect_left(self.range, coordinate)
        return (
            translateCoordinate(point.x),
            translateCoordinate(point.y),
        )

    def getMesh(self):
        for firstCoordinate in self.range:
            for secondCoordinate in self.range:
                yield Point(firstCoordinate, secondCoordinate)

    def computeDistances(self):
        for point in self.getMesh():
            yield [point, self.getGrid().distance_from(point)]


if __name__ == "__main__":
    print("TEST")
    loader = Loader('''
    definition:
      board:
        pixel_resolution: 5
        square:
          range: [0, 1]
      distance_points:
        - [0.5, 0.5]
    ''')
    assert len(loader.getGrid().points) == 1
    assert loader.getGrid().points[0].equals(Point(0.5, 0.5))
    # print("TEST COMPUTEDISTANCES") TODO fix test
    # values = list(loader.computeDistances())[-3]
    # print(values[0])
    # assert values[0].equals(Point(1.0, 0.5))
    # assert values[1] == 0.5
    print("TEST TRANSLATEPOINT")
    assert loader.tranlatePoint(Point(0, 0)) == (0, 0)
    assert loader.tranlatePoint(Point(0.5, 0.5)) == (2, 2)
    print("TEST MESH")
    mesh = list(loader.getMesh())
    assert mesh[8].equals(Point(0.25, 0.75))
    assert mesh[12].equals(Point(0.5, 0.5))
    print("TEST SUCCEEDED")
