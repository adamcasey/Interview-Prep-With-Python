# Provide the functional design of software that controls a vending machine. 
# The vending machine has a predefined set of items that the user can purchase using cash. 
# The vending machine has the following actions:
# 1. User inserts cash
# 2. User selects item
# 3. Item dispensed if available
# 4. Change dispensed

# Design the structure of the program that controls the vending machine
# Implement a method dispenseChange()
# item name : [item quantity, item price]
inventory = {"cookies" : [5, 100], "granola" : [2, 200] }
# Amount of the money the user put in
amountReceived = 250

# Only receive coins
# Coin value : coin quantity
denomation = {25 : 3, 10 : 5, 5 : 5, 1 : 10}
# Determine if the user should just receive the amount they put in because the item wasn't \
# available
itemAvailable = True

def dispenseChange(inventory, amountReceived, itemAvailable, denomation, itemSelected=None):
  # Check if item was available or not
  if itemAvailable == False:
    # Need to make change for that amount out of denominations
    amountToReturn = 0
    # So if the user gave 75 cents, return 3 quarters
    while amountReceived > 0:
      print ("amountReceived: ", amountReceived)
      # need to get the largest coin that makes sense from denomination
      for key, value in denomation.items():
        
        while amountReceived >= key and denomation.get(key) > 0:
          coinCount = denomation[key]
          amountReceived -= key
          amountToReturn += key
          coinCount -= 1
          denomation[key] = coinCount
    
  else:
    # Decrement inventory count for that item
    itemCount = inventory[itemSelected][0]
    itemCount -= 1
    itemCost = inventory[itemSelected][1]
    inventory[itemSelected][0] = itemCount
    #print("inventory: ", inventory)
    
    # Now figure out how to make change for the user
    # Need to make change for that amount out of denominations
    # 250 - 100 = 150
    amountToReturn = amountReceived - itemCost
    actualChange = 0
    # So if the user gave 75 cents, return 3 quarters
    while amountToReturn > 0:
      print ("amountToReturn: ", amountToReturn)
      # need to get the largest coin that makes sense from denomination
      for key, value in denomation.items():
        
        while amountToReturn >= key and denomation.get(key) > 0:
          coinCount = denomation[key]
          amountToReturn -= key
          actualChange += key
          coinCount -= 1
          denomation[key] = coinCount
          
    print("actualChange: ", actualChange)
    
     
     
    
          
        
          
dispenseChange(inventory, amountReceived, itemAvailable, denomation, 'cookies')
          
          
          
      
  



