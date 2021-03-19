import numpy
import random
import pylab


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


def sem(popSD, sampleSize):
    return popSD / sampleSize ** 0.5


if __name__ == "__main__":
    sampleSizes = (25, 50, 100, 200, 300, 400, 500, 600)
    numTrials = 50

    population = getHighs()

    popSd = numpy.std(population)
    sems = []
    sampleSds = []

    for size in sampleSizes:
        sems.append(sem(popSd, size))
        means = []
        for t in range(numTrials):
            sample = random.sample(population, size)
            means.append(sum(sample) / len(sample))

        sampleSds.append(numpy.std(means))

    pylab.plot(sampleSizes, sampleSds, label="Std of " + str(numTrials) + ' means')
    pylab.plot(sampleSizes, sems, 'r--', label='SEM')
    pylab.xlabel('Sample size')
    pylab.ylabel('Std and SEM')
    pylab.title('SD for ' + str(numTrials) + ' Means and SEM')
    pylab.legend()
    pylab.show()
