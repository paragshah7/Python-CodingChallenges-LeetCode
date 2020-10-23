def meanderingArray(unsorted):

    unsorted.sort(reverse=True)
    meanderedArray = []
    i = 0
    arrayLength = len(unsorted)

    while i < arrayLength // 2:
        meanderedArray.append(unsorted[i])
        meanderedArray.append(unsorted[-(i+1)])
        i += 1

    if arrayLength % 2 != 0:
        meanderedArray.append(unsorted[i])

    return meanderedArray


print(meanderingArray([5, 2, 7, 8, -2, 25, 25]))