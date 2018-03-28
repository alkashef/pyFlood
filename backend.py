
import plotly.graph_objs as go
import random as rn
import numpy as np

#------------------------------------------------------------------------------

size = 18
rn.seed(4321)
no_colors = 6

board = np.zeros((size, size))
for i in range(0, size):
    for j in range(0, size):
        board[i, j] = rn.randint(1, no_colors)

navy   = 'rgb(0  , 0  , 128)'
blue   = 'rgb(30 , 144, 255)'
green  = 'rgb(0  , 128, 0  )'
red    = 'rgb(255,  10, 10 )'
orange = 'rgb(255, 140, 0  )'
yellow = 'rgb(255, 255, 0  )'

color_map=[[0.00, navy],
           [0.16, navy],
           [0.16, blue],
           [0.33, blue],
           [0.33, green],
           [0.50, green],
           [0.50, red],
           [0.66, red],
           [0.66, orange],
           [0.83, orange],
           [0.83, yellow],
           [1.00, yellow]]

data = [go.Heatmap(z=board, colorscale=color_map, zmin=1, zmax=no_colors)]

layout = go.Layout(
    autosize=False,
    width=500,
    height=500,
    margin=go.Margin(l=50, r=50, b=100, t=100, pad=4),
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

#------------------------------------------------------------------------------
