import dash
import flask

import dash_auth
import dash_bootstrap_components as dbc
import os

from helpers.secrets import VALID_USERNAME_PASSWORD_PAIRS

###########################################################################################################################
### SERVER ###
server = flask.Flask(__name__)
app = dash.Dash(
    __name__,
    server=server,
    title="App",
    update_title="App is working",
    serve_locally=True,
)

auth = dash_auth.BasicAuth(app, VALID_USERNAME_PASSWORD_PAIRS)

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
