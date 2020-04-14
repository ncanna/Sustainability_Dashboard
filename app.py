import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from pages import (
    overview,
    distributions,
    home,
    radio
)

app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}]
)
"""
This line is needed because dash will raise a callback exception when it attempts to update an object via callbacks, but the 
object is not on the page. This will happen when the user switches pages, e.g. from Radio to Home.
"""
app.config.suppress_callback_exceptions = True
server = app.server

# Describe the layout/ UI of the app
app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content")]
)

# Update page
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/overview":
        return overview.create_layout(app)
    elif pathname == "/distributions":
        return distributions.create_layout(app)
    elif pathname == "/radio":
        return radio.create_layout(app)
    elif pathname == "/home":
        return (
            home.create_layout(app),
        )
    else:
        return home.create_layout(app)

"""
Section for radio.py
"""
# test callback for radio page textbox
@app.callback(Output("output_textbox", "children"), [Input("input_textbox", "value")])
def update_textbox(value):
    return radio.update_textbox(value)

@app.callback(Output("radio_graph", "figure"), [Input("x_axis_option", "value"), Input("y_axis_option", "value")])
def update_graph(x_axis, y_axis):
    return radio.update_graph(x_axis, y_axis)
#

if __name__ == "__main__":
    app.run_server(debug=True)
