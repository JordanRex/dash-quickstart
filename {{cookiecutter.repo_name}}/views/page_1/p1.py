from dash import html, Input, Output, State
import dash_bootstrap_components as dbc

from app import app

from helpers.monitoring_utils import user_logs

from views.page_1 import (
    p11,
    p12,
)

###########################################################################################################################
# PROPS
###########################################################################################################################


###########################################################################################################################
# LAYOUT
###########################################################################################################################


def layout_p1():
    tabs = dbc.Card(
        [
            dbc.CardHeader(
                dbc.Tabs(
                    [
                        dbc.Tab(
                            label="Page 1 1",
                            tab_id="tab-p1-p11",
                            activeTabClassName="fw-bold",
                        ),
                        dbc.Tab(
                            label="Page 1 2",
                            tab_id="tab-p1-p12",
                            activeTabClassName="fw-bold",
                        ),
                    ],
                    id="p1-tabs",
                    active_tab="tab-p1-p11",
                    className="justify-content-center",
                )
            ),
            dbc.CardBody(html.P(id="p1-tabs-content", className="card-text")),
        ]
    )

    return tabs


###########################################################################################################################
# CALLBACKS
###########################################################################################################################


@app.callback(
    Output("p1-tabs-content", "children"),
    [Input("p1-tabs", "active_tab")],
    [State("user_store", "data")],
)
def tab_content(at, userstore):
    if at == "tab-p1-p11":
        user_logs(userstore["username"], f"/{at}")
        return p11.layout_p11()
    else:
        user_logs(userstore["username"], f"/{at}")
        return p12.layout_p12()
