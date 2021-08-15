list1 = [1, 3, 4, 5]
list2 = [2, 6, 7, 8]

def merge_lists(lst1, lst2):
    newList = []
    total_length = len(lst1) + len(lst2)
    i, j = 0, 0
    while len(newList) < total_length:
        if i == len(lst1):
            newList.extend(lst2[j:])
        elif j == len(lst2):
            newList.extend(lst1[i:])
        elif lst1[i] <= lst2[j]:
            newList.append(lst1[i])
            i += 1
        elif lst1[i] > lst2[j]:
            newList.append(lst2[j])
            j += 1
    return newList


print(merge_lists(list1, list2))
