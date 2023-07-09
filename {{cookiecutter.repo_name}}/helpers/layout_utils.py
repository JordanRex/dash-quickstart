from helpers.styles import SIDEBAR_STYLE
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash import dash_table
import dash_ag_grid as dag

import dash_mantine_components as dmc
from dash_iconify import DashIconify

import pandas as pd
from app import app
from datetime import datetime
from math import ceil

import base64
from builtins import paths

abi_logo = base64.b64encode(
    open(str(paths["assets_path"]) + "/images/logo_abi/FullColor-White.png", "rb").read()
).decode("ascii")
ts_logo = base64.b64encode(
    open(
        str(paths["assets_path"]) + "/images/logo_abi/TechSupplyTransformationLogo.png", "rb"
    ).read()
).decode("ascii")

###########################################################################################################################


def return_modeofaccess():
    return dbc.Button(
        "Login/Signup",
        color="primary",
        outline=True,
        href="/login",
        className="h-50 mx-auto",
        style={"textAlign": "center", "width": "200px", "margin": "auto"},
    )


def get_sidebar(user=None):
    admin_nav = []
    if user == "admin":
        admin_nav += [
            html.Hr(),
            dbc.NavLink(
                [
                    html.I(className="fas fa-user-cog me-2"),
                    html.Span("Admin Panel"),
                ],
                href="/admin",
                active="exact",
            ),
            html.Hr(),
        ]

    return html.Div(
        [
            html.Img(
                src=f"data:image/png;base64,{abi_logo}",
                style={"width": "5rem"},
                alt="AB InBev Logo",
            ),
            html.Br(),
            html.Img(
                src=f"data:image/png;base64,{ts_logo}",
                style={"width": "5rem"},
                alt="TechSupplyTransformation Logo",
            ),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Div(
                [
                    # width: 3rem ensures the logo is the exact width of the
                    # collapsed sidebar (accounting for padding)
                    html.H5(["Supply", html.Br(), "GenAI"]),
                ],
                className="sidebar-header",
            ),
            html.Br(),
            html.Hr(),
            html.Br(),
            dbc.Nav(
                [
                    dbc.NavLink(
                        [html.I(className="fas fa-home me-2"), html.Span("Home")],
                        href="/",
                        active="exact",
                    ),
                    dbc.NavLink(
                        [
                            html.I(className="fas fa-solid fa-mortar-pestle me-2"),
                            html.Span("Library"),
                        ],
                        href="/library",
                    ),
                    dbc.NavLink(
                        [
                            html.I(className="fas fa-solid fa-filter me-2"),
                            html.Span("Services"),
                        ],
                        href="/services",
                        active="exact",
                    ),
                    *admin_nav,
                ],
                vertical=True,
                pills=True,
            ),
            html.Br(),
        ],
        className="sidebar",
        style=SIDEBAR_STYLE,
    )


###########################################################################################################################


# dash card fn to generate dropdown boxes
def div_dropdown(
    div_title,
    div_id="dummy",
    options=None,
    disable=False,
    multi=False,
    pers_type=None,
    value=None,
    clearable=False,
    footer=False,
    width="250px",
    height="200px",
    classname="ml-auto text-left",
):
    params = {
        "multi": multi,
        "disabled": disable,
        "clearable": clearable,
        "optionHeight": 35,
        # "maxHeight": 200,
    }
    if options is not None:
        params["options"] = options
    if pers_type in ["local", "memory", "session"]:
        params["persistence"] = True
        params["persistence_type"] = pers_type
    if value is not None:
        params["value"] = value
    params["id"] = f"{div_id}"

    card_children = [
        dbc.CardHeader(div_title, className="card-title"),
        dbc.CardBody([dcc.Dropdown(**params)]),
    ]

    if footer is True:
        card_children += [
            dbc.CardFooter(
                dbc.Button(
                    "Select/Unselect all",
                    id={"type": "dropdown-select_all", "index": div_id},
                    n_clicks=0,
                )
            )
        ]

    return dbc.Card(
        card_children,
        style={
            "width": width,
            "height": height,
            "overflow": "auto",
            "display": "inline",
        },
        className=classname,
    )


