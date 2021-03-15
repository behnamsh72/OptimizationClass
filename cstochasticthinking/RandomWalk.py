import random
import matplotlib.pyplot as plt
import numpy
import math


# Immutable type
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


class Drunk(object):
    def __init__(self, name=None):
        """Assume name is a str"""
        self.name = name

    def __str__(self):
        if self != None:
            return self.name
        return 'Anonymous'


class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        return random.choice(stepChoices)


class MasochistDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0.0, 1.1), (0.0, -0.9), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)


class Field(object):
    def __init__(self):
        self.drunks = {}

    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk')
        else:
            self.drunks[drunk] = loc

    def getLoc(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        return self.drunks[drunk]

    def moveDrunk(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        xDist, yDist = drunk.takeStep()
        # use move method of Location to get new location
        self.drunks[drunk] = self.drunks[drunk].move(xDist, yDist)


def walk(f, d, numSteps):
    """Assumes: f  a Field, d a Drunk in f, and numSteps an
    int >=0 .
    Moved d numSteps times: returns the distance between the final
    location and the location at the start of the walk"""
    start = f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)

    return start.distFrom(f.getLoc(d))


def simWalks(numSteps, numTrials, dClass):
    """Assumes numSteps an int>=0, numTrials an int >0,
    dClass  a subclass of Drunk Simulates numTrials walks of
    numSteps steps each. Returns a list of the final distances
    for each Trial"""
    Homer = dClass()
    origin = Location(0, 0)
    distances = []
    for t in range(numTrials):
        f = Field()
        f.addDrunk(Homer, origin)
        distances.append(round(walk(f, Homer, numSteps), 1))
    return distances


def drunkTest(walkLengths, numTrials, dclass):
    """Assumes walkLengths a sequence of ints >=0
    numTrials an int>0,
    dClass a subclass of Drunk
    For each number of steps in walkLengths,
    runs simWalks with numTrials walks and print results"""
    x = []
    y = []
    for numSteps in walkLengths:
        distances = simWalks(numSteps, numTrials, dclass)
        print(dclass.__name__, 'random walk of', numSteps, 'steps')
        print(' Mean= ', round(sum(distances) / len(distances), 4))
        print(' Max = ', max(distances), 'Min =', min(distances))
        x.append(numSteps)
        y.append(round(sum(distances) / len(distances), 4))
    if dclass == UsualDrunk:
        plt.plot(x, y, 'r-', label='UsualDrunk')
        plt.plot(x, [math.sqrt(i) for i in x], 'g-.', label="Square root of steps")

    elif dclass == MasochistDrunk:
        plt.plot(x, y, 'b--', label='UsualDrunk')
        plt.plot(x, [i * 0.05 for i in x], 'y-.', label="num steps * 0.05")


if __name__ == "__main__":
    random.seed(0)
    drunkTest((1, 10, 100, 1000, 10000, 100000), 100, UsualDrunk)
    random.seed(0)
    drunkTest((10, 100, 1000, 10000, 100000), 100, MasochistDrunk)
    plt.legend()
    plt.xlabel("Number of Steps")
    plt.ylabel("Distance From Origin")
    plt.show()




