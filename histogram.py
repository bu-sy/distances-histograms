from points import Range

import bisect
from collections import Counter


class Histogram(object):
    def __init__(self, data, steps):
        self.minimum = min(data)
        self.maximum = max(data)
        myRange = list(Range(self.minimum, self.maximum).getDivide(steps+1))[1:]
        histogramValues = Counter([
            bisect.bisect_left(myRange, datapoint) for datapoint in data
        ])
        self.result = {
            myRange[index]: histogramValues[index]
            for index in range(steps)
        }

    def getRowValuesOnly(self):
        return [self.result[key] for key in sorted(self.result.keys())]


if __name__ == '__main__':
    histogram = Histogram(
        [0, 1, 1, 1, 3, 4, 9, 10], 4
    )
    print("TESTS")
    assert histogram.minimum == 0
    assert histogram.maximum == 10
    assert histogram.result == {2.5: 4, 5.0: 2, 7.5: 0, 10.0: 2}
    assert histogram.getRowValuesOnly() == [4, 2, 0, 2]
    print("TESTS SUCCEEDED")
