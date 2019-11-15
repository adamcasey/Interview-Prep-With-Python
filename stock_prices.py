'''
Have to buy before you can 
Complexity
O(n) time and O(1) space. We only loop through the list once. 
'''
# [10, 7, 5, 8, 11, 9]
def get_max_profit_bf(stock_prices):
    max_profit = 0

    # Go through every time
    # outer_time is an int representing the index values
    for outer_time in range(len(stock_prices)):
        print("outer_time: {}".format(outer_time))
        # For every time, go through every other time
        # inner_time is an int representing the index values
        for inner_time in range(len(stock_prices)):
            # For each pair, find the earlier and later times
            earlier_time = min(outer_time, inner_time)
            later_time   = max(outer_time, inner_time)

            # And use those to find the earlier and later prices
            earlier_price = stock_prices[earlier_time]
            later_price   = stock_prices[later_time]

            # See what our profit would be if we bought at the
            # earlier price and sold at the later price
            potential_profit = later_price - earlier_price

            # Update max_profit if we can do better
            max_profit = max(max_profit, potential_profit)

    return max_profit

# Using one pass and constant space
# Problem with this is if the prices go down all day it doesn't return a negative profit
def get_max_profit_greedy(stock_prices):
    min_price  = stock_prices[0]
    max_profit = 0

    for current_price in stock_prices:
        # Ensure min_price is the lowest price we've seen so far
        print("current_price: {}".format(current_price))
        min_price = min(min_price, current_price)
        print("min_price: {}".format(min_price))

        # See what our profit would be if we bought at the
        # min price and sold at the current price
        potential_profit = current_price - min_price

        # Update max_profit if we can do better
        max_profit = max(max_profit, potential_profit)
        print("max_profit: {}".format(max_profit))

    return max_profit


def get_max_profit_soln(stock_prices):
    if len(stock_prices) < 2:
        raise ValueError('Getting a profit requires at least 2 prices')

    # We'll greedily update min_price and max_profit, so we initialize
    # them to the first price and the first possible profit
    min_price  = stock_prices[0]
    max_profit = stock_prices[1] - stock_prices[0]

    # Start at the second (index 1) time
    # We can't sell at the first time, since we must buy first,
    # and we can't buy and sell at the same time!
    # If we started at index 0, we'd try to buy *and* sell at time 0.
    # This would give a profit of 0, which is a problem if our
    # max_profit is supposed to be *negative*--we'd return 0.
    for current_time in range(1, len(stock_prices)):
        current_price = stock_prices[current_time]

        # See what our profit would be if we bought at the
        # min price and sold at the current price
        potential_profit = current_price - min_price

        # Update max_profit if we can do better
        max_profit = max(max_profit, potential_profit)

        # Update min_price so it's always
        # the lowest price we've seen so far
        min_price  = min(min_price, current_price)

    return max_profit


stock_prices = [10, 7, 5, 8, 11, 9]
#print(get_max_profit_bf(stock_prices))
print(get_max_profit_greedy(stock_prices))
#print(get_max_profit_soln(stock_prices))
# Returns 6 (buying for $5 and selling for $11)