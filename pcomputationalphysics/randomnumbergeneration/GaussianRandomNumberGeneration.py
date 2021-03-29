import random
import math
import numpy
import pylab


def convertMethod(x1, x2):
    rho = rhoFunction(x1)
    thetha = thethaFunction(x2)

    return (rho * math.cos(thetha), rho * math.sin(thetha))


def thethaFunction(x):
    return 2 * math.pi * x


def rhoFunction(x):
    return math.sqrt(math.log(1 / x))


if __name__ == "__main__":
    x1s = []
    x2s = []
    m = 0
    while (m < 10000):
        x1 = random.random()
        if x1 == 0:
            print("zero")
            continue
        x1s.append(x1)
        m += 1

    random.seed()
    n = 0
    while (n < 10000):
        x2 = random.random()
        if x2 == 0:
            continue
        x2s.append(x2)
        n += 1
    y1s = []
    y2s = []
    for i in range(len(x1s)):
        y1, y2 = convertMethod(x1s[i], x2s[i])
        y1s.append(y1)
        y2s.append(y2)

    meanY1 = numpy.mean(y1s)
    stdY1s = numpy.std(y1s)
    print(meanY1)
    print(stdY1s)
    dictY1 = {}
    for i in range(10):
        dictY1[i] = 0

    for num in y1s:
        if math.fabs(num - meanY1) <= stdY1s / 2:
            dictY1[0] += 1
        elif math.fabs(num - meanY1) <= 2 * stdY1s / 2 and math.fabs(num - meanY1) > stdY1s / 2:
            dictY1[1] += 1

        elif math.fabs(num - meanY1) <= 3 * stdY1s / 2 and math.fabs(num - meanY1) > 2 * stdY1s / 2:
            dictY1[2] += 1

        elif math.fabs(num - meanY1) <= 4 * stdY1s / 2 and math.fabs(num - meanY1) > 3 * stdY1s / 2:
            dictY1[3] += 1

        elif math.fabs(num - meanY1) <= 5 * stdY1s / 2 and math.fabs(num - meanY1) > 4 * stdY1s / 2:
            dictY1[4] += 1

        elif math.fabs(num - meanY1) <= 6 * stdY1s / 2 and math.fabs(num - meanY1) > 5 * stdY1s / 2:
            dictY1[5] += 1

        elif math.fabs(num - meanY1) <= 7 * stdY1s / 2 and math.fabs(num - meanY1) > 6 * stdY1s / 2:
            dictY1[6] += 1

        elif math.fabs(num - meanY1) <= 8 * stdY1s / 2 and math.fabs(num - meanY1) > 7 * stdY1s / 2:
            dictY1[7] += 1

        elif math.fabs(num - meanY1) <= 9 * stdY1s / 2 and math.fabs(num - meanY1) > 8 * stdY1s / 2:
            dictY1[8] += 1
        else:
            dictY1[9] += 1

    xAxis = list(dictY1.keys())
    yAxis = list(dictY1.values())
    pylab.plot(xAxis, yAxis, '.')
    pylab.show()
