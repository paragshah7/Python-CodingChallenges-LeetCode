"""
https://www.interviewcake.com/question/python3/merge-sorted-arrays?course=fc1&section=array-and-string-manipulation
my_list     = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]

# Prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
print(merge_lists(my_list, alices_list))
"""
from icecream import ic as print

def merge_lists(my_list: list, alices_list: list) -> list:
    merged_list = []
    i = 0
    j = 0

    for counter in range(len(my_list)+len(alices_list) - 1):
        print(my_list[i], alices_list[j])

        if my_list[i] < alices_list[j]:
            merged_list.append(my_list[i])
            i += 1
        else:
            merged_list.append(alices_list[j])
            j += 1
        counter += 1
        print(merged_list, counter)

    # For the last element (and up for loop counter is len + len - 1)
    if i == len(my_list):
        merged_list.append(alices_list[j])
    elif j == len(alices_list):
        merged_list.append(my_list[i])

    return merged_list


my_list = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]
print(merge_lists(my_list, alices_list))
