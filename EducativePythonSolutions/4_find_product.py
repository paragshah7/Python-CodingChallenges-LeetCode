def find_product(lst):

    num = 1
    prod = []

    for i in range(len(lst)):
        j = len(lst) - 1
        while j != -1:
            if j == i:
                pass
            else:
                num = num * lst[j]
            j -= 1
        prod.append(num)
        num = 1
    return prod


arr = [1, 2, 3, 4]
print(find_product(arr))