
# Sort a Python Dictionary by values
def sort_dict_by_value(dict_param):
  sorted_dict = sorted(dict_param.items(), key=lambda x: x[1])
  return sorted_dict

if __name__ == '__main__':
  print(sort_dict_by_value({'a': 4, 'b': 3, 'c': 2, 'd': 1}))