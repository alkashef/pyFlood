
# dash
import dash
import dash_core_components as dcc # higher-level components
import dash_html_components as html # has a component for every HTML tag
from dash.dependencies import Input, Output, State

# game modules
import backend
import settings
import colors

#------------------------------------------------------------------------------

def buttonStyle(color):
    return {'width':'50', 'height':'30', 'background-color':color}

#------------------------------------------------------------------------------

init_data, init_layout = backend.initializeGrid(settings.board_size,
                                                colors.no_colors,
                                                colors.color_map)

app = dash.Dash()

app.layout = html.Div([html.H1('pyFlood', style = {'textAlign': 'left'}),
                       html.Div('A Color Flood Game in Python', style = {'textAlign': 'left'}),
                       html.Div([dcc.Graph(id = 'board', figure = {'data': init_data, 'layout': init_layout}),
                                 # To identify which button was clicked:
                                 # https://community.plot.ly/t/input-two-or-more-button-how-to-tell-which-button-is-pressed/5788/26
                                 # [maral] Mar 18, 2018 5:35 am
                                 html.Button('', id = 'b1', n_clicks = 0, style = buttonStyle(colors.color_dict['navy'])),
                                 html.Button('', id = 'b2', n_clicks = 0, style = buttonStyle(colors.color_dict['blue'])),
                                 html.Button('', id = 'b3', n_clicks = 0, style = buttonStyle(colors.color_dict['green'])),
                                 html.Button('', id = 'b4', n_clicks = 0, style = buttonStyle(colors.color_dict['red'])),
                                 html.Button('', id = 'b5', n_clicks = 0, style = buttonStyle(colors.color_dict['orange'])),
                                 html.Button('', id = 'b6', n_clicks = 0, style = buttonStyle(colors.color_dict['yellow'])),
                                 html.Div('b1:0 b2:0 b3:0 b4:0 b5:0 b6:0 last:nan', id='clicked-button', style={'display': 'none'})
                                 ]),
                      ])

@app.callback(
        Output(component_id = 'board', component_property = 'figure'),
        [Input(component_id = 'clicked-button', component_property = 'children')]
)

def update_figure(clicked):
    lst_clk = clicked[-1:]
    data, layout = backend.plotGrid(lst_clk)
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

def updated_clicked(b1_clks, b2_clks, b3_clks, b4_clks, b5_clks, b6_clks, prv_clks):
    prv_clks = dict([i.split(':') for i in prv_clks.split(' ')])
    lst_clk = 'nan'
    if b1_clks > int(prv_clks['b1']):
        lst_clk = 'b1'
    elif b2_clks > int(prv_clks['b2']):
        lst_clk = 'b2'
    elif b3_clks > int(prv_clks['b3']):
        lst_clk = 'b3'
    elif b4_clks > int(prv_clks['b4']):
        lst_clk = 'b4'
    elif b5_clks > int(prv_clks['b5']):
        lst_clk = 'b5'
    elif b6_clks > int(prv_clks['b6']):
        lst_clk = 'b6'
    cur_clicks = 'b1:{} b2:{} b3:{} b4:{} b5:{} b6:{} last:{}'.format(b1_clks, b2_clks, b3_clks, b4_clks, b5_clks, b6_clks, lst_clk)
    return cur_clicks

if __name__ == '__main__':
    app.run_server()

