import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import os
import base64

from utils import Header, make_dash_table
import pathlib
#import json

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()
ASSET_PATH = PATH.joinpath("../assets").resolve()

image_path = ASSET_PATH.joinpath('zombiemap.png')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

#Get dash to accept image format from local source
#Map is created from "map.py", allows for many more cities plotted.
with open(os.getcwd() + "/assets/zombiemap.png", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode()
# Add the prefix that plotly will want when using the string as source
encoded_image = "data:image/png;base64," + encoded_string

#Allow for resizing, and other plotly tools on a static image
# Create figure
fig = go.Figure()

# Constants
img_width = 3636
img_height = 4733
scale_factor = 0.2

# Add invisible scatter trace.
# This trace is added to help the autoresize logic work.
fig.add_trace(
    go.Scatter(
        x=[0, img_width * scale_factor],
        y=[0, img_height * scale_factor],
        mode="markers",
        marker_opacity=0
    )
)

# Configure axes
fig.update_xaxes(
    visible=False,
    range=[0, img_width * scale_factor]
)

fig.update_yaxes(
    visible=False,
    range=[0, img_height * scale_factor],
    # the scaleanchor attribute ensures that the aspect ratio stays constant
    scaleanchor="x"
)

# Add image
fig.add_layout_image(
    dict(
        x=0,
        sizex=img_width * scale_factor,
        y=img_height * scale_factor,
        sizey=img_height * scale_factor,
        xref="x",
        yref="y",
        opacity=1.0,
        layer="below",
        sizing="stretch",
        source=encoded_image)
)

# Configure other layout
fig.update_layout(
    width=img_width * scale_factor,
    height=img_height * scale_factor,
    margin={"l": 0, "r": 0, "t": 0, "b": 0},
)

# Disable the autosize on double click because it adds unwanted margins around the image
config={'doubleClick': 'reset'}


#Create the page itself
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
                        html.H2(children='Zombie spread'),
                        html.H5(children='The zombie pandemic is largely centered around the large cities, where the population is the most dense.'),
                        dcc.Graph(
                            id='graph',
                            figure=fig,
                            config=config,
                        ),
                    ], className='row'),
                ], className='sub_page'),
        ], className='page')
