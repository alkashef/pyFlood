# py modules
import random as rn
import numpy as np
from plotly import graph_objs as go

# game modules
import settings

# ------------------------------------------------------------------------------

def flood_grid(color):
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
