import argparse
from pathlib import Path
import pandas as pd
import platform
import sys
import warnings
from dotenv import load_dotenv
import builtins

from app import app, server, cache
from flask import redirect, request

import dash_bootstrap_components as dbc
from dash import html, dcc, Input, Output, State, ctx, no_update
import dash_mantine_components as dmc
from dash_iconify import DashIconify

# Set warning filters and pandas options
warnings.filterwarnings("ignore")
pd.set_option("display.max_columns", 100)

# Constants
DEFAULT_MODE = "dev"
DEFAULT_PROD_SERVER = "waitress"
DEFAULT_DEV_MODE = "dash"
DEFAULT_WORKERS_NUM = 6

def main():
    """
    The main function to run the app.
    Runs off index.py based on the arguments passed at server time
    """
    # Parse command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', default=DEFAULT_MODE,
                        help='Can take values of prod, dev and maintenance')
    parser.add_argument('--prod-server', default=DEFAULT_PROD_SERVER)
    parser.add_argument('--dev-mode', default=DEFAULT_DEV_MODE)
    parser.add_argument('--workers', type=int, default=DEFAULT_WORKERS_NUM)
    args = parser.parse_args()

    with server.app_context():
        cache.clear()

    from helpers.utils import num_workers, error404, under_construction
    n_workers = num_workers(args.workers)

    load_dotenv()

    builtins.sqldb = "{{cookiecutter.sqldb}}"

    """
    Define the paths variable
    """
    # Paths
    paths = dict()
    base_path = Path.cwd()
    paths["base_path"] = base_path
    paths["assets_path"] = base_path / "assets"

    # Normalize paths
    for k in paths.keys():
        paths[k] = paths[k].resolve()
    builtins.paths = paths

    ###########################################################################################################################
    #### IMPORTS ####
    ###########################################################################################################################

    """
    Import the various pages and utils
    """
    # the helper functions from various modules
    from helpers.layout_utils import get_sidebar
    from helpers.monitoring_utils import user_logs

    from views import home, admin
    from views.page_1 import p1, p11, p12
    from views.page_2 import (
        p2,
        p21,
        p22,
    )

    ###########################################################################################################################
    # LAYOUT
    ###########################################################################################################################

    # Creating the base layout for the application
    base_layout = dmc.NotificationsProvider(
        html.Div(
            [
                # Container for notifications
                html.Div(id="notify-container"),
                # Main content of the application
                dbc.Container(
                    dbc.Row(
                        [
                            # Sidebar
                            dbc.Col(get_sidebar(user=None), width=2),
                            # Main content area
                            dbc.Col(
                                [
                                    # User store
                                    dcc.Store(id="user_store",
                                              storage_type="session"),
                                    # URL location
                                    dcc.Location(id="url", refresh=False),
                                    # Page content
                                    html.Div(id="page-content",
                                             className="content"),
                                    # Admin navigation
                                    html.Div(id="admin_nav",
                                             className="content"),
                                    # Breakline
                                    html.Br(),
                                ],
                                width=12,
                            ),
                        ],
                        align="center",
                        justify="center",
                    ),
                    fluid=True,
                ),
            ],
            id="main-div",
            style={
                "display": "flex",
                "alignItems": "center",
                "justifyContent": "center",
                "padding": "10px",
                "backgroundImage": 'url("assets/images/home/white_abstract.jpg")',
                "backgroundSize": "cover",
                "backgroundRepeat": "no-repeat",
                "minHeight": "100vh",
                "backgroundAttachment": "fixed",
            },
        )
    )

    # Validation layout includes all the possible layouts that could be returned by callbacks
    validation_layout = html.Div(
        [
            base_layout,
            home.layout_home,
            admin.layout_admin,
            p1.layout_p1,
            p11.layout_p11,
            p12.layout_p12,
            p2.layout_p2,
            p21.layout_p21,
            p22.layout_p22,
        ]
    )

    # Set the validation layout of the app
    app.validation_layout = validation_layout

    # Set the layout of the app
    app.layout = base_layout


    ###########################################################################################################################
    # CALLBACKS
    ###########################################################################################################################
    # Define a dictionary mapping URL paths to layout functions
    LAYOUTS = {
        "/": home.layout_home,
        "/home": home.layout_home,
        "/page_1": p1.layout_p1,
        "/page_2": p2.layout_p2,
        "/admin": admin.layout_admin,
    }

    # Define a list of URLs that require authentication
    AUTH_REQUIRED_URLS = ["/home", "/page_1", "/page_2", "/admin"]

    def get_style():
        return {
            "display": "flex",
            "alignItems": "center",
            "justifyContent": "center",
            "padding": "10px",
            "backgroundColor": "white",
        }

    # Define the callback function
    @app.callback(
        [
            Output("page-content", "children"),
            Output("user_store", "data"),
            Output("main-div", "style"),
        ],
        [Input("url", "pathname")],
        [State("user_store", "data")],
    )
    def render_page_content(pathname, userstore):
        style = get_style()
        user_store = dict()

        if mode == "maintenance":
            return under_construction(), None, no_update

        if mode == "dev":
            user_store["username"] = "Admin"
            if pathname == "/":
                style = no_update
            return LAYOUTS[pathname](), user_store, style

        if pathname == "/":
            user_store["username"] = "No Azure AD" if not cookiecutter.azure_ad else request.headers.get(
                "X-MS-CLIENT-PRINCIPAL-NAME")
            return home.layout_home(), user_store, no_update

        if pathname in AUTH_REQUIRED_URLS:
            if (userstore is None) or (userstore["username"] is None):
                user_store["username"] = request.headers.get(
                    "X-MS-CLIENT-PRINCIPAL-NAME")
                return home.layout_home(), user_store, no_update
            else:
                user_logs(userstore["username"], pathname)
                return LAYOUTS[pathname](), no_update, style

        # If the user tries to reach a different page, return a 404 error
        return error404(), no_update, no_update

    @app.callback(
        Output("admin_nav", "children"),
        Input("user_store", "data"),
    )
    def update_sidebar(userstore):
        if userstore["username"] == "Admin":
            return get_sidebar("admin")

    @app.callback(
        Output("notify-container", "children"),
        Input("user_store", "data"),
        prevent_initial_call=True,
    )
    def notify(store):
        username = store["username"]
        title = {{cookiecutter.app_title}}
        return dmc.Notification(
            id="my-notification",
            title=f"Welcome {username} to {title}",
            message="Logged in",
            # loading=True,
            color="green",
            action="show",  # update
            # autoClose=False,
            # disallowClose=True,
            icon=DashIconify(icon="emojione:beer-mug"),
        )

    ###########################################################################################################################

    def dashapp_fn(app_obj, flask=False):
        params = {
            "host": "0.0.0.0",
            "port": 8080,
            "debug": True,
            "threaded": True,
            "use_reloader": True,
        }
        if flask == True:
            return app_obj.run(**params)
        else:
            return app_obj.run_server(**params)

    def waitress_fn():
        from waitress import serve

        serve(
            app.server,
            host="0.0.0.0",
            port=8080,
            threads=n_workers,
            channel_timeout=3600,
            log_socket_errors=False,
            url_scheme="https",
        )

    def gunicorn_fn():
        gunicorn_options = {
            "bind": "%s:%s" % ("0.0.0.0", "8080"),
            "workers": n_workers,
            "preload_app": True,
            "keepalive": 3600,
            "worker_class": "gevent",
        }

        from helpers.gunicorn import StandaloneApplication

        StandaloneApplication(app.server, gunicorn_options).run()

    if mode == "prod":
        if platform.system() in ["Linux", "Darwin"]:
            if prod_server == "gunicorn":
                gunicorn_fn()
            else:
                waitress_fn()
        else:
            waitress_fn()
    else:
        if dev_mode == "dash":
            dashapp_fn(app)
        else:
            dashapp_fn(app.server, True)


if __name__ == "__main__":
    main()
