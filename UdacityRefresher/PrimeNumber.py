import os


def isPrime(n):
    # Write your code here
    if n < 2:
        return 1
    for i in range(2, n):
        if (n % i) == 0:
            j = 1
            while j <= n:
                if n % i == 0:
                    print(j)
                i = i + 1
            break
        else:
            return 1
    return i


if __name__ == '__main__':

    n = 12
    result = isPrime(n)
    print(result)
