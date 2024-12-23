from points import Point, Range, Grid
import yaml


class Loader(object):
    def __init__(self, yamlDefinition):
        self._grid = None
        definition = yaml.safe_load(yamlDefinition)['definition']
        self._pixelResolution = definition['board']['pixel_resolution']
        xrange = definition['board']['square']['xrange']
        yrange = definition['board']['square']['yrange']
        self._firstRange = Range(xrange[0], xrange[1])
        self._secondRange = Range(yrange[0], yrange[1])

        points = []
        for pointDefinition in definition['distance_points']:
            assert len(pointDefinition) == 2
            points.append(
                Point(*pointDefinition)
            )
        self._grid = Grid(points)

    def getGrid(self):
        return self._grid

    def getMesh(self):
        for firstCoordinate in self._firstRange.getDivide(self._pixelResolution):
            for secondCoordinate in self._firstRange.getDivide(self._pixelResolution):
                yield Point(firstCoordinate, secondCoordinate)


if __name__ == "__main__":
    print("TEST")
    loader = Loader('''
    definition:
      board:
        pixel_resolution: 5
        square:
          xrange: [0, 1]
          yrange: [0, 1]
      distance_points:
        - [0.5, 0.5]
    ''')
    assert len(loader.getGrid().points) == 1
    assert loader.getGrid().points[0].equals(Point(0.5, 0.5))
    print("TEST MESH")
    mesh = list(loader.getMesh())
    assert mesh[8].equals(Point(0.25, 0.75))
    assert mesh[12].equals(Point(0.5, 0.5))
    print("TEST SUCCEEDED")
