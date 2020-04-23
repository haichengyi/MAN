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

def MyNodeEdgeAttributeGenerate():
    # 数据: 18 种 association
    # M: mRNA;  Mi: MiRNA;  Di: Disease;    Dr: Drug;
    # P: Protein;   L: LncRNA;  Microbe: Microbe；   Ci: CircRNA;
    AllEdge = []
    for association in ["LncDiseaseMergeAssociation", "LncMLncRNA2TargetAssociation",
                        "LncMiSNPAssociation", "LncProteinNPInterAssociation",
                        "MiDiseaseCuiAssociation", "MiProteinMergeAssociation",
                        "MiDrugSM2Association", "MiMNMiTarbaseAssociation",
                        "CircDiseaseMergeAssociation",
                        "CircMiSomamiRAssociation", "DiseaseMDisGeNETAssociation",
                        "DiseaseMicrobeHMDADAssociation", "DrugDiseaseSCMFDDAssociation",
                        "DrugMicrobeAssociation","DrugMPharmGKBAssociation","MProteinNCBIAssociation",
                        "DrugProteinDrugBankAssociationThreshold5", "PPI"]:
        association_temp = []
        ReadMyCsv(association_temp, "FirstAllNodeEdge/" + association + ".csv")
        AllEdge.extend(association_temp)

    print(len(AllEdge))
    print(AllEdge[0])
    StorFile(AllEdge, 'FirstAllNodeEdge/AllEdge.csv')

    # 属性特征 Attribute
    AllNode = []
    AllNodeAttribute = []
    for Attribute in ["AllCircKmer", "AllDiseaseFeatureDAGLocal", "AllDrugFeature", "AllLncKmer",
                      "AllMicrobeFeatureDAGLocal", "AllMiKmer", "AllMKmer", "AllProteinKmer"]:
        attribute_temp = []
        ReadMyCsv(attribute_temp, "FirstAllNodeEdge/"+ str(Attribute) + ".csv")

        AllNodeAttribute.extend(attribute_temp)

        Node = np.array(attribute_temp)[:, 0]
        AllNode.extend(Node)

        print("attribute[0]: ", attribute_temp[0])

    print('len(AllNode)', len(AllNode))
    counter = 0
    while counter < len(AllNode):
        pair = []
        pair.append(AllNode[counter])
        AllNode[counter] = pair
        counter = counter + 1
    print(AllNode[0])

    StorFile(AllNode, "FirstAllNodeEdge/AllNode.csv")
    StorFile(AllNodeAttribute, 'FirstAllNodeEdge/AllNodeAttribute.csv')
    print(np.array(AllNodeAttribute).shape)

    return AllNode, AllEdge, AllNodeAttribute
