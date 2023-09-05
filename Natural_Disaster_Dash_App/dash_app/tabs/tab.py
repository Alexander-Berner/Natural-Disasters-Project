from ..app import app
from dash import dcc
from dash import html
import dash_daq as daq
from dash.dependencies import Input, Output
from .map_plots import make_map_plot_layout
from .bar_chart import make_bar_chart_layout
from .linegraph import make_line_chart_layout
from .table import make_table_layout


def make_tab_layout():
    return html.Div(className="container", id="tab-layout", children=[
        html.Div([
            dcc.Store(id='dark-mode'),
            html.Div(
                children=[
                    html.Div(
                        className="app-header",
                        children=[
                            html.Div(className="container", children=[
                                html.Img(
                                    src="../assets/logo_square.png",
                                    height="80"
                                ),
                                html.H1(
                                    'INTERNATIONAL GEOGRAPHIC',
                                    className="title"
                                )
                            ]),

                            daq.ToggleSwitch(
                                className="night-mode",
                                id='toggle-dark-mode',
                                label='Night Mode 🌙',
                                value=False,
                                color='orange'
                            )
                        ]
                    ),

                    html.Div([
                        # Tabs
                        dcc.Tabs(
                            id='tab-menu',
                            value='map-tab',
                            className="tabs",
                            children=[
                                dcc.Tab(label='Maps',
                                        value='map-tab',
                                        id='tab-map'),
                                dcc.Tab(label='Bar Charts',
                                        value='bar-charts-tab',
                                        id='tab-bar'),
                                dcc.Tab(label='Line Graphs',
                                        value='line-charts-tab',
                                        id='tab-line'),
                                dcc.Tab(label='Data Table',
                                        value='data-table-tab',
                                        id='tab-table'),
                            ]
                        ),
                    ]),
                ]
            ),

            html.Div(id='tab-content'),
        ], style={'width': '80%', 'display': 'inline-block'})
    ])


@app.callback(
    Output('tab-content', 'children'),
    [Input('tab-menu', 'value'), Input('toggle-dark-mode', 'value')]
)
def render_content(tab, dark_mode):
    if tab == 'map-tab':
        return make_map_plot_layout(dark_mode)
    elif tab == 'bar-charts-tab':
        return make_bar_chart_layout(dark_mode)
    elif tab == 'line-charts-tab':
        return make_line_chart_layout(dark_mode)
    elif tab == 'data-table-tab':
        return make_table_layout(dark_mode)


@app.callback(
    Output('tab-content', 'style'),
    Input('toggle-dark-mode', 'value')
)
def update_page_style(dark_mode):
    if dark_mode:
        style = {
            'color': '#FFFFFF',
            'backgroundColor': '#282828'
        }
    else:
        style = {
            'color': '#000000',
            'backgroundColor': '#FFFFFF'
        }
    return style


@app.callback(
    Output('tab-layout', 'style'),
    Input('toggle-dark-mode', 'value'),
)
def update_dark_mode(value):
    style = {
        'backgroundColor': ('#282828' if value else 'white'),
        'text-align': 'center',
        'min-height': '1000px'
    }
    return style


@app.callback(
    [Output('tab-menu', 'colors'), Output('tab-menu', 'style')],
    Input('toggle-dark-mode', 'value')
)
def update_tab_colors(dark_mode):
    if dark_mode:
        return {
            'border': '#d6d6d6',
            'primary': 'orange',
            'background': '#353535ff'
        }, {
            'color': 'white',
        }
    else:
        return {
            'border': '#d6d6d6',
            'primary': 'orange',
            'background': '#f9f9f9'
        }, {
            'color': 'black'
        }
