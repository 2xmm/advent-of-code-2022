"""

--- Day 5: Supply Stacks ---

===

input
- file with stack definitions followed by instructions
- unusual parsing requirements

part 1
    output
    - str -- what crate ends up on top of each stack?

    idea
    - parse file
      - look for first move command, 2 lines before that we have number of stack
      - create a dict with number keys and list values
      - start from bottom and build stacks upwards into the dict lists
      - know stack value positions based on number positions
    - parse command
    - apply commands
      - add assertions to catch any errors at runtime

part 2
    idea
    - reverse list when applying move command

"""
import re
from enum import Enum


class CrateMoverVersion(Enum):
    CRATE_MOVER_9000 = 1
    CRATE_MOVER_9001 = 2


class SupplyStacks:
    def __init__(self, crate_mover_version: CrateMoverVersion) -> None:
        assert crate_mover_version in list(CrateMoverVersion)
        self.crate_mover_version = crate_mover_version
        self.stacks = {}

    def parse_stack_definition(
        self, stack_index_line: str, stack_definition_lines: list[str]
    ) -> None:
        stack_key_to_index = {}

        # initialize stacks
        for index, char in enumerate(stack_index_line):
            if char.isnumeric():
                stack_key = int(char)
                stack_key_to_index[stack_key] = index
                self.stacks[stack_key] = []

        # build stacks
        for stack_definition_line in stack_definition_lines[::-1]:
            for stack_key, line_index in stack_key_to_index.items():
                char_at_index = stack_definition_line[line_index]
                if char_at_index.strip():
                    self.stacks[stack_key].append(char_at_index)

    def parse_command(self, line: str) -> tuple:
        numbers = re.findall(r"\d+", line)
        return tuple(map(int, numbers))

    def apply_command(self, quantity, from_stack, to_stack) -> None:
        assert len(self.stacks[from_stack]) >= quantity

        moved_items = []
        for _ in range(quantity):
            moved_items.append(self.stacks[from_stack].pop())

        if self.crate_mover_version == CrateMoverVersion.CRATE_MOVER_9000:
            self.stacks[to_stack] += moved_items
        else:
            self.stacks[to_stack] += moved_items[::-1]

    def parse(self, filename: str) -> str:
        result = ""
        stack_definition_lines = []

        with open(filename) as file:
            for line in file:

                # skip empty lines
                if not line.strip():
                    continue

                # line with stack number definitions, this wouldn't work if num stacks > 9
                elif line.strip().replace(" ", "").isnumeric():
                    self.parse_stack_definition(line, stack_definition_lines)

                # if we haven't already defined the stacks, must be in the stack definition
                elif not self.stacks:
                    stack_definition_lines.append(line)

                # we must be in the moves
                else:
                    quantity, from_stack, to_stack = self.parse_command(line.strip())
                    self.apply_command(quantity, from_stack, to_stack)

        for index in range(1, 1 + len(self.stacks)):
            result += self.stacks[index].pop() if self.stacks[index] else ""

        return result


result_part_1 = SupplyStacks(CrateMoverVersion.CRATE_MOVER_9000).parse("05.input")
print(result_part_1)  # SVFDLGLWV

result_part_2 = SupplyStacks(CrateMoverVersion.CRATE_MOVER_9001).parse("05.input")
print(result_part_2)  # DCVTCVPCL
