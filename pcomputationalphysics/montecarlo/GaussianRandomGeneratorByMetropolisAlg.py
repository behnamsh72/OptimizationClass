import math
import random
import numpy
import pylab


def gaussianDistribution(x, sigma, mean):
    return (1 / sigma * math.sqrt(2 * math.pi)) * math.exp((-1 / 2) * (((x - mean) / sigma) ** 2))


if __name__ == "__main__":
    sigma = 1
    mean = 0
    xSequences = []

    x0 = 0.4
    numSamples = 100000
    delta = 1.28  # a.r=0.5
    # delta = 0.25

    acceptanceCounter = 0
    x = x0
    for i in range(numSamples):
        y = x + (delta * random.choice([-1, 1]))
        w = gaussianDistribution(y, sigma, mean) / gaussianDistribution(x, sigma, mean)
        if w > 1:
            acceptanceCounter += 1
            x = y
            xSequences.append(x)
        else:
            r = random.uniform(0, 1)
            if r < w:
                acceptanceCounter += 1
                x = y
                xSequences.append(x)

    # print(xSequences)
    print("Acceptance ratio= ", acceptanceCounter / numSamples)

    meanX = numpy.mean(xSequences)
    dictX = {}
    stdX = numpy.std(xSequences)

    print("mean = ", meanX, " Std = ", stdX)
    for i in range(10):
        dictX[i] = 0

    for num in xSequences:
        if math.fabs(num - meanX) <= stdX / 5:
            dictX[0] += 1
        elif math.fabs(num - meanX) <= 2 * stdX / 4 and math.fabs(num - meanX) > stdX / 4:
            dictX[1] += 1

        elif math.fabs(num - meanX) <= 3 * stdX / 4 and math.fabs(num - meanX) > 2 * stdX / 4:
            dictX[2] += 1

        elif math.fabs(num - meanX) <= 4 * stdX / 4 and math.fabs(num - meanX) > 3 * stdX / 4:
            dictX[3] += 1

        elif math.fabs(num - meanX) <= 5 * stdX / 4 and math.fabs(num - meanX) > 4 * stdX / 4:
            dictX[4] += 1

        elif math.fabs(num - meanX) <= 6 * stdX / 4 and math.fabs(num - meanX) > 5 * stdX / 4:
            dictX[5] += 1

        elif math.fabs(num - meanX) <= 7 * stdX / 4 and math.fabs(num - meanX) > 6 * stdX / 4:
            dictX[6] += 1

        elif math.fabs(num - meanX) <= 8 * stdX / 4 and math.fabs(num - meanX) > 7 * stdX / 4:
            dictX[7] += 1

        elif math.fabs(num - meanX) <= 9 * stdX / 4 and math.fabs(num - meanX) > 8 * stdX / 4:
            dictX[8] += 1
        else:
            dictX[9] += 1
    xAxis = list(dictX.keys())
    yAxis = list(dictX.values())
    print(yAxis)
    pylab.plot(xAxis, yAxis, '.')
    pylab.show()

    j = 10 #tole hambastegi dar evaluate correlation 1 be das
    # amad ba fit kardan 3-10 barabar an ra az avale data joda mikonim
    xSequencesPlusJ = []
    for m in range(len(xSequences) - j):
        xSequencesPlusJ.append(xSequences[m + j])
    xSequencesTimesXSequencesPlusJ = []
    for k in range(len(xSequencesPlusJ)):
        xSequencesTimesXSequencesPlusJ.append(xSequences[k] * xSequencesPlusJ[k])
    xSequencePow2 = []
    for s in range(len(xSequences)):
        xSequencePow2.append(xSequences[s] * xSequences[s])
    autoCorrelation = ((numpy.mean(xSequencesTimesXSequencesPlusJ)) - (
            numpy.mean(xSequences) * numpy.mean(xSequencesPlusJ))) / (
                              numpy.mean(xSequencePow2) - numpy.mean(xSequences) ** 2)

    print("Auto correlation= ", autoCorrelation)

    uncorrelatedList = []
    for t in range(len(xSequences)):
        if (t % round(autoCorrelation * 100)) == 0:
            uncorrelatedList.append(xSequences[t])

    print(len(uncorrelatedList))

    dictY1 = {}
    for i in range(10):
        dictY1[i] = 0

    meanUncorrelatedList = numpy.mean(uncorrelatedList)
    stdUncorrelatedList = numpy.std(uncorrelatedList)
    for num in uncorrelatedList:
        if math.fabs(num - meanUncorrelatedList) <= stdUncorrelatedList / 2:
            dictY1[0] += 1
        elif math.fabs(num - meanUncorrelatedList) <= 2 * stdUncorrelatedList / 4 and math.fabs(
                num - meanUncorrelatedList) > stdUncorrelatedList / 4:
            dictY1[1] += 1

        elif math.fabs(num - meanUncorrelatedList) <= 3 * stdUncorrelatedList / 4 and math.fabs(
                num - meanUncorrelatedList) > 2 * stdUncorrelatedList / 4:
            dictY1[2] += 1

        elif math.fabs(num - meanUncorrelatedList) <= 4 * stdUncorrelatedList / 4 and math.fabs(
                num - meanUncorrelatedList) > 3 * stdUncorrelatedList / 4:
            dictY1[3] += 1

        elif math.fabs(num - meanUncorrelatedList) <= 5 * stdUncorrelatedList / 4 and math.fabs(
                num - meanUncorrelatedList) > 4 * stdUncorrelatedList / 4:
            dictY1[4] += 1

        elif math.fabs(num - meanUncorrelatedList) <= 6 * stdUncorrelatedList / 4 and math.fabs(
                num - meanUncorrelatedList) > 5 * stdUncorrelatedList / 4:
            dictY1[5] += 1

        elif math.fabs(num - meanUncorrelatedList) <= 7 * stdUncorrelatedList / 4 and math.fabs(
                num - meanUncorrelatedList) > 6 * stdUncorrelatedList / 4:
            dictY1[6] += 1

        elif math.fabs(num - meanUncorrelatedList) <= 8 * stdUncorrelatedList / 4 and math.fabs(
                num - meanUncorrelatedList) > 7 * stdUncorrelatedList / 4:
            dictY1[7] += 1

        elif math.fabs(num - meanUncorrelatedList) <= 9 * stdUncorrelatedList / 4 and math.fabs(
                num - meanUncorrelatedList) > 8 * stdUncorrelatedList / 4:
            dictY1[8] += 1
        else:
            dictY1[9] += 1

    xAxis = list(dictY1.keys())
    yAxis = list(dictY1.values())
    pylab.plot(xAxis, yAxis, '.')
    pylab.show()
