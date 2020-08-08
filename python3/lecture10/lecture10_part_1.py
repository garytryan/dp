# Problem:
# 	Maximum Profit in a Grid (homework for lecture9)

# 	A robot is located at the top-left corner of a m x n grid (marked 'S' in the diagram below).
# 	The robot can only move either down or right at any point in time.
# 	The robot is trying to reach the bottom-right corner of the grid (marked 'E' in the diagram below).
# 	Each cell contains a coin the robot can collect.

# 	What is the path that lead to the maximum profit the robot can accumulate?

# 	+---+---+---+---+
# 	| S | 2 | 2 | 1 |
# 	+---+---+---+---+
# 	| 3 | 1 | 1 | 1 |
# 	+---+---+---+---+
# 	| 4 | 4 | 2 | E |
# 	+---+---+---+---+


# Time complexity: O(mn)
# Space complexity: O(mn)

def maxProfit(grid: [[int]]) -> [[int]]:
    m = len(grid)
    n = len(grid[0])
    dp = [[0]*n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                dp[i][j] = ((i, j), grid[i][j])
            elif i == 0:
                dp[i][j] = ((i, j-1), dp[i][j-1][1] + grid[i][j])
            elif j == 0:
                dp[i][j] = ((i-1, j), dp[i-1][j][1] + grid[i][j])
            elif dp[i-1][j][1] > dp[i][j-1][1]:
                dp[i][j] = ((i-1, j), dp[i-1][j][1] + grid[i][j])
            else:
                dp[i][j] = ((i, j-1), dp[i][j-1][1] + grid[i][j])

    coor = (m-1, n-1)
    path = [coor]

    while coor[0] > 0 or coor[1] > 0:
        path.append(dp[coor[0]][coor[1]][0])
        coor = dp[coor[0]][coor[1]][0]

    path.reverse()

    return tuple(path)
