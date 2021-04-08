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
    xMax = 100
    xMin = -100
    yMax = 100
    yMin = -100
    loc = Location(0, 0)
    initialPoint = loc
    numberOfMoves = 0
    distances = []
    pow2Distances = []
    locations = []
    numberOfAvoiding = 0
    memory = [(loc.getX(), loc.getY())]
    locations.append(loc)
    random.seed()
    while numberOfMoves < 10000:
        choices = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        xMove, yMove = random.choice(choices)
        if (loc.getX() + xMove, loc.getY() + yMove) in memory:
            numberOfAvoiding += 1
            print("move x= ", xMove, " y move=", yMove)
            print(loc.getX(), loc.getY())
            print("Avoiding number ", numberOfAvoiding)
            if numberOfAvoiding>100000:
                break
            continue
        else:
            loc = loc.move(xMove, yMove)
            memory.append((loc.getX(), loc.getY()))
            locations.append(loc)
            distances.append(loc.distFrom(initialPoint))
            pow2Distances.append(loc.distFrom(initialPoint) ** 2)
            numberOfMoves += 1
    print("Number Of Avoiding: ", numberOfAvoiding)
    print("XFinal =", loc.getX(), " Y Final = ", loc.getY(), " Number of Moves=  ", numberOfMoves)

    print("Mean of distances=", numpy.mean(distances))

    print("Rg= sigma = ", numpy.std(distances))
    print("t^3/4= N^3/4 =Moving numbers =", numberOfMoves ** (3 / 4))
    print("Apporximately Rg=N^first/2=t^first/2 and this fact is true")
    xAxis = []
    yAxis = []

    for point in locations:
        xAxis.append(point.getX())
        yAxis.append(point.getY())

    pylab.plot(xAxis, yAxis)
    pylab.show()
