"""Starting in the top left corner of a 2×2 grid, and only being able
to move to the right and down, there are exactly 6 routes to the bottom
right corner.

How many such routes are there through a 20×20 grid?

"""

import numpy as np


n = 20
grid = np.zeros((n+1, n+1))
grid[0, :] = 1
grid[:, 0] = 1
for i in range(n+1):
    for j in range(n+1):
        if grid[i, j] == 0:
            grid[i, j] = grid[i-1, j] + grid[i, j-1]

print(int(grid[n, n]))
