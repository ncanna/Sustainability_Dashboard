#High Level Pages
#Home

#Team A Pages (Trends)
#Seasonality
#Predictions (Normalized for pop. and Not)
#Location/Heatmap

#Team B Pages (Waste Reduction)
#Waste Streams

import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

from utils import Header, make_dash_table

import pandas as pd
import pathlib

# fet relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()


df_waste = pd.read_csv(DATA_PATH.joinpath("waste.csv"))

def create_layout(app):
    # Page layouts
    return html.Div(
        [
            html.Div([Header(app)]),
            # page 1
            html.Div(
                [
                    # Row 3
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H5("Analysis Summary"),
                                    html.Br([]),
                                    html.P(
                                        "\
                                    The University of Virginia has laid out an ambitious 10-year plan to accelerate the University’s sustainability goals across operations, research, curriculum, accountability and engagement – a framework of stewardship and discovery. The 2020-30 UVA Sustainability Plan includes six goals that UVA’s Board of Visitors approved in December, when the University committed to pursuing carbon neutrality by 2030 in partnership with the College of William & Mary. The full 2030 Plan also outlines strategic actions for success and adds four new goals.",
                                        style={"color": "#ffffff"},
                                        className="row",
                                    ),
                                ],
                                className="product",
                            )
                        ],
                        className="row",
                    ),
                    # Row 4
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["Quick Facts"], className="subtitle padded"
                                    ),
                                    html.Table(make_dash_table(df_waste)),
                                ],
                                className="six columns",
                            ),
                            html.Div(
                                [
                                    html.H6(
                                        "Bar Graph",
                                        className="subtitle padded",
                                    ),
                                    dcc.Graph(
                                        id="graph-1",
                                        figure={
                                            "data": [
                                                go.Bar(
                                                    x=[
                                                        "Factor 1",
                                                        "Factor 2",
                                                        "Factor 3",
                                                        "Factor 4",
                                                        "Factor 5",
                                                    ],
                                                    y=[
                                                        "21.67",
                                                        "11.26",
                                                        "15.62",
                                                        "8.37",
                                                        "11.11",
                                                    ],
                                                    marker={
                                                        "color": "#141E3C",
                                                        "line": {
                                                            "color": "rgb(255, 255, 255)",
                                                            "width": 2,
                                                        },
                                                    },
                                                    name="Group 1",
                                                ),
                                                go.Bar(
                                                    x=[
                                                        "Factor 1",
                                                        "Factor 2",
                                                        "Factor 3",
                                                        "Factor 4",
                                                        "Factor 5",
                                                    ],
                                                    y=[
                                                        "21.83",
                                                        "11.41",
                                                        "15.79",
                                                        "8.50",
                                                    ],
                                                    marker={
                                                        "color": "#dddddd",
                                                        "line": {
                                                            "color": "rgb(255, 255, 255)",
                                                            "width": 2,
                                                        },
                                                    },
                                                    name="Group 2",
                                                ),
                                            ],
                                            "layout": go.Layout(
                                                autosize=False,
                                                bargap=0.35,
                                                font={"family": "Raleway", "size": 10},
                                                height=200,
                                                hovermode="closest",
                                                legend={
                                                    "x": -0.0228945952895,
                                                    "y": -0.189563896463,
                                                    "orientation": "h",
                                                    "yanchor": "top",
                                                },
                                                margin={
                                                    "r": 0,
                                                    "t": 20,
                                                    "b": 10,
                                                    "l": 10,
                                                },
                                                showlegend=True,
                                                title="",
                                                width=330,
                                                xaxis={
                                                    "autorange": True,
                                                    "range": [-0.5, 4.5],
                                                    "showline": True,
                                                    "title": "",
                                                    "type": "category",
                                                },
                                                yaxis={
                                                    "autorange": True,
                                                    "range": [0, 22.9789473684],
                                                    "showgrid": True,
                                                    "showline": True,
                                                    "title": "",
                                                    "type": "linear",
                                                    "zeroline": False,
                                                },
                                            ),
                                        },
                                        config={"displayModeBar": False},
                                    ),
                                ],
                                className="six columns",
                            ),
                        ],
                        className="row",
                        style={"margin-bottom": "35px"},
                    ),


                ],
                className="sub_page",
            ),
        ],
        className="page",
    )
