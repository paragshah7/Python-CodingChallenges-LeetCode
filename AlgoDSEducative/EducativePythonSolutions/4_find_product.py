def find_product(lst):
    """
    Do not use division
    """

    prod = 1
    lst1 = [1]
    for num in lst[:-1]:
        prod = prod*num
        lst1.append(prod)
    print(lst1)

    prod = 1
    lst2 = [1] * len(lst1)
    for i in range(len(lst1)-1, -1, -1):
        print(i)
        lst2[i] = lst1[i] * prod
        prod = prod * lst[i]
        print(lst2)


arr = [1, 2, 3, 4, 5]
print(find_product(arr))