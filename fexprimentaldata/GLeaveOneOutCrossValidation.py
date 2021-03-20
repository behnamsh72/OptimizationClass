# Let D be the original data set

def leavingOneOutCrossValidation(D):
    testResults = []
    for i in range(len(D)):
        training = D[:].pop(i)
        model = buildModel(training)
        testResults.append(test(model, D[i]))
    return testResults
