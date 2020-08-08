from lecture4 import climbStairs


def test_climbStairs():
  tests = [
    {
      "name": "a simple test 1",
      "args": {"n": 3},
      "want": 3,
    },
    {
      "name": "a simple test 2",
      "args": {"n": 5},
      "want": 8,
    },
  ]

  for test in tests:
    got = climbStairs(**test["args"])

    if test['want'] != got:
      raise Exception(f"climbStairs() = {got}, want {test['want']}")
