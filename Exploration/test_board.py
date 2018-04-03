
import random as rn
import numpy as np
import time

# ------------------------------------------------------------------------------

def random_grid(size, no_colors):
    rn.seed(4321)
    grid = np.zeros((size, size))
    for r in range(size):
        for c in range(size):
            grid[r, c] = rn.randint(1, no_colors)
    return grid

def hard_coded_grid():
    grid = np.matrix([[1, 11, 111, 1111, -1],
                      [2, 22, 222, 2222, -2],
                      [3, 33, 333, 3333, -3],
                      [4, 44, 444, 4444, -4]])
    return grid

def hard_coded_grid2():
    grid = np.matrix([[1, 0, 1, 1, 1],
                      [0, 0, 2, 2, 2],
                      [2, 2, 3, 3, 0],
                      [3, 3, 3, 2, 0]])
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

def game_over(grid):
    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if grid[r, c] != grid[0, 0]:
                return False
    return True

def flood_grid(grid, target_color, chosen_color, cell):

    # Source: http://en.wikipedia.org/wiki/Flood_fill
    #         Stack-based recursive implementation (Four-way)

    original_grid = grid

    #target_color = grid[0, 0]
    cell_color = grid[int(cell[0]), int(cell[1])]
    cell_neighbours = get_neighbours(grid, cell)

    # 1. If target-color is equal to replacement-color, return.
    if chosen_color == target_color:
        return original_grid

    # 2. If the color of cell is not equal to target-color, return.
    if cell_color != target_color:
        return original_grid

    # 3. Set the color of node to replacement-color.
    grid[int(cell[0]), int(cell[1])] = chosen_color

    # 4. Perform Flood-fill for all neighbours.
    for n in range(cell_neighbours.shape[0]):
        grid = flood_grid(grid, target_color, chosen_color, cell_neighbours[n])

    return grid

def play(grid, color):
    if not game_over(grid):
        flood_grid(grid, grid[0, 0], color, [0, 0])
        print_grid(grid)
        print("--------------------------")
        time.sleep(2)
    else:
        print("Game over")
    return np.matrix(grid)

# ------------------------------------------------------------------------------

rn.seed(4321)

g1 = hard_coded_grid2()
#print_grid(g1)

#for r in range(g1.shape[0]):
#    for c in range(g1.shape[1]):
#        neighbours = get_neighbours(g1, [r, c])
#        print("neighbours of", g1[r, c], "are:", get_neighbours_str(neighbours, g1))

print_grid(g1)
print("-------------------")
g1 = play(g1, 0)
g1 = play(g1, 2)
g1 = play(g1, 3)
g1 = play(g1, 1)
g1 = play(g1, 2)
g1 = play(g1, 0)
g1 = play(g1, 1)
