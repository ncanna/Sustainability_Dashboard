import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

from utils import Header, make_dash_table

import pandas as pd
import numpy as np
import pathlib

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()


df_waste = pd.read_csv(DATA_PATH.joinpath("waste.csv"))
radio_buttons = [""]
df_graph = pd.DataFrame(
    {'col1': np.random.randn(10),
     'col2': np.random.randn(10),
     'col3': np.random.randn(10),
     'col4': np.random.randn(10)})
x_axis_options = [
    {'label': 'Column 1', 'value':'col1'},
    {'label': 'Column 2', 'value':'col2'},
    {'label': 'Column 3', 'value':'col3'},
    {'label': 'Column 4', 'value':'col4'},
]
y_axis_options = [
    {'label': 'Column 1', 'value':'col1'},
    {'label': 'Column 2', 'value':'col2'},
    {'label': 'Column 3', 'value':'col3'},
    {'label': 'Column 4', 'value':'col4'},
]

def create_layout(app):
    # Page layouts    
    return html.Div(
        [
            html.Div([Header(app)]),
            # page 1
            html.Div(
                [
                    html.H4(
                        "Radio Page",
                        className="subtitle padded",
                    ),
                    html.Div(
                        html.Table(make_dash_table(df_graph)), className="padded"
                    ),
                    dcc.Input(
                        placeholder='Enter a value...',
                        type='text',
                        value='',
                        id='input_textbox'
                    ),
                    html.P(id='output_textbox'),

                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        "X-Axis",
                                        className="subtitle padded",
                                    ),
                                    dcc.RadioItems(
                                        options=x_axis_options,
                                        value=x_axis_options[0]['value'],
                                        className="padded",
                                        id='x_axis_option'
                                    )
                                ], className="two columns"
                            ),
                            html.Div(
                                [
                                    html.H6(
                                        "Y-Axis",
                                        className="subtitle padded",
                                    ),
                                    dcc.RadioItems(
                                        options=y_axis_options,
                                        value=y_axis_options[1]['value'],
                                        className="padded",
                                        id='y_axis_option'
                                    )
                                ], className="two columns"
                            ),
                        ], className="row"
                    ),


                    dcc.Graph(id="radio_graph")
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )

def update_textbox(value):
    return value

def update_graph(x_axis, y_axis):
    return go.Figure(
        data = go.Scatter(x = df_graph[x_axis], y = df_graph[y_axis], mode = 'markers')
        )