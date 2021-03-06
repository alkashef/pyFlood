# py modules
import random as rn
import numpy as np
from plotly import graph_objs as go

# game modules
from colors import no_colors

# ------------------------------------------------------------------------------

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

# ------------------------------------------------------------------------------

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

# ------------------------------------------------------------------------------

def stupid_bot(grid):
    chosen_color = rn.randint(1, no_colors)
    while(same_color(grid, chosen_color)):
        chosen_color = rn.randint(1, no_colors)
    return chosen_color

# ------------------------------------------------------------------------------

def initialize_grid(size, no_colors):
    #rn.seed(4321)
    grid = np.zeros((size, size))
    for i in range(0, size):
        for j in range(0, size):
            grid[i, j] = rn.randint(1, no_colors)
    return grid

# ------------------------------------------------------------------------------

def reset(string):
    if is_button(string):
        if int(string) == 7:
            return True
    return False

# ------------------------------------------------------------------------------

def is_color_button(string):
    if is_button(string) and int(string) < 7:
        return True
    return False

# ------------------------------------------------------------------------------

def is_bot_button(string):
    if is_button(string) and int(string) == 8:
        return True
    return False

# ------------------------------------------------------------------------------

def plot_grid(grid, color_map, no_colors):

    layout = go.Layout(
        showlegend=False,
        autosize=False,
        width=400,
        height=400,
        margin=go.Margin(l=0, r=0, b=0, t=0, pad=0),
        xaxis=dict(
            autorange=True,
            showgrid=False,
            zeroline=False,
            showline=False,
            autotick=True,
            ticks='',
            showticklabels=False
        ),
        yaxis=dict(
            autorange='reversed', # https://github.com/plotly/plotly.py/issues/413
            showgrid=False,
            zeroline=False,
            showline=False,
            autotick=True,
            ticks='',
            showticklabels=False
        )
    )

    data = [go.Heatmap(z=grid,
                       colorscale=color_map,
                       zmin=1,
                       zmax=no_colors,
                       showscale=False)]

    figure = {'data': data, 'layout': layout}

    return figure

# ------------------------------------------------------------------------------

def game_over(grid):
    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if grid[r, c] != grid[0, 0]:
                return False
    return True

# ------------------------------------------------------------------------------

def start_game(grid_size, no_colors, color_map):
    grid = initialize_grid(grid_size, no_colors)
    figure = plot_grid(grid, color_map, no_colors)
    return grid, figure

# ------------------------------------------------------------------------------

def is_button(string):
    try:
        int(string)
        return True
    except ValueError:
        return False

# ------------------------------------------------------------------------------

def same_color(grid, chosen_color):
    if int(chosen_color) == grid[0, 0]:
        return True
    return False

# ------------------------------------------------------------------------------
