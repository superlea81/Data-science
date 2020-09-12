import random
from math import log
import operator
import copy
import sys


def upload(filename):
    data = []
    with open(filename, 'r') as file:
        while True:
            lines = file.readline()
            if not lines:
                break
            if "".join(lines.split()) != "":
                tmp = [i for i in lines.split()]
            data.append(tmp)
    label = []
    for i in range(len(data[0])):
        label.append(data[0][i])
    data = data[1:]
    return data, label


def entropy(dataSet):
    totalNumber = len(dataSet)
    labelCount = {}
    for x in dataSet:
        curLabel = x[-1]
        if curLabel not in labelCount:
            labelCount[curLabel] = 0
        labelCount[curLabel] += 1
    shannonEnt = 0.0
    for k in labelCount:
        prob = labelCount[k] / totalNumber
        shannonEnt -= prob * log(prob, 2)
    return shannonEnt


def splitDataSet(dataSet, index, value):
    newDataSet = []
    for data in dataSet:
        if data[index] == value:
            newData = data[:index]
            newData.extend(data[index + 1:])
            newDataSet.append(newData)
    return newDataSet


def bestFeatureSplit(dataSet):
    numFeature = len(dataSet[0]) - 1  # total feature 4
    baseEnt = entropy(dataSet)
    bestInfoGain = 0.0
    bestFeatureIndex = -1  # the best gain info
    for i in range(numFeature):
        featureList = [d[i] for d in dataSet]  # split the feature
        uniqueFeature = set(featureList)
        ent = 0.0
        for j in uniqueFeature:
            subDataSet = splitDataSet(dataSet, i, j)
            weight = len(subDataSet) / len(dataSet)
            ent += (weight * entropy(subDataSet))
        infoGain = baseEnt - ent
        if infoGain >= bestInfoGain:
            bestInfoGain = infoGain
            bestFeatureIndex = i
    return bestFeatureIndex


def majorityVote(detailLabel):
    labelCount = {}
    for v in detailLabel:
        if v not in labelCount.keys():
            labelCount[v] = 0
        labelCount[v] += 1
    sortedLabelCount = sorted(labelCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedLabelCount[0][0]


def createTree(dataSet, label, maxDepth, curDepth):
    labelValue = [d[-1] for d in dataSet]
    if labelValue.count(labelValue[0]) == len(labelValue):
        return labelValue[0]

    if len(dataSet[0]) == 1 or len(label) == 0:
        return majorityVote(labelValue)
    if curDepth == maxDepth:
        return majorityVote(labelValue)

    bestFeatureIndex = bestFeatureSplit(dataSet)
    bestFeatureName = label[bestFeatureIndex]
    myTree = {bestFeatureName: {}}
    del (label[bestFeatureIndex])
    featureValue = [d[bestFeatureIndex] for d in dataSet]
    uniqueFeatureValue = set(featureValue)
    for value in uniqueFeatureValue:
        subLabel = label[:]
        myTree[bestFeatureName][value] = createTree(splitDataSet(dataSet, bestFeatureIndex, value),
                                                    subLabel, maxDepth, curDepth + 1)
    return myTree


def testTree(tree, label, testData):
    # get the root feature
    keyList = [key for key in tree.keys()]
    key = keyList[0]
    node = tree[key]
    labelIndex = label.index(key)
    feature = testData[labelIndex]
    value = node[feature]
    if isinstance(value, dict):
        res = testTree(value, label, testData)
    else:
        res = value
    return res


def accuracy(tree, testDataSet, label):
    count = 0
    for data in testDataSet:
        if data[-1] == testTree(tree, label, data):
            count += 1
    return count / len(testDataSet)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        dataSet, label = upload(filename)
        backLabel = copy.deepcopy(label)
        tree = createTree(dataSet, label, float("inf"), 0)
        res = accuracy(tree, dataSet, backLabel)
        print("The training set accuracy is:", res)

    if len(sys.argv) == 3:
        filename = sys.argv[1]
        depth = int(sys.argv[2])
        dataSet, label = upload(filename)
        backLabel = copy.deepcopy(label)
        tree = createTree(dataSet, label, depth, 0)
        res = accuracy(tree, dataSet, backLabel)
        print("The training set accuracy is:", res)
    
    if len(sys.argv) == 4:
        trainFilename = sys.argv[1]
        depth = int(sys.argv[2])
        testFilename = sys.argv[3]
        trainSet, trainLabel = upload(trainFilename)
        backLabel = copy.deepcopy(trainLabel)
        tree = createTree(trainSet, trainLabel, depth, 0)
        trainRes = accuracy(tree, trainSet, backLabel)
        print("The training set accuracy is:", trainRes)

        testSet, testLabel = upload(testFilename)
        testRes = accuracy(tree, testSet, backLabel)
        print("The testing set accuracy is:", testRes)

