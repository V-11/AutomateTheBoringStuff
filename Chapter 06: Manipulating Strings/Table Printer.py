def PrintTable(InputList):
    NumberOfLists = len(InputList)
    NumberOfElementsInList = len(InputList[0])
    MaxElementLength = []

    for list in InputList:
        MaxElement = 0
        for Element in list:
            if len(Element) > MaxElement:
                MaxElement = len(Element)
        MaxElementLength.append(MaxElement)

    for i in range(NumberOfElementsInList):
        for j in range(NumberOfLists):
            print(InputList[j][i].ljust(MaxElementLength[j]), end=' ')
        print('')

DataTable = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]

PrintTable(DataTable)
