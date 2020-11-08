import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from helpers.layout_utils import get_menuheader
from helpers.styles import *

from app import app

###########################################################################################################################
# LAYOUT
###########################################################################################################################
def layout_page2():
    return dbc.Container(
        [
            dbc.Textarea()
        ],
        fluid=True,
        style=CONTAINER_STYLE
    )
