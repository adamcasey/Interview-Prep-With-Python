
INFINITY = 99999


def DPchange(money, coins):

    """
    Returns the minimum number of coins and denominations change of the minimum number of coins.
    :param money: Money to be changed.
    :param coins: Coins that are available.
    :return: dictionary with minMoney and change

    """
    minNumCoins = [0]
    change = [0] * (money + 1)
    # m will go from 1 -> money + 1 
    for m in range(1, money + 1):
        minNumCoins.append(INFINITY)
        #print(f'm = {m}')
        # 'i' is the index of each coin in the coin list
        for i in range(0, len(coins)):
            #print(f'i = {i}')
            if (m >= coins[i]):
                #print(f'minNumCoins[m - coins[i]]'
                if (minNumCoins[m - coins[i]] + 1 < minNumCoins[m]):

                    minNumCoins[m] = minNumCoins[m - coins[i]] + 1
                    change[m] = coins[i]
    return {'minMoney': minNumCoins[money], 'change': change}





def printCoins(coinsUsed, money):

    """
    Prints the denominations of the changes of the minimum number of Coins
    :param coinsUsed: Coins used for change of the minimum number of coins.
    :param money: Money to be changed.
    :return: None
    """

    allChangeItems = []
    while money > 0:
        coinUsed = coinsUsed[money]
        allChangeItems.append(coinUsed)
        money = money - coinUsed
    listChange = dict((i, allChangeItems.count(i)) for i in allChangeItems)
    for coin, nums in listChange.items():

        print (nums, coin, "cents")





def main():
    """
    Main function to initialize and call the DPchange function and printCoins function.
    :return: None
    """
    
    coins = [1, 2, 5]
    money = 11
    #coins = [25, 10, 1]
    #money = 31
    print (coins)
    print (money)
    value = DPchange(money, coins)
    print(f'Value is a {type(value)}')
    print ("Minimum number of coins: ", value['minMoney'])

    printCoins(value['change'], money)
    
#main()

def myMakeChangeDP(change_amt, coin_list):

    # We use this to fill the dp table with default values
    max_amt = change_amt + 1;

    #This table will store the answer to our sub problems
    dp = [max_amt] * change_amt + 1;
    
    '''
      The answer to making change with minimum coins for 0
      will always be 0 coins no matter what the coins we are
      given are
    '''
    dp[0] = 0;

    # Solve every subproblem from 1 to amount
    for i in range(1, change_amt):
      # For each coin we are given
        for j in range (0, len(coin_list)):
        # If it is less than or equal to the sub problem amount
           if (coin_list[j] <= i):
          # Try it. See if it gives us a more optimal solution
              dp[i] = min(dp[i], dp[i - coins[j]] + 1)
'''
dp[amount] has our answer. If we do not have an answer then dp[amount] will be amount + 1 and hence dp[amount] > amount will be true. We then return -1. Otherwise, dp[amount] holds the answer
'''  
       if (dp[amount] > amount):
            return -1
     else:
        return dp[amount]
    

print(myMakeChangeDP(11, [1,2,5]))