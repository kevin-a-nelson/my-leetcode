def moveElementToEnd(array, toMove):
    lastToMoveIdx = len(array) - 1

    for idx, num in enumerate(array):
        if num == toMove:
            while array[lastToMoveIdx] == toMove:
                lastToMoveIdx -= 1
            array[idx], array[lastToMoveIdx] = array[lastToMoveIdx], array[idx]

    return array


moveElementToEnd([2, 1, 2, 2, 2, 3, 4, 2], 2)
