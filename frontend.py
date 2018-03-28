
import dash
import dash_core_components as dcc # higher-level components
import dash_html_components as html # has a component for every HTML tag
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
import numpy as np
import backend as be

#------------------------------------------------------------------------------

size = be.size
data = be.data
layout = be.layout
color_map = be.color_map
no_colors = be.no_colors

#------------------------------------------------------------------------------

# To identify which button was clicked:
    # https://community.plot.ly/t/input-two-or-more-button-how-to-tell-which-button-is-pressed/5788/26
    # maral Mar 18, 2018 5:35 am

app = dash.Dash()

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
                                                             'data': be.data,
                                                             'layout': be.layout
                                                             }
                                                     ),
                                                html.Button('', id='b1', n_clicks=0, style={'width':'50', 'height':'30', 'background-color':'navy',}),
                                                html.Button('', id='b2', n_clicks=0, style={'width':'50', 'height':'30', 'background-color':'blue'}),
                                                html.Button('', id='b3', n_clicks=0, style={'width':'50', 'height':'30', 'background-color':'green'}),
                                                html.Button('', id='b4', n_clicks=0, style={'width':'50', 'height':'30', 'background-color':'red'}),
                                                html.Button('', id='b5', n_clicks=0, style={'width':'50', 'height':'30', 'background-color':'orange'}),
                                                html.Button('', id='b6', n_clicks=0, style={'width':'50', 'height':'30', 'background-color':'yellow'}),
                                                html.Div(id='clicked-button', children='b1:0 b2:0 b3:0 b4:0 b5:0 b6:0 last:nan', style={'display': 'none'})
                                             ]),

                            html.Div(id='display-clicked', children="")
])

@app.callback(
        Output(component_id='board', component_property='figure'),
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

if __name__ == '__main__':
    app.run_server()

