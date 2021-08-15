def find_sum(lst, k):

    nums = []
    for l in range(len(lst)):
        print(l)
        sum = k - lst[l]
        for i in lst[l+1:]:
            if i == sum:
                nums.extend([lst[l], i])
                return nums

def find_sum_sort(lst, k):
    lst.sort()

    i = 0
    j = len(lst) - 1
    nums = []

    while i!=j:
        if lst[i] + lst[j] < k:
            i += 1
        elif lst[i] + lst[j] > k:
            j -= 1
        else:
            nums.extend([lst[i], lst[j]])
            return nums


lst = [1, 21, 3, 14, 5, 60, 7, 6]
k = 81

# print(find_sum(lst, k))
print(find_sum_sort(lst, k))

