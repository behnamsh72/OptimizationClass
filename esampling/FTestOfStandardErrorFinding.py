import random
import numpy


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


# if sample size is good enough we can replace std(population) with std(sample)
def test(temp, sampleSize, popMean, numTrials):
    numBad = 0
    for t in range(numTrials):
        sample = random.sample(temp, sampleSize)
        sampleMean = sum(sample) / sampleSize
        se = numpy.std(sample) / sampleSize ** 0.5
        if abs(popMean - sampleMean) > 1.96 * se:
            numBad += 1
    print("Num of Bads: ", numBad)
    print('Fraction outside 95% confidence interval = ', numBad / numTrials)


if __name__ == "__main__":
    population = getHighs()
    meanOfPopulation = sum(population) / len(population)
    test(population, 200, meanOfPopulation, 1500)
