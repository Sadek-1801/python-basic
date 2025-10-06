tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(tableData):
    # Calculate the width needed for each column
    colWidths = [0] * len(tableData)
    for i in range(len(tableData)):
        colWidths[i] = len(max(tableData[i]))
    
    # Print the table row by row
    for row in range(len(tableData[0])):  # Number of rows (items in each sublist)
        for col in range(len(tableData)):  # Number of columns (sublists)
            print(tableData[col][row].rjust(colWidths[col]), end=' ')
        print()  # New line after each row
    return

printTable(tableData)