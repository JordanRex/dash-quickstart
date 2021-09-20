from dash import html, dcc
import dash_bootstrap_components as dbc

from helpers.layout_utils import get_menuheader
from helpers.styles import *

from app import app


###########################################################################################################################
# LAYOUT
###########################################################################################################################
def layout_home():
    return dbc.Container(
        [
            dbc.Row(dbc.Col([get_menuheader()]))
        ],
        fluid=True,
        style=CONTAINER_STYLE
    )


###########################################################################################################################
# CALLBACKS
###########################################################################################################################