import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import numpy as np
import plotly.graph_objects as go

from utils import Header, make_dash_table
import pathlib
import json

import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# get relative data folder
PATH = pathlib.Path(__file__) #.parent
DATA_PATH = PATH.joinpath("../data").resolve()

df = pd.read_csv(DATA_PATH.joinpath('pop.csv'))
x = 26 #First x cities in the dataframe

# initialise
map = Basemap(llcrnrlon=3, llcrnrlat=57, urcrnrlon=30,urcrnrlat=72., lat_0 = 60., lon_0 = 9, projection='merc', resolution='h') #Default projection is cyl
# background color
map.drawmapboundary(fill_color='lightsteelblue', color="black")
# country color
map.fillcontinents(color='grey',lake_color='blue')
map.drawcountries(color='white', linewidth=1)

map.scatter(df['lng'][:x].values, df['lat'][:x].values, marker='o',s=df['population'][:x].values/3e3,alpha=0.8, c='green', latlon=True, zorder=3) #zorder to be ON TOP of map
plt.savefig('assets/zombiemap.png', bbox_inches='tight', dpi=1200)
#plt.show()
