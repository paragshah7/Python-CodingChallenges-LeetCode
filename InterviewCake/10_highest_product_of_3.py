"""
https://www.interviewcake.com/question/python3/highest-product-of-3?course=fc1&section=greedy
Given a list of integers, find the highest product you can get from three of the integers.

The input list_of_ints will always have at least three integers.
"""

from icecream import ic as print

def highest_product(list_of_ints):

    if len(list_of_ints) < 3:
        raise ValueError('Less than 3 items!')

    max = list_of_ints[0]
    max_2 = list_of_ints[0] * list_of_ints[1]
    max_3 = list_of_ints[0] * list_of_ints[1] * list_of_ints[2]
    prev_max = max
    prev_max_2 = max_2

    for i in range(1, len(list_of_ints)):

        # Calculate all maxes
        num = list_of_ints[i]
        if num > max:
            max = num

        product_2 = num * prev_max
        if product_2 > max_2:
            max_2 = product_2
        # print(max_2, prev_max, list_of_ints[i])

        product_3 = num * prev_max_2
        if product_3 > max_3:
            max_3 = product_3
        # print(max_3, prev_max_2, list_of_ints[i])

        # Storing
        prev_max = max
        prev_max_2 = max_2

    return max_3


# Basic logic is finding max and max_2 and storing in prev_max and prev_max_2
list_of_ints = [19, 5, 2, 9, 1, 45, 3, 100]
print(highest_product(list_of_ints))
