# simulating Buffon-Laplace Method
import random
import numpy


def throwNeedles(numNeedles):
    inCircle = 0
    for needle in range(1, numNeedles + 1, 1):
        x = random.random()
        y = random.random()
        if (x * x + y * y) ** 0.5 <= 1.0:
            inCircle += 1

    return 4 * (inCircle / float(numNeedles))


def getEst(numNeedles, numTrials):
    estimates = []
    for t in range(numTrials):
        piGuess = throwNeedles(numNeedles)
        estimates.append(piGuess)
    sDev = numpy.std(estimates)
    curEst = sum(estimates) / len(estimates)
    print('Est. = ' + str(curEst) + ' , Std. dev. = ' + str(round(sDev, 6)) + ' , Needles =' + str(numNeedles))
    return (curEst, sDev)


def estPi(precision, numTrials):
    numNeedles = 1000
    sDev = precision

    # it's just going to keep increasing the number of needles,doubling the number needles
    # until it's confident about the estimate,confident enough
    while sDev >= precision / 2:
        curEst, sDev = getEst(numNeedles, numTrials)
        numNeedles *= 2
        # 2 or 1.96

    return curEst


if __name__ == "__main__":
    estPi(0.005, 100)
