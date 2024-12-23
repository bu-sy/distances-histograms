from points import Point, Grid
import yaml

class Loader(object):
    def __init__(self, yamlDefinition):
        self._grid = None
        self._board = None

        definition = yaml.safe_load(yamlDefinition)['definition']
        points = []
        for pointDefinition in definition['distance_points']:
            assert len(pointDefinition) == 2
            points.append(
                Point(*pointDefinition)
            )
        self._grid = Grid(points)

    def getGrid(self):
        return self._grid


if __name__ == "__main__":
    print("TEST")
    loader = Loader('''
    definition:
      board:
        mesh_resolution: 0.01
        square:
          xrange: [0, 1]
          yrange: [0, 1]
      distance_points:
        - [0.5, 0.5]
    ''')
    assert len(loader.getGrid().points) == 1
    assert loader.getGrid().points[0].equals(Point(0.5, 0.5))
    print("TEST SUCCEEDED")