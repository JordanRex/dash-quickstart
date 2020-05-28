import dash_html_components as html
import dash_bootstrap_components as dbc

from helpers.layout_utils import get_menuheader
from helpers.styles import *

from app import app


###########################################################################################################################
# LAYOUT
###########################################################################################################################
def layout_home(linkclass):
    return dbc.Container(
        [
            dbc.Row(dbc.Col([get_menuheader(linkclass)]))
        ],
        fluid=True,
        style=CONTAINER_STYLE
    )
