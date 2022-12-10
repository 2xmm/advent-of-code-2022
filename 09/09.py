"""

--- Day 9: Rope Bridge ---

===

input
- file of lines of string 
- each line a move with format format `str int`

part 1
    output
    - int -- How many positions does the tail of the rope visit at least once?

    idea
    - maintain coords of tail in a set
    - result is length of set
    - update position of T based on H's move
    - assume start position is 0,0, there is no boundary


    three cases for R 2

    TH       TH       TH
    ---- -> ---- -> ----

    T        T
    H         H       TH
    ---- -> ---- -> ----

    H        H      TH
    T       T       
    ---- -> ---- -> ----

     H      >H  # distance > 1
    T      T

part 2
    output

    idea
    - watch the L shaped offsets
           1    1
     1          2
    2     2

    - head position minus direction vector

                  H          H
        H                    1
    4321      4321       432 
"""
up = (1, 0)
down = (-1, 0)
left = (0, -1)
right = (0, 1)
directions = {"U": up, "R": right, "D": down, "L": left}


def add_vectors(v0: tuple[int, int], v1: tuple[int, int]) -> tuple[int, int]:
    return (v0[0] + v1[0], v0[1] + v1[1])


def subtract_vectors(v0: tuple[int, int], v1: tuple[int, int]) -> tuple[int, int]:
    return (v0[0] - v1[0], v0[1] - v1[1])


def distance(v0: tuple[int, int], v1: tuple[int, int]) -> int:
    return abs(v0[0] - v1[0]) + abs(v0[1] - v1[1])


def is_diagonal(v0: tuple[int, int], v1: tuple[int, int]) -> int:
    return v0[0] != v1[0] and v0[1] != v1[1]


def part_1(
    filename: str,
) -> int:
    seen = set()
    t_pos = h_pos = (0, 0)
    seen.add(t_pos)

    with open(filename) as file:
        for line in file:
            direction, count = line.strip().split(" ")
            count = int(count)
            direction_vector = directions[direction]

            for _ in range(count):
                was_diagonal = is_diagonal(h_pos, t_pos)
                h_pos_new = add_vectors(h_pos, direction_vector)

                # t doesn't move
                if not was_diagonal and is_diagonal(h_pos_new, t_pos):
                    pass

                # t must follow h
                elif distance(h_pos_new, t_pos) > 1:
                    t_pos = h_pos
                    seen.add(t_pos)

                h_pos = h_pos_new

    return len(seen)


def part_2(filename: str, rope_length: int) -> int:
    seen = set()
    rope = [(0, 0) for _ in range(rope_length)]
    seen.add(rope[0])

    with open(filename) as file:
        for line in file:
            direction, count = line.strip().split(" ")
            count = int(count)
            direction_vector = directions[direction]

            for _ in range(count):
                # always move head
                rope[0] = add_vectors(rope[0], direction_vector)

                for index in range(1, rope_length):
                    lead_pos = rope[index - 1]
                    delta_row, delta_col = subtract_vectors(lead_pos, rope[index])

                    # move tail if there's a gap of at least 2 spaces in any direction
                    if abs(delta_row) >= 2 or abs(delta_col) >= 2:

                        # knot is either inline or on some diagonal, fill that space
                        if delta_row >= 1:
                            rope[index] = add_vectors(rope[index], up)
                        elif delta_row <= -1:
                            rope[index] = add_vectors(rope[index], down)

                        if delta_col >= 1:
                            rope[index] = add_vectors(rope[index], right)
                        elif delta_col <= -1:
                            rope[index] = add_vectors(rope[index], left)

                seen.add(rope[-1])
    return len(seen)


result_part_1 = part_1("09.input")
print(result_part_1)  # 6269

result_part_2 = part_2("09.input", 10)
print(result_part_2)  # 2557
