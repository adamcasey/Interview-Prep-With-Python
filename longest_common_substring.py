# Brute force solution:
# For each substring of 'X' check if the substring exists in 'Y'.
# The longest existing substring is the answer.

# For each characters at indexes i and j from s1 and s2 we want to find the
# longest common substrings ending at those indexes. If the characters are
# same, we check if their neighboring characters are same as well. We do this
# until the characters are different. The overall time complexity of this will
# be O(mn^2).

# However, we can optimize this using dynamic programming. Instead of having to
# check the longest substring ending at neighboring characters at index i-1 and
# j-1, we could have stored longest substring for i-1 and j-1 in an array. This
# would bring down the complexity of O(nm)

# Dynamic programming solution
#   |   | a | b | c | d | x | y
# ------------------------------
#   | 0 | 0 | 0 | 0 | 0 | 0 | 0
# ------------------------------
# x | 0 | 0 | 0 | 0 | 0 | 1 | 0  
# ------------------------------
# z | 0 | 0 | 0 | 0 | 0 | 0 | 0
# ------------------------------
# b | 0 | 0 | 1 | 0 | 0 | 0 | 0
# ------------------------------
# c | 0 | 0 | 0 | 2 | 0 | 0 | 0
# ------------------------------
# d | 0 | 0 | 0 | 0 | 3 | 0 | 0
# ------------------------------

def longest_common_substring(x, y):
  # Get x and y lengths
  x_len, y_len = len(x), len(y)
  # Build the matrix
  dp = [[0 for _ in range(y_len+1)] for _ in range(x_len+1)]
  longest_subs_length = 0
  # Answer will be in lower right hand corner
  for i in range(1, x_len+1):
    for j in range(1, y_len+1):
      if x[i-1] == y[j-1]:
        dp[i][j] = dp[i-1][j-1] + 1
        if dp[i][j]  > longest_subs_length:
          longest_subs_length = dp[i][j]
  for row in dp:
    print(row)
  return longest_subs_length

print(longest_common_substring('zxabcdezy', 'yzabcdezx'))
print(longest_common_substring('abcdxyz', 'xyzabcd'))
print(longest_common_substring('GeeksforGeeks', 'GeeksQuiz'))
print(longest_common_substring("AdamAdamAdam", "MadamMadamMadam"))