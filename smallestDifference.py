

def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    idx1 = 0
    idx2 = 0
    runningSmallest = float('inf')
    smallest = float('inf')
    smallestNums = [0, 0]

    while idx1 < len(arrayOne) and idx2 < len(arrayTwo):
        if arrayOne[idx1] < arrayTwo[idx2]:
            runningSmallest = arrayTwo[idx2] - arrayOne[idx1]
            idx1 += 1
        elif arrayOne[idx1] > arrayTwo[idx2]:
            runningSmallest = arrayOne[idx1] - arrayTwo[idx2]
            idx2 += 1
        else:
            return [arrayOne[idx1], arrayTwo[idx2]]

        if runningSmallest < smallest:
            smallestNums = [arrayOne[idx1], arrayTwo[idx2]]
            smallest = runningSmallest

    return smallestNums


arrayOne = [-1, 5, 10, 20, 28, 3]
arrayTwo = [26, 134, 135, 15, 17]

smallestDifference(arrayOne, arrayTwo)
