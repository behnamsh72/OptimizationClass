import numpy


def calculateAutoCorrelation(sequences, j):
    sequencesPlusJ = []
    for m in range(len(sequences) - j):
        sequencesPlusJ.append(sequences[m + j])
    sequencesTimesSequencesPlusJ = []
    for k in range(len(sequencesPlusJ)):
        sequencesTimesSequencesPlusJ.append(sequences[k] * sequencesPlusJ[k])
    SequencePow2 = []
    for s in range(len(sequences)):
        SequencePow2.append(sequences[s] * sequences[s])

    autoCorrelation = ((numpy.mean(sequencesTimesSequencesPlusJ)) - (
            numpy.mean(sequences) * numpy.mean(sequencesPlusJ))) / (
                              numpy.mean(SequencePow2) - numpy.mean(sequences) ** 2)

    return autoCorrelation
