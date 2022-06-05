def getDepthAndArrays(array, depthAndArrays, depth):

    subArray = []
    for elem in array:
        if type(elem) is list:
            getDepthAndArrays(elem, depthAndArrays, depth + 1)
        else:
            subArray.append(elem)

    if depth in depthAndArrays:
        depthAndArrays[depth].append(subArray)
    else:
        depthAndArrays[depth] = [subArray]

    return depthAndArrays


def productSum(array):
    depthAndArrays = getDepthAndArrays(array, {}, 1)

    runningSum = 0
    for depth, arrays in depthAndArrays.items():
        for array in arrays:
            runningSum += sum(array) * depth

    return runningSum


productSum([5, 2, [7, -1], 3, [6, [-13, 8], 4]])
