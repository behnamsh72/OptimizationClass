import numpy
import pylab
import random
import math
from pcomputationalphysics.eisingmodel.Initial import initialState
from pcomputationalphysics.eisingmodel.Energy import calculateEnergy
from pcomputationalphysics.eisingmodel.EnergyDelta import calculateEnergyDelta
from pcomputationalphysics.eisingmodel.CalculateMagnetization import magnetizationCalculation
from pcomputationalphysics.eisingmodel.AutoCorrelation import calculateAutoCorrelation
from pcomputationalphysics.eisingmodel.SpatialCorrelationLength import calculatesSpatialCorrelationLength


def metropolisAlgForIsingModel(size, beta, flag, sigma, J):
    initial = initialState(size, flag, sigma)
    print(initial)
    energy = calculateEnergy(size, initial, J)
    initMagn = magnetizationCalculation(initial)
    number = 0
    numSamples = 100000
    accepted = 0
    checkR = 0
    J = 4  # STAND FOR SPATIAL CORRELATION FUCNTION J
    magnetizationList = []
    magnetizationList.clear()
    absoluteValueOfMagnetizationList = []
    absoluteValueOfMagnetizationList.clear()
    magnetizationList.append(initMagn)
    print("Initial magn =", math.fabs(initMagn))
    absoluteValueOfMagnetizationList.append(math.fabs(initMagn))
    energies = []
    energies.append(energy)
    spatialFunctionNorms = []
    random.seed()
    while (number < numSamples):
        i = random.randint(0, size - 1)
        j = random.randint(0, size - 1)
        # newSigma = initial
        # newSigma[i][j] = -initial[i][j]
        # newEnergy = calculateEnergy(size, newSigma)
        # energyDelta = newEnergy - energy
        energyDelta = calculateEnergyDelta(i, j, initial)
        minusBeta = -beta
        r = random.uniform(0, 1)
        if energyDelta < 0:
            initial[i][j] = -initial[i][j]
            magnetization = magnetizationCalculation(initial)
            magnetizationList.append(magnetization)
            absoluteValueOfMagnetizationList.append(math.fabs(magnetization))
            energy += energyDelta
            energies.append(energy)
            spatialFunctionNorms.append(calculatesSpatialCorrelationLength(sigma, J))

            accepted += 1
        elif r < math.exp(minusBeta * energyDelta):
            initial[i][j] = -initial[i][j]
            energy += energyDelta
            magnetization = magnetizationCalculation(initial)
            magnetizationList.append(magnetization)
            absoluteValueOfMagnetizationList.append(math.fabs(magnetization))

            energies.append(energy)
            spatialFunctionNorms.append(calculatesSpatialCorrelationLength(sigma, J))

            accepted += 1
            checkR += 1

        number += 1
    print("Check R=", checkR)
    print("For Beta= \n", beta)
    print("Number of accepted move:", accepted)
    print("acceptance rate:", accepted / numSamples)
    jInAutoCorr = 25  # best choice for
    print("Magnetization Auto correlation for j=", jInAutoCorr, " is :",
          calculateAutoCorrelation(magnetizationList, jInAutoCorr))
    print("Energy Auto correlation for j=", jInAutoCorr, " is :",
          calculateAutoCorrelation(energies, jInAutoCorr))
    unCorrelatedMagnetization = []
    unCorrelatedAbsoluteMagnetization = []
    unCorrelatedEnergy = []
    for s in range(len(magnetizationList)):
        if s % jInAutoCorr == 0 and s > 10 * jInAutoCorr:
            unCorrelatedMagnetization.append(magnetizationList[s])
            unCorrelatedAbsoluteMagnetization.append(absoluteValueOfMagnetizationList[s])

    for t in range(len(energies)):
        if t % jInAutoCorr == 0 and t > 10 * jInAutoCorr:
            unCorrelatedEnergy.append(energies[t])
    mean = 0
    if len(unCorrelatedAbsoluteMagnetization) != 0:
        mean = numpy.mean(unCorrelatedAbsoluteMagnetization)
    else:
        mean = math.fabs(initMagn)
    energyMean = 0
    if len(unCorrelatedEnergy) != 0:
        energyMean = numpy.mean(unCorrelatedEnergy)
    else:
        energyMean = energy
    # we return normalize magnetization sigma(i,j)/L^2
    print("Final Sigma:\n")
    print(initial)
    return initial, mean, energyMean, numpy.mean(spatialFunctionNorms), numpy.var(unCorrelatedEnergy), -numpy.var(
        unCorrelatedAbsoluteMagnetization)


if __name__ == "__main__":
    j = 1
    kb = 1
    size = 10
    flag = False
    magVersusTemp = {}
    energyVersusTemp = {}
    spatialCorrelationFunctionVersusTemp = {}
    temperature = 20
    temp = numpy.random.choice([0], size=(size, size))
    temperatures = []
    heatCapacities = {}
    susceptibilities = {}
    while (temperature > 0.1):
        beta = (1.0000000 / temperature)
        temp, mag, meanOfEnergy, spatialCorrelation, heatCapacity, susceptibility = metropolisAlgForIsingModel(size,
                                                                                                               beta,
                                                                                                               flag,
                                                                                                               temp, j)
        heatCapacities[beta] = (heatCapacity / (temperature ** 2))
        susceptibilities[beta] = math.fabs(susceptibility)
        magVersusTemp[beta] = mag
        energyVersusTemp[beta] = meanOfEnergy
        spatialCorrelationFunctionVersusTemp[beta] = spatialCorrelation
        print("For T=", temperature, " Magn =", mag)
        print("For B=", beta, ' Spatial Correlation= ', spatialCorrelation)
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

    spatialCorrelationAxis = list(spatialCorrelationFunctionVersusTemp.values())
    pylab.xlabel('B')
    pylab.ylabel('Kisi(J)')
    pylab.plot(temperatureInverseAxis, spatialCorrelationAxis, '.', color='b')
    pylab.show()
    maxKisi = numpy.nanmax(numpy.array(spatialCorrelationAxis))
    print("Critical kisi: ", maxKisi, "\n")

    index = spatialCorrelationAxis.index(maxKisi)
    criticalTemperature = temperatureInverseAxis.__getitem__(index)
    print("Critical Temperature ", 1 / criticalTemperature)

    tMinusTc=criticalTemperature-2.26918531421
    heatCapacityAxis = list(heatCapacities.values())
    pylab.xlabel('B')
    pylab.ylabel('C')
    pylab.plot(temperatureInverseAxis, heatCapacityAxis, '.', color='r')
    pylab.show()

    susceptibilityAxis = list(susceptibilities.values())
    pylab.xlabel('B')
    pylab.ylabel('X')
    pylab.plot(temperatureInverseAxis, susceptibilityAxis, '.', color='b')
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
