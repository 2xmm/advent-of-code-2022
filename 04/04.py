"""

--- Day 4: Camp Cleanup ---

===

input
- file with lines of int range pairs `int-int,int-int`

part 1
    output
    - int -- how many assignment pairs does one range fully contain the other?

    idea
    - sort pairs so that smallest number comes first
      - guaranteed that smallest number within range comes first? -> yes
    - with sorted pairs
      - if second pair ending number <= first pair ending number, fully contained
        - does <= imply fully contained? -> yes

part 2
    output
    - int -- how many assignment pairs do the ranges overlap?

    idea
    - can rewrite as total lines less no overlap pairs
    - sort by first element, if s2 > e1, +1 no_overlap
    - result = total - no_overlap

"""


def get_integer_pairs(line: str) -> list[tuple[int, int]]:
    pairs = [
        (int(a), int(b)) for a, b in [v.split("-") for v in line.strip().split(",")]
    ]
    return pairs


def camp_cleanup_part_1(filename: str) -> int:
    result = 0

    with open(filename) as file:
        for line in file:
            pairs = get_integer_pairs(line.strip())
            (s1, e1), (s2, e2) = pairs

            if s1 <= s2 and e1 >= e2 or s2 <= s1 and e2 >= e1:
                result += 1

    return result


def camp_cleanup_part_2(filename: str) -> int:
    total_lines = 0
    no_overlap = 0

    with open(filename) as file:
        for line in file:
            total_lines += 1

            pairs = get_integer_pairs(line.strip())
            pairs.sort(key=lambda x: x[0])

            (s1, e1), (s2, _) = pairs
            assert s1 <= s2

            if s2 > e1:
                no_overlap += 1

    return total_lines - no_overlap


result_part_1 = camp_cleanup_part_1("04.input")
print(result_part_1)  # 582

result_part_2 = camp_cleanup_part_2("04.input")
print(result_part_2)  # 893
