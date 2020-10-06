# coding=utf-8

# List
x = [3, 1, 2]     # this is a list
sorted_x = sorted(x)
print("Using sorted function:", sorted_x)

x.sort()
x.append(4)
print("Sorted list:", x)
print("Last value:", x[-1])     # -1 gets us the last value

x.sort(reverse=True)
print("Reverse sorting:", x)

z = [10, 20]
x.extend(z)   # use extend if merging 2 lists of same data type or else append will add z as 1 element in the x list
print("Added new list:", x)

courses = ['Math', 'Science', 'History']
print('Courses list is:', courses)
courses_output = ' - '.join(courses)
print('New String output is:', courses_output)
new_list = courses_output.split(' - ')
print('Converting back to list:', new_list)

# Tuple - Can't modify tuples, immutable
y = (1, 2, 3)
print("Tuple:", y)

# Sets - unique elements
cs_courses = {'Math', 'CS', 'Science'}
art_courses = {'Math', 'History', 'Photography'}
print('Intersection is', cs_courses.intersection(art_courses))
print('Difference is', cs_courses.difference(art_courses))

# Dictionary
student = {'name': 'Parag', 'age': '25', 'course': ['Math', 'Science']}
print(student.get('name', 'Not found'))     # 2nd value string if key not found

student.update({'name': 'Sandy', 'age': '27'})
print(student.get('age', 'Not found'))

age = student.pop('age')
print(age)
print(student)  # age gets popped out

print(student.keys())
print(student.values())
print(student.items())

for key, value in student.items():
    print(key, value)

# typecasting
num1 = '100'
num1 = int(num1)
print(num1)
