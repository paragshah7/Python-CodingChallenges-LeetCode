"""
Iterate over
[1, [2, 3], 4, [[5,6]], 7]
"""
import time

lst = [1, [2, 3, [5,[9,[10]]]], 4, [2, 3, [5,6]], 7]

def list_iterative(lst):
    op_lst = []
    for l in lst:
        l_type = type(l)
        in_lst = l

        while l_type == list:
            for i in in_lst:
                if type(i) != int:
                    l_type = type(in_lst)
                    in_lst = i
                elif type(i) == int:
                    op_lst.append(i)
                    l_type = int
        if type(l) == int:
            op_lst.append(l)
    return op_lst


lst_2 = [1, [2, 3, [5,[9,[10]]]], 4, [2, 3, [5,6]], 7]
len_lst = len(lst_2)

def list_recur(lst_2, len_lst):
    i = 0

    if type(lst_2[0]) == int:
        print(lst_2[i], end=', ')

    list_recur(lst_2[i+1], len_lst-1)


list_recur(lst_2, len_lst)

# print(list_iterative(lst))
