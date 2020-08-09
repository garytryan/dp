from lecture5_part2 import climbStairs3Steps


def test_climbStairs3Steps():
  tests = [
    {
      "name": "when n is 3",
      "args": {"n": 3},
      "want": 4,
    },
    {
      "name": "when n is 5",
      "args": {"n": 5},
      "want": 13,
    },
  ]

  for test in tests:
    got = climbStairs3Steps(**test["args"])

    if test['want'] != got:
      raise Exception(f"climbStairs3Steps() = {got}, want {test['want']}")
