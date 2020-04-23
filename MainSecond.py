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
import os

def ReadMyCsv(SaveList, fileName):
    csv_reader = csv.reader(open(fileName))
    for row in csv_reader:
        SaveList.append(row)
    return

def StorFile(data, fileName):
    with open(fileName, "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)
    return

from SecondRandomShuffle.AssociationMatrixRandomList import MyAssociationMatrixRandomList
MyAssociationMatrix, RandomListGroup = MyAssociationMatrixRandomList()

from SecondRandomShuffle.PositiveSample import MyPositiveSample
PositiveSample = MyPositiveSample()

from SecondRandomShuffle.NegativeSample import MyNegativeSample
NegativeSample = MyNegativeSample()

from SecondRandomShuffle.Segmentation import MySegmentation
Segmentation = MySegmentation()

# for i in range(5):
#     os.system("python -m openne --method gcn --input TrainName" + i +".txt --graph-format edgelist --output tr" + i + ".txt --epochs 50")