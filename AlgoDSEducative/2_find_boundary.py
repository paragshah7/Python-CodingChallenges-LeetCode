'''
Find Boundary - Returns index whenever True is found in the array
https://www.educative.io/courses/algorithms-ds-interview/RMjKr8LgzyL
'''
from icecream import ic as print

def find_boundary(arr: list) -> int:
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        # print(left, right, mid, arr[mid])
        if arr[mid] == True:
            right = mid - 1
            if arr[mid-1] == False or mid == 0:
                return mid
        elif arr[mid] == False:
            left = mid + 1

    return -1


# arr = [False, False, False, False, True]
arr = [False, True, True, True, True]
print(find_boundary(arr))

print("Find boundary :", find_boundary([False, False, True, True, True]))
print("Find boundary :", find_boundary([True]))
print("Find boundary :", find_boundary([False, False, False]))
print("Find boundary :", find_boundary([False, False, True, True, True]))
print("Find boundary :", find_boundary([True, True, True, True, True]))
print("Find boundary :", find_boundary([False, True]))
