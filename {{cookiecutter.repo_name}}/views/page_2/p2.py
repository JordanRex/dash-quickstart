from dash import html, Input, Output, State
import dash_bootstrap_components as dbc

from app import app

from helpers.monitoring_utils import user_logs

from views.page_2 import (
    p21,
    p22,
)

###########################################################################################################################
# PROPS
###########################################################################################################################


###########################################################################################################################
# LAYOUT
###########################################################################################################################


def layout_p2():
    tabs = dbc.Card(
        [
            dbc.CardHeader(
                dbc.Tabs(
                    [
                        dbc.Tab(
                            label="Page 2 1",
                            tab_id="tab-p2-p21",
                            activeTabClassName="fw-bold",
                        ),
                        dbc.Tab(
                            label="Page 2 2",
                            tab_id="tab-p2-p22",
                            activeTabClassName="fw-bold",
                        ),
                    ],
                    id="p2-tabs",
                    active_tab="tab-p2-p21",
                    className="justify-content-center",
                )
            ),
            dbc.CardBody(html.P(id="p2-tabs-content", className="card-text")),
        ]
    )

    return tabs


###########################################################################################################################
# CALLBACKS
###########################################################################################################################


@app.callback(
    Output("p2-tabs-content", "children"),
    [Input("p2-tabs", "active_tab")],
    [State("user_store", "data")],
)
def tab_content(at, userstore):
    if at == "tab-p2-p21":
        user_logs(userstore["username"], f"/{at}")
        return p21.layout_p21()
    else:
        user_logs(userstore["username"], f"/{at}")
        return p22.layout_p22()
