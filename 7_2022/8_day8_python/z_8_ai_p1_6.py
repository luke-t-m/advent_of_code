import os
import sys
from typing import List


def main():
    with open(os.path.join(sys.path[0], "8_input"), "r") as f:
        lines = f.readlines()

    trees = []
    for line in lines:
        line = line.rstrip()
        trees.append([int(x) for x in line])

    # count the number of trees on the edge
    num_trees = sum([1 for x in trees[0] if x > 0])
    num_trees += sum([1 for x in trees[-1] if x > 0])
    num_trees += sum([1 for row in trees[1:-1] for x in row if x == row[0]])
    num_trees += sum([1 for row in trees[1:-1] for x in row if x == row[-1]])

    # count the number of trees in the interior
    num_trees += count_trees(trees)

    print(num_trees)


def count_trees(trees: List[List[int]]) -> int:
    num_trees = 0
    for i in range(1, len(trees) - 1):
        for j in range(1, len(trees[i]) - 1):
            if trees[i][j] > 0:
                if trees[i][j] > trees[i - 1][j]:
                    num_trees += 1
                if trees[i][j] > trees[i + 1][j]:
                    num_trees += 1
                if trees[i][j] > trees[i][j - 1]:
                    num_trees += 1
                if trees[i][j] > trees[i][j + 1]:
                    num_trees += 1
    return num_trees


if __name__ == "__main__":
    main()