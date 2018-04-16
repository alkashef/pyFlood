import dash_core_components as dcc
import dash_html_components as html

import colors

# ------------------------------------------------------------------------------

app_name = 'pyFlood'
subtitle_text = 'iteratively select a color to flood the entire board with a single color in the minimum number of steps'
game_width = '400'

# ------------------------------------------------------------------------------

def color_button_style(color):
    return {'width': '50',
            'height': '30',
            'marginRight': '20',
            'marginTop': '20',
            'background-color': color}

# ------------------------------------------------------------------------------

def subtitle_style():
    return {'textAlign': 'left',
            'color': 'grey',
            'margin': '20px 0px 20px 0',
            'width': game_width}

# ------------------------------------------------------------------------------

def header_style():
    return {'textAlign': 'left'}

# ------------------------------------------------------------------------------

def counter_style():
    return {'font-size': '150%',
            'display': 'inline-block',
            'vertical-align': 'middle'}

# ------------------------------------------------------------------------------

def above_grid_style():
    return {'width': game_width,
            'margin': '20px 0px 20px 0'}

# ------------------------------------------------------------------------------

def reset_style():
    return {'width': '70',
            'height': '30',
            'color': 'white',
            'background-color': 'black',
            'margin': '0px 0px 0px 0px',
            'font-size': '110%',
            'display': 'inline-block',
            'float': 'right'}

# ------------------------------------------------------------------------------

def flood_style():
    return {'width': '400',
            'margin': '20px 0px 20px 0px'}

# ------------------------------------------------------------------------------

def bot_flood_style():
    return {'width': '100',
            'height': '30',
            'color': 'white',
            'background-color': 'black',
            'margin': '0px 0px 0px 0px',
            'font-size': '110%',
            'display': 'inline-block',
            'float': 'right'}

# ------------------------------------------------------------------------------

def grid_div(figure):
    return html.Div([dcc.Graph(id='grid-component', figure=figure, config={'displayModeBar': False})])

# ------------------------------------------------------------------------------

def header():
    return html.H1('pyFlood', style=header_style())

# ------------------------------------------------------------------------------

def subtitle():
    return html.Div(subtitle_text, style=subtitle_style())

# ------------------------------------------------------------------------------

def hidden_button():
    return html.Div('b1:0 b2:0 b3:0 b4:0 b5:0 b6:0 b7:0 b8:0 last:nan', id='clicked-button', style={'display': 'none'})

# ------------------------------------------------------------------------------

def bot_flood_button(hide):
    if hide == True:
        return html.Button('bot flood', id='b8', n_clicks=0, style={'display': 'none'})
    else:
        return html.Button('bot flood', id='b8', n_clicks=0, style=bot_flood_style())

# ------------------------------------------------------------------------------

def color_button(hide, color, id):
    if hide == True:
        return html.Button('', id=id, n_clicks=0, style={'display': 'none'})
    else:
        return html.Button('', id=id, n_clicks=0, style=color_button_style(colors.color_dict[color]))

# ------------------------------------------------------------------------------

def counter():
    return html.Div('', id='step-counter', style=counter_style())

# ------------------------------------------------------------------------------

def reset_component():
    return html.Button('Reset', id='b7', n_clicks=0, style=reset_style())

# ------------------------------------------------------------------------------
