import dash_html_components as html
import dash_core_components as dcc


def Header(app):
    return html.Div([get_header(app), html.Br([]), get_menu()])


def get_header(app):
    header = html.Div(
        [
            html.Div(
                [
                    html.Img(
                        src=app.get_asset_url("zombie2.jpg"),
                        className="logo",
                        style={'width': '5%', 'height': '5%'}
                        ),
                    # html.A(
                    #     html.Button("Learn More", id="learn-more-button"),
                    #     href="https://plot.ly/dash/pricing/",
                    # ),
                ],
                className="row",
            ),
            html.Div(
                [
                    html.Div(
                        [html.H5("The zombie apocalypse")],
                        className="seven columns main-title",
                    ),
                    html.Div(
                        [
                            dcc.Link(
                                "Full View",
                                href="/zombies/full-view",
                                className="full-view-link",
                            )
                        ],
                        className="five columns",
                    ),
                ],
                className="twelve columns",
                style={"padding-left": "0"},
            ),
        ],
        className="row",
    )
    return header


def get_menu():
    menu = html.Div(
        [
            dcc.Link(
                "Overview",
                href="/zombies/zombieoverview",
                className="tab first",
            ),
            dcc.Link(
                "Zombie future",
                href="/zombies/zombie-future",
                className="tab",
            ),
            dcc.Link(
                "Zombie geography",
                href="/zombies/zombie-geography",
                className="tab",
            ),
            # dcc.Link(
            #     "Test 2", href="/zombies/fees", className="tab"
            # ),
            # dcc.Link(
            #     "Test 3",
            #     href="/zombies/test2",
            #     className="tab",
            # ),
            # dcc.Link(
            #     "News & Reviews",
            #     href="/zombies/test3",
            #     className="tab",
            # ),
        ],
        className="row all-tabs",
    )
    return menu


def make_dash_table(df):
    """ Return a dash definition of an HTML table for a Pandas dataframe """
    table = []
    for index, row in df.iterrows():
        html_row = []
        for i in range(len(row)):
            html_row.append(html.Td([row[i]]))
        table.append(html.Tr(html_row))
    return table
