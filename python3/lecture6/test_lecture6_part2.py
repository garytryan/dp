from lecture6_part2 import climbStairsKStepsSkipRed


def test_climbStairsKStepsSkipRed():
  tests = [
    {
      "name": "a simple test case",
      "args": {
        "n": 7,
        "k": 3,
        "stairs": [False, True, False, True, True, False, False, ],
      },
      "want": 2,
    }
  ]

  for test in tests:
    got = climbStairsKStepsSkipRed(**test["args"])

    if test['want'] != got:
      raise Exception(f"climbStairsKStepsSkipRed() = {got}, want {test['want']}")
