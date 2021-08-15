"""
Reverse list of chars in place
https://www.interviewcake.com/question/python3/reverse-string-in-place?course=fc1&section=array-and-string-manipulation
"""

# While loop solution
def reverse(list_of_chars):

    l = 0
    r = len(list_of_chars) - 1

    while l < r:
        # Swap characters
        list_of_chars[l], list_of_chars[r] = list_of_chars[r], list_of_chars[l]
        # Move towards middle
        l += 1
        r -= 1

    return list_of_chars

# For loop solution
def reverse_for(list_of_chars):

    for i in range(len(list_of_chars) // 2):
        temp = list_of_chars[i]
        list_of_chars[i] = list_of_chars[-(i+1)]
        list_of_chars[-(i+1)] = temp

    return list_of_chars


print(reverse(['a','b','c','d']))
