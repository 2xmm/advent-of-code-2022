"""

--- Day 10: Cathode-Ray Tube ---

===

input
- instructions
  - noop -- 1 cycle
  - addx int -- 2 cycles, add int to X register

- signal strength
  - cycle number * value of X register

part 1
    output
    - int
    - Find the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles. What is the sum of these six signal strengths?

    idea
    - need to ensure changes to X register only happen after end of cycle

"""
lines = [line.split() for line in open("10.input").read().splitlines()]


def part_1() -> int:
    result = 0
    x = 1
    cycle = 1

    def execute_cycle():
        nonlocal result, cycle
        if (cycle - 20) % 40 == 0:
            result += cycle * x
        cycle += 1

    for instruction in lines:
        execute_cycle()

        if instruction[0] == "addx":
            execute_cycle()
            x += int(instruction[1])

    return result


def part_2() -> str:
    result = ""
    x = 1
    cycle = 1

    def execute_cycle():
        nonlocal result, cycle

        if (cycle - 1) % 40 in (x - 1, x, x + 1):
            result += "#"
        else:
            result += "."

        if cycle % 40 == 0:
            result += "\n"

        cycle += 1

    for instruction in lines:
        execute_cycle()

        if instruction[0] == "addx":
            execute_cycle()
            x += int(instruction[1])

    return result


result_part_1 = part_1()
print(result_part_1)  # 13140

result_part_2 = part_2()
print(result_part_2)  # PAPKFKEJ
