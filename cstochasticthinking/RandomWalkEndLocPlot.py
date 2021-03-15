import random
from matplotlib import pyplot as plt
import math
from cstochasticthinking.RandomWalk import Location
from cstochasticthinking.RandomWalk import UsualDrunk
from cstochasticthinking.RandomWalk import MasochistDrunk
from cstochasticthinking.RandomWalk import Field


def walk(f, d, numSteps):
    """Assumes: f  a Field, d a Drunk in f, and numSteps an
    int >=0 .
    Moved d numSteps times: returns final loc of drunk"""
    start = f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)

    return f.getLoc(d)


def simWalks(numSteps, numTrials, dClass):
    """Assumes numSteps an int>=0, numTrials an int >0,
    dClass  a subclass of Drunk Simulates numTrials walks of
    numSteps steps each. Returns a list of the final distances
    for each Trial"""
    Homer = dClass()
    origin = Location(0, 0)
    finalLocs = []
    for t in range(numTrials):
        f = Field()
        f.addDrunk(Homer, origin)
        finalLocs.append(walk(f, Homer, numSteps))
    return finalLocs


def drunkTest(numSteps, numTrials, dclass):
    """Assumes numSteps an int >=0
    numTrials an int>0,
    dClass a subclass of Drunk
    For numSteps,
    runs simWalks with numTrials walks and print results"""

    finalLocs = simWalks(numSteps, numTrials, dclass)
    itrator = 1
    for loc in finalLocs:
        print("Number " + str(itrator) + " : X= ", loc.getX(), " Y = ", loc.getY())
        if dclass == UsualDrunk:
            plt.plot(loc.getX(), loc.getY(), 'r+')
        elif dclass == MasochistDrunk:
            plt.plot(loc.getX(), loc.getY(), 'b.')
        itrator += 1


if __name__ == "__main__":
    random.seed(0)
    drunkTest(10000, 1000, UsualDrunk)
    random.seed(0)
    drunkTest(10000, 1000, MasochistDrunk)
    plt.legend()
    axes = plt.gca()
    axes.set_xlim([-1000, 1000])
    axes.set_ylim([-1000, 1000])
    plt.xlabel("Steps East/West of Origin")
    plt.ylabel("Steps North/South of Origin")
    plt.show()
