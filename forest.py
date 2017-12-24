#!/usr/bin/python
import sys

values = []  # list like arraylist
listMap = {}  #dictionary like hashmap
def readValues():
    try:
        for i in range(1,1000):
            tmpList = list(map(int, input().strip().split(' ')))
           # values.append(tmpList[0])
           # values.append(tmpList[1])
            listMap.update({tmpList[0]:tmpList[1]})
    except EOFError:
        print('Read is finish! ')
       # pass
    except Exception:
      # print('Error Detected, No Reading!')
        raise
def findChildCount(parent):
    count = 0
    for indx, val in listMap.items():
        if val == parent:
            count += 1
    return count
def findChildList(parent):  # find child list of nodes 
    list = []
    for indx, val in listMap.items():
        if val == parent:
            list.append(indx)
    return list        
def findParentCount(child):
    count = 1
    parent = listMap[child]
    while(val > 1) :
        parent = listMap[parent]
        count += 1
    return count

def findParentList(child):
    list = [1]
    val = listMap[child]
    while(val > 1) :
        list.append(val)
        val = listMap[val]
    return list

def findChildConnComp(parent):  # find all children
    childs = []
    childs = findChildList(parent)
    for k, childVal in enumerate(childs):
        for indx, val in listMap.items():
            if childVal == val:
                childs.append(indx)
    return childs 
def findChildFast(list):  # find all fastlist that cleavable node
    #tmpList[indx] = 0
    tmpList2 = list
    fastList = []
    for indx2, val2 in tmpList2.items():
            if len(findChildConnComp(indx2))%2 == 0:
                tmpList2[indx2] = val2
               # print(indx2)
            else:
                fastList.append(indx2)
    return fastList
def calculateForest(list):
   # print(list)
    max = 0
    tmpList = list
    print(len(findChildFast(listMap)))        
            
    return 0

readValues()
calculateForest(listMap)
