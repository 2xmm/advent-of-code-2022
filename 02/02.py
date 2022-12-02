"""

--- Day 2: Rock Paper Scissors ---

===

input
- file with lines of `str str`
  - A | X = rock ~ 1 point if you select
  - B | Y = paper ~ 2 point if you select
  - C | Z = scissors ~ 3 point if you select
  - A, B, C = move 1 other player
  - X, Y, Z = move 2 your move
  - points from wins
    - 0 if lose
    - 3 if same
    - 6 if win

  - rock beats scissors
  - paper beats rock
  - scissors beats paper

part 1
    output
    - int -- total score

    idea
    - iterate through each line
      - add value of selected move (from dict)
      - add value of round result
        - same = 3
        - tuple comparison
            (rock, scissors) = 0
            (rock, paper) = 6
            (paper, scissors) = 6
            (paper, rock) = 0
            (scissors, rock) = 6
            (scissors, paper) = 0
        - could spend some time to find cleaner solution but this works for now
"""

SAME_SHAPE_DISTANCE = 23


def rock_paper_scissors_part_1(filename: str) -> int:
    result = 0

    shape_value = {
        "X": 1,
        "Y": 2,
        "Z": 3,
    }

    you_win_shape_pair_set = {
        ("A", "Y"),
        ("B", "Z"),
        ("C", "X"),
    }

    with open(filename) as file:
        for line in file:
            opponent_shape, your_shape = (shape.strip() for shape in line.split(" "))
            is_same_shape = ord(your_shape) - ord(opponent_shape) == SAME_SHAPE_DISTANCE

            if is_same_shape:
                result += 3
            elif (opponent_shape, your_shape) in you_win_shape_pair_set:
                result += 6

            result += shape_value[your_shape]

    return result


result_part_1 = rock_paper_scissors_part_1("02.input")
print(result_part_1)  # 14531
