def increment(number, by):
    """This function returns the increment"""
    return number+by


print(increment(2, 3))


def incrementtuple(number: int, by: int = 2) -> tuple:
    """This function returns tuple as a return type, also 'by' has 2 by default if value is not passed below"""
    return number, by, number + by


print(incrementtuple(5))


def multiply(*numbers):
    """This function multiplies list of numbers, asterisk means it recognizes numbers as tuple"""

    print("Passing multiple values -", numbers)
    total = 1
    for x in numbers:
        total *= x
    return total


print(multiply(2, 3, 4))
