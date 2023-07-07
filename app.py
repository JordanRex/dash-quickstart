import dash
import flask

import dash_auth
import dash_bootstrap_components as dbc
import os

from helpers.secrets import VALID_USERNAME_PASSWORD_PAIRS

from config import * 

###########################################################################################################################
### FLASK SERVER ###
server = flask.Flask(__name__)

FONT_AWESOME = "https://use.fontawesome.com/releases/v5.10.2/css/all.css"

# 3rd party js to export as xlsx
external_scripts = ["https://oss.sheetjs.com/sheetjs/xlsx.full.min.js"]

app = dash.Dash(
    __name__,
    server=server,
    title=app_title,
    update_title=app_update_title,
    serve_locally=True,
    prevent_initial_callbacks=False,
    meta_tags=[
        {
            "name": "viewport",
            "content": "width=device-width, initial-scale=1.0",
        }
    ],
    external_stylesheets=[FONT_AWESOME],
    external_scripts=external_scripts,
    requests_pathname_prefix="/app/"
)

auth = dash_auth.BasicAuth(app, VALID_USERNAME_PASSWORD_PAIRS)

app.scripts.config.serve_locally = True
app.css.config.serve_locally = True
app.config.suppress_callback_exceptions = True
###########################################################################################################################

from flask_caching import Cache

cacheconfig = {
    "CACHE_TYPE": "filesystem",
    "CACHE_DIR": "cache-directory",
    "CACHE_THRESHOLD": 100,
}

cache = Cache(app.server, config=cacheconfig)
TIMEOUT = 50
###########################################################################################################################
