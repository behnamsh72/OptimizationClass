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


def aveMeanSquaredError(data, predicted):
    error = 0.0
    for i in range(len(data)):
        error += (data[i] - predicted[i]) ** 2
    return error / len(data)


def rSquared(observed, predicted):
    error = ((predicted - observed) ** 2).sum()
    meanError = error / len(
        observed)  # we devide by length because if denominator we use variance instead
    # of denominator is R so ratio is same wirh R
    return 1 - (meanError / numpy.var(observed))


if __name__ == "__main__":
    xVals, yVals = getData("mysteryData.txt")
    model = pylab.polyfit(xVals, yVals, 1)
    estYValsForLinearModel = pylab.polyval(model, xVals)
    print('Ave. mean square error for linear model = ', aveMeanSquaredError(yVals, estYValsForLinearModel))
    model2 = pylab.polyfit(xVals, yVals, 2)
    estYValsForQuadraticModel = pylab.polyval(model2, xVals)
    print('Ave. mean square error for quadratic model = ', aveMeanSquaredError(yVals, estYValsForQuadraticModel))

    print("R squared for linear model= ", rSquared(yVals, estYValsForLinearModel))
    print("R squared for linear model= ", rSquared(yVals, estYValsForQuadraticModel))
