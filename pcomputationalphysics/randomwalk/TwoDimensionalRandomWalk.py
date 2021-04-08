import numpy
import random
import pylab
import math


class Location(object):
    def __init__(self, x, y):
        """x and y are floats"""
        self.x = x
        self.y = y

    # what move is doing is it's not changing the location
    # it's returning a new location(Immutable type)
    def move(self, deltaX, deltaY):
        """deltaX and delta Y are floats"""
        return Location(self.x + deltaX, self.y + deltaY)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distFrom(self, other):
        xDist = self.x - other.getX()
        yDist = self.y - other.getY()
        return (xDist ** 2 + yDist ** 2) ** 0.5

    def __str__(self):
        return '<' + str(self.x) + ', ' \
               + str(self.y) + '>'


if __name__ == "__main__":
    xMax = 10
    xMin = -10
    yMax = 10
    yMin = -10
    loc = Location(0, 0)
    initialPoint = loc
    numberOfMoves = 0
    distances = []
    pow2Distances = []
    locations = []
    locations.append(loc)
    random.seed()
    while numberOfMoves < 10000:
        choices = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        xMove, yMove = random.choice(choices)

        loc = loc.move(xMove, yMove)
        locations.append(loc)
        distances.append(loc.distFrom(initialPoint))
        pow2Distances.append(loc.distFrom(initialPoint) ** 2)
        numberOfMoves += 1
    print("XFinal =", loc.getX(), " Y Final = ", loc.getY(), " Number of Moves=  ", numberOfMoves)

    print("Mean of distances=", numpy.mean(distances))

    print("Rg= Sqrt(mean(distances**2)) = ", math.sqrt(numpy.mean(pow2Distances)))
    print("t^first/2= N^first/2 =Moving numbers=", math.sqrt(numberOfMoves))
    print("Apporximately Rg=N^first/2=t^first/2 and this fact is true")
    xAxis = []
    yAxis = []

    for point in locations:
        xAxis.append(point.getX())
        yAxis.append(point.getY())

    pylab.plot(xAxis, yAxis)
    pylab.show()
