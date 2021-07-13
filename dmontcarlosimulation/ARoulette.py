import random


class FairRoulette():
    def __init__(self):
        self.pockets = []
        for i in range(1, 37):
            self.pockets.append(i)

        self.ball = None
        self.pocketOdds = len(self.pockets) - 1

    def spin(self):
        self.ball = random.choice(self.pockets)

    def betPocket(self, pocket, amt):
        if str(pocket) == str(self.ball):
            return amt * self.pocketOdds
        else:
            return -amt

    def __str__(self):
        return 'Fair Roulette'


class EuRoulette(FairRoulette):
    def __init__(self):
        FairRoulette.__init__(self)
        self.pockets.append('0')

    def __str__(self):
        return 'European Roulette'


class AmRoulette(EuRoulette):
    def __init__(self):
        EuRoulette.__init__(self)
        self.pockets.append('00')

    def __str__(self):
        return 'American Roulette'


def playRoulette(game, numSpins, pocket, bet, toPrint=False):
    totPocket = 0
    for i in range(numSpins):
        game.spin()
        totPocket += game.betPocket(pocket, bet)

    if toPrint:
        print(numSpins, 'Spins of', game)
        # it's an average of return betting for this pocket
        print("Expected return betting", pocket, '=', str(100 * totPocket / numSpins) + "%\n")
    return (totPocket / numSpins)


# added new for standard deviation
def getMeanAndStd(X):
    mean = sum(X) / float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean) ** 2
    std = (tot / len(X)) ** 0.5
    return mean, std


def findPocketReturn(game, numTrials, trialSize, toPrint):
    pocketReturns = []
    for t in range(numTrials):
        trialVals = playRoulette(game, trialSize, 2, 1, toPrint)
        pocketReturns.append(trialVals)
    return pocketReturns


def applyEmpricalRule():
    random.seed(0)
    numTrials = 20
    resultDict = {}
    games = (FairRoulette, EuRoulette, AmRoulette)
    for G in games:
        resultDict[G().__str__()] = []
    for numSpins in (1000, 100000, 1000000):
        print("\n Simulate betting  a pocket for ", numTrials, ' trials of ', numSpins, ' spins each')

        for G in games:
            pocketReturns = findPocketReturn(G(), 20, numSpins, False)
            mean, std = getMeanAndStd(pocketReturns)
            resultDict[G().__str__()].append((numSpins, 100 * mean, 100 * std))
            print('Exp. return for ', G(), '=', str(round(100 * mean, 3)) + ' %, ',
                  '+/-' + str(round(100 * 1.96 * std, 3)) + '% woth 95% confidence')


if __name__ == "__main__":
    # for infinite number of spins Excepted return betting -> 0 percent because the law of large numbers
    # for numSpins in (1000, 10000, 100000, 1000000):
    #     fairRoulette = 0
    #     euRoulette = 0
    #     amRoulette = 0
    #     for i in range(20):
    #         random.seed(0)
    #         fairRoulette += playRoulette(FairRoulette(), numSpins, 2, a, True)
    #         random.seed(0)
    #         euRoulette += playRoulette(EuRoulette(), numSpins, 2, a, True)
    #         random.seed(0)
    #         amRoulette += playRoulette(AmRoulette(), numSpins, 2, a, False)
    #     print("Num spins : ", numSpins, " FairRoulette=", fairRoulette / 20, "%\n")
    #     print("Num spins : ", numSpins, " EuRoulette=", euRoulette / 20, "%\n")
    #     print("Num spins : ", numSpins, " AmRoulette=", amRoulette / 20, "%\n")

    # new for standard deviation
    applyEmpricalRule()
