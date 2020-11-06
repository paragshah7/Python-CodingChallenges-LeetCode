lower = 0
upper = 10
if lower < 2:
    lower = 2
for num in range(lower, upper+1):
    if num % 2 == 0:
        continue
    else:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)
