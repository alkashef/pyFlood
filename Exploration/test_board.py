
import random as rn
import numpy as np

# ------------------------------------------------------------------------------

def initialize_grid(size, no_colors):
    rn.seed(4321)
    grid = np.zeros((size, size))
    for r in range(size):
        for c in range(size):
            grid[i, j] = rn.randint(1, no_colors)
    return grid

def hard_coded_grid():
    grid = np.matrix([[1, 11, 111, 1111, -1],
                      [2, 22, 222, 2222, -2],
                      [3, 33, 333, 3333, -3],
                      [4, 44, 444, 4444, -4]])
    return grid

def print_grid(grid):
    for r in range(grid.shape[0]):
        row = ""
        for c in range(grid.shape[1]):
            row = row + "  " + str(grid[r, c])
        print(row)

def get_neighbours(grid, cell):

    cell_neighbours = np.zeros((0, 2))

    if cell[0] > 0:
        cell_neighbours = np.vstack([cell_neighbours, [cell[0] - 1, cell[1]]])

    if cell[1] > 0:
        cell_neighbours = np.vstack([cell_neighbours, [cell[0], cell[1] - 1]])

    if cell[1] < grid.shape[1] - 1:
        cell_neighbours = np.vstack([cell_neighbours, [cell[0], cell[1] + 1]])

    if cell[0] < grid.shape[0] - 1:
        cell_neighbours = np.vstack([cell_neighbours, [cell[0] + 1, cell[1]]])

    return cell_neighbours

def get_neighbours_str(neighbours, grid):
    neighbours_str = ""
    for n in range(neighbours.shape[0]):
        neighbours_str = neighbours_str + " " + str(grid[int(neighbours[n][0]), int(neighbours[n][1])])
    return neighbours_str

# ------------------------------------------------------------------------------

rn.seed(4321)

#g1 = initialize_grid(4, 6)
g1 = hard_coded_grid()
print_grid(g1)

for r in range(g1.shape[0]):
    for c in range(g1.shape[1]):
        neighbours = get_neighbours(g1, [r, c])
        print("neighbours of", g1[r, c], "are:", get_neighbours_str(neighbours, g1))