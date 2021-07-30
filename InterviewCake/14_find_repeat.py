"""
https://www.interviewcake.com/question/python3/find-duplicate-optimize-for-space?course=fc1&section=sorting-searching-logarithms
Write a function which finds an integer that appears more than once in our list. Don't modify the input!

https://leetcode.com/problems/find-the-duplicate-number/solution/
"""

# O(n) space
def find_repeat_On_space(numbers):
    unique_numbers = set()
    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.add(num)
        else:
            return num

    return 'No duplicates'

# O(1) space
# Binary search approach
def find_repeat(numbers):
    left = 1
    right = len(numbers) - 1

    while left < right:
        mid = (left + right) // 2
        count = 0

        for num in numbers:
            if num <= mid:
                count += 1
        if count <= mid:
            left = mid + 1
        else:
            right = mid

    return left


list_of_ints = [7, 2, 3, 3, 4, 5, 6, 1]
print(find_repeat(list_of_ints))
