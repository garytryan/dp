from lecture10_part_2 import numWays


def test_numWays():
  tests = [
    {
      "name": "test case #1",
      "args": {
        "n": 3
      },
      "want": 6
    },
    {
      "name": "test case #1",
      "args": {
        "n": 4
      },
      "want": 10
    },
    {
      "name": "test case #1",
      "args": {
        "n": 5
      },
      "want": 16
    },
  ]

  for test in tests:
    got = numWays(**test["args"])

    if test['want'] != got:
      raise Exception(f"numWays() = {got}, want {test['want']}")
