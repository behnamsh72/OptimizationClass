import random
import pylab
import numpy


def makeHist(data, title, xlabel, ylabel, bins=20):
    pylab.hist(data, bins=bins)
    pylab.title(title)
    pylab.xlabel(xlabel)
    pylab.ylabel(ylabel)
    pylab.show()


def getMeansAndSDs(population, sample, verbose=False):
    popMean = sum(population) / len(population)
    sampleMean = sum(sample) / len(sample)
    if verbose:
        makeHist(population,
                 'Daily High 1961-2015, Population\n' + \
                 '(mean = ' + str(round(popMean, 2)) + ')',
                 'Degrees C', 'Number Days')
        pylab.figure()
        makeHist(sample, 'Daily High 1961-2015, Sample\n' + \
                 '(mean = ' + str(round(sampleMean, 2)) + ')',
                 'Degrees C', 'Number Days')
        print('Population mean =', popMean)
        print('Standard deviation of population =',
              numpy.std(population))
        print('Sample mean =', sampleMean)
        print('Standard deviation of sample =',
              numpy.std(sample))
    return popMean, sampleMean, \
           numpy.std(population), numpy.std(sample)


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


if __name__ == "__main__":
    random.seed(0)
    population = getHighs()
    sample = random.sample(population, 100)
    getMeansAndSDs(population, sample, True)

    random.seed(0)
    population = getHighs()
    sampleSize = 100
    numSamples = 1000
    sampleMeans = []
    for i in range(numSamples):
        sample = random.sample(population, sampleSize)
        popMean, sampleMean, popSD, sampleSD = \
            getMeansAndSDs(population, sample, verbose=False)
        sampleMeans.append(sampleMean)
    print('Mean of sample Means =',
          round(sum(sampleMeans) / len(sampleMeans), 3))
    print('Standard deviation of sample means =',
          round(numpy.std(sampleMeans), 3))
    makeHist(sampleMeans, 'Means of Samples', 'Mean', 'Frequency')
    pylab.axvline(x=popMean, color='r')
    pylab.show()
