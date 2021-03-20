# Let D be the original data set
# n be the number of random samples usually between 20% and 50%
# k  be number of trials

def repeatedRandomSampling(D):
    testResults = []
    for i in range(k):
        # randomly selected n elements for testSet,keep rest for training

        model = buildModel(training)
        testResults.append(test(model, testSet))

    return AverageTestResults
