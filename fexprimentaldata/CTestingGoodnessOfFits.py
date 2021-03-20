import pylab
import numpy


def getData(fileName):
    file = open(fileName, 'r')
    xvals, yvals = [], []
    for line in file:
        try:
            print(line)
            array = line.split(' ')
            xvals.append(float(array[1]))
            yvals.append(float(array[0]))
        except:
            continue

    file.close()
    return xvals, yvals


def rSquared(observed, predicted):
    error = ((predicted - observed) ** 2).sum()
    meanError = error / len(
        observed)  # we devide by length because if denominator we use variance instead
    # of denominator is R so ratio is same wirh R
    return 1 - (meanError / numpy.var(observed))


def genFits(xVals, yVals, degrees):
    models = []
    for d in degrees:
        model = pylab.polyfit(xVals, yVals, d)
        models.append(model)
    return models


def testFits(models, degrees, xVals, yVals, title):
    pylab.plot(xVals, yVals, 'o', label='Data')
    for i in range(len(models)):
        estYVals = pylab.polyval(models[i], xVals)
        error = rSquared(yVals, estYVals)
        pylab.plot(xVals, estYVals, label='Fit of degree' + str(degrees[i]) +
                                          ', R2 =' + str(round(error, 5)))

    pylab.legend(loc='best')
    pylab.title(title)
    pylab.show()


if __name__ == "__main__":
    xVals, yVals = getData("mysteryData.txt")
    degrees = ( 2, 4, 8, 16)
    models = genFits(xVals, yVals, degrees)
    testFits(models, degrees, xVals, yVals, "Mystery Data")
