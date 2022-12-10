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

"""


class Solution:
    def part_1(self, filename: str) -> int:
        def add_vectors(v0: tuple[int, int], v1: tuple[int, int]) -> tuple[int, int]:
            return (v0[0] + v1[0], v0[1] + v1[1])

        def distance(v0: tuple[int, int], v1: tuple[int, int]) -> int:
            return abs(v0[0] - v1[0]) + abs(v0[1] - v1[1])

        def is_diagonal(v0: tuple[int, int], v1: tuple[int, int]) -> int:
            return v0[0] != v1[0] and v0[1] != v1[1]

        directions = {"U": (1, 0), "R": (0, 1), "D": (-1, 0), "L": (0, -1)}
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

result_part_1 = Solution().part_1("09.input")
print(result_part_1)  # 6269

# result_part_2 = Solution().part_2("09.example2", 9)
# result_part_2 = Solution().part_2("09.input")
# print(result_part_2)  #
