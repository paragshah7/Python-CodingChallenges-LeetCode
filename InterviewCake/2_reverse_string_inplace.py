"""
Reverse list of chars in place
https://www.interviewcake.com/question/python3/reverse-string-in-place?course=fc1&section=array-and-string-manipulation
"""

# While loop solution
def reverse(list_of_chars):

    left_index  = 0
    right_index = len(list_of_chars) - 1

    while left_index < right_index:
        # Swap characters
        list_of_chars[left_index], list_of_chars[right_index] = \
            list_of_chars[right_index], list_of_chars[left_index]
        # Move towards middle
        left_index += 1
        right_index -= 1

    return list_of_chars

# For loop solution
def reverse_for(list_of_chars):

    for i in range(len(list_of_chars) // 2):
        temp = list_of_chars[i]
        list_of_chars[i] = list_of_chars[-(i+1)]
        list_of_chars[-(i+1)] = temp

    return list_of_chars


print(reverse(['a','b','c','d']))
