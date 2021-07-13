import sklearn.linear_model
import pylab, random

# set line width
pylab.rcParams['lines.linewidth'] = 4
# set font size for titles
pylab.rcParams['axes.titlesize'] = 20
# set font size for labels on axes
pylab.rcParams['axes.labelsize'] = 20
# set size of numbers on x-axis
pylab.rcParams['xtick.labelsize'] = 16
# set size of numbers on y-axis
pylab.rcParams['ytick.labelsize'] = 16
# set size of ticks on x-axis
pylab.rcParams['xtick.major.size'] = 7
# set size of ticks on y-axis
pylab.rcParams['ytick.major.size'] = 7
# set size of markers
pylab.rcParams['lines.markersize'] = 10
# set number of examples shown in legends
pylab.rcParams['legend.numpoints'] = 1


def getTitanicData(fname):
    data = {}
    data['class'], data['survived'], data['age'] = [], [], []
    data['gender'], data['name'] = [], []
    f = open(fname)
    line = f.readline()
    while line != '':
        split = line.split(',')
        data['class'].append(int(split[0]))
        data['age'].append(float(split[1]))
        if split[2] == 'M':
            data['gender'].append(1)
        else:
            data['gender'].append(0)
        if split[3] == '1':
            data['survived'].append('Survived')
        else:
            data['survived'].append('Died')
        data['name'].append(split[4:])
        line = f.readline()
    return data


def buildTitanicExamples(fileName):
    data = getTitanicData(fileName)
    examples = []
    for i in range(len(data['class'])):
        p = Passenger(data['class'][i], data['age'][i],
                      data['gender'][i], data['survived'][i],
                      data['name'][i])
        examples.append(p)
    print('Finishe processing', len(examples), 'passengers\n')
    return examples


def accuracy(truePos, falsePos, trueNeg, falseNeg):
    numerator = truePos + trueNeg
    denominator = truePos + trueNeg + falsePos + falseNeg
    return numerator / denominator


def sensitivity(truePos, falseNeg):
    try:
        return truePos / (truePos + falseNeg)
    except ZeroDivisionError:
        return float('nan')


def specificity(trueNeg, falsePos):
    try:
        return trueNeg / (trueNeg + falsePos)
    except ZeroDivisionError:
        return float('nan')


def posPredVal(truePos, falsePos):
    try:
        return truePos / (truePos + falsePos)
    except ZeroDivisionError:
        return float('nan')


def negPredVal(trueNeg, falseNeg):
    try:
        return trueNeg / (trueNeg + falseNeg)
    except ZeroDivisionError:
        return float('nan')


def getStats(truePos, falsePos, trueNeg, falseNeg, toPrint=True):
    accur = accuracy(truePos, falsePos, trueNeg, falseNeg)
    sens = sensitivity(truePos, falseNeg)
    spec = specificity(trueNeg, falsePos)
    ppv = posPredVal(truePos, falsePos)
    if toPrint:
        print(' Accuracy =', round(accur, 3))
        print(' Sensitivity =', round(sens, 3))
        print(' Specificity =', round(spec, 3))
        print(' Pos. Pred. Val. =', round(ppv, 3))
    return (accur, sens, spec, ppv)


def leaveOneOut(examples, method, toPrint=True):
    truePos, falsePos, trueNeg, falseNeg = 0, 0, 0, 0
    for i in range(len(examples)):
        testCase = examples[i]
        trainingData = examples[0:i] + examples[i + 1:]
        results = method(trainingData, [testCase])
        truePos += results[0]
        falsePos += results[1]
        trueNeg += results[2]
        falseNeg += results[3]
    if toPrint:
        getStats(truePos, falsePos, trueNeg, falseNeg)
    return truePos, falsePos, trueNeg, falseNeg



def minkowskiDist(v1, v2, p):
    """Assumes v1 and v2 are equal-length arrays of numbers
       Returns Minkowski distance of order p between v1 and v2"""
    dist = 0.0
    for i in range(len(v1)):
        dist += abs(v1[i] - v2[i]) ** p
    return dist ** (1 / p)


class Passenger(object):
    featureNames = ('C1', 'C2', 'C3', 'age', 'male gender')

    def __init__(self, pClass, age, gender, survived, name):
        self.name = name
        self.featureVec = [0, 0, 0, age, gender]
        self.featureVec[pClass - 1] = 1
        self.label = survived
        self.cabinClass = pClass

    def distance(self, other):
        return minkowskiDist(self.featureVec, other.featureVec, 2)

    def getClass(self):
        return self.cabinClass

    def getAge(self):
        return self.featureVec[3]

    def getGender(self):
        return self.featureVec[4]

    def getName(self):
        return self.name

    def getFeatures(self):
        return self.featureVec[:]

    def getLabel(self):
        return self.label




