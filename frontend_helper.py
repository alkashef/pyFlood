
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
            'margin': '20px 0px 20px 0'}

# ------------------------------------------------------------------------------

def reset_style():
    return {'width': '70',
            'height': '30',
            'color': 'white',
            'background-color': 'black',
            'margin': '20px 0px 20px 0',
            'font-size': '110%'}

# ------------------------------------------------------------------------------

def represents_int(string):
    try:
        int(string)
        return True
    except ValueError:
        return False