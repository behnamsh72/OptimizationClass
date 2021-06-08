import numpy
import random


def calculateEnergyDelta(i, j, sigma):
    if i == 0:
        iMinus1 = len(sigma) - 1
    else:
        iMinus1 = (i) - 1

    if j == 0:
        jMinus1 = len(sigma) - 1
    else:
        jMinus1 = (j) - 1

    deltaEnergy = -2 * sigma[i][j] * (
            sigma[iMinus1][j] + sigma[i][jMinus1] + sigma[i][
        (j + 1) % (len(sigma))] +
            sigma[(i + 1) % (len(sigma))][j])

    return deltaEnergy
