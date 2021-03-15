# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from pages import (
    zombieoverview,
    zombiefuture,
    zombiegeography
)

app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}]
)
server = app.server

# Describe the layout/ UI of the app
app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content")]
)

# Update page

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/zombies/zombie-future":
        return zombiefuture.create_layout(app)
    elif pathname == "/zombies/zombie-density":
        return zombiegeography.create_layout(app)
    # elif pathname == "/dash-financial-report/fees":
    #     return feesMins.create_layout(app)
    # elif pathname == "/dash-financial-report/distributions":
    #     return distributions.create_layout(app)
    # elif pathname == "/dash-financial-report/news-and-reviews":
    #     return newsReviews.create_layout(app)
    elif pathname == "/zombies/full-view":
        return (
            zombieoverview.create_layout(app),
            zombiefuture.create_layout(app),
            zombiegeography.create_layout(app),
    #         feesMins.create_layout(app),
    #         distributions.create_layout(app),
    #         newsReviews.create_layout(app),
        )
    else:
        return zombieoverview.create_layout(app)


if __name__ == "__main__":
    app.run_server(debug=True)
