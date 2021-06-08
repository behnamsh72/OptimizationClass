import random
import numpy
import math


def magnetizationCalculation(sigma):
    magnetization = 0
    for i in range(len(sigma)):
        for j in range(len(sigma[0])):
            magnetization += sigma[i][j]
    return magnetization
