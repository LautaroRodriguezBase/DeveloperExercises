#Python 3.9.6

import random

lenList = 10

def CreateDicList():

    dicList = [None] * lenList

    for i in range(0, lenList):

        dicList[i] = {'id':i+1, 'age': random.randint(1, 100)}

    return dicList

def SortList(dicList):

    idMayMen = """
Id de la persona mayor: {}
Id de la persona menor: {}
"""
    sortDicList = dicList
    ageList = [None] * lenList

    for i in range(0, lenList):

        ageList[i] = sortDicList[i]['age']

    ageList.sort(reverse=False)

    for age in ageList:

        for i in range(0, lenList):

            if sortDicList[i]['age'] == age:

                x = 0
                sortDicList.insert(x, sortDicList[i])
                ++x
                sortDicList.pop(i+1)

    print(idMayMen.format(sortDicList[0]['id'], sortDicList[9]['id']))
    return sortDicList

def main():

    print(SortList(CreateDicList()))

main()