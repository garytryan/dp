# Problem:
# 	Maximum Profit in a Grid

# 	A robot is located at the top-left corner of a m x n grid (marked 'S' in the diagram below).
# 	The robot can only move either down or right at any point in time.
# 	The robot is trying to reach the bottom-right corner of the grid (marked 'E' in the diagram below).
# 	Each cell contains a coin the robot can collect.

# 	What is the maximum profit the robot can accumulate?

# 	+---+---+---+---+
# 	| S | 2 | 2 | 1 |
# 	+---+---+---+---+
# 	| 3 | 1 | 1 | 1 |
# 	+---+---+---+---+
# 	| 4 | 4 | 2 | E |
# 	+---+---+---+---+


# Time complexity:
# Space complexity:


def maxProfit(grid: [[int]]) -> int:
  m = len(grid)
  n = len(grid[0])

  dp = [[0]*n for _ in range(m)]

  for i in range(m):
    for j in range(n):
      if i == 0 and j == 0:
        dp[i][j] = grid[i][j]
      elif i == 0:
        dp[i][j] = grid[i][j] + dp[i][j-1]
      elif j == 0:
        dp[i][j] = grid[i][j] + dp[i-1][j]
      else:
        dp[i][j] = grid[i][j] + max(dp[i][j-1], dp[i-1][j])

  return dp[-1][-1]
