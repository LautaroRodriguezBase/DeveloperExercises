#Python 3.9.6

import random

def CreateDicList():

    dicList = [None] * 10

    for i in range(0, len(dicList)):

        dicList[i] = {'id':i+1, 'age': random.randint(1, 100)}

    return dicList

def SortList():

    sortDicList = CreateDicList()
    ageList = [None]*10

    for i in range(0, len(sortDicList)):

        ageList[i] = sortDicList[i]['age']

    ageList.sort(reverse=False)

    for age in ageList:

        for i in range(0, len(ageList)):

            if sortDicList[i]['age'] == age:

                x = 0
                sortDicList.insert(x, sortDicList[i])
                ++x
                sortDicList.pop(i+1)

    return sortDicList

def main():

    print(SortList())

main()