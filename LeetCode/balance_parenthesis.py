"""
https://leetcode.com/discuss/interview-question/1317099/VMWare-Interview-question-or-Golang-developer

Given a string containing only paranthesis ')' or '(', find the minimum number of swaps (need not be adjacent characters) to balance the string. If it's not possible to balance, return -1.

For eg: ))((
Ans - 1, Swap first and last bracket -> ()()

eg: (()())
Ans - 0
"""
from icecream import ic as print

def balance_parenthesis(string):
    swaps = 0
    left = 0
    right = 0
    swap_count = 0

    for i in string:
        if i == '(':
            left += 1
        elif i == ')':
            right += 1
        if right > left + 1:
            swap_count += 1

    print(left, right, swap_count)
    swaps = swap_count
    return swaps


string = '(())()'
print(balance_parenthesis(string))
