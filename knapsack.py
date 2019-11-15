# Complexity:

# Time: O(n * k) where n is the number of types of cakes and k is the capacity \
# of the bag

# Space: O(k)
# If you cared more about time, it might be worth using a faster algorithm
# that gives you a 'good' answer, even if it's not always the 'optimal' answer


def max_bag_value(cake_tuples, weight_cap):
    # Make a list to hold the max possible value at every bag weight capacity \
    # from 0 to weight_cap starting each index with value 0
    max_values_at_cap = [0] * (weight_cap +1)

    for current_capacity in range(weight_cap + 1):
        # Set a varaible to hold the max monetary valu so far for current_capacity
        current_max_value = 0
        
        for cake_weight, cake_value in cake_tuples:
            # If a cake weighs 0 and has a positive value the value of our
            # bag is infinite!

            if cake_weight == 0 and cake_value != 0:
                # Advantage of using this way to return infinity is we get the 'behavior' \
                # of infinity. Compared to any other integer, float('inf') will be great.
                # And it's a nubmer, which can be an advantage or disadvantage --> \
                # You might want the result to always be the same type, but without manually \
                # checking you don't know if you mean an actual value or the special case of inf.
                return float('inf')

            # If the current cake weighs as much or less than the current weight capacity it's \
            # possible taking the cake would get a better value
            if cake_weight <= current_capacity:

                # So we  check: should we use the cake or not?
                # If we use the cake, the most kilograms we can include in addiiton \
                # to the cake we're adding is the current capacity minus the cake's \
                # weight. We find th emax value at that integer capacity in our list \
                # max_values_at_cap
                max_value_using_cake= (cake_value + max_values_at_cap[current_capacity - cake_weight])


                # Now we see if it's worth taking the cake. How does the value with the \
                # cake compare to the current_max_value?
                current_max_value = max(max_value_using_cake, current_max_value)

        # Add each capacity's max value to our list so we can use them 
        # when calculating all the remaining capacities
        max_values_at_cap[current_capacity] = current_max_value

    return max_values_at_cap[weight_cap]

# Test Cases: parameters --> (weight, value)

# Test Case 1
cake_tuples_param = [(3, 40), (5, 70)]
capacity_param = 9

# Test Case 2
#cake_tuples_param = [(7, 160), (3, 90), (2,15)]
#capacity_param = 20

#Test Case 3
#cake_tuples_param = [(7, 160), (3, 90), (2,15)]
#capacity_param = 20

print(max_bag_value(cake_tuples_param, capacity_param))
