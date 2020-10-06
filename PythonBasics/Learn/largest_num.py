num_list = [10,30,2,85,2,100,1,20]
largest = num_list[0]
for x in num_list:
    if x > largest:
        largest = x
print('Largest -',largest)

smallest = num_list[0]
for x in num_list:
    if x < smallest:
        smallest = x
print('Smallest -',smallest)