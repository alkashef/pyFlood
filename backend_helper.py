from plotly import graph_objs as go

# ------------------------------------------------------------------------------

def plot_grid(board, color_map, no_colors):

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

    data = [go.Heatmap(z=board,
                       colorscale=color_map,
                       zmin=1,
                       zmax=no_colors)]

    return data, layout
