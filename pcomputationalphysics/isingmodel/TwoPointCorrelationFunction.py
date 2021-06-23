import numpy


def calculatesPointsCorrelationFunction(sigma, j):
    size = len(sigma)
    sigmaIsigmaIPlusJ = []
    for i in range(len(sigma) - j):
        temp = sigma[0][i] * sigma[0][i + j]
        sigmaIsigmaIPlusJ.append(temp)

    sigmaIsigmaIPlusJMean = numpy.mean(sigmaIsigmaIPlusJ)
    sigmaIMean = numpy.mean(sigma[0])

    sigmaIPlusJ = []
    for f in range(len(sigma - j)):
        sigmaIPlusJ.append(sigma[0][f + j])

    sigmaIPlusJmean = numpy.mean(sigmaIPlusJ)

    sigmaPow2Mean = numpy.mean(sigma[0])

    answer = (sigmaIsigmaIPlusJMean - (sigmaIMean * sigmaIPlusJmean)) / (sigmaPow2Mean - sigmaIMean * sigmaIMean)

    return answer
