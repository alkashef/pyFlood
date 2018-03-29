
import plotly.graph_objs as go
import random as rn
import numpy as np
import settings
import colors

#------------------------------------------------------------------------------

rn.seed(4321)

#------------------------------------------------------------------------------

def plotGrid(color):

    size = settings.board_size
    no_colors = colors.no_colors
    color_map = colors.color_map

    board = np.zeros((size, size))

    for i in range(0, size):
        for j in range(0, size):
            board[i, j] = color

    layout = go.Layout(
        autosize = False,
        width = 500,
        height = 500,
        margin = go.Margin(l=50, r=50, b=100, t=100, pad=4),
        xaxis = dict(
            autorange = True,
            showgrid = False,
            zeroline = False,
            showline = False,
            autotick = True,
            ticks = '',
            showticklabels = False
        ),
        yaxis = dict(
            autorange = True,
            showgrid = False,
            zeroline = False,
            showline = False,
            autotick = True,
            ticks = '',
            showticklabels = False
        )
    )

    data = [go.Heatmap(z = board,
                       colorscale = color_map,
                       zmin = 1,
                       zmax = no_colors)]

    return data, layout

#------------------------------------------------------------------------------

def initializeGrid(size, no_colors, color_map):

    board = np.zeros((size, size))
    for i in range(0, size):
        for j in range(0, size):
            board[i, j] = rn.randint(1, no_colors)

    layout = go.Layout(
        autosize = False,
        width = 500,
        height = 500,
        margin = go.Margin(l=50, r=50, b=100, t=100, pad=4),
        xaxis = dict(
            autorange = True,
            showgrid = False,
            zeroline = False,
            showline = False,
            autotick = True,
            ticks = '',
            showticklabels = False
        ),
        yaxis = dict(
            autorange = True,
            showgrid = False,
            zeroline = False,
            showline = False,
            autotick = True,
            ticks = '',
            showticklabels = False
        )
    )

    data = [go.Heatmap(z = board,
                       colorscale = color_map,
                       zmin = 1,
                       zmax = no_colors)]

    return data, layout