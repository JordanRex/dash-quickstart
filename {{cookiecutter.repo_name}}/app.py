import flask
from flask_caching import Cache
import dash_bootstrap_components as dbc
from dash import Dash

# Constants
EXTERNAL_SCRIPTS = [
    "https://oss.sheetjs.com/sheetjs/xlsx.full.min.js",
    "https://unpkg.com/dash.nprogress@latest/dist/dash.nprogress.js",
]

CACHE_CONFIG = {
    "CACHE_TYPE": "filesystem",
    "CACHE_DIR": "cache-directory",
    "CACHE_THRESHOLD": 1000,
}

def create_server():
    """
    Creates and returns a Flask server.
    
    :return: A Flask server instance.
    :rtype: flask.Flask
    """
    return flask.Flask(__name__)

def create_app(server):
    """
    Creates and returns a Dash app with specified server.
    
    :param server: The server for the Dash app.
    :type server: flask.Flask
    :return: A Dash app instance.
    :rtype: dash.Dash
    """
    print(getattr(dbc.themes, "{{ cookiecutter.bootstrap_theme }}"))
    app = Dash(
        __name__,
        server=server,
        title="{{ cookiecutter.app_title }}",
        update_title="{{ cookiecutter.app_update_title }}",
        serve_locally=True,
        suppress_callback_exceptions=True,
        meta_tags=[
            {
                "name": "viewport",
                "content": "width=device-width, initial-scale=1.0",
            }
        ],
        external_stylesheets=[
            getattr(dbc.themes, "{{ cookiecutter.bootstrap_theme }}"),
            dbc.icons.FONT_AWESOME,
        ],
        external_scripts=EXTERNAL_SCRIPTS,
        prevent_initial_callbacks="initial_duplicate",
    )
    return app

def create_cache(server, config):
    """
    Creates and returns a Cache instance with specified server and configuration.
    
    :param server: The server for the Cache.
    :type server: flask.Flask
    :param config: The configuration for the Cache.
    :type config: dict
    :return: A Cache instance.
    :rtype: flask_caching.Cache
    """
    return Cache(server, config=config)

server = create_server()
app = create_app(server)
cache = create_cache(server, CACHE_CONFIG)
