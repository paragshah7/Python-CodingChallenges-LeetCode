"""
https://www.educative.io/courses/grokking-the-coding-interview/7XMlMEQPnnQ

Input: [2, 1, 5, 2, 3, 2], S=7
Output: 2
Explanation: The smallest subarray with a sum greater than or equal to '7' is [5, 2]
"""

arr = [3, 4, 1, 1, 6]
arr_in = arr.copy()
sum_ = 8
total = 0
sub_arr_len = 0
res = 9999999

for v in arr:
    sub_arr = []
    total = 0
    print('outer', arr_in)
    for val in arr_in:
        print('--inner', val)
        total += val
        sub_arr.append(val)
        if total >= sum_:
            print(sub_arr)
            sub_arr_len = len(sub_arr)
            arr_in = arr_in[1:]
            break
    if sub_arr_len < res:
        res = sub_arr_len

print('Output -', res)