from points import Point
import yaml

class Loader(object):
    def __init__(self, yamlDefinition):
        self._startPoints = []
        self._board = None

        definition = yaml.safe_load(yamlDefinition)['definition']
        for pointDefinition in definition['distance_points']:
            assert len(pointDefinition) == 2
            self._startPoints.append(
                Point(*pointDefinition)
            )

    def getStartPoints(self):
        return self._startPoints


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
    assert len(loader.getStartPoints()) == 1
    assert loader.getStartPoints()[0].equals(Point(0.5, 0.5))
    print("TEST SUCCEEDED")