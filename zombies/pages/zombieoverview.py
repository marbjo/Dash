# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

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


# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Sales" : ["Web", "Store", "Referral", "Post"],
    "Amount" : [400,300,100,200]
})

df2 = pd.DataFrame({
    "State" : ["Transformation", "Dead", "Alive", "Zombie"],
    "Amount" : [437,322,178,204]
})
# This dataframe has 244 lines, but 4 distinct values for `day`
#df2 = px.data.tips()

fig = px.bar(df, x="Sales", y="Amount") #, color="Amount", barmode="group")
fig2 = px.pie(df2, values='Amount', names='State')


# #Table
# df3 = pd.read_csv('https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv')
#
# def generate_table(dataframe, max_rows=10):
#     return html.Table([
#         html.Thead(
#             html.Tr([html.Th(col) for col in dataframe.columns])
#         ),
#         html.Tbody([
#             html.Tr([
#                 html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
#             ]) for i in range(min(len(dataframe), max_rows))
#         ])
#     ])


def create_layout(app):
    # Page layouts
    return html.Div(
        [
            html.Div([Header(app)]),
            # page 1
            html.Div(
                [
                    html.H1(children='2100 in numbers', style={'textAlign': 'center', 'color': 'black', 'font-weight': 'bold'}),
                    html.H2(children='Where are we now, and where we are going.', style={'textAlign': 'center', 'color': 'black'}),

                    # Row 2
                    html.Div([
                        #One Div with className='six columns'
                        html.Div([
                            html.H3(children='Distribution of sales from our different outlets'),
                            html.Div(children='Web sales continues to be the dominating factor, and are expected to increase their share of sales even more in the future.'), #, style={'textAlign': 'center', 'color': 'magenta'}),
                            dcc.Graph(
                                id='graph1',
                                figure=fig
                            ),
                        ], className='six columns'),
                        #Another Div with className='six columns'
                        html.Div([
                            html.H3(children='The Zombie apocalypse in numbers'),
                            html.Div(children='We are heading for dark times, as the number of alive humans is expected to sharply decline in the forseeable future.'), #, style={'textAlign': 'center', 'color': 'magenta'}),
                            dcc.Graph(
                                id='graph2',
                                figure=fig2
                            ),
                        ], className='six columns'),
                    ], className='row'),

                    #Row 3
                    html.Div([
                        html.Div([
                            html.H5("Brain", style={'color' : 'white', 'marginLeft': 20, 'marginRight': 20}),
                            #html.Br([]),
                            html.P('The zombies seem to prefer to eat the brain.'
                            ,style={'color': 'white', 'marginLeft': 20, 'marginRight': 20}),
                        ],className='three columns', style={'backgroundColor': 'darkRed'}),
                        html.Div([
                            html.H5("Kill", style={'marginLeft': 20, 'marginRight': 20}),
                            #html.Br([]),
                            html.P('A shot to head seems to be the most effective way of killing zombies.'
                            ,style={'marginLeft': 20, 'marginRight': 20}),
                        ],className='three columns', style={'color': 'white','backgroundColor': 'darkRed'}),
                        html.Div([
                            html.H5("Infection", style={'marginLeft': 20, 'marginRight': 20}),
                            #html.Br([]),
                            html.P('A simple bite from a zombie seems to be sufficient for a full infection.'
                            ,style={'marginLeft': 20, 'marginRight': 20}),
                        ],className='three columns', style={'color': 'white','backgroundColor': 'darkRed'}),
                        html.Div([
                            html.H5("Survival", style={'marginLeft': 20, 'marginRight': 20}),
                            #html.Br([]),
                            html.P('Avoid contact at all costs. Carry weapons.'
                            , style={'marginLeft': 20, 'marginRight': 20}),
                        ],className='three columns', style={'color': 'white','backgroundColor': 'darkRed'}),
                    ], className='row'),

                    # #Row 5
                    # html.Div([
                    #     html.H4(children='US Agriculture Exports (2011)'),
                    #     generate_table(df3)
                    # ]),
                ],className="sub_page"),
            ], className="page")

if __name__ == '__main__':
    app.run_server(debug=True)
