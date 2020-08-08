# Problem:
# 	Paint Fence With Two Colors

# 	There is a fence with n posts, each post can be painted with either green or blue color.
# 	You have to paint all the posts such that no more than two adjacent fence posts have the same color.
# 	Return the total number of ways you can paint the fence.


def numWays(n: int) -> int:
    dp = [[0, 0] for _ in range(n)]
    dp[0][0] = 1
    dp[0][1] = 1
    dp[1][0] = 2
    dp[1][1] = 2

    for i in range(2, n):
        for j in range(2):
            print(i, j)
            dp[i][j] = dp[i-2][1-j] + dp[i-1][1-j]

    print(dp)
    return dp[-1][0] + dp[-1][1]
