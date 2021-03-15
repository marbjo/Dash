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
x_start = 2021
x_end = 2050
x = np.linspace(x_start, x_end, N)
mu, sigma = 0, 1
y_0 = np.linspace(0,8,N)
y = np.random.normal(mu,sigma,N)
y_inc = y + y_0
deg = 1
coeffs = np.polyfit(x,y_inc,deg)
x2 = np.linspace(x_start,x_end+20,N+20)
values = np.polyval(coeffs,x2)

exp_pop_2060 = 10.151448761

# Create traces
fig3 = go.Figure()
fig3.add_trace(go.Scatter(x=x, y=y_inc,
                    mode='markers', name='Zombie estimates'))
fig3.add_trace(go.Scatter(x=x2, y=values,
                    mode='lines',
                    name='Best linear fit'))
fig3.add_trace(go.Scatter(x=[2060, 2060], y=[exp_pop_2060, exp_pop_2060], name='Last human',
                         marker = dict(color='green', size=12)))

fig3.update_layout(
                   xaxis_title='Years',
                   yaxis_title='Number of zombies (billion)')

########################
#Table
# get relative data folder
df = pd.read_csv(DATA_PATH.joinpath('pop.csv'))
x = 10 #First x cities in the dataframe
new_df = df[['city','population']][:x] #Slicing only city and population, up to x cities

rand_vec = np.random.random((x)) #Randomize zombie conversion numbers
new_col = np.floor(new_df['population'].values * rand_vec) #Create new column for number of zombies

new_df = new_df.assign(zombies=new_col, percentage=np.round(rand_vec*100,1)) #Add to dataframe

def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])

def create_layout(app):
    # Page layouts
    return html.Div(
        [
            Header(app),
            # page 2
            html.Div(
                [
                    #Row 1
                    html.Div([
                        html.H2(children='Number of zombies', style={'color': 'green'}),
                        html.H6(children='We are heading for dark times, as the number of alive humans is expected to sharply decline in the forseeable future.\
                        The green dot represents the expected world population in 2060, meaning everyone on earth is a zombie if the trend continues.'), #, style={'textAlign': 'center', 'color': 'magenta'}),
                        dcc.Graph(
                            id='graph3',
                            figure=fig3
                        ),
                    ], className='row'),

                    #Row 2
                    html.Div(
                        [
                            html.Div(
                                [
                                    #html.Br([]),
                                    html.H2("Zombie distribution in cities", style={'color': 'green'}),
                                    html.H6(children='A large percentage of the population in major cities has already been \
                                    converted to zombies. It may be time to flee for the hills.'),
                                    html.Div(
                                        [
                                            html.Table(
                                                generate_table(new_df),
                                                #className="tiny-header",
                                            )
                                        ],
                                        style={"overflow-x": "auto"},
                                    ),
                                ],
                                className="twelve columns",
                            )
                        ],
                        className="row ",
                    ),
                ], className='sub_page'),
        ], className='page')
