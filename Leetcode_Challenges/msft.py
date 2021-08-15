'''

A = [3 2 1 1 2 3 1]
1 + 1 and 3 - 1
111 22 33
number of steps to make all elements equal

'''


def minMoves(arr):
    len_arr = len(arr)
    arr.sort()
    count = 0
    for n in range(len_arr-1,0,-1):
        # print('n =',n)
        count += arr[n] - arr[0]
    return count


arr = [3, 2, 1, 1, 2, 3, 1]
arr2 = [4, 1, 4, 1]
arr3 = [3, 3, 3]
print(minMoves(arr))
print(minMoves(arr2))
print(minMoves(arr3))