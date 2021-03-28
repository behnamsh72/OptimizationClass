import numpy
import random
import pylab
import math
import time

if __name__ == "__main__":
    x = 0
    positions = []
    pow2Positions = []
    nPlus = 0
    nMinus = 0
    numberOfRepeatedX = {}
    for i in range(0, 100000):
        r = random.choice([-1, 1])
        if r == 1:
            nPlus += 1
        elif r == -1:
            nMinus += 1
        x += r
        if x in numberOfRepeatedX.keys():
            numberOfRepeatedX[x] += 1
        else:
            numberOfRepeatedX[x] = 1
        positions.append(x)
        pow2Positions.append(x ** 2)
    print("N+ =", nPlus, " N Minus = ", nMinus)
    print("N= ", nPlus + nMinus)
    meanX2 = numpy.mean(pow2Positions)
    meanX = numpy.mean(positions)
    print("last position", x)
    print("Mean= ", meanX)
    print("Std=", numpy.std(positions))
    print("Mean x^2= ", meanX2)
    print("Sigma ^2=", numpy.std(positions) ** 2)
    print("Standard deviation for formula sqrt(<x^2> - <x>^2):", math.sqrt(meanX2 - meanX ** 2))

    print("NUmber of moves N=", nPlus + nMinus, " and sima^2 =", numpy.std(positions) ** 2)
    print("So apporximately N=sigma^2 motonaseb ast ba t")
    xAxis = list(numberOfRepeatedX.keys())
    yAxis = list(numberOfRepeatedX.values())

    pylab.plot(xAxis, yAxis, '.')
    pylab.show()
