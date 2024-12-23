from PIL import Image
from loader import Loader
import math

def normalizedCosine(value):
    # Varies from 0 -> 1 and oscilates from 0 -> 1
    return (1 - math.cos(value * math.pi * 4)) / 2


def translateColor(minimum, maximum, changenum, value):
    colorValue = int(normalizedCosine((value-minimum) / (maximum - minimum) * changenum) * 255)
    return (colorValue, colorValue, colorValue)


def buildImageFromLoader(loader):
    size = loader.pixelResolution

    img = Image.new('RGB', (size, size), 'black')

    for pair in loader.computeDistances():
        point, distance = pair
        img.putpixel(
            loader.tranlatePoint(point),
            translateColor(0, 2, 8, distance)
        )

    img.show()
    img.save('test.png')


with open('definitions/test_definition.yml') as fileObj:
    loader = Loader(fileObj.read())

buildImageFromLoader(loader)
