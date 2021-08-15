"""
Problem:
Input: '1 + 2/2 - 3*3 + 1'
output: -4
String can have spaces and invalid characters
"""
from icecream import ic as print
import operator


def infix(text):
    numbers = []
    operators = []
    output = 0
    temp_output = 0

    for op in text:
        num = 0
        print(op)

        # spaces
        if op == ' ':
            continue

        # nums
        try:
            if int(op):
                num = int(op)
                numbers.append(num)
                if len(operators) == 0:
                    output += int(op)
        except:
            pass

        # operators
        if op == '/' or op == '*':
            operators.append(op)
            if not temp_output:
                temp_output = numbers.pop()
            temp_output = operator.floordiv(temp_output, numbers.pop())

        elif op == '+' or op == '-':
            if len(operators) == 0:
                operators.append(op)
            elif len(numbers) > 1:
                opr = operators.pop()
                if opr == '+':
                    output = operator.add(output, numbers.pop())
                elif opr == '-':
                    output = operator.sub(output, numbers.pop())
                operators.append(op)

        print(numbers, output, operators)

    output += temp_output
    print(numbers, operators)
    print(output)


# or op == '*' or op == '/'
text = '1 + 3 + 2/2 '
# text = '1 + 2 + 2 - 3 + 3 - 1'
print(infix(text))
