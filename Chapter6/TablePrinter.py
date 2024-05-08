# Write a function named printTable() that takes a list of lists of strings 
# and displays it in a well-organized table with each column right-justified. 
# Assume that all the inner lists will contain the same number of strings.

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def printTable(data):

    sortedItems = []

    colWidths = [0] * len(data)
    for x in range(len(data)):
        colWidths[x] = len(max(data[x], key=len))

    for x in range(len(data[0])):
        temp = []
        for y in range(len(data)):
            temp.append(data[y][x].rjust(colWidths[y]))
        sortedItems.append(temp)

    for x in range(len(sortedItems)):
        print(' '.join(sortedItems[x]))


printTable(tableData)