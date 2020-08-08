from lecture10_part_1 import maxProfit


def test_maxProfit():
  tests = [
    {
      "name": "simple test 1",
      "args": {
          "grid": [
            [0, 2, 2, 1],
            [3, 1, 1, 1],
            [4, 4, 2, 0]
          ]
      },
      "want": ((0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3))
    },
    {
      "name": "simple test 2",
      "args": {
        "grid": [
          [0, 2, 2, 50],
          [3, 1, 1, 100],
          [4, 4, 2, 0]
        ],
      },
      "want": ((0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3))
    },
  ]

  for test in tests:
    got = maxProfit(**test["args"])

    if test['want'] != got:
      raise Exception(f"maxProfit() = {got}, want {test['want']}")
