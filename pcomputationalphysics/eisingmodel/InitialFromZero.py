import numpy
import random


def initialStateFromZero(size, flag, sigma):
    if size < 1:
        raise ValueError("Dimension of lattice must bigger than one")
    if flag:
        return sigma
    else:
        initState = numpy.random.choice([-1], size=(size, size))
        return initState
