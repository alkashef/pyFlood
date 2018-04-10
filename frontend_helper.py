
app_name = 'pyFlood'

subtitle_text = 'iteratively select a color to flood the entire board with a single color in the minimum number of steps'

game_width = '400'

# ------------------------------------------------------------------------------

def color_button_style(color):
    return {'width': '50',
            'height': '30',
            'marginRight':'20',
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
            'vertical-align':'middle'}

# ------------------------------------------------------------------------------

def above_grid_style():
    return {'width': game_width,
            'margin': '20px 0px 30px 0'}

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



