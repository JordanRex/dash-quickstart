import flask
from flask_caching import Cache
import dash_bootstrap_components as dbc
from dash import Dash

###########################################################################################################################
# SERVER
server = flask.Flask(__name__)

# 3rd party js to export as xlsx
external_scripts = [
    "https://oss.sheetjs.com/sheetjs/xlsx.full.min.js",
    "https://unpkg.com/dash.nprogress@latest/dist/dash.nprogress.js",
]

app = Dash(
    __name__,
    server=server,
    title={{cookiecutter.app_title}},
    update_title={{cookiecutter.update_title}},
    serve_locally=True,
    suppress_callback_exceptions=True,
    meta_tags=[
        {
            "name": "viewport",
            "content": "width=device-width, initial-scale=1.0",
        }
    ],
    external_stylesheets=[
        getattr(dbc.themes, {{cookiecutter.bootstrap_theme}}),
        dbc.icons.FONT_AWESOME,
    ],
    external_scripts=external_scripts,
    prevent_initial_callbacks="initial_duplicate",
)

###########################################################################################################################

cacheconfig = {
    "CACHE_TYPE": "filesystem",
    "CACHE_DIR": "cache-directory",
    "CACHE_THRESHOLD": 1000,
}

cache = Cache(server, config=cacheconfig)
###########################################################################################################################
