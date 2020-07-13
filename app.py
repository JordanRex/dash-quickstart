import dash
import dash_auth
import flask
import dash_bootstrap_components as dbc

from helpers.secrets import VALID_USERNAME_PASSWORD_PAIRS

###########################################################################################################################
### SERVER ###
server = flask.Flask(__name__)
app = dash.Dash(__name__, server=server, external_stylesheets=[dbc.themes.COSMO])

app.title = 'TITLE'
app.scripts.config.serve_locally = True
app.config.suppress_callback_exceptions = True
app.css.config.serve_locally = True

auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)
###########################################################################################################################

from flask_caching import Cache

cacheconfig = {
    'CACHE_TYPE': 'filesystem',
    'CACHE_DIR': 'cache-directory',
    'CACHE_THRESHOLD': 20
}

cache = Cache(app.server, config=cacheconfig)
TIMEOUT = 5
