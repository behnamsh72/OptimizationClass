import random
import numpy
import pylab
import math
import scipy.integrate
import time


def integrand(x):
    return math.exp(-x * x)


if __name__ == "__main__":
    begin = time.time()
    numSamples = 1000000
    I = 0
    f = []
    f2 = []
    for i in range(numSamples):
        r = random.uniform(0, 1) * 2
        f.append(integrand(r))
        f2.append(integrand(r) ** 2)
        I += integrand(r)

    sigma = numpy.std(f)

    sigmaAnotherWay = math.sqrt(numpy.mean(f2) - (numpy.mean(f) ** 2))
    I /= numSamples
    I *= 2
    print("Integram exp(-x*x) between 0 & 2 is equall : ", I)

    delta = sigma / math.sqrt(numSamples)
    print("Delta=", delta)

    realValue = scipy.integrate.quad(integrand, 0, 2)[0]
    print("Real Value= ", realValue)

    print("Real Error= ", math.fabs(I - realValue))
    end = time.time()
    print("time= ", end - begin)
