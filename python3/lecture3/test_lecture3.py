from lecture3 import nSum


def test_nSum():
  tests = [
    {
      "name": "edge case #1",
      "args": {
          "n": 0,
      },
      "want": 0,
    },
    {
      "name": "edge case #2",
      "args": {
          "n": 1,
      },
      "want": 1,
    },
    {
      "name": "simple test #1",
      "args": {
          "n": 5,
      },
      "want": 15,
    },
  ]

  for test in tests:
    got = nSum(**test["args"])

    if test['want'] != got:
      raise Exception(f"nSum() = {got}, want {test['want']}")
