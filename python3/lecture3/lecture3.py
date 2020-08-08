# Problem:
# 	Find the sum of the first N numbers.

# Objective function:
# 	f(i) is the sum of the first i elements.

# Recurrence relation:
# 	f(n) = f(n-1) + n
def nSum(n: int) -> int:
  dp = [0]*(n+1)

  for i in range(n+1):
    dp[i] = dp[i-1] + i

  return dp[-1]