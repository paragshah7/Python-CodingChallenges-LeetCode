def removeEven(List):
    newList = []
    for l in List:
        if l % 2 != 0:
            newList.append(l)
    return newList


# Pythonic solution - List comprehension
''' newList = [expression(i) for i in oldList if filter(i)] '''
def removeEven2(List):
    return [item for item in List if item % 2 != 0]


numbers = [-182, 174, -169, -38, 119, 47, -144, -111, 44, 161, 41, 83, 32,
           -64, 9, -27, -114, -168, 74, -9, -149, -130, 36, -171, 49, 12, 90, 152,
           -180, 186, -33, 23, 61, 160, -6, 67]
print(removeEven(numbers))
print(removeEven2(numbers))

