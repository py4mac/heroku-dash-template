import os
from os.path import dirname, join

from flask import Flask, render_template, request
import pandas as pd
import numpy as np

import dash
import dash_core_components as dcc
import dash_html_components as html

# See: https://pythonprogramming.net/data-visualization-application-dash-python-tutorial-introduction/
app = dash.Dash()
server = app.server

app.layout = html.Div(children=[
    html.H1(children='Dash Tutorials'),
    dcc.Graph(
        id='example',
        figure={
            'data': [
                {'x': [1, 2, 3, 4, 5], 'y': [9, 6, 2, 1, 5], 'type': 'line', 'name': 'Boats'},
                {'x': [1, 2, 3, 4, 5], 'y': [8, 7, 2, 7, 3], 'type': 'bar', 'name': 'Cars'},
            ],
            'layout': {
                'title': 'Basic Dash Example'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
