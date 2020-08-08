# this is NOT dynamic programming, but a regular recursion
def fib(n: int) -> int:
    if n < 2:
        return n
    else:
        return fib(n-2)+fib(n-1)


# this is a top-down dynamic programming (a.k.a. recursion + memoization)
def fibTopDown(n: int) -> int:
    memo = {}

    if n < 2:
        return n
    elif n in memo:
        return memo[n]
    else:
        memo[n] = fib(n-1) + fib(n-2)
        return memo[n]


# this is a bottom-up dynamic programming (forward dynamic programming)
#
# f(i-1)
#      \
#       >-------> f(i)
#      /
# f(i-2)
#
def fibBottomUpDPForward(n: int) -> int:
    if n < 2:
        return n

    dp = [0]*(n+1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-2] + dp[i-1]

    return dp[-1]


# this is a bottom-up dynamic programming (backward dynamic programming)
#
#   -----> f(i+2)
#   |
# f(i)
#   |
#   -----> f(i+1)
#
def fibBottomUpDPBackward(n: int) -> int:
    if n < 2:
        return n

    dp = [0]*(n+2)
    dp[0] = 0
    dp[1] = 1

    for i in range(1, n):
        dp[i+1] += dp[i]
        dp[i+2] += dp[i]

    return dp[-2]