"""

--- Day 7: No Space Left On Device ---

===

input
- file of lines of str
- each line a command (ls or cd) or the result of a command

part 1
    output
    - int
      - Find all of the directories with a total size of at most 100_000.
      - What is the sum of the total sizes of those directories?

    idea
    - build graph using a dict containing links to all folders and the files within them
    - use dfs to calculate the total size of each folder in the graph
      - if that folder is less than 100_000, add it to the result
"""


class Node:
    def __init__(self):
        self.parent = None
        self.children = {}
        self.local_size = 0
        self.total_size = 0


class Solution:
    def build_graph(self, filename: str) -> dict:
        node = Node()
        root = node

        with open(filename) as file:
            for line in file:
                line = line.strip()

                # new command
                if line.startswith("$"):
                    command = line[2:]

                    if command == "cd /":
                        node = root

                    elif command.startswith("cd"):
                        target_folder = command.replace("cd ", "")

                        if target_folder == ".." and node.parent:
                            node = node.parent
                        else:
                            node = node.children[target_folder]

                elif line.startswith("dir"):
                    child_folder = line.replace("dir ", "")
                    node.children[child_folder] = Node()
                    node.children[child_folder].parent = node

                # must be a file
                else:
                    size, filename = line.split(" ")
                    size = int(size)
                    node.local_size += size

        return root

    def part_1(self, filename: str, size_max: int) -> int:
        def dfs(node: Node) -> int:
            total_size = node.local_size
            bounded_size = 0

            if node.children:
                for child in node.children.values():
                    child_bounded_size, child_total_size = dfs(child)
                    bounded_size += child_bounded_size
                    total_size += child_total_size

            if total_size <= size_max:
                bounded_size += total_size

            return bounded_size, total_size

        root = self.build_graph(filename=filename)
        result, _ = dfs(root)

        return result

    def part_2(self, filename: str, total_space: int, required_space: int) -> int:
        def augment_with_folder_size(self, node: Node) -> int:
            total_size = node.local_size
            for child in node.children.values():
                total_size += self.augment_with_folder_size(child)
            node.total_size = total_size
            return total_size

        def dfs(node: Node, minimum_folder_size: int, smallest_size: int) -> int:

            # early exit
            if node.total_size < minimum_folder_size:
                return smallest_size

            if minimum_folder_size <= node.total_size < smallest_size:
                smallest_size = node.total_size

            for child in node.children.values():
                smallest_size = min(
                    smallest_size, dfs(child, minimum_folder_size, smallest_size)
                )

            return smallest_size

        # initial pass to build graph O(n)
        root = self.build_graph(filename=filename)

        # additional pass to calculate folder sizes O(n)
        augment_with_folder_size(root)

        available_space = total_space - root.total_size
        remainder_required = required_space - available_space

        # final pass to calculate minimum folder size to delete
        result = dfs(root, remainder_required, root.total_size)
        return result


result_part_1 = Solution().part_1(filename="07.input", size_max=100_000)
print(result_part_1)  # 1428881

result_part_2 = Solution().part_2(
    filename="07.input", total_space=70_000_000, required_space=30_000_000
)
print(result_part_2)  # 10475598
