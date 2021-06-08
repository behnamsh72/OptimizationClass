import numpy
import random


def calculateEnergy(size, sigma):
    energy = 0
    for i in range(size):
        for j in range(size):
            energy += -sigma[i][j] * (sigma[i][(j + 1) % (size)] +
                                      sigma[(i + 1) % (size)][j])
    return energy
