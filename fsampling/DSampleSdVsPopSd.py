import numpy
import pylab
import random


def getHighs():
    inFile = open('temperatures.csv')
    population = []
    for l in inFile:
        try:
            tempC = float(l.split(',')[1])
            population.append(tempC)
        except:
            continue
    return population


def getDiffs(population, sampleSizes):
    popStd = numpy.std(population)
    diffsFracs = []
    for sampleSize in sampleSizes:
        diffs = []
        for t in range(100):
            sample = random.sample(population, sampleSize)
            diffs.append(abs(popStd - numpy.std(sample)))
        diffMean = sum(diffs) / len(diffs)
        diffsFracs.append(diffMean / popStd)
    return pylab.array(diffsFracs) * 100


def plotDiffs(sampleSizes, diffs, title, label, color='b'):
    pylab.plot(sampleSizes, diffs, label=label,
               color=color)
    pylab.xlabel('Sample Size')
    pylab.ylabel('% Difference in SD')
    pylab.title(title)
    pylab.legend()
    pylab.show()

if __name__ == "__main__":
    sampleSizes = range(20, 600, 1)
    diffs = getDiffs(getHighs(), sampleSizes)
    plotDiffs(sampleSizes, diffs,
              'Sample SD vs Population SD, Temperatures',
              label='High temps')
