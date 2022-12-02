"""
--- Day 1: Calorie Counting ---

===

input
- file with lines of int
  - each int number of calories in a meal
  - blank line separates each elf

part 1
    output
    - int -- elf with most calories

    idea
    - iterate through input accumulating sum until blank
    - maintain largest quantity using max

part 2
    output
    - int -- sum of calories carried by the top 3 elfs'

    idea
    - iterate through input accumulating sum until blank
    - use heap to maintain sorted list of top 3 values
    - sum terminal values of heap for result

test
- empty file
- single line without additional blanks
- blank between multiple numbers
"""
from heapq import heappush, heappop


def calorie_counting_part_1(filename: str) -> int:
    result = 0
    elf_sum = 0

    with open(filename) as file:
        for line in file:
            if line.strip() == "":
                result = max(result, elf_sum)
                elf_sum = 0
            else:
                elf_sum += int(line)

    return result


def calorie_counting_part_2(filename: str) -> int:
    heap = []
    elf_sum = 0

    with open(filename) as file:
        for line in file:
            if line.strip() == "":
                if len(heap) < 3 or elf_sum > heap[0]:
                    heappush(heap, elf_sum)

                    if len(heap) > 3:
                        heappop(heap)
                elf_sum = 0
            else:
                elf_sum += int(line)

    return sum(heap)


result_part_1 = calorie_counting_part_1("01.input")
print(result_part_1)  # 72240

result_part_2 = calorie_counting_part_2("01.input")
print(result_part_2)  # 210957
