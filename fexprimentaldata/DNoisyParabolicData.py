import pylab
import random


def getNoisyParabolicData(a, b, c, xVals, fName):
    yVals = []
    for x in xVals:
        theoreticalVal = a * x ** 2 + b * x + c
        yVals.append(theoreticalVal + random.gauss(0, 35))

    f = open(fName, 'w')
    f.write('x       y\n')
    for i in range(len(yVals)):
        f.write(str(xVals[i]) + ' ' + str(yVals[i]) + '\n')
    f.close()


if __name__ == "__main__":
    # parameters for generating data
    xVals = range(-10, 11, 1)
    a, b, c = 3, 0, 0
    getNoisyParabolicData(a, b, c, xVals, 'MysteryDataGen.ext')
