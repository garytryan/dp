# Problem:
# 	Unique Paths

# 	A robot is located at the top-left corner of a m x n grid (marked 'S' in the diagram below).
# 	The robot can only move either down or right at any point in time.
# 	The robot is trying to reach the bottom-right corner of the grid (marked 'E' in the diagram below).

# 	How many possible unique paths are there?

# 	+---+---+---+---+
# 	| S |   |   |   |
# 	+---+---+---+---+
# 	|   |   |   |   |
# 	+---+---+---+---+
# 	|   |   |   | E |
# 	+---+---+---+---+

# 	Above is a 3 x 4 grid. How many possible unique paths are there?


# Time complexity:
# Space complexity:
# F(i,j) = F(i-1,j) + F(i,j-1)

def uniquePaths(m: int, n: int) -> int:
  dp = [[0]*n for _ in range(m)]

  for i in range(m):
    for j in range(n):
      if i == 0  and j == 0:
        dp[i][j] = 1
      elif i == 0:
        dp[i][j] = dp[i][j-1]
      elif j == 0:
        dp[i][j] = dp[i-1][j]
      else:
        dp[i][j] = dp[i][j-1] + dp[i-1][j]

  return dp[-1][-1]
