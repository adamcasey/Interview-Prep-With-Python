# Find missing value between two lists

class MissingValue:
  def __init__(self):
    self.missing_value = None

  # Use default None assignment in definition because empty list would \ 
  # always cause error
  def find_missing_value(self, list_one=None, list_two=None):
    if list_one != None and list_two != None:
      #print("you called me")
      print(set(list_one) - set(list_two))
    else: 
      print("Lists are empty!")

if __name__ == '__main__':
  missing_val = MissingValue()
  test_list_one = [10, 28, 35, 33, 2]
  test_list_two = [10, 28, 35, 2]

  missing_val.find_missing_value(test_list_one, test_list_two)
  print("missing_val: {}".format(missing_val.missing_value))