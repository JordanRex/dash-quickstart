## layout_utils

###########################################################################################################################
## functions to generate dynamic layout for dash

from helpers.styles import *
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from app import app

###########################################################################################################################
###########################################################################################################################
PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"

navbar = dbc.Navbar(
    [
        html.A(
            # Use row and col to control vertical alignment of logo / brand
            dbc.Row(
                [
                    dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px")),
                    dbc.Col(dbc.NavbarBrand("Header")),
                ],
                align="center",
                no_gutters=True,
            ),
            href="https://plot.ly",
        ),
    ],
    color="dark",
    dark=True,
)

# menu function
def get_menuheader():
    return dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(
                        [
                            navbar
                        ], width=12
                    )
                ]
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dcc.Link(
                                "Home",
                                href="/home",
                                id='home-link'
                            )
                        ], width=4
                    ),
                    dbc.Col(
                        [
                            dcc.Link(
                                "Page One",
                                href="/page_1",
                                id='p1-link'
                            ),
                        ], width=4
                    ),
                    dbc.Col(
                        [
                            dcc.Link(
                                "Page One",
                                href="/page_2",
                                id='p2-link'
                            )
                        ], width=4
                    )
                ]
            )
        ], style=HEADER_STYLE)



###########################################################################################################################
###########################################################################################################################
# dash card fn to generate dropdown boxes
def div_dropdown(div_title, div_id, disable):
    return dbc.Card([
        dbc.CardHeader(div_title),
        dbc.CardBody([
            dcc.Dropdown(
                id=f'{div_id}-dropdown',
                multi=False,
                disabled=disable,
                style=dropdown_style)
        ]),
    ], color='light')


def sidebar_filters(attr_prop, disable=False):
    div_filters = []
    for k, v in attr_prop.items():
        if len(k) > 1:
            div_filters.append(div_dropdown(v['label'], k, disable))
            div_filters.append(html.Br())

    return html.Div([
        dbc.Nav(
            div_filters,
            vertical=True,
            pills=True)],
        style=SIDEBAR_STYLE)

