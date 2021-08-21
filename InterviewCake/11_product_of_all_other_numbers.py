"""
Write a function get_products_of_all_ints_except_at_index() that takes a list of integers and returns a list of the products.

For example, given:

  [1, 7, 3, 4]

Python 3.6
your function would return:

  [84, 12, 28, 21]
"""

def product_all_other(nums):
    """
    nums
    nums_1 - multiply all prev at current index and store starting with 1
    res - Rev, take last elem in nums_1 and multiply with last elem in nums, update counter by mul nums elem
    """

    product = 1
    n = len(nums)
    output = []

    for i in range(0,n):
        output.append(product)
        product = product * nums[i]

    product = 1
    for i in range(n-1,-1,-1):
        output[i] = output[i] * product
        product = product * nums[i]

    return output


nums = [1, 2, 3, 4, 5]
print(product_all_other(nums))
