
import dash
import dash_core_components as dcc # higher-level components
import dash_html_components as html # has a component for every HTML tag
from dash.dependencies import Input, Output, State
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
                                                     id='board',
                                                     figure={
                                                             'data': data,
                                                             'layout': layout
                                                             }
                                                     ),
    # https://community.plot.ly/t/input-two-or-more-button-how-to-tell-which-button-is-pressed/5788/26
    # maral Mar 18, 2018 5:35 am
                                                html.Button('1', id='b1', n_clicks=0, style={'width':'50', 'height':'30', 'background-color':'navy',}),
                                                html.Button('2', id='b2', n_clicks=0, style={'width':'50', 'height':'30', 'background-color':'blue'}),
                                                html.Button('3', id='b3', n_clicks=0, style={'width':'50', 'height':'30', 'background-color':'green'}),
                                                html.Button('4', id='b4', n_clicks=0, style={'width':'50', 'height':'30', 'background-color':'red'}),
                                                html.Button('5', id='b5', n_clicks=0, style={'width':'50', 'height':'30', 'background-color':'orange'}),
                                                html.Button('6', id='b6', n_clicks=0, style={'width':'50', 'height':'30', 'background-color':'yellow'}),
                                                html.Div(id='clicked-button', children='b1:0 b2:0 b3:0 b4:0 b5:0 b6:0 last:nan', style={'display': 'none'})
                                             ]),

                            html.Div(id='display-clicked', children="")
])

@app.callback(
        Output(component_id='board', component_property='figure'),
        #Output('display-clicked', 'children'),
        [Input(component_id='clicked-button', component_property='children')]
)

def update_figure(clicked):

    last_clicked = clicked[-1:]

    board = np.zeros((size, size))

    for i in range(0, size):
        for j in range(0, size):
            board[i, j] = last_clicked

    data = [go.Heatmap(z=board, colorscale=color_map, zmin=1, zmax=no_colors)]

    figure = {'data': data, 'layout': layout}

    return figure

    #return last_clicked

@app.callback(
    Output('clicked-button', 'children'),
    [Input('b1', 'n_clicks'),
     Input('b2', 'n_clicks'),
     Input('b3', 'n_clicks'),
     Input('b4', 'n_clicks'),
     Input('b5', 'n_clicks'),
     Input('b6', 'n_clicks')],
    [State('clicked-button', 'children')]
)

def updated_clicked(b1_clicks, b2_clicks, b3_clicks, b4_clicks, b5_clicks, b6_clicks, prev_clicks):

    prev_clicks = dict([i.split(':') for i in prev_clicks.split(' ')])
    last_clicked = 'nan'

    if b1_clicks > int(prev_clicks['b1']):
        last_clicked = 'b1'
    elif b2_clicks > int(prev_clicks['b2']):
        last_clicked = 'b2'
    elif b3_clicks > int(prev_clicks['b3']):
        last_clicked = 'b3'
    elif b4_clicks > int(prev_clicks['b4']):
        last_clicked = 'b4'
    elif b5_clicks > int(prev_clicks['b5']):
        last_clicked = 'b5'
    elif b6_clicks > int(prev_clicks['b6']):
        last_clicked = 'b6'

    cur_clicks = 'b1:{} b2:{} b3:{} b4:{} b5:{} b6:{} last:{}'.format(b1_clicks, b2_clicks, b3_clicks, b4_clicks, b5_clicks, b6_clicks, last_clicked)

    return cur_clicks

#------------------------------------------------------------------------------

if __name__ == '__main__':
    app.run_server()

#------------------------------------------------------------------------------
