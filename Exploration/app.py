
import dash
import dash_core_components as dcc # higher-level components
import dash_html_components as html # has a component for every HTML tag
import plotly.graph_objs as go
import pandas as pd
import random as rn
import numpy as np

#------------------------------------------------------------------------------

app = dash.Dash()

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

df = pd.read_csv(
    'https://gist.githubusercontent.com/chriddyp/' +
    '5d1ea79569ed194d432e56108a04d188/raw/' +
    'a9f9e8076b837d541398e999dcbac2b2826a81f8/'+
    'gdp-life-exp-2007.csv')

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

app.layout = html.Div(children=[
                            html.H1(
                                children='pyFlood',
                                style={'textAlign': 'left'}
                            ),

                            html.Div(children='A Color Flood Game in Python',
                                     style={'textAlign': 'left'}
                                     ),

                            html.Div(children=[dcc.Graph(
                                                     id='life-exp-vs-gdp',
                                                     figure={
                                                             'data': data,
                                                             'layout': layout
                                                             }
                                                     ),
                                                html.Button('', id='b1', style={'width':'50', 'height':'30', 'background-color':'navy',}),
                                                html.Button('', id='b2', style={'width':'50', 'height':'30', 'background-color':'blue'}),
                                                html.Button('', id='b3', style={'width':'50', 'height':'30', 'background-color':'green'}),
                                                html.Button('', id='b4', style={'width':'50', 'height':'30', 'background-color':'red'}),
                                                html.Button('', id='b5', style={'width':'50', 'height':'30', 'background-color':'orange'}),
                                                html.Button('', id='b6', style={'width':'50', 'height':'30', 'background-color':'yellow'})
                                             ]),


])

#------------------------------------------------------------------------------

if __name__ == '__main__':
    app.run_server(debug=True)

#------------------------------------------------------------------------------
