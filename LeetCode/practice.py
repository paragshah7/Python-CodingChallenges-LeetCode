a = [1, 3, 2, 4]
b = a.copy()
first = 0
last = 1
for elem in a:
    if elem % 2 == 0:
        b[first] = elem
        first += 1
    else:
        b[-last] = elem
        last += 1
print(b)
