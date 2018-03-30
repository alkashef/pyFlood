# py modules
import random as rn
import numpy as np
from plotly import graph_objs as go

# game modules
import settings

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

    # targetColor    = grid(1, 1)
    cell_color = grid[cell[0], cell[1]]
    cell_neighbours = get_neighbours(grid, cell)

    # 1. If target-color is equal to replacement-color, return.
    if chosen_color == target_color:
        return

    # 2. If the color of cell is not equal to target-color, return.
    if cell_color != target_color:
        return

    # 3. Set the color of node to replacement-color.
    grid[cell[0], cell[1]] = chosen_color

    # 4. Perform Flood-fill for all neighbours.
    #for n in range(1, cell_neighbours.shape[0] + 1):
    for n in range(1, cell_neighbours[0] + 1):
        #grid = flood_grid(grid, target_color, chosen_color, cell_neighbours[n,:])
        grid = flood_grid(grid, target_color, chosen_color, cell_neighbours[n])

    return grid

# ------------------------------------------------------------------------------

def flood_grid_old(color):
    size = settings.grid_size

    grid = np.zeros((size, size))

    for i in range(0, size):
        for j in range(0, size):
            grid[i, j] = color

    grid[size-1, size-1] = 6

    return grid

# ------------------------------------------------------------------------------

def initialize_grid(size, no_colors):
    #rn.seed(4321)
    grid = np.zeros((size, size))
    for i in range(0, size):
        for j in range(0, size):
            grid[i, j] = rn.randint(1, no_colors)
    return grid

# ------------------------------------------------------------------------------

def plot_grid(grid, color_map, no_colors):

    layout = go.Layout(
        showlegend=False,
        autosize=False,
        width=400,
        height=400,
        margin=go.Margin(l=0, r=0, b=40, t=40, pad=0),
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
            autorange=True,
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
    size = settings.grid_size
    for i in range(0, size):
        for j in range(0, size):
            if grid[i, j] != grid[1, 1]:
                return False
    return True

# ------------------------------------------------------------------------------

def start_game(grid_size, no_colors, color_map):
    grid = initialize_grid(grid_size, no_colors)
    figure = plot_grid(grid, color_map, no_colors)
    return grid, figure
