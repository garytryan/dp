# Problem:
# 	Paid Staircase II

# 	You are climbing a paid staircase. It takes n steps to reach to the top and you have to
# 	pay p[i] to step on the i-th stair. Each time you can climb 1 or 2 steps.
# 	Return the cheapest path to the top of the staircase.

# Template to reconstruct the path
# ================================

# 	path = []
# 	for curr = best_last_state; curr exists; curr = from[curr] {
# 		path.push(curr)
# 	}
# 	return path.reverse()
# Time complexity: O(n)
# Space complexity: O(n)

# 1. Identify the sub-problem
# 2. Identify the base cases
# 3. Identify the recursive relationship


def paidStaircase(n: int, p: [int]) -> [int]:
  dp = [None]*(n+1)
  dp[0] = (p[0], 0)
  dp[1] = (p[1], 0)

  for i in range(2, n+1):
    if dp[i-1] < dp[i-2]:
      dp[i] = (p[i] + dp[i-1][0], i-1)
    else:
      dp[i] = (p[i] + dp[i-2][0], i-2)

  path = []
  i = n
  while i > 0:
    path.append(i)
    i = dp[i][1]
  path.append(0)
  path.reverse()

  return path
