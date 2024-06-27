#!/usr/bin/python3
"""Calculate the perimeter of an island in a grid."""


def island_perimeter(grid):
    """Calculate island perimeter in grid.

    Args:
        grid (list of list of int): Grid representation of the island.

    Returns:
        int: Perimeter of the island.
    """
    perim = 0
    rows, cols = len(grid), len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perim += 4
                if i > 0 and grid[i - 1][j] == 1:
                    perim -= 1
                if i < rows - 1 and grid[i + 1][j] == 1:
                    perim -= 1
                if j > 0 and grid[i][j - 1] == 1:
                    perim -= 1
                if j < cols - 1 and grid[i][j + 1] == 1:
                    perim -= 1

    return perim
