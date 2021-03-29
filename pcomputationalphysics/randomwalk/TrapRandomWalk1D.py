import random
import matplotlib.pyplot as plt
import numpy
import math

if __name__ == "__main__":
    totlalN = []
    x0 = random.randint(1, 20)
    print("x0 = ", x0)
    random.seed()
    for i in range(0, 1000000):
        x = x0
        n = 0
        while True:
            move = random.choice([-1, 1])
            x += move
            n += 1
            if x == 0 or x == 20:
                break
        # print("for ", i, " n = ", n)
        totlalN.append(n)

    print(totlalN)
    print("mean = ", numpy.mean(totlalN), " += ", numpy.std(totlalN))
    std = 0
    mean = numpy.mean(totlalN)
    for i in totlalN:
        std += (i - mean) ** 2

    std /= len(totlalN)

    std = math.sqrt(std)
    print("std: ", std)
