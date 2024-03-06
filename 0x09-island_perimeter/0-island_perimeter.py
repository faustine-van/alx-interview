#!/usr/bin/python3
"""0-island_perimeter.py"""


def island_perimeter(grid):
    """returns the perimeter of the island
       args:
            - grid:  a list of lists
        returns:
            perimeter
    """
    p = 0
    rows = len(grid)
    cols = len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                p += 4
                if i < rows - 1 and grid[i + 1][j] == 1:
                    p -= 2
                if j < cols - 1 and grid[i][j + 1] == 1:
                    p -= 2
    return p
