import numpy
import random
import pylab
import math
import scipy.integrate
import time


def convertRandomGenerator(x):
    return math.log(1 / (1 - x))


def weightFunction(x):
    return math.exp(-x)


def integrandFunction(x):
    return math.exp(-x * x)


if __name__ == "__main__":
    begin = time.time()
    numSamples = 1000000
    I = 0
    fDividedByG = []
    fDividedByPow2 = []
    weightFunctionIntegral = scipy.integrate.quad(weightFunction, 0, math.inf)[0]

    for i in range(numSamples):
        r = random.uniform(0, 1)
        weightedRandom = convertRandomGenerator(r)
        fDividedByG.append(integrandFunction(weightedRandom) / weightFunction(weightedRandom))
        fDividedByPow2.append((integrandFunction(weightedRandom) / weightFunction(weightedRandom)) ** 2)
        I += (integrandFunction(weightedRandom) / weightFunction(weightedRandom))
    I /= numSamples
    I *= weightFunctionIntegral
    print("Integral of exp(-x^2) from 0 to 2 :", I)
    std = numpy.std(fDividedByG)
    stdAnotherWay = (math.sqrt(numpy.mean(fDividedByPow2) - numpy.mean(fDividedByG) ** 2))
    print("Std =", std, " another way:", stdAnotherWay)

    delta = (std / math.sqrt(numSamples)) * weightFunctionIntegral

    print("Delta=", delta)

    realValue = scipy.integrate.quad(integrandFunction, 0, 2)[0]
    print("Real Value= ", realValue)
    print("Real Error= ", math.fabs(I - realValue))
    end = time.time()
    print("time= ", end - begin)
