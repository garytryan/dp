from lecture9_prob2 import uniquePathsWithObstacles


# {
# 	name: "small matrix",
# 	args: args{grid: [][]int{
# 		{0, 0},
# 	}},
# 	want: 1,
# },
# {
# 	name: "simple matrix",
# 	args: args{grid: [][]int{
# 		{0, 0, 0, 0},
# 		{0, 0, 1, 1},
# 		{0, 0, 0, 0},
# 	}},
# 	want: 3,
def test_uniquePathsWithObstacles():
  tests = [
    {
      "name": "small matrix",
      "args": {
          "grid": [
            [0, 0]
          ]
      },
      "want": 1
    },
    {
      "name": "small matrix",
      "args": {
        "grid": [
          [0, 0, 0, 0],
          [0, 0, 1, 1],
          [0, 0, 0, 0]
        ],
      },
      "want": 3
    },
  ]

  for test in tests:
    got = uniquePathsWithObstacles(**test["args"])

    if test['want'] != got:
      raise Exception(f"uniquePathsWithObstacles() = {got}, want {test['want']}")