def input_field_col(
    field, placeholder, div_id, value=None, disabled=False, pers_type=None
):
    params = {
        "autoComplete": "true",
        "id": div_id,
        "debounce": "true",
        "maxLength": 200,
        "disabled": disabled,
    }
    if value is None:
        params["placeholder"] = placeholder
    else:
        params["value"] = value
    if pers_type in ["local", "memory", "session"]:
        params["persistence"] = "true"
        params["persistence_type"] = pers_type
    return dbc.Row(
        dbc.Col(
            [
                dbc.InputGroup(
                    [
                        dbc.InputGroupText(field),
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
                        dbc.InputGroupText(field),
                        dbc.Input(
                            placeholder=placeholder1,
                            autoComplete="true",
                            id=id1,
                        ),
                        dbc.Input(
                            placeholder=placeholder2,
                            autoComplete="true",
                            id=id2,
                        ),
                    ],
                    className="mb-3",
                )
            ],
            width={"size": 12},
        )
    )


def text_field_col(field, placeholder, id):
    return dbc.Row(
        dbc.Col(
            [
                dbc.InputGroup(
                    [
                        dbc.InputGroupText(field),
                        dbc.Textarea(
                            placeholder=placeholder,
                            id=id,
                            minLength=200,
                        ),
                    ],
                )
            ],
            width={"size": 12},
        )
    )


