# coding=utf-8

x = 'global x'


def scope():
    """ variable scope """
    global x   # without this, the last value printed will be 'global x'
    print(x)
    x = 'local x'
    print(x)
    y = 'local y'


def scope2():
    print('scope2:', x)


scope()
scope2()
print(x)  # because of the 'global x' defined in scope(), it uses x and changes the value of x


def save_user(**user):
    """ json data, ** is used to pass keyword arguments """
    print(user)
    print(user["name"], "\n")


# save_user(id=1, name="parag")


def student_info(*args, **kwargs):
    """* = basic multiple arguments (list / tuple), ** = keyword arguments/json """
    print(type(args), args)
    print(type(kwargs), kwargs)


courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}

student_info(*courses, **info)
# student_info('Math', 'Art', name='John', age=22)


def fizz_buzz(x):
    """ print output accordingly """
    print("Number is:", x)
    if (x%3 == 0) and (x%5 == 0):
        return "Fizz_Buzz"
    elif x%3 == 0:
        return "Fizz"
    elif x % 5 == 0:
        return "Buzz"
    return x


# print(fizz_buzz(45))

