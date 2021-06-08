import numpy
import pylab
import random
import math
from pcomputationalphysics.isingmodel.Initial import initialState
from pcomputationalphysics.isingmodel.Energy import calculateEnergy
from pcomputationalphysics.isingmodel.EnergyDelta import calculateEnergyDelta
from pcomputationalphysics.isingmodel.CalculateMagnetization import magnetizationCalculation
from pcomputationalphysics.isingmodel.AutoCorrelation import calculateAutoCorrelation


def metropolisAlgForIsingModel(size, beta, flag, sigma):
    initial = initialState(size, flag, sigma)
    print(initial)
    energy = calculateEnergy(size, initial)
    initMagn = magnetizationCalculation(initial)
    number = 0
    numSamples = 100000
    accepted = 0
    checkR = 0
    magnetizationList = []
    magnetizationList.append(initMagn)
    energies = []
    energies.append(energy)
    random.seed()
    while (number < numSamples):
        i = random.randint(0, size - 1)
        j = random.randint(0, size - 1)
        # newSigma = initial
        # newSigma[i][j] = -initial[i][j]
        # newEnergy = calculateEnergy(size, newSigma)
        # energyDelta = newEnergy - energy
        energyDelta = calculateEnergyDelta(i, j, initial)
        r = random.uniform(0, 1)
        if energyDelta < 0:
            initial[i][j] = -initial[i][j]
            magnetization = magnetizationCalculation(initial)
            magnetizationList.append(math.fabs(magnetization))
            energy += energyDelta
            energies.append(energy)
            accepted += 1
        elif r < numpy.exp(-beta * energyDelta):
            initial[i][j] = -initial[i][j]
            energy += energyDelta
            magnetization = magnetizationCalculation(initial)
            magnetizationList.append(magnetization)
            energies.append(energy)
            accepted += 1
            checkR += 1

        number += 1

    print("For Beta= \n", beta)
    print("Number of accepted move:", accepted)
    print("acceptance rate:", accepted / numSamples)
    jInAutoCorr = 100  # best choice for
    print("Magnetization Auto correlation for j=", jInAutoCorr, " is :",
          calculateAutoCorrelation(magnetizationList, jInAutoCorr))
    print("Energy Auto correlation for j=", jInAutoCorr, " is :",
          calculateAutoCorrelation(energies, jInAutoCorr))
    unCorrelatedMagnetization = []
    unCorrelatedEnergy = []
    for s in range(len(magnetizationList)):
        if s % jInAutoCorr == 0 and s > 1000:
            unCorrelatedMagnetization.append(magnetizationList[s])

    for t in range(len(energies)):
        if t % jInAutoCorr == 0 and t > 1000:
            unCorrelatedEnergy.append(energies[t])
    mean = 0
    if len(unCorrelatedMagnetization) != 0:
        mean = numpy.mean(unCorrelatedMagnetization)
    else:
        mean = initMagn
    energyMean = 0
    if len(unCorrelatedEnergy) != 0:
        energyMean = numpy.mean(unCorrelatedEnergy)
    else:
        energyMean = energy
    # we return normalize magnetization sigma(i,j)/L^2
    return initial, mean / (size * size), energyMean / (size * size)


if __name__ == "__main__":
    j = 1
    kb = 1
    size = 10
    flag = False
    magVersusTemp = {}
    energyVersusTemp = {}
    temperature = 1000
    temp = numpy.random.choice([0], size=(size, size))
    temperatures = []
    while (temperature > 0.1):
        beta = (1 / temperature)
        temp, mag, meanOfEnergy = metropolisAlgForIsingModel(size, beta, flag, temp)
        magVersusTemp[beta] = mag
        energyVersusTemp[beta] = meanOfEnergy
        flag = True
        temperatures.append(temperature)
        temperature *= 0.92

    print(magVersusTemp)
    temperatureInverseAxis = list(magVersusTemp.keys())
    magnAxis = list(magVersusTemp.values())
    energyAxis = list(energyVersusTemp.values())
    pylab.xlabel("B")
    pylab.ylabel("|M|")
    pylab.plot(temperatureInverseAxis, magnAxis, '.')
    pylab.show()
    pylab.xlabel("B")
    pylab.ylabel("E")
    pylab.plot(temperatureInverseAxis, energyAxis, '.', color='r')
    pylab.show()

    sortedTemp = temperatures[::-1]
    sortedMagn = magnAxis[::-1]
    sortedEnergy = energyAxis[::-1]
    pylab.xlabel("T")
    pylab.ylabel("M")
    pylab.plot(sortedTemp, sortedMagn, '.', color='b')
    pylab.show()
    pylab.xlabel('T')
    pylab.ylabel('E')
    pylab.plot(sortedTemp, sortedEnergy, '.', color='r')
    pylab.show()
