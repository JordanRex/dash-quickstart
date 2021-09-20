## layout_utils

###########################################################################################################################
## functions to generate dynamic layout for dash

from helpers.styles import *
from dash import html, dcc
import dash_bootstrap_components as dbc

from app import app
from config import app_support
###########################################################################################################################
###########################################################################################################################

# top header
def get_login_header():
    return dbc.NavbarSimple(
        [
            dbc.NavItem(
                dbc.NavLink(
                    "My account",
                    href="/home",
                    style=Ribbon_Style,
                    id="my-account",
                )
            ),
            dbc.NavItem(
                dbc.NavLink(
                    "Contact us",
                    href="/home",
                    style=Ribbon_Style,
                    id="contact-us",
                )
            ),
            dbc.Modal(
                [
                    dbc.ModalHeader(
                        "Have any queries?",
                        style=CONTAINER_STYLE,
                        className="card-title mb-3 text-primary text-sentencecase",
                    ),
                    dbc.ModalBody(
                        f"Please reach out to us at {app_support}",
                        style=CONTAINER_STYLE,
                    ),
                    dbc.ModalFooter(
                        [
                            dbc.Button(
                                "Close",
                                id="close",
                                className="ml-auto",
                                style=save_btn_style,
                                color="primary",
                            ),
                        ]
                    ),
                ],
                id="query-modal",
            ),
            dbc.NavItem(
                dbc.NavLink(
                    "Help",
                    # href="/assets/user_guide/User Guide.pdf",
                    # external_link="False",
                    # target="_blank",
                    style=Ribbon_Style,
                    id="help-btn",
                )
            ),
            dbc.NavItem(
                dbc.DropdownMenu(
                    children=[
                        dbc.DropdownMenuItem("Home", href="/home"),
                        dbc.DropdownMenuItem(
                            "Page 1", href="/page_1"
                        ),
                        dbc.DropdownMenuItem(divider=True),
                        dbc.DropdownMenuItem("Pages", header=True),
                        dbc.DropdownMenuItem(
                            "Page_2", href="/page_2"
                        ),
                        dbc.DropdownMenuItem(divider=True),
                    ],
                    right=True,
                    label="Menu",
                    nav=True,
                    toggle_style=Ribbon_Style,
                )
            ),
        ],
        sticky="top",
        fluid=True,
    )


# logo header
def get_logo_header():
    return dbc.Navbar(
        [
            html.A(
                dbc.Row(
                    [
                        dbc.Col(
                            html.Img(
                                src="/assets/images/lotr_icon.png",
                                height="40px",
                            )
                        ),
                    ],
                    align="center",
                    no_gutters=True,
                ),
                href="/home",
            ),
        ]
    )

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
def div_dropdown(
    div_title,
    div_id,
    options=None,
    disable=False,
    multi=False,
    pers=False,
    pers_type="session",
    value=None,
):
    params = {
        "id": f"{div_id}-dropdown",
        "multi": multi,
        "disabled": disable,
        "style": dropdown_style,
        "persistence": pers,
    }
    if options is not None:
        params["options"] = options
    if pers is True:
        params["persistence_type"] = pers_type
    if value is not None:
        params["value"] = value

    return dbc.Card(
        [
            dbc.CardHeader(div_title, style=Section_Header),
            dbc.CardBody([dcc.Dropdown(**params)]),
        ],
        color="light",
    )


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


def input_field_col(field, placeholder, id, value=None):
    params = {
        "autoComplete": True,
        "id": id,
        "debounce": True,
        "bs_size": "lg",
        "maxLength": 200,
        "style": {"font-size": "15px", "height": "100%"},
        # "minLength":"6",
    }
    if value is None:
        params["placeholder"] = placeholder
    else:
        params["value"] = value
    return dbc.Row(
        dbc.Col(
            [
                dbc.InputGroup(
                    [
                        dbc.InputGroupAddon(
                            field,
                            addon_type="prepend",
                            style={
                                "text-align": "center",
                            },
                        ),
                        dbc.Input(**params),
                    ],
                )
            ],
            width={"size": 12},
        )
    )


def input_field_col_double(field, placeholder1, id1, placeholder2, id2):
    return dbc.Row(
        dbc.Col(
            [
                dbc.InputGroup(
                    [
                        dbc.InputGroupAddon(field, addon_type="prepend"),
                        dbc.Input(
                            placeholder=placeholder1,
                            autoComplete=True,
                            id=id1,
                        ),
                        dbc.Input(
                            placeholder=placeholder2,
                            autoComplete=True,
                            id=id2,
                        ),
                    ],
                    className="mb-3",
                )
            ],
            width={"size": 12},
        )
    )


def text_field_col(field, placeholder, id, size="md"):
    return dbc.Row(
        dbc.Col(
            [
                dbc.InputGroup(
                    [
                        dbc.InputGroupAddon(field, addon_type="prepend"),
                        dbc.Textarea(
                            placeholder=placeholder,
                            bs_size=size,
                            id=id,
                            style={"font-size": "15px", "height": "100%"},
                            minLength=200,
                        ),
                    ],
                )
            ],
            width={"size": 12},
        )
    )


def check_boxes(label, id):
    return dbc.FormGroup(
        [
            dbc.Label(label, style={"font-size": "15px", "font-weight": "bold"}),
            dbc.RadioItems(
                options=[
                    {"label": "Yes", "value": 1},
                    {"label": "No", "value": 2},
                ],
                value=2,
                id=id,
                inline=True,
            ),
        ]
    )


def colrow2(a, b):
    return dbc.Row([dbc.Col([a], width=6), dbc.Col([b], width=6)])


def colrow3(a, b, c):
    return dbc.Row(
        [
            dbc.Col([a], width=4),
            dbc.Col([b], width=4),
            dbc.Col([c], width=4),
        ]
    )


def listgroupitem_obj(heading, text, textid, pers=False):
    return dbc.ListGroupItem(
        [
            dbc.ListGroupItemHeading(
                heading,
                style={
                    "textAlign": "center",
                    # "font-family": "Ariel",
                    "font-size": "12",
                },
            ),
            dbc.ListGroupItemText(
                children=text,
                id=textid,
                color="dark",
                style={
                    "textAlign": "center",
                    # "font-family": "Ariel",
                    "font-size": "20",
                },
            ),
        ],
    )


def alert_box(title, placeholder, prop_id, color="light"):
    return dbc.Row(
        [
            dbc.Col(
                [dbc.Alert(title, color="light")],
                width=4,
            ),
            dbc.Col(
                [
                    dbc.Alert(
                        placeholder,
                        id=prop_id,
                        color="light",
                    )
                ],
                width=8,
            ),
        ]
    )


def col_img(url, w, header, footer=None):
    img_card = [
        dbc.CardHeader(header),
        dbc.CardBody(html.A(html.Img(src=app.get_asset_url(url)))),
    ]

    if footer is not None:
        img_card.append(dbc.CardFooter(footer))

    return dbc.Col(
        [dbc.Card(img_card)],
        width=w,
    )
