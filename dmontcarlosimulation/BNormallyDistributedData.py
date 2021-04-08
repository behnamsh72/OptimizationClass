# Genrating Normally Distributed data
import random
from matplotlib import pyplot as plt
from matplotlib import pylab as plb


def normallyDistributedGenerator():
    dist, numSamples = [], 1000000
    for i in range(numSamples):
        dist.append(random.gauss(0, 100))
        # mean =0 and sigma=100
    weights = [1 / numSamples] * len(dist)
    print(len(weights))
    #An array of weights, of the same shape as x. Each value in x only contributes its
    # associated weight towards the bin count (instead of first). If density is True, the weights are
    # normalized, so that the integral of the density over the range remains first.
    v = plb.hist(dist, bins=100, weights=[1 / numSamples] * len(dist))
    # the value of v is a tuple with length 2, the first element is a list or an array
    # giving me how many items are in each bin.and the second is the patches used to
    # produce the beautiful pictures we're use to seeing.

    plb.xlabel('x')
    plb.ylabel('Relative Frequency')
    #plt is a Discrete Approximation to PDF
    plb.show()
    #If i devide 200 by 2 i get 100.which happens to be the standard deviation,so in this case what i'm
    #going to be looking at is what fraction of the values fall within two standard deviations of the mean?
    #kind of check on the emprerical rule
    print('Fraction within ~200 of mean =', sum(v[0][30:70]))


if __name__ == "__main__":
    normallyDistributedGenerator()
