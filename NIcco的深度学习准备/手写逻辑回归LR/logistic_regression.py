# 逻辑回归logistics regression代码
from math import exp
import numpy as np


def loadDataSet():
    dataMat = []
    labelMat = []
    fr = open('testSet.txt')  ##打开文本
    for line in fr.readlines():  ##逐行读取，每行前两个值为X1和X2，第三个值是数据对应的标签，将X0的值设置为1
        lineArr = line.strip().split()
        dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])
        labelMat.append(int(lineArr[2]))


def sigmoid(inX):  # 定义sigmoid函数
    return 1.0 / (1 + exp(-inX))


def gradAscent(dataMatIn, classLabels):
    dataMatrix = np.asmatrix(dataMatIn)
    labelMat = np.asmatrix(classLabels).transpose()  # 这两行不用太在意，和算法没关系就是格式转换而已
    # labelMat是0-1标签值，dataMatrix是特征矩阵
    m, n = np.shape(dataMatrix)

    alpha = 0.001  # 学习率，用于调整梯度下降的步幅

    maxCycles = 500  # 最大迭代次数，因为这里直接使用的是批梯度下降法（BGD），所以这里的迭代次数
    # 就是使用全部数据计算全部样本的损失函数的值的并进行统一的梯度更新 这个过程重复多少次

    weights = np.ones((n, 1))  # 权重和偏置统一放在一起变成一个大权重，这样计算方便的多
    # 这里使用的是全1初始化，lr对于初始化并不敏感

    for k in range(maxCycles):
        h = sigmoid(dataMatrix * weights)  #
        error = h - labelMat  # 这句就是根据上面求的梯度更新量的那个公式得到的
        weights = weights - alpha * dataMatrix.transpose() * error  # 因为是梯度下降所以每次都是减去
    # 相应的梯度更新量，这里就是根据前面求解出来的公式得到梯度更新量 的表达式
    return weights