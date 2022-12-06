"""

--- Day 6: Tuning Trouble ---

===

input
- file with a single line of str

part 1
    output
    - number of characters until a unique pattern of length 4 appears

    idea
    - sliding window
    - maintain dict of char counts
      - increment when char seen
      - decrement char at index - pattern_length once index >= pattern_length

part 2
    output
    - number of characters until a unique pattern of length 14 appears

"""
from collections import defaultdict


class Solution:
    def __init__(self, unique_pattern_length: int) -> None:
        self.unique_pattern_length = unique_pattern_length

    def characters_before_first_marker(
        self,
        line: str,
    ) -> int:
        char_to_count = defaultdict(int)

        for index, char in enumerate(line):

            # remove char outside sliding window
            if index >= self.unique_pattern_length:
                removed_char = line[index - self.unique_pattern_length]
                char_to_count[removed_char] -= 1
                if char_to_count[removed_char] == 0:
                    del char_to_count[removed_char]

            # add new char now inside sliding window
            char_to_count[char] += 1

            if len(char_to_count) == self.unique_pattern_length:
                return index + 1

        return -1

    def ending_character(self, filename: str) -> None:
        result = 0

        with open(filename) as file:
            for line in file:
                print(self.characters_before_first_marker(line.strip()))


result_part_1 = Solution(unique_pattern_length=4).ending_character("06.example")
result_part_1 = Solution(unique_pattern_length=4).ending_character("06.input")  # 1953

result_part_2 = Solution(unique_pattern_length=14).ending_character("06.example")
result_part_2 = Solution(unique_pattern_length=14).ending_character("06.input")
