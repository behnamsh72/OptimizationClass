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
    v = plb.hist(dist, bins=100, weights=[1 / numSamples] * len(dist))
    # the value of v is a tuple with length 2, the first element is a list or an array
    # giving me how many items are in each bin.and the second is the patches used to
    # produce the beautiful pictures we're use to seeing.

    plb.xlabel('x')
    plb.ylabel('Relative Frequency')
    plb.show()
    print('Fraction within ~200 of mean =', sum(v[0][30:70]))


if __name__ == "__main__":
    normallyDistributedGenerator()
