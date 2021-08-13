import math

import numpy


def calculatesSpatialCorrelationLength(sigma, j):
    size = len(sigma)
    sigmaISigmaIPlusJ = []
    sigmaI = []
    sigmaIPlusJ = []
    for k in range(len(sigma)):
        for l in range(len(sigma) - j):
            sigmaISigmaIPlusJ.append(sigma[k][l] * sigma[k][l + j])
            sigmaI.append(sigma[k][l])
            sigmaIPlusJ.append(sigma[k][l + j])

    pow2Sigma = []
    for f in range(len(sigma)):
        for g in range(len(sigma) - j):
            pow2Sigma.append(sigma[f][g + j] * sigma[f][g + j])

    numerator = numpy.mean(sigmaISigmaIPlusJ) - (numpy.mean(sigmaI) * numpy.mean(sigmaIPlusJ))
    denominator = numpy.mean(pow2Sigma) - (numpy.mean(sigma) ** 2)

    if denominator != 0 or numerator != 0:
        return math.fabs(numerator / denominator)
    else:
        return 0
