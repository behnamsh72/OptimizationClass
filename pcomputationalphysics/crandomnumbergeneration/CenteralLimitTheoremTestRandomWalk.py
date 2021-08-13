import numpy
import random
import pylab
import math
import time
import collections

if __name__ == "__main__":
    meanPositions = []
    n, y = 0, 0

    while y < 1000:
        positions = []
        print(y)
        while n < 1000:
            random.seed()
            x = 0
            for i in range(0, 100):
                r = random.choice([-1, 1])
                x += r
            positions.append(x)
            n += 1
        meanPositions.append(numpy.mean(positions))
        n = 0
        y += 1

print(meanPositions)
meansPopulation = {}
for mean in meanPositions:
    if mean in meansPopulation.keys():
        meansPopulation[mean] += 1
    else:
        meansPopulation[mean] = 1

xAxis = list(meansPopulation.keys())
yAxis = list(meansPopulation.values())

print(yAxis)

pylab.plot(xAxis, yAxis, '.')
pylab.show()
