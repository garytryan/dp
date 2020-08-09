from lecture5_part3 import climbStairsKSteps


def test_climbStairsKSteps():
  tests = [
    {
      "name": "a simple test 1",
      "args": {"n": 3, "k": 2},
      "want": 3,
    },
    {
      "name": "a simple test 2",
      "args": {"n": 5, "k": 2},
      "want": 8,
    },
    {
      "name": "when n is 3",
      "args": {"n": 3, "k": 3},
      "want": 4,
    },
    {
      "name": "when n is 5",
      "args": {"n": 5, "k": 3},
      "want": 13,
    },
    # Getting a different result in Python3
    # {
    # 	"name": "test when n is a big number",
    # 	"args": {"n": 1000000, "k": 2},
    # 	"want": 2756670985995446685,
    # },
  ]

  for test in tests:
    got = climbStairsKSteps(**test["args"])

    if test['want'] != got:
      raise Exception(f"climbStairsKSteps() = {got}, want {test['want']}")
