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


def showErrorBars(population, sizes, numTrials):
    xVals = []
    sizeMeans, sizeSDs = [], []
    for sampleSize in sizes:
        xVals.append(sampleSize)
        trialMeans = []
        for t in range(numTrials):
            sample = random.sample(population, sampleSize)
            popMean, sampleMean, popSD, sampleSD = \
                getMeansAndSDs(population, sample)
            trialMeans.append(sampleMean)
        sizeMeans.append(sum(trialMeans) / len(trialMeans))
        sizeSDs.append(numpy.std(trialMeans))
    print(sizeSDs)
    pylab.errorbar(xVals, sizeMeans,
                   yerr=1.96 * pylab.array(sizeSDs), fmt='o',
                   label='95% Confidence Interval')
    pylab.title('Mean Temperature ('
                + str(numTrials) + ' trials)')
    pylab.xlabel('Sample Size')
    pylab.ylabel('Mean')
    pylab.axhline(y=popMean, color='r', label='Population Mean')
    pylab.xlim(0, sizes[-1] + 10)
    pylab.legend()
    pylab.show()


if __name__ == "__main__":
    random.seed(0)
    population = getHighs()
    showErrorBars(population,
              (50, 100, 200, 300, 400, 500, 600), 100)
