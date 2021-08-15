def binarySearch(array, s, l, find):
    start = s
    end = l
    while start <= end:
        mid = int((s+l-1) / 2)
        if find == array[mid]:
            print(mid)
            return mid
        elif find <= array[mid]:
            end = mid - 1
            print(end)
            mid = int((s + l - 1) / 2)
            return end
        elif find >= array[mid]:
            start = mid + 1
            print(start)
            return start
        start = 100


a = [10, 20, 30, 40, 50, 60, 70]
binarySearch(a, 0, len(a), 70)
