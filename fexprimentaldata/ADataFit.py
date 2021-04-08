import pylab


def fitData(fileName):
    xVals, yVals = getData(fileName)

    # for do math on the array without loop
    xVals = pylab.array(xVals)
    yVals = pylab.array(yVals)
    xVals = xVals * 9.81

    pylab.plot(xVals, yVals, 'bo', label='Measured Displacements')
    pylab.xlabel('|Force| (Newtons)')
    pylab.ylabel('Distance (meters)')

    a, b = pylab.polyfit(xVals, yVals, 1)

    estValues = a * pylab.array(xVals) + b
    print('a = ', a, ' b = ', b)
    pylab.plot(xVals, estValues, 'r', label='Linear fit , k = ' + str(round(1 / a, 5)))
    pylab.legend(loc='best')
    pylab.show()


def fitDataUsingPolyVal(fileName, polynomial, fitDegree, color, plotActualData=False):
    xVals, yVals = getData(fileName)

    # for do math on the array without loop
    xVals = pylab.array(xVals)
    yVals = pylab.array(yVals)
    xVals = xVals * 9.81

    if plotActualData:
        pylab.plot(xVals, yVals, 'bo', 'Actual data')
        pylab.xlabel('X vals)')
        pylab.ylabel('Y vals')
    # this model could be  a line or parabola or quartic ,... in fact any order polynomial
    model = pylab.polyfit(xVals, yVals, polynomial)

    estValues = pylab.polyval(model, xVals)

    pylab.plot(xVals, estValues, color, label=fitDegree)
    pylab.legend(loc='best')


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


if __name__ == "__main__":
    # fitData("springData.txt",first,"Linear fit")
    # fitDataUsingPolyVal("springData.txt", first,"Linear fit")
    fitDataUsingPolyVal("mysteryData.txt", 2, "Quadratic Fit", 'r', True)
    fitDataUsingPolyVal("mysteryData.txt", 4, "Quadrature Fit", 'b')
    fitDataUsingPolyVal("mysteryData.txt", 8, "Degree8 Fit", 'g')
    fitDataUsingPolyVal("mysteryData.txt", 16, "Degree16 Fit", 'y')
    pylab.show()
