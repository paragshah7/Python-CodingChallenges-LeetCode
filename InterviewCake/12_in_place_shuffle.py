"""
https://www.interviewcake.com/question/python3/shuffle?course=fc1&section=greedy
In place shuffle of items in a list with same probability

O(n) time and O(1) space
"""

import random

def get_random(floor, ceiling):
    return random.randrange(floor, ceiling + 1)

def shuffle(the_list):
    if len(the_list) <= 1:
        return the_list

    last_index = len(the_list) - 1
    for i in range(0, last_index):
        random_i = get_random(i, last_index)  # pass i instead of 0 is crucial, this make sure its even probability
        print(random_i)

        if random_i != i:
            the_list[i], the_list[random_i] = the_list[random_i], the_list[i]

    print(the_list)


shuffle([1, 2, 3, 4, 5])
