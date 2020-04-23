import csv
import numpy as np
import pandas as pd
import os
def ReadMyCsv(SaveList, fileName):
    csv_reader = csv.reader(open(fileName))
    for row in csv_reader:          # 注意表头
        SaveList.append(row)
    return

def StorFile(data, fileName):
    with open(fileName, "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)
    return

# def StorTxt(data, fileName):
#     with open(fileName, "w", newline='') as txtfile:
#         for item in data:
#             txtfile.write(str(item) + "\n")
#     return

def save_txt(data, fileName):
    file = open(fileName, "a")
    for i in range(len(data)):
        s = str(data[i]).replace('[', '').replace(']', '')  # 去除[],这两行按数据不同，可以选择
        s = s.replace("'",'').replace(',','') + '\n'
        file.write(s)
    file.close()
    return

allAttribute = []
ReadMyCsv(allAttribute, 'AllNodeAttribute.csv')
# alllabels = []
# ReadMyCsv(alllabels, "allfeatures.csv")
for i in range(5):
    fileName = "TrainName" + str(i) + ".csv"
    outName = "TrainName" + str(i) + ".txt"
    outName2 = "TrainNode" + str(i) + ".txt"
    # NodeAttribute = "NodeFeature" + str(i) + ".csv"
    NodeAttribute2 = "NodeFeature" + str(i) + ".txt"
    # NodeLabels = "NodeLabel" + str(i) + ".csv"
    NodeLabels2 = "NodeLabel" + str(i) + ".txt"
    TrainLabel = []
    TrainAttribute = []
    temp_TrainName = []
    existName = []
    ReadMyCsv(temp_TrainName, fileName)

    save_txt(temp_TrainName, outName)

    # temp_TrainName = sorted(set(np.array(temp_TrainName).flatten()))
    # for index in temp_TrainName:
    #     existName.append([index])
    #     TrainAttribute.append(allAttribute[int(index)])
    #     TrainLabel.append(alllabels[int(index)])
    # print(existName)
    # StorFile(existName, outName)
    # save_txt(temp_TrainName, outName2)

    # print(np.shape(TrainAttribute))
    # print(np.shape(TrainLabel))

    # StorFile(TrainAttribute, NodeAttribute)
    # save_txt(TrainAttribute, NodeAttribute2)

    # StorFile(TrainLabel, NodeLabels)
    # save_txt(TrainLabel, NodeLabels2)
    # print(allAttribute[0])
for i in range (5):
    os.system("python -m openne --method node2vec --input TrainName"
              + str(i)
              +".txt --graph-format edgelist --output tr"
              + str(i) + ".txt --representation-size 64") # --number-walks 10 --walk-length 100 --p 4 --q 4
