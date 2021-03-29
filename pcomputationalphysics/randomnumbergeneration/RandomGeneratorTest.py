import random
import pylab
import numpy
import math
import collections

if __name__ == "__main__":
    n = 0
    numbers = {}
    randomNumbers = []
    random.seed()
    while (n < 100000):
        r = random.randint(0, 10)
        n += 1
        randomNumbers.append(r)
        if r in numbers.keys():
            numbers[r] += 1
        else:
            numbers[r] = 1

    numbers = collections.OrderedDict(sorted(numbers.items()))
    xAxis = list(numbers.keys())
    yAxis = list(numbers.values())
    pylab.plot(xAxis, yAxis)
    pylab.show()
    print("Standard Deviation/N = ", numpy.std(randomNumbers) / n, "and 1/sqrt(n)=", 1 / math.sqrt(n))
