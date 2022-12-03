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
from enum import IntEnum, StrEnum


def rock_paper_scissors_part_1(filename: str) -> int:
    SAME_SHAPE_DISTANCE = 23

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


def rock_paper_scissors_part_2(filename: str) -> int:
    class ShapeValue(IntEnum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    class RoundValue(IntEnum):
        WIN = 6
        DRAW = 3
        LOSE = 0

    class OpponentShape(StrEnum):
        ROCK = "A"
        PAPER = "B"
        SCISSORS = "C"

    class RoundEndCondition(StrEnum):
        LOSE = "X"
        DRAW = "Y"
        WIN = "Z"

    result = 0

    with open(filename) as file:
        for line in file:
            opponent_shape, round_end_condition = (
                shape.strip() for shape in line.split(" ")
            )

            if round_end_condition == RoundEndCondition.WIN:
                result += RoundValue.WIN
                match opponent_shape:
                    case OpponentShape.ROCK:
                        result += ShapeValue.PAPER
                    case OpponentShape.PAPER:
                        result += ShapeValue.SCISSORS
                    case OpponentShape.SCISSORS:
                        result += ShapeValue.ROCK

            elif round_end_condition == RoundEndCondition.LOSE:
                result += RoundValue.LOSE
                match opponent_shape:
                    case OpponentShape.ROCK:
                        result += ShapeValue.SCISSORS
                    case OpponentShape.PAPER:
                        result += ShapeValue.ROCK
                    case OpponentShape.SCISSORS:
                        result += ShapeValue.PAPER
            else:
                result += RoundValue.DRAW
                match opponent_shape:
                    case OpponentShape.ROCK:
                        result += ShapeValue.ROCK
                    case OpponentShape.PAPER:
                        result += ShapeValue.PAPER
                    case OpponentShape.SCISSORS:
                        result += ShapeValue.SCISSORS

    return result


# with inspiration from r/adventofcode
def rock_paper_scissors_part_2_simplified(filename: str) -> int:
    result = 0
    score = {
        "AX": 3,
        "AY": 4,
        "AZ": 8,
        "BX": 1,
        "BY": 5,
        "BZ": 9,
        "CX": 2,
        "CY": 6,
        "CZ": 7,
    }

    with open(filename) as file:
        for line in file:
            round = line.strip().replace(" ", "")
            result += score[round]

    return result


result_part_1 = rock_paper_scissors_part_1("02.input")
print(result_part_1)  # 14531

result_part_2 = rock_paper_scissors_part_2("02.input")
print(result_part_2)  # 11258

result_part_2 = rock_paper_scissors_part_2_simplified("02.input")
print(result_part_2)  # 11258
