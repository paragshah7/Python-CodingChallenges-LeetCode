def fib_recur(n):
    if n <= 1:
        return n
    else:
        return fib_recur(n-1) + fib_recur(n-2)


# for i in range(7):
#     print(fib_recur(i))


def fib(number_of_terms): 

    count = 0
    first = 0
    second = 1

    while count < number_of_terms:
        print(first)
        temp = first + second
        first = second
        second = temp
        count = count + 1


fib(5)
