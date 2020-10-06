# coding=utf-8


class Employee:

    num_of_employees_1 = 0
    num_of_employees_2 = 2

    def __init__(self, first, last, pay):      # constructor
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

        Employee.num_of_employees_1 += 1
        self.num_of_employees_2 += 1
        # Employee.num_of_employees will keep counter and increase as per the objects
        # But if we type self.num_of_employees here then the count would be 0

    def full_name(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Parag', 'Shah', 100)          # these are objects
emp_2 = Employee('Sanika', 'Nikam', '200')      # new class instances are created each time

print(emp_1.__dict__)
print(emp_2.__dict__)
print(emp_1.email)
print(emp_2.full_name())
print(Employee.full_name(emp_1))
print(Employee.num_of_employees_1)
print(Employee.num_of_employees_2)  # Print 2 from class reference, it'll pick the topmost variable
print(emp_2.num_of_employees_2)
