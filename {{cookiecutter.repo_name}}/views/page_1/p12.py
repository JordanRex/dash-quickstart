import dash_bootstrap_components as dbc
from dash import html


def layout_p12():
    return dbc.Container(
        [
            html.Br(),
            dbc.Row(
                dbc.Col(html.H3("TITLE"), width="auto"),
                justify="center",
            ),
            html.Br(),
        ],
        fluid=True,
    )


###########################################################################################################################
# CALLBACKS
###########################################################################################################################
