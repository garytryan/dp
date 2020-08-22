# Problem:
# 	Climbing Stairs (k steps, space optimized)

# 	You are climbing a stair case. It takes n steps to reach to the top.
# 	Each time you can climb 1..k steps.
# 	In how many distinct ways can you climb to the top?


# Time complexity: O(nk)
# Space complexity: O(k)

def climbStairsKSteps(n: int, k: int) -> int:
    dp = [0]*(k)
    dp[0] = 1

    for i in range(1, n+1):
        for j in range(1, k):
            if i-j >= 0:
                dp[i % k] += dp[(i-j) % k]

    return dp[n % k]
