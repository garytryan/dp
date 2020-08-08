from lecture11 import fib, fibTopDown, fibBottomUpDPForward, fibBottomUpDPBackward


def test_fib():
  tests = [
    {
      "name": "base case #1",
      "args": {
        "n": 0
      },
      "want": 0
    },
    {
      "name": "base case #1",
      "args": {
        "n": 1
      },
      "want": 1
    },
    {
      "name": "base case #1",
      "args": {
        "n": 2
      },
      "want": 1
    },
    {
      "name": "simple test case",
      "args": {
        "n": 10
      },
      "want": 55
    },
  ]

  for test in tests:
    got = fib(**test["args"])

    if test['want'] != got:
      raise Exception(f"fib() = {got}, want {test['want']}")



def test_fibTopDown():
  tests = [
    {
      "name": "base case #1",
      "args": {
        "n": 0
      },
      "want": 0
    },
    {
      "name": "base case #1",
      "args": {
        "n": 1
      },
      "want": 1
    },
    {
      "name": "base case #1",
      "args": {
        "n": 2
      },
      "want": 1
    },
    {
      "name": "simple test case",
      "args": {
        "n": 10
      },
      "want": 55
    },
  ]

  for test in tests:
    got = fibTopDown(**test["args"])

    if test['want'] != got:
      raise Exception(f"fibTopDown() = {got}, want {test['want']}")


def test_fibBottomUpDPForward():
  tests = [
    {
      "name": "base case #1",
      "args": {
        "n": 0
      },
      "want": 0
    },
    {
      "name": "base case #1",
      "args": {
        "n": 1
      },
      "want": 1
    },
    {
      "name": "base case #1",
      "args": {
        "n": 2
      },
      "want": 1
    },
    {
      "name": "simple test case",
      "args": {
        "n": 10
      },
      "want": 55
    },
  ]

  for test in tests:
    got = fibBottomUpDPForward(**test["args"])

    if test['want'] != got:
      raise Exception(f"fibBottomUpDPForward() = {got}, want {test['want']}")


def test_fibBottomUpDPBackward():
  tests = [
    {
      "name": "base case #1",
      "args": {
        "n": 0
      },
      "want": 0
    },
    {
      "name": "base case #1",
      "args": {
        "n": 1
      },
      "want": 1
    },
    {
      "name": "base case #1",
      "args": {
        "n": 2
      },
      "want": 1
    },
    {
      "name": "simple test case",
      "args": {
        "n": 10
      },
      "want": 55
    },
  ]

  for test in tests:
    got = fibBottomUpDPBackward(**test["args"])

    if test['want'] != got:
      raise Exception(f"fibBottomUpDPBackward() = {got}, want {test['want']}")
