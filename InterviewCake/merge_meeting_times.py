"""
https://www.interviewcake.com/question/python3/merging-ranges?course=fc1&section=array-and-string-manipulation
"""

def merge_ranges(times):
    times.sort()
    result = []
    temp = []

    for i in range(len(times)-1):
        if times[i+1][0] <= times[i][1]:
            if not temp:
                temp.append(times[i])
            temp.append(times[i+1])
            temp.sort()
        else:
            if temp:
                print(temp)
                tup = (temp[0][0],max(max(temp)))
                result.append(tup)
                temp = []
            else:
                result.append(times[i])

    print('Last', temp)
    tup = (temp[0][0], max(max(temp)))
    result.append(tup)

    return result


ranges = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
print(merge_ranges(ranges))


# [(0, 1), (3, 5), (4, 8), (9, 10), (10, 12)]