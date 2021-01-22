# Solved by Parag Shah

def product_numbers(input_):

    """ Output is a list of arrays replaced with the product of all the elements except the num itself """
    input_list = input_

    product = 1
    key_zeros = []
    output_list = []

    # Get the product of all integers except 0
    for key, num in enumerate(input_list):
        if num == 0:
            key_zeros.append(key)
            continue
        else:
            product *= num

    number_of_zeros = len(key_zeros)

    # More than 1 '0' in the input_list
    if number_of_zeros > 1:
        output_list = [0] * len(input_list)

    # 1 '0' in the input_list
    elif number_of_zeros == 1:
        output_list = [0] * len(input_list)
        output_list[key_zeros[0]] = product

    # For all other integers
    else:
        for num in input_list:
            output_list.append(product // num)

    print('For Input -', input_list, '  Output --> ', output_list, '\n')

#       Time Complexity - O(n)
#       Space Complexity - O(n)


""" Testing the above product_numbers function """

print('Testing product of remaining numbers in a list')
# Assumptions made:
# Input is a list of integers
# Size of the product variable is not an issue

# Empty array
input_1 = []
product_numbers(input_1)

# Positive Integers
input_2 = [1, 4, 5, 6, 8, 9]
product_numbers(input_2)

# More than 1 zeros
input_3 = [10, 0, 100, 0]
product_numbers(input_3)

# Only 1 zero
input_4 = [0, 10, 100]
product_numbers(input_4)

# All zeros
input_5 = [0, 0, 0]
product_numbers(input_5)

# Few negative integers
input_6 = [-1, 4, 5, 6, -8, 9]
product_numbers(input_6)

# All negative integers
input_7 = [-1, -4, -5, -6, -8, -9]
product_numbers(input_7)