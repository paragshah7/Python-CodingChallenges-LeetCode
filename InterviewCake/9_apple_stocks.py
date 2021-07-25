"""
https://www.interviewcake.com/question/python3/stock-price?course=fc1&section=greedy

Write an efficient function that takes stock_prices and returns the best profit I could have made from one purchase and one sale of one share of Apple stock yesterday.

For example:

  stock_prices = [10, 7, 5, 8, 11, 9]

get_max_profit(stock_prices)
# Returns 6 (buying for $5 and selling for $11)
"""
from icecream import ic as print

def get_max_profit(stock_prices):
    if len(stock_prices) < 2:
        raise ValueError('Getting a profit requires at least 2 prices')

    min_price = stock_prices[0]
    max_profit = stock_prices[1] - stock_prices[0]  # this is important, having some default max profit

    for current_price in stock_prices[1:]:

        profit = current_price - min_price

        if profit > max_profit:
            max_profit = profit
        if current_price < min_price:
            min_price = current_price

    return max_profit


# stock_prices = [20, 7, 2, 5, 1, 1]
print(get_max_profit([20, 7, 6, 5, 1]))
print(get_max_profit([10, 7, 5, 8, 11, 9]))
print(get_max_profit([10, 7, 5, 2, 11, 9]))
