# coding=utf-8

try:
    pass

except Exception as e:
    print('There is an Exception -', e)


try:
    f = open('data.txt')
    print(f.read())
    f.close()
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
