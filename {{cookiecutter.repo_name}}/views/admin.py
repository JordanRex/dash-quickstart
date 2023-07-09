from app import app
import glob
import pandas as pd
import dash_bootstrap_components as dbc
from dash import html, dcc, Input, Output
from dbconfig.sqlite3_script import pd_from_sql
from helpers.layout_utils import dmc_select


###########################################################################################################################
# PROPS
###########################################################################################################################


def markdown_viewer():
    files = glob.glob("docs/*.md")
    files_opts = [{"label": x.split("\\")[1], "value": x} for x in files]
    return dbc.Col(
        [
            html.P("Markdown Viewer"),
            dmc_select("md-viewer-opts", files_opts),
            html.Br(),
            dcc.Markdown(id="md-viewer"),
        ],
        width=8,
    )


###########################################################################################################################
# LAYOUT
##########################################################################################################################


def layout_admin():
    # create layout with slider and store
    return dbc.Container(
        [dbc.Row([markdown_viewer()], align="center", justify="center")],
        fluid=True,
        className="mx-auto",
    )


###########################################################################################################################
# CALLBACKS
###########################################################################################################################


@app.callback(
    Output("md-viewer", "children"),
    Input("md-viewer-opts-select", "value"),
    prevent_initial_call=True,
)
def md_viewer(file):
    with open(file, "r") as file:
        x = file.read()
    return f"""{x}"""
