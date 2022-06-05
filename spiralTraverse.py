def myRange(num1, num2, inc=1):
    nums = []

    if inc > 0:
        for i in range(num1, num2 + 1, inc):
            nums.append(i)
    else:
        for i in range(num1, num2 - 1, inc):
            nums.append(i)
    return nums


def spiralTraverse(array):
    spiralNums = []
    startRow = 0
    endRow = len(array) - 1
    startColumn = 0
    endColumn = len(array[0]) - 1

    while startRow <= endRow and startColumn <= endColumn:
        for col in myRange(startColumn, endColumn):
            spiralNums.append(array[startRow][col])
        for row in myRange(startRow + 1, endRow):
            spiralNums.append(array[row][endColumn])
        for col in myRange(endColumn - 1, startColumn, -1):
            if startRow == endRow:
                break
            spiralNums.append(array[endRow][col])
        for row in myRange(endRow - 1, startRow + 1, -1):
            if startColumn == endColumn:
                break
            spiralNums.append(array[row][startColumn])

        startRow += 1
        startColumn += 1
        endColumn -= 1
        endRow -= 1

    return spiralNums
