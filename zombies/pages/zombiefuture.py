import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import numpy as np
import plotly.graph_objects as go

from utils import Header, make_dash_table
import pathlib

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Create random data with numpy
np.random.seed(1)
N = 100
x_start = 2000
x_end = 2100
x = np.linspace(x_start, x_end, N)
mu, sigma = 0, 20
y = np.random.normal(mu,sigma,N)
y_inc = y + x
deg = 1
coeffs = np.polyfit(x,y_inc,deg)
x2 = np.linspace(x_start,x_end+60,N+60)
values = np.polyval(coeffs,x2)

# Create traces
fig3 = go.Figure()
fig3.add_trace(go.Scatter(x=x, y=y_inc,
                    mode='markers', name='Data'))
fig3.add_trace(go.Scatter(x=x2, y=values,
                    mode='lines',
                    name='Best linear fit'))
fig3.add_trace(go.Scatter(x=[2150, 2150], y=[2150, 2150], name='Goal',
                         marker = dict(color='green', size=12)))

fig3.update_layout(
                   xaxis_title='Years',
                   yaxis_title='Number of sales (million)')

def create_layout(app):
    # Page layouts
    return html.Div(
        [
            Header(app),
            # page 2
            html.Div(
                [
                    #Row 4
                    html.Div([
                        html.H2(children='Predicted sales'),
                        html.Div(children='If the positive trend continues, the goal of "2150 in 2150" will be reached by a margin of almost ~8 million.'), #, style={'textAlign': 'center', 'color': 'magenta'}),
                        dcc.Graph(
                            id='graph3',
                            figure=fig3
                        ),
                    ], className='row'),
                ], className='sub_page'),
        ], className='page')
