"""

--- Day 3: Rucksack Reorganization ---

===

input
- file with lines of str
  - each line has even length
  - each line made up of {a-zA-Z}
  - one character duplicated between first and second half

part 1
    output
    - sum of ordinal values of duplicated character with a=1, Z=52

    idea
    - for each line
        - intersect first and second half character sets

part 2
    output
    - sum of ordinal values of duplicated character between groups of three consecutive lines

    idea
    - for each group of three lines, find common character using set intersections

"""


def get_ordinal_value_from_base(character: str, base: str) -> int:
    return ord(character) - ord(base)


def get_character_value(character: str) -> int:
    if character.islower():
        return 1 + get_ordinal_value_from_base(character, "a")
    else:
        return 27 + get_ordinal_value_from_base(character, "A")


def get_line_value(line: str) -> int:
    result = 0
    midpoint = len(line) // 2
    first_half_characters = set(line[:midpoint])
    second_half_characters = set(line[midpoint:])
    result = get_character_value(
        first_half_characters.intersection(second_half_characters).pop()
    )
    return result


def rucksack_reorganization_part_1(filename: str) -> int:
    result = 0

    with open(filename) as file:
        for line in file:
            result += get_line_value(line.strip())

    return result


def get_line_group_priority(line_group: list[set[str]]) -> int:
    a, b, c = line_group
    return get_character_value(a.intersection(b).intersection(c).pop())


def rucksack_reorganization_part_2(filename: str) -> int:
    result = 0

    with open(filename) as file:
        line_group = []

        for line in file:
            line_group.append(set(line.strip()))

            if len(line_group) == 3:
                result += get_line_group_priority(line_group)
                line_group.clear()

    return result


result_part_1 = rucksack_reorganization_part_1("03.input")
print(result_part_1)  # 8053

result_part_2 = rucksack_reorganization_part_2("03.input")
print(result_part_2)  #
