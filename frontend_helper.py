
def button_style(color):
    return {'width': '50',
            'height': '30',
            'marginRight':'20',
            'background-color': color}

# ------------------------------------------------------------------------------

def represents_int(string):
    try:
        int(string)
        return True
    except ValueError:
        return False