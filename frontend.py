# dash modules
import dash
import dash_core_components as dcc  # higher-level components
import dash_html_components as html  # has a component for every HTML tag
from dash.dependencies import Input, Output, State

# game modules
import settings
import colors
from backend import start_game, game_over, flood_grid, plot_grid, initialize_grid
from frontend_helper import color_button_style, represents_int, reset_style, subtitle_style

# ------------------------------------------------------------------------------

grid, figure = start_game(settings.grid_size, colors.no_colors, colors.color_map)
initial_grid = grid

app = dash.Dash()

app.layout = html.Div([html.H1('pyFlood', style={'textAlign': 'left'}),
                       html.Div('select a color to flood the entire board with a single color in the minimum number of steps', style=subtitle_style()),
                       html.Div([dcc.Graph(id='grid-component', figure=figure, config={'displayModeBar': False})]),
                       # To identify which button was clicked:
                       # https://community.plot.ly/t/input-two-or-more-button-how-to-tell-which-button-is-pressed/5788/26
                       # [maral] Mar 18, 2018 5:35 am
                       html.Div([html.Button('', id='b1', n_clicks=0, style=color_button_style(colors.color_dict['navy'])),
                                 html.Button('', id='b2', n_clicks=0, style=color_button_style(colors.color_dict['blue'])),
                                 html.Button('', id='b3', n_clicks=0, style=color_button_style(colors.color_dict['green'])),
                                 html.Button('', id='b4', n_clicks=0, style=color_button_style(colors.color_dict['red'])),
                                 html.Button('', id='b5', n_clicks=0, style=color_button_style(colors.color_dict['orange'])),
                                 html.Button('', id='b6', n_clicks=0, style=color_button_style(colors.color_dict['yellow']))]),
                       html.Div([html.Button('Reset', id='b7', n_clicks=0, style=reset_style()),
                                 html.Div('b1:0 b2:0 b3:0 b4:0 b5:0 b6:0 b7:0 last:nan', id='clicked-button', style={'display': 'none'})])
                       ])

app.title = 'pyFlood'

@app.callback(
    Output(component_id='grid-component', component_property='figure'),
    [Input(component_id='clicked-button', component_property='children')]
)

def play(clicked):
    global grid, initial_grid
    clicked_color = clicked[-1:]
    if represents_int(clicked_color):
        if not game_over(grid):
            grid = flood_grid(grid, grid[0, 0], int(clicked_color), [0, 0])
        if int(clicked_color) == 7:
            grid, dummy_fig = start_game(settings.grid_size, colors.no_colors, colors.color_map)
    else:
        grid = initial_grid
    return plot_grid(grid, colors.color_map, colors.no_colors)

@app.callback(
    Output('clicked-button', 'children'),
    [Input('b1', 'n_clicks'),
     Input('b2', 'n_clicks'),
     Input('b3', 'n_clicks'),
     Input('b4', 'n_clicks'),
     Input('b5', 'n_clicks'),
     Input('b6', 'n_clicks'),
     Input('b7', 'n_clicks')],
    [State('clicked-button', 'children')]
)

def updated_clicked(b1_clicks, b2_clicks, b3_clicks, b4_clicks, b5_clicks, b6_clicks, b7_clicks, prv_clicks):
    prv_clicks = dict([i.split(':') for i in prv_clicks.split(' ')])
    last_click = 'nan'
    if b1_clicks > int(prv_clicks['b1']):
        last_click = 'b1'
    elif b2_clicks > int(prv_clicks['b2']):
        last_click = 'b2'
    elif b3_clicks > int(prv_clicks['b3']):
        last_click = 'b3'
    elif b4_clicks > int(prv_clicks['b4']):
        last_click = 'b4'
    elif b5_clicks > int(prv_clicks['b5']):
        last_click = 'b5'
    elif b6_clicks > int(prv_clicks['b6']):
        last_click = 'b6'
    elif b7_clicks > int(prv_clicks['b7']):
        last_click = 'b7'
    cur_clicks = 'b1:{} b2:{} b3:{} b4:{} b5:{} b6:{} b7:{} last:{}'.format(b1_clicks,
                                                                            b2_clicks,
                                                                            b3_clicks,
                                                                            b4_clicks,
                                                                            b5_clicks,
                                                                            b6_clicks,
                                                                            b7_clicks,
                                                                            last_click)
    return cur_clicks

# ------------------------------------------------------------------------------

if __name__ == '__main__':
    app.run_server()
