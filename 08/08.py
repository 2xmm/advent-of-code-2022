"""

--- Day 8: Treetop Tree House ---

===

input
- lines of str representing grid of ints

part 1
    output
    - int -- how many trees are visible from outside the grid?

    idea
    - convert file to 2d array of ints
    - pass from each direction looking for visible trees, add coords to visible set
    - union each set to ensure we don't double count if a tree is visible from multiple directions
    - can unify all passes in a single method

part 2
    output
    - int -- What is the highest scenic score possible for any tree?

    idea
    - brute force first
    - then look for ways to reduce duplicated work
"""


class Solution:
    def part_1(self, filename: str) -> int:
        visible = set()
        grid = []

        with open(filename) as file:
            for line in file:
                grid.append([int(v) for v in list(line.strip())])

        num_rows = len(grid)
        num_cols = len(grid[0])

        # left to right
        for row in range(num_rows):
            max_height = -1
            for col in range(num_cols):
                height = grid[row][col]
                if height > max_height:
                    visible.add((row, col))
                    max_height = height

        # right to left
        for row in range(num_rows):
            max_height = -1
            for col in range(num_cols - 1, -1, -1):
                height = grid[row][col]
                if height > max_height:
                    visible.add((row, col))
                    max_height = height

        # top to bottom
        for col in range(num_cols):
            max_height = -1
            for row in range(num_rows):
                height = grid[row][col]
                if height > max_height:
                    visible.add((row, col))
                    max_height = height

        # bottom to top
        for col in range(num_cols):
            max_height = -1
            for row in range(num_rows - 1, -1, -1):
                height = grid[row][col]
                if height > max_height:
                    visible.add((row, col))
                    max_height = height

        return len(visible)

    def part_2(self, filename: str) -> int:
        def get_scenic_score(grid: list, tree_row: int, tree_col: int) -> int:
            height = grid[tree_row][tree_col]

            down_score = 0
            for row in range(tree_row + 1, num_rows):
                if grid[row][tree_col] >= height:
                    down_score += 1
                    break
                down_score += 1

            right_score = 0
            for col in range(tree_col + 1, num_cols):
                if grid[tree_row][col] >= height:
                    right_score += 1
                    break
                right_score += 1

            up_score = 0
            for row in range(tree_row - 1, -1, -1):
                if grid[row][tree_col] >= height:
                    up_score += 1
                    break
                up_score += 1

            left_score = 0
            for col in range(tree_col - 1, -1, -1):
                if grid[tree_row][col] >= height:
                    left_score += 1
                    break
                left_score += 1

            return down_score * up_score * left_score * right_score

        result = -1
        grid = []

        with open(filename) as file:
            for line in file:
                grid.append(list(map(int, line.strip())))

        num_rows = len(grid)
        num_cols = len(grid[0])

        for row in range(num_rows):
            for col in range(num_cols):
                result = max(result, get_scenic_score(grid, row, col))

        return result


result_part_1 = Solution().part_1("08.input")
print(result_part_1)  # 1803

result_part_2 = Solution().part_2("08.input")
print(result_part_2)  # 268912
