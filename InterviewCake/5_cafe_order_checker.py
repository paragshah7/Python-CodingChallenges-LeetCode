"""
https://www.interviewcake.com/question/python3/cafe-order-checker?course=fc1&section=array-and-string-manipulation
Check if orders are first come first serve

Incorrect -
Take Out Orders: [1, 3, 5]
 Dine In Orders: [2, 4, 6]
  Served Orders: [1, 2, 4, 6, 5, 3]

Correct -
Take Out Orders: [17, 8, 24]
 Dine In Orders: [12, 19, 2]
  Served Orders: [17, 8, 12, 19, 24, 2]

"""
from icecream import ic as print

def served_order_checker(take_out_orders, dine_in_orders, served_orders):

    i = 0
    j = 0
    orders = 0

    # Imp: i == len(take_out_orders) is done to avoid out of index error
    for order in served_orders:
        print(i, j)
        if i == len(take_out_orders) or order == take_out_orders[i]:
            orders += 1
            i += 1
        elif j == len(dine_in_orders) or order == dine_in_orders[j]:
            orders += 1
            j += 1

    print(orders)
    if orders == len(take_out_orders) + len(dine_in_orders):
        return True
    else:
        return False


take_out_orders = [17, 8, 24]
dine_in_orders = [12, 19, 2]
served_orders = [17, 8, 12, 19, 2, 24]
print(served_order_checker(take_out_orders, dine_in_orders, served_orders))
