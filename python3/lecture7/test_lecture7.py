from lecture8 import paidStaircase


def test_paidStaircase():
  tests = [
    {
      # 0   3   2   4   6   1   1   5   3
      # |---|---|---|---|---|---|---|---|
      # 0   1   2   3   4   5   6   7   8
      # 0 -> 2 -> 3 -> 5 -> 6 -> 8 = 11
      "name": "complex case",
      "args": {
          "n": 8,
          "p": [0, 3, 2, 4, 6, 1, 1, 5, 3]
      },
      "want": [0, 2, 3, 5, 6, 8]
    },
  ]

  for test in tests:
    got = paidStaircase(**test["args"])

    if test['want'] != got:
      raise Exception(f"paidStaircase() = {got}, want {test['want']}")