def split80_20(examples):
    sampleIndices = random.sample(range(len(examples)),
                                  len(examples) // 5)
    trainingSet, testSet = [], []
    for i in range(len(examples)):
        if i in sampleIndices:
            testSet.append(examples[i])
        else:
            trainingSet.append(examples[i])
    return trainingSet, testSet


def randomSplits(examples, method, numSplits, toPrint=True):
    truePos, falsePos, trueNeg, falseNeg = 0, 0, 0, 0
    random.seed(0)
    for t in range(numSplits):
        trainingSet, testSet = split80_20(examples)
        results = method(trainingSet, testSet)
        truePos += results[0]
        falsePos += results[1]
        trueNeg += results[2]
        falseNeg += results[3]
    getStats(truePos / numSplits, falsePos / numSplits,
             trueNeg / numSplits, falseNeg / numSplits, toPrint)
    return truePos / numSplits, falsePos / numSplits, \
           trueNeg / numSplits, falseNeg / numSplits


def buildModel(examples, toPrint=True):
    featureVecs, labels = [], []
    for e in examples:
        featureVecs.append(e.getFeatures())
        labels.append(e.getLabel())
    LogisticRegression = sklearn.linear_model.LogisticRegression
    model = LogisticRegression().fit(featureVecs, labels)
    if toPrint:
        print('model.classes_ =', model.classes_)
        for i in range(len(model.coef_)):
            print('For label', model.classes_[1])
            for j in range(len(model.coef_[0])):
                print('   ', Passenger.featureNames[j], '=',
                      model.coef_[0][j])
    return model


##list comprehension
def listComprehensionExample():
    L = [x * x for x in range(10)]
    print(L)
    L = [x * x for x in range(10) if x % 2 == 0]
    print(L)


def applyModel(model, testSet, label, prob=0.5):
    testFeatureVecs = [e.getFeatures() for e in testSet]
    probs = model.predict_proba(testFeatureVecs)
    truePos, falsePos, trueNeg, falseNeg = 0, 0, 0, 0
    for i in range(len(probs)):
        if probs[i][1] > prob:
            if testSet[i].getLabel() == label:
                truePos += 1
            else:
                falsePos += 1
        else:
            if testSet[i].getLabel() != label:
                trueNeg += 1
            else:
                falseNeg += 1
    return truePos, falsePos, trueNeg, falseNeg


def lr(trainingData, testData, prob=0.5):
    model = buildModel(trainingData, False)
    results = applyModel(model, testData, 'Survived', prob)
    return results

def buildROC(trainingSet, testSet, title, plot = True):
    model = buildModel(trainingSet, True)
    xVals, yVals = [], []
    p = 0.0
    while p <= 1.0:
        truePos, falsePos, trueNeg, falseNeg =\
                               applyModel(model, testSet,
                               'Survived', p)
        xVals.append(1.0 - specificity(trueNeg, falsePos))
        yVals.append(sensitivity(truePos, falseNeg))
        p += 0.01
    # auroc = sklearn.metrics.auc(xVals, yVals, True)
    auroc = sklearn.metrics.auc(xVals, yVals)

    if plot:
        pylab.plot(xVals, yVals)
        pylab.plot([0,1], [0,1])
        title = title + '\nAUROC = ' + str(round(auroc,3))
        pylab.title(title)
        pylab.xlabel('1 - specificity')
        pylab.ylabel('Sensitivity')
        pylab.show()
    return auroc


if __name__ == "__main__":
    # listComprehensionExample()
    examples = buildTitanicExamples('TitanicPassengers.txt')
    random.seed(0)
    numSplits = 10
    print('Average of', numSplits, '80/20 splits LR')
    truePos, falsePos, trueNeg, falseNeg = \
        randomSplits(examples, lr, numSplits)

    print('Average of LOO testing using LR')
    truePos, falsePos, trueNeg, falseNeg = \
        leaveOneOut(examples, lr)

    # Look at weights
    trainingSet, testSet = split80_20(examples)
    model = buildModel(trainingSet, True)

    #Look at changing prob
    random.seed(0)
    trainingSet, testSet = split80_20(examples)
    model = buildModel(trainingSet, False)
    print('Try p = 0.1')
    truePos, falsePos, trueNeg, falseNeg =\
                      applyModel(model, testSet, 'Survived', 0.1)
    getStats(truePos, falsePos, trueNeg, falseNeg)
    print('Try p = 0.9')
    truePos, falsePos, trueNeg, falseNeg =\
                      applyModel(model, testSet, 'Survived', 0.9)
    getStats(truePos, falsePos, trueNeg, falseNeg)

    random.seed(0)
    trainingSet, testSet = split80_20(examples)
    buildROC(trainingSet, testSet, 'ROC for Predicting Survival, 1 Split')