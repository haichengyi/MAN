from numpy import *
import numpy as np
import random
import math
import os
import time
import pandas as pd
import csv
import math
import random
import copy

# 定义函数
def ReadMyCsv(SaveList, fileName):
    csv_reader = csv.reader(open(fileName))
    for row in csv_reader:  # 把每个rna疾病对加入OriginalData，注意表头
        SaveList.append(row)
    return

def ReadMyCsv2(SaveList, fileName):
    csv_reader = csv.reader(open(fileName))
    for row in csv_reader:
        counter = 0
        while counter < len(row):
            row[counter] = int(row[counter])      # 转换数据类型
            counter = counter + 1
        SaveList.append(row)
    return

def StorFile(data, fileName):
    with open(fileName, "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)
    return

AllNode = []
ReadMyCsv(AllNode, 'AllNode.csv')

FinalDrugFeatureNum = []
ReadMyCsv(FinalDrugFeatureNum, 'FinalMiKmerNum.csv')

FinalDiseaseFeatureNum = []
ReadMyCsv(FinalDiseaseFeatureNum, 'FinalDiseaseFeatureNum.csv')

testbreastNum = []
testbreastNum1 = []
ReadMyCsv(testbreastNum, 'MDCuiMiDiseaseNum.csv')
ReadMyCsv(testbreastNum1,'NegativeSample.csv')
testbreastNum.extend(testbreastNum1)
# StorFile(testbreastNum,'testbreastNum.csv')


#查看vec_all0.txt文件内容  自测
#LineEmbeddingName1 = 'vec_all.txt'
#LineEmbedding1 = np.loadtxt(LineEmbeddingName1, dtype=str, skiprows=1)
#StorFile(LineEmbedding1, 'LineEmbedding1.csv')

test_attribute = []
test_attribute_manner = []
test_manner = []
test_1 = []
test_2 = []
test_3 = []
test_4 = []


# 生成AllNodeManner
counterP = 0
while counterP < 1:
    #LineEmbeddingName = 'vec_all' + str(counterP) + '.txt'
    LineEmbedding = np.loadtxt('vec_all.txt', dtype=str, skiprows=1)
    #StorFile(LineEmbedding, 'LineEmbedding1.csv')

    # manner
    AllNodeMannerNum = []
    counter = 0
    while counter < len(AllNode):
        pair = []
        counter1 = 0
        while counter1 < len(LineEmbedding[0]) - 1:        # 如果节点孤立，则Feature全为0
            pair.append(0)
            counter1 = counter1 + 1
        AllNodeMannerNum.append(pair)
        counter = counter + 1

    # manner
    counter = 0
    while counter < len(LineEmbedding):
        num = int(LineEmbedding[counter][0])
        AllNodeMannerNum[num] = list(LineEmbedding[counter][1:])
        counter = counter + 1

    print(np.array(AllNodeMannerNum).shape)
    #AllNodeMannerNumName = 'AllNodeMannerNum' + str(counterP) + '.csv'
    # StorFile(AllNodeMannerNum, 'ALL_manner.csv')


    number_1 = []
    counter_1 = 0
    while counter_1 < len(testbreastNum):
        counter_2 = 0
        while counter_2 < len(LineEmbedding):
            if testbreastNum[counter_1][0] == LineEmbedding[counter_2][0]:
                test_1.append(LineEmbedding[counter_2][1:])
            counter_2 = counter_2+1
        counter_1 = counter_1+1
        print(counter_1)

    # StorFile(test_1, 'test_1.csv')

    counter_1 = 0

    while counter_1 < len(testbreastNum):
        counter_2 = 0
        while counter_2 < len(FinalDiseaseFeatureNum):
            if testbreastNum[counter_1][0] == FinalDiseaseFeatureNum[counter_2][0]:
                number_1 = counter_2
                test_2.append(FinalDiseaseFeatureNum[counter_2][1:])
            counter_2 = counter_2 + 1
        counter_1 = counter_1 + 1
        print(counter_1)
    # StorFile(test_2, 'test_2.csv')

    counter_1 = 0

    while counter_1 < len(testbreastNum):
        counter_2 = 0
        while counter_2 < len(LineEmbedding):
            if testbreastNum[counter_1][1] == LineEmbedding[counter_2][0]:
                number_1 = counter_2
                test_3.append(LineEmbedding[number_1][1:])
            counter_2 = counter_2 + 1
        counter_1 = counter_1 + 1
        print(counter_1)

    # StorFile(test_3, 'test_3.csv')

    counter_1 = 0

    while counter_1 < len(testbreastNum):
        counter_2 = 0
        while counter_2 < len(FinalDrugFeatureNum):
            if testbreastNum[counter_1][1] == FinalDrugFeatureNum[counter_2][0]:
                number_1 = counter_2
                test_4.append(FinalDrugFeatureNum[counter_2][1:])
            counter_2 = counter_2 + 1
        counter_1 = counter_1 + 1
        print(counter_1)

    # StorFile(test_4, 'test_4.csv')

    # test_attribute=c = np.hstack((test_2,test_4))
    #StorFile(test_attribute,'test_attribute.csv')

    # test_manner = np.hstack((test_1,test_3))
    #StorFile(test_manner, 'test_manner.csv')

    test_attribute_manner = np.hstack((test_1,test_2,test_3,test_4))
    StorFile(test_attribute_manner, 'train_attribute_manner.csv')

    num1 = 0
    # 将lnc和disease的feature加入manner中，[manner,lnc/disease]
    counter = 0
    while counter < len(FinalDrugFeatureNum):
        AllNodeMannerNum[int(FinalDrugFeatureNum[counter][0])].extend(FinalDrugFeatureNum[counter][1:])
        num1 = num1 + 1
        counter = counter + 1
    print(num1)

    num2 = 0
    counter = 0
    while counter < len(FinalDiseaseFeatureNum):
        AllNodeMannerNum[int(FinalDiseaseFeatureNum[counter][0])].extend(FinalDiseaseFeatureNum[counter][1:])
        num2 = num2 + 1
        counter = counter + 1
    print(num2)

    print(np.array(AllNodeMannerNum).shape)
    #AllNodeFeatureNumName = 'AllNodeAttributeMannerNum' + str(counterP) + '.csv'
    # StorFile(AllNodeMannerNum, 'ALL_attribute+manner.csv')

    counterP = counterP + 1


