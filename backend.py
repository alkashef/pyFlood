
# py modules
import random as rn
import numpy as np

# game modules
import settings
import colors
from backend_helper import plot_grid

# ------------------------------------------------------------------------------

def one_color_grid(color):

    size = settings.board_size
    no_colors = colors.no_colors
    color_map = colors.color_map

    board = np.zeros((size, size))

    for i in range(0, size):
        for j in range(0, size):
            board[i, j] = color

    data, layout = plot_grid(board, color_map, no_colors)

    return data, layout

# ------------------------------------------------------------------------------

def initialize_grid(size, no_colors, color_map):

    rn.seed(4321)

    board = np.zeros((size, size))

    for i in range(0, size):
        for j in range(0, size):
            board[i, j] = rn.randint(1, no_colors)

    data, layout = plot_grid(board, color_map, no_colors)

    return data, layout
