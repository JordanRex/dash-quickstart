from dash import html, dcc, Input, Output
import dash_bootstrap_components as dbc

from helpers.layout_utils import get_menuheader
from helpers.styles import *

from app import app


###########################################################################################################################
# LAYOUT
###########################################################################################################################
def layout_page2():
    return dbc.Container([dbc.Textarea()], fluid=True, style=CONTAINER_STYLE)


###########################################################################################################################
# CALLBACKS
###########################################################################################################################
