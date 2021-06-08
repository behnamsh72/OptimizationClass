import numpy
import random


def initialState(size, flag, sigma):
    if size < 1:
        raise ValueError("Dimension of lattice must bigger than one")
    if flag:
        return sigma
    else:
        numpy.random.seed()
        initState = numpy.random.choice([-1, 1], size=(size, size))
        return initState
