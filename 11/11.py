"""

--- Day 11: Monkey in the Middle ---

===

input
- file of lines of money descriptions as str

part 1
    output
    - int
    - monkey business is the product of the two most active monkeys
    - What is the level of monkey business after 20 rounds of stuff-slinging simian shenanigans?

    idea
    - parse monkeys
    - use eval for expression

part 2
    idea
    - set worry level to the remainder after divinding by the least common multiple of all divisors
"""
import math

lines = [line for line in open("11.input").read().splitlines() if line.strip()]


class Monkey:
    def __init__(
        self,
        starting_items: list[int],
        operation: str,
        divisor: int,
        divisor_success: int,
        divisor_failure: int,
    ):
        self.items = starting_items
        self.operation = operation
        self.divisor_success = divisor_success
        self.divisor_failure = divisor_failure
        self._inspection_count = 0
        self._divisor = divisor

    @property
    def inspection_count(self):
        return self._inspection_count

    @property
    def divisor(self):
        return self._divisor

    def catch_item(self, item: int):
        self.items.append(item)

    def apply_worry_operation(self, old: int) -> int:
        return eval(self.operation)

    def has_items(self):
        return len(self.items) > 0

    def inspect_item(self, worry_level_divisor: int) -> tuple[int, int]:
        self._inspection_count += 1
        item = self.items.pop(0)
        worry_level = self.apply_worry_operation(item)
        bored_level = worry_level // worry_level_divisor
        target_monkey = (
            self.divisor_success
            if bored_level % self.divisor == 0
            else self.divisor_failure
        )
        return target_monkey, bored_level


def parse_monkeys(lines: list[str]) -> list[Monkey]:
    result = []
    for index in range(0, len(lines), 6):
        monkey_slice = lines[index : index + 6][1:]
        items = [int(v.strip()) for v in monkey_slice[0].split(":")[1].split(",")]
        operation = monkey_slice[1].split("=")[1].strip()
        divisor = int(monkey_slice[2].split(" ")[-1])
        divisor_success = int(monkey_slice[3].split(" ")[-1])
        divisor_failure = int(monkey_slice[4].split(" ")[-1])
        monkey = Monkey(
            starting_items=items,
            operation=operation,
            divisor=divisor,
            divisor_success=divisor_success,
            divisor_failure=divisor_failure,
        )
        result.append(monkey)

    return result


def part_1(num_rounds: int) -> int:
    monkeys = parse_monkeys(lines)

    for _ in range(num_rounds):
        for monkey in monkeys:
            while monkey.has_items():
                target_monkey, item = monkey.inspect_item(worry_level_divisor=3)
                monkeys[target_monkey].catch_item(item)

    inspection_counts = sorted([m.inspection_count for m in monkeys])
    return inspection_counts[-2] * inspection_counts[-1]


def part_2(num_rounds: int) -> int:
    monkeys = parse_monkeys(lines)
    least_common_multiple = math.lcm(*[m.divisor for m in monkeys])

    for _ in range(num_rounds):
        for monkey in monkeys:
            while monkey.has_items():
                target_monkey, item = monkey.inspect_item(worry_level_divisor=1)
                item = item % least_common_multiple
                monkeys[target_monkey].catch_item(item)

    inspection_counts = sorted([m.inspection_count for m in monkeys])
    return inspection_counts[-2] * inspection_counts[-1]


result_part_1 = part_1(num_rounds=20)
print(result_part_1)  # 88208

result_part_2 = part_2(num_rounds=10_000)
print(result_part_2)  # 21115867968
