from lecture9_prob1 import uniquePaths


def test_uniquePaths():
  tests = [
    {
      "name": "small matrix",
      "args": {
          "m": 1,
          "n": 1
      },
      "want": 1
    },
    {
      "name": "small matrix",
      "args": {
          "m": 3,
          "n": 4
      },
      "want": 10
    },
  ]

  for test in tests:
    got = uniquePaths(**test["args"])

    if test['want'] != got:
      raise Exception(f"uniquePaths() = {got}, want {test['want']}")
