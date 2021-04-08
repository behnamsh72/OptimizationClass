import random
import pylab
from dmontcarlosimulation.ARoulette import FairRoulette
from dmontcarlosimulation.ARoulette import findPocketReturn


def getMeanAndStd(X):
    mean = sum(X) / float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean) ** 2
    std = (tot / len(X)) ** 0.5
    return mean, std


def plotMeans(numDice, numRolls, numBins, legend, color, style):
    # numDice : how many die ( sample size)
    # NumRolls: how many times are we going to roll that number of die
    # we'll take a  bunch of samples which i'm calling number of rolls
    means = []
    # num of trials: numRolls//numDice so if i have more dice.i get to have fewer samples more dice per sample
    for i in range(numRolls // numDice):
        vals = 0
        for j in range(numDice):
            vals += 5 * random.random()
        means.append(vals / float(numDice))

    pylab.hist(means, numBins, color=color, label=legend, weights=pylab.array(len(means) * [1]) / len(means),
               hatch=style)
    return getMeanAndStd(means)


def testForDice():
    mean, std = plotMeans(1, 1000000, 19, 'first die', 'b', '*')
    print('Mean of rolling first die = ', str(mean) + ' , ' + 'Std= ', std)
    mean, std = plotMeans(50, 1000000, 19, ' Mean of 50 dice', 'r', '//')
    print('Mean of rolling 50 die = ', str(mean) + ' , ' + 'Std= ', std)

    pylab.title('Rolling Continues Dice')
    pylab.xlabel('Value')
    pylab.ylabel('Probability')
    pylab.legend()
    pylab.show()


def testForFairRoulette():
    numTrials = 1000000
    numSpins = 200
    game = FairRoulette()
    means = []
    for i in range(numTrials):
        means.append(findPocketReturn(game, 1, numSpins, False)[0])

    pylab.hist(means, bins=19, weights=[1 / len(means)] * len(means))
    pylab.xlabel('Mean return')
    pylab.ylabel('Probability')
    pylab.title('Expected return Betting a pocket 200 Times ')
    pylab.show()


if __name__ == "__main__":
    # testForDice()
    testForFairRoulette()
    print("End")