def check_boxes(label, id, default=None):
    if label == "":
        label_children = []
    else:
        label_children = [dbc.Label(label)]
    children = label_children + [
        dbc.RadioItems(
            options=[
                {"label": "Yes", "value": 1},
                {"label": "No", "value": 2},
            ],
            value=default,
            id=id,
            inline=True,
        )
    ]
    return dbc.Row(children)


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
    return dbc.ListGroup(
        [
            dbc.ListGroupItem(heading),
            dbc.ListGroupItem(text, id=textid),
        ],
        horizontal=True,
        className="mb-2",
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


def donut_cardcol(title, id, width=4):
    return dbc.Col(
        [
            dbc.Card(
                [
                    dbc.CardHeader(title),
                    dbc.CardBody(id=id),
                ]
            )
        ],
        width=width,
    )


def dcc_dt(div_id, df=None, columns=None, data=None):
    dt_params = dict()
    dt_params["id"] = div_id
    dt_params["style_cell"] = {
        "whiteSpace": "normal",
        "textAlign": "left",
        "height": "auto",
        "padding": "5px",
        "border": "1px solid white",
    }
    dt_params["style_header"] = {
        "color": "black",
        "backgroundColor": "white",
        "fontWeight": "bold",
        "border": "1px solid pink",
    }
    dt_params["sort_action"] = "native"
    dt_params["sort_mode"] = "multi"
    dt_params["sort_by"] = []
    dt_params["filter_action"] = "native"
    dt_params["filter_query"] = ""
    dt_params["page_size"] = 12
    dt_params["export_format"] = "xlsx"
    dt_params["export_columns"] = "all"
    dt_params["include_headers_on_copy_paste"] = True

    if df is not None:
        dt_params["data"] = df.to_dict("records")
        dt_params["columns"] = [{"name": i, "id": i} for i in df.columns]
    else:
        if columns is not None:
            dt_params["columns"] = columns
        if data is not None:
            if isinstance(data, pd.DataFrame):
                dt_params["data"] = data
            else:
                dt_params["data"] = data.to_dict("records")

    return dash_table.DataTable(**dt_params)


def input_div(placeholder, label, div_id, validate=False):
    div_content = [
        dbc.Input(
            type="text",
            placeholder=placeholder,
            id=div_id,
            autocomplete="true",
            debounce="true",
        ),
    ]

    if validate == True:
        div_content += [
            dbc.FormFeedback("That seems alright. You are good to go!", type="valid"),
            dbc.FormFeedback(
                "Sorry, seems like this name has already been used for a project",
                type="invalid",
            ),
        ]

    return dbc.Row(
        [
            dbc.Label(label, width=2),
            dbc.Col(
                html.Div(div_content),
                width=10,
            ),
        ],
        className="mb-3",
    )


def select_div(opts, label, div_id, multi=False, classname="mb-3"):
    return dbc.Row(
        [
            dbc.Label(label, width=2),
            dbc.Col(
                dcc.Dropdown(options=opts, id=div_id, multi=multi),
                width=10,
            ),
        ],
        className=classname,
    )


def modal_div(header, content, div_id):
    return html.Div(
        [
            dbc.Modal(
                [
                    dbc.ModalHeader(header),
                    dbc.ModalBody(content),
                    dbc.ModalFooter(
                        dbc.Button("Close", id=f"close-{div_id}", className="ml-auto")
                    ),
                ],
                id=div_id,
            )
        ]
    )


def dmc_textbox_div(label, placeholder, div_id):
    return dmc.Textarea(
        label=label,
        placeholder=placeholder,
        autosize=True,
        minRows=3,
        maxRows=5,
        id=div_id,
    )


def accordion_div(items_lst, div_id_prefix):
    if any(arg is None for arg in (items_lst, div_id_prefix)):
        return html.P("Provide inputs")
    else:
        accordions = []
        for k, v in items_lst.items():
            accordions += [
                dbc.AccordionItem(
                    [
                        html.P(v),
                    ],
                    title=k,
                ),
            ]
        return html.Div(
            dbc.Accordion(accordions, flush=True, always_open=True, className="mx-auto")
        )


def offcanvas_div(offcanvas_title, div_id_prefix):
    return html.Div(
        [
            dbc.Button("Open", id=f"{div_id_prefix}-open-offcanvas", n_clicks=0),
            dbc.Offcanvas(
                [html.P(offcanvas_title)],
                id=f"{div_id_prefix}-offcanvas",
                title="Title",
                is_open=False,
                placement="bottom",
                scrollable=True,
            ),
        ]
    )


def dmc_select(div_id_prefix, dat, label=None, classname="mx-auto"):
    params = {
        "icon": DashIconify(icon="radix-icons:magnifying-glass"),
        "rightSection": DashIconify(icon="radix-icons:chevron-down"),
        "id": f"{div_id_prefix}-select",
        "searchable": True,
        "nothingFound": "No options found",
        "data": dat,
        "radius": 10,
        # size="md",
        "className": classname,
    }
    if label is not None:
        params["label"] = label
    return dmc.Select(**params)


def dmc_multiselect(placeholder, div_id, opts, value=[], req=True, classname="mx-auto"):
    return dmc.MultiSelect(
        placeholder=placeholder,
        id=div_id,
        value=value,
        data=opts,
        rightSection=DashIconify(icon="radix-icons:chevron-down"),
        switchDirectionOnFlip=True,
        required=req,
        maxDropdownHeight=400,
        maxSelectedValues=5,
        debounce="true",
        radius=10,
        # size="md",
        className=classname,
    )


def dmc_grid(label, content):
    return dmc.Grid(
        [dmc.Col(dbc.Label(label), span=2), dmc.Col(content, span=10)],
        gutter="md",
        grow=True,
    )


def dmc_input(
    div_id,
    label,
    description=None,
    vals=[5, 0, 100, 5],
    type="number",
    icon="icon-park:dollar",
):
    return dmc.NumberInput(
        label=label,
        description=description,
        value=vals[0],
        min=vals[1],
        max=vals[2],
        step=vals[3],
        icon=DashIconify(icon=icon),
    )


def email_form(div_id):
    return dbc.FormFloating(
        [
            dbc.Input(type="email", placeholder="example@ab-inbev.com", id=div_id),
            dbc.Label("Email address"),
        ]
    )


def dmc_email_form(div_id, label="Email", icon="line-md:account"):
    return dmc.TextInput(
        # label=label,
        placeholder="Enter username",
        icon=DashIconify(icon="ic:round-alternate-email"),
        rightSection=DashIconify(icon=icon),
        radius=20,
        id=div_id,
    )


def password_form(div_id, label="Password"):
    return dbc.FormFloating(
        [
            dbc.Input(
                type="password",
                id=div_id,
                placeholder="Enter password",
            ),
            dbc.Label(label, html_for="example-password"),
        ],
    )


def dmc_password_form(div_id, label="Password"):
    return dmc.PasswordInput(
        # label=label,
        placeholder="Enter password",
        icon=DashIconify(icon="radix-icons:lock-closed"),
        radius=20,
        id=div_id,
    )


def ag_grid(
    div_id,
    df,
    pinned_cols=[],
    checkbox_col=None,
    add=False,
    height=700,
    defaultColDef={
        "filter": True,
        "resizable": True,
        "sortable": True,
        "editable": True,
        "floatingFilter": True,
        "minWidth": 125,
        "initialWidth": 200,
        "wrapHeaderText": True,
        "autoHeaderHeight": True,
    },
):
    columndefs = dict()
    for i in df.columns:
        columndefs[i] = {"field": i, "autoHeight": True}
        if i in pinned_cols:
            columndefs[i] = {**columndefs[i], "pinned": "left"}
        if checkbox_col is not None:
            if i == checkbox_col:
                columndefs[i] = {**columndefs[i], "checkboxSelection": True}

    columndefs = list(columndefs.values())

    dashgridoptions = {
        "rowSelection": "single",
        "pagination": True,
        "paginationPageSize": 50,
        "columnHoverHighlight": True,
    }

    if height == "auto":
        dashgridoptions = {**dashgridoptions, "domLayout": "autoHeight"}
        style = {}
    else:
        style = {"height": height}

    grid = dag.AgGrid(
        id=div_id,
        columnDefs=columndefs,
        rowData=df.to_dict("records"),
        columnSize="sizeToFit",
        defaultColDef=defaultColDef,
        dashGridOptions=dashgridoptions,
        className="ag-theme-alpine",
        style=style,
    )

    row_cols = []

    if add is True:
        row_cols += [
            dbc.Col(dbc.Button("Add", id=f"{div_id}-add", n_clicks=2), width=1)
        ]

    if all(x is False for x in [add]):
        return html.Div(
            grid,
            style={"margin": 15},
        )
    else:
        return html.Div(
            [
                dbc.Row(row_cols, align="center", justify="center"),
                grid,
            ],
            style={"margin": 15},
        )


def accordian_div(title, obj):
    return dmc.Accordion(
        children=[
            dmc.AccordionItem(
                [
                    dmc.AccordionControl(title),
                    dmc.AccordionPanel(obj),
                ],
                value="accordion",
            ),
        ],
        styles={
            "root": {
                "backgroundColor": dmc.theme.DEFAULT_COLORS["gray"][0],
                "borderRadius": 5,
            },
            "item": {
                "backgroundColor": dmc.theme.DEFAULT_COLORS["gray"][1],
                "border": "1px solid transparent",
                "position": "relative",
                "zIndex": 0,
                "transition": "transform 150ms ease",
                "&[data-active]": {
                    "transform": "scale(1.03)",
                    "backgroundColor": "white",
                    "boxShadow": 5,
                    "borderColor": dmc.theme.DEFAULT_COLORS["gray"][2],
                    "borderRadius": 5,
                    "zIndex": 1,
                },
            },
            "chevron": {
                "&[data-rotate]": {
                    "transform": "rotate(-90deg)",
                },
            },
        },
    )


def create_table(df):
    columns, values = df.columns, df.values
    header = [html.Tr([html.Th(col) for col in columns])]
    rows = [html.Tr([html.Td(cell) for cell in row]) for row in values]
    table = [html.Thead(header), html.Tbody(rows)]

    tbl = dmc.Table(
        striped=True,
        highlightOnHover=True,
        withBorder=True,
        withColumnBorders=True,
        children=table,
        style={"textAlign": "left"},
    )
    return tbl
