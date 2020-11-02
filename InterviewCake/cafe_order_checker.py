"""
https://www.interviewcake.com/question/python3/cafe-order-checker?course=fc1&section=array-and-string-manipulation
"""

take_out_orders = [17, 8, 24]
dine_in_orders = [12, 19, 2]
served_orders = [17, 8, 12, 19, 2, 24]

take_out_index = 0
dine_in_index = 0
served_counter = 0

for order in served_orders:
    served_counter += 1
    if take_out_index >= len(take_out_orders) or dine_in_index >= len(dine_in_orders):
        pass
    elif order == take_out_orders[take_out_index]:
        take_out_index += 1
    elif order == dine_in_orders[dine_in_index]:
        dine_in_index += 1
    else:
        print('Not in order')
        break

if served_counter == len(served_orders):
    print('In order')
