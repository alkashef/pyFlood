# dash modules
import dash
import dash_core_components as dcc  # higher-level components
import dash_html_components as html  # has a component for every HTML tag
from dash.dependencies import Input, Output, State

# game modules
import settings
import colors
import backend as be
import frontend_helper as feh

# ------------------------------------------------------------------------------

grid_size = settings.grid_size
no_colors = colors.no_colors
color_map = colors.color_map

grid, figure = be.start_game(grid_size, no_colors, color_map)
initial_grid = grid
step_counter = 0
chosen_color = 0

# ------------------------------------------------------------------------------

def grid_div():
    return html.Div([dcc.Graph(id='grid-component', figure=figure, config={'displayModeBar': False})])

def header():
    return html.H1('pyFlood', style=feh.header_style())

def subtitle():
    return html.Div(feh.subtitle_text, style=feh.subtitle_style())

def hidden_button():
    return html.Div('b1:0 b2:0 b3:0 b4:0 b5:0 b6:0 b7:0 b8:0 last:nan', id='clicked-button', style={'display': 'none'})

def bot_flood_button(hide):
    if hide == True:
        return html.Button('bot flood', id='b8', n_clicks=0, style={'display': 'none'})
    else:
        return html.Button('bot flood', id='b8', n_clicks=0, style=feh.bot_flood_style())

def color_button(hide, color, id):
    if hide == True:
        return html.Button('', id=id, n_clicks=0, style={'display': 'none'})
    else:
        return html.Button('', id=id, n_clicks=0, style=feh.color_button_style(colors.color_dict[color]))

def counter():
    return html.Div('', id='step-counter', style=feh.counter_style())

def reset_component():
    return html.Button('Reset', id='b7', n_clicks=0, style=feh.reset_style())

# ------------------------------------------------------------------------------

app = dash.Dash()

if settings.mood == 'human':
    app.layout = html.Div([header(),
                           subtitle(),
                           html.Div([counter(), reset_component()], style=feh.above_grid_style()),
                           grid_div(),
                           # To identify which button was clicked:
                           # https://community.plot.ly/t/input-two-or-more-button-how-to-tell-which-button-is-pressed/5788/26
                           # [maral] Mar 18, 2018 5:35 am
                           html.Div([color_button(False, 'navy',   'b1'),
                                     color_button(False, 'blue',   'b2'),
                                     color_button(False, 'green',  'b3'),
                                     color_button(False, 'red',    'b4'),
                                     color_button(False, 'orange', 'b5'),
                                     color_button(False, 'yellow', 'b6')]),
                           html.Div([bot_flood_button(hide=True)], style=feh.flood_style()),
                           hidden_button()
                           ])

if settings.mood == 'bot':
    app.layout = html.Div([header(),
                           subtitle(),
                           html.Div([counter(), reset_component()], style=feh.above_grid_style()),
                           grid_div(),
                           html.Div([color_button(True, '', 'b1'),
                                     color_button(True, '', 'b2'),
                                     color_button(True, '', 'b3'),
                                     color_button(True, '', 'b4'),
                                     color_button(True, '', 'b5'),
                                     color_button(True, '', 'b6')]),
                           html.Div([bot_flood_button(hide=False)], style=feh.flood_style()),
                           hidden_button()
                           ])

app.title = feh.app_name

# ------------------------------------------------------------------------------

@app.callback(
    Output(component_id='grid-component', component_property='figure'),
    [Input(component_id='clicked-button', component_property='children')]
)
def play(clicked):

    global grid
    global initial_grid
    global chosen_color

    clicked_button = clicked[-1:]

    if not be.represents_int(clicked_button):
        grid = initial_grid
    elif be.reset(clicked_button):
        grid, dummy_fig = be.start_game(grid_size, no_colors, color_map)
    elif be.is_color_button(clicked_button) and not be.game_over(grid):
        grid = be.flood_grid(grid, grid[0, 0], int(clicked_button), [0, 0])
    elif be.is_bot_button(clicked_button) and not be.game_over(grid):
        chosen_color = be.stupid_bot(grid)
        grid = be.flood_grid(grid, grid[0, 0], chosen_color, [0, 0])

    return be.plot_grid(grid, color_map, no_colors)

# ------------------------------------------------------------------------------

@app.callback(
    Output(component_id='clicked-button', component_property='children'),
    [Input(component_id='b1', component_property='n_clicks'),
     Input(component_id='b2', component_property='n_clicks'),
     Input(component_id='b3', component_property='n_clicks'),
     Input(component_id='b4', component_property='n_clicks'),
     Input(component_id='b5', component_property='n_clicks'),
     Input(component_id='b6', component_property='n_clicks'),
     Input(component_id='b7', component_property='n_clicks'),
     Input(component_id='b8', component_property='n_clicks')],
    [State(component_id='clicked-button', component_property='children')]
)
def updated_clicked(b1_clicks, b2_clicks, b3_clicks, b4_clicks, b5_clicks, b6_clicks, b7_clicks, b8_clicks, prv_clicks):
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
    elif b8_clicks > int(prv_clicks['b8']):
        last_click = 'b8'
    cur_clicks = 'b1:{} b2:{} b3:{} b4:{} b5:{} b6:{} b7:{} b8:{} last:{}'.format(b1_clicks,
                                                                                  b2_clicks,
                                                                                  b3_clicks,
                                                                                  b4_clicks,
                                                                                  b5_clicks,
                                                                                  b6_clicks,
                                                                                  b7_clicks,
                                                                                  b8_clicks,
                                                                                  last_click)
    return cur_clicks

# ------------------------------------------------------------------------------

@app.callback(
    Output(component_id='step-counter', component_property='children'),
    [Input(component_id='clicked-button', component_property='children')]
)
def update_step_counter(clicked):

    global step_counter
    global grid
    global chosen_color

    clicked_button = clicked[-1:]

    if be.reset(clicked_button):
        step_counter = 0
    else:
        if (be.is_color_button(clicked_button) and not be.game_over(grid) and not be.same_color(grid, clicked_button)) or  \
           (be.is_bot_button(clicked_button) and not be.game_over(grid)):
                step_counter += 1

    return step_counter

# ------------------------------------------------------------------------------

if __name__ == '__main__':
    app.run_server()
