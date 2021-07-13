import pylab
import random
import numpy


class tempDatum(object):
    def __init__(self, s):
        info = s.split(',')
        self.high = float(info[1])
        self.year = int(info[2][0:4])

    def getHigh(self):
        return self.high

    def getYear(self):
        return self.year


def getTempData():
    inFile = open('temperatures.csv')
    data = []
    for l in inFile:
        data.append(tempDatum(l))

    return data


# Get Mean high temperature for each year

def getYearlyMeans(data):
    years = {}

    for d in data:
        try:
            years[d.getYear()].append(d.getHigh())
        except:
            years[d.getYear()] = [d.getHigh()]

    for y in years:
        years[y] = sum(years[y]) / len(years[y])

    return years


def splitData(XVals, yVals):
    toTrain = random.sample(range(len(xVals)), len(xVals) // 2)
    trainX, trainY, testX, testY = [], [], [], []

    for i in range(len(xVals)):
        if i in toTrain:
            trainX.append(xVals[i])
            trainY.append(yVals[i])
        else:
            testX.append(xVals[i])
            testY.append(yVals[i])

    return trainX, trainY, testX, testY


def rSquared(observed, predicted):
    error = ((predicted - observed) ** 2).sum()
    meanError = error / len(
        observed)  # we devide by length because if denominator we use variance instead
    # of denominator is R so ratio is same wirh R
    return 1 - (meanError / numpy.var(observed))


if __name__ == "__main__":
    data = getTempData()
    years = getYearlyMeans(data)
    xVals, yVals = [], []
    for e in years:
        xVals.append(e)
        yVals.append(years[e])

    pylab.plot(xVals, yVals)
    pylab.xlabel('Year')
    pylab.ylabel('Mean Daily High (C) ')
    pylab.title('Select U.S. Cities')

    pylab.show()

    numSubsets = 10
    dimensions = (1, 2, 3, 4)
    rSquares = {}

    for d in dimensions:
        rSquares[d] = []

    for f in range(numSubsets):
        trainX, trainY, testX, testY = splitData(xVals, yVals)
        for d in dimensions:
            model = pylab.polyfit(trainX, trainY, d)
            estYVals = pylab.polyval(model, testX)

            rSquares[d].append(rSquared(testY, estYVals))

    print('Mean R-Squares for test Data ')
    for d in dimensions:
        mean = round(sum(rSquares[d]) / len(rSquares[d]), 4)
        sd = round(numpy.std(rSquares[d]), 4)
        print('For dimentionality ', d, ' mean=', mean, 'Std = ', sd)

# Line seems to be the winner
# a-Highest average  r-squared
# 2-Smallest deviation across trials
# 3-Simplest Model
