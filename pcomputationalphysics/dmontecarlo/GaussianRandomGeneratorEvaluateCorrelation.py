import math
import random
import numpy
import pylab
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


def exp_fit(x, b):
    y = numpy.exp(-b * x)
    return y


def gaussianDistribution(x, sigma, mean):
    return (1 / sigma * math.sqrt(2 * math.pi)) * math.exp((-1 / 2) * (((x - mean) / sigma) ** 2))


if __name__ == "__main__":
    sigma = 1
    mean = 0
    xSequences = []

    x0 = 0.4
    numSamples = 1000000
    delta = 1.28  # a.r=0.5
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
    print("Acceptance ratio= ", acceptanceCounter / numSamples)
    js = []
    autocorr = []
    for j in [0, 1, 2, 5, 7, 10, 15, 20, 25, 30, 35, 40, 50, 60, 70, 80, 90, 100]:
        xSequencesPlusJ = []
        xSequencesTimesXSequencesPlusJ = []
        xSequencePow2 = []
        for m in range(len(xSequences) - j):
            xSequencesPlusJ.append(xSequences[m + j])
        for k in range(len(xSequencesPlusJ)):
            xSequencesTimesXSequencesPlusJ.append(xSequences[k] * xSequencesPlusJ[k])
        for s in range(len(xSequences)):
            xSequencePow2.append(xSequences[s] * xSequences[s])
        autoCorrelation = ((numpy.mean(xSequencesTimesXSequencesPlusJ)) - (
                numpy.mean(xSequences) * numpy.mean(xSequencesPlusJ))) / (
                                  numpy.mean(xSequencePow2) - numpy.mean(xSequences) ** 2)
        print("Auto correlation for j=", j, "  is :", autoCorrelation)
        js.append(j)
        autocorr.append(autoCorrelation)

    pylab.plot(js, autocorr, '.')
    pylab.show()
    x = numpy.array(js)
    y = numpy.array(autocorr)
    fit = curve_fit(exp_fit, x, y)
    print(fit)
    fit_eq =numpy.exp(-fit[0][0] * x)

    fig = plt.figure()
    ax = fig.subplots()
    ax.scatter(x, y, color='b', s=5)
    ax.plot(x, fit_eq, color='r', alpha=0.7)
    plt.show()
    print("Tole hambastegi taghribi=",1/fit[0][0])
