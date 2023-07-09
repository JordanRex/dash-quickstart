import pandas as pd
import numpy as np
from dash import dcc, html, Output, Input, State
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc

from helpers.layout_utils import (
    accordion_div,
    offcanvas_div,
    return_modeofaccess,
    create_table,
)
from app import app

from dbconfig.sqlite3_script import pd_from_sql

import base64
from builtins import paths

logo = base64.b64encode(
    open(paths["assets_path"] + "/images/home/logo.png", "rb").read()
).decode("ascii")

###########################################################################################################################
# PROPS
###########################################################################################################################


###########################################################################################################################
# LAYOUT
###########################################################################################################################


def layout_home():
    home_content = [
        html.P(
            "WELCOME to SupplyGenAI Platform!",
            style={"font-weight": "bold", "font-size": 48, "color": "white"},
        )
    ]

    return dbc.Container(
        home_content,
        fluid=True,
        style={"textAlign": "center", "margin": "auto"},
        className="divcenter",
    )


###########################################################################################################################
# CALLBACKS
###########################################################################################################################
