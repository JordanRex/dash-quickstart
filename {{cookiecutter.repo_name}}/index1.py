import pandas as pd
import platform
import sys

from app import (
    app,
    server,
    cache,
)
from flask import redirect, request

import dash_bootstrap_components as dbc
from dash import html, dcc, Input, Output, State, ctx, no_update
import dash_mantine_components as dmc
from dash_iconify import DashIconify

import os
import builtins

import warnings

warnings.filterwarnings("ignore")

pd.set_option("display.max_columns", 100)

###########################################################################################################################
# APP
###########################################################################################################################

if __name__ == "__main__":
    with server.app_context():
        cache.clear()

    from helpers.utils import num_workers, error404, under_construction

    mode = (
        sys.argv[1] if len(sys.argv) > 1 else "dev"
    )  # can take values of prod, dev and maintenance
    prod_server = sys.argv[2] if len(sys.argv) > 2 else "waitress"
    dev_mode = sys.argv[3] if len(sys.argv) > 3 else "dash"
    n = sys.argv[4] if len(sys.argv) > 4 else 6
    n_workers = num_workers(n)

    from dotenv import load_dotenv

    load_dotenv()

    builtins.sqldb = {{cookiecutter.sqldb}}

    ###########################################################################################################################
    #### PATHS ####
    ###########################################################################################################################

    # the various absolute paths
    paths = dict()
    paths["base_path"] = os.getcwd()
    paths["assets_path"] = paths["base_path"] + r"/assets"

    for k in paths.keys():
        paths[k] = os.path.normpath(paths[k])
    builtins.paths = paths

    ###########################################################################################################################
    #### IMPORTS ####
    ###########################################################################################################################

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

    base_layout = dmc.NotificationsProvider(
        html.Div(
            [
                html.Div(id="notify-container"),
                dbc.Container(
                    dbc.Row(
                        [
                            dbc.Col(get_sidebar(user=None), width=2),
                            dbc.Col(
                                [
                                    # user stores
                                    dcc.Store(id="user_store", storage_type="session"),
                                    dcc.Location(id="url", refresh=False),
                                    html.Div(id="page-content", className="content"),
                                    html.Div(id="admin_nav", className="content"),
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

    app.validation_layout = validation_layout
    app.layout = base_layout

    ###########################################################################################################################
    # CALLBACKS
    ###########################################################################################################################

    # Define a dictionary mapping URL paths to layout functions
    LAYOUTS = {
        "/": home.layout_home(),
        "/home": home.layout_home(),
        "/page_1": p1.layout_p1(),
        "/page_2": p2.layout_p2(),
        "/admin": admin.layout_admin(),
    }

    # Define a list of URLs that require authentication
    AUTH_REQUIRED_URLS = ["/home", "/page_1", "/page_2", "/admin"]

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
        style = {
            "display": "flex",
            "alignItems": "center",
            "justifyContent": "center",
            "padding": "10px",
            "backgroundColor": "white",
        }
        # Check if the website is in maintenance mode
        if mode == "maintenance":
            return under_construction(), None, no_update
        elif mode == "dev":
            user_store = dict()
            user_store["username"] = "Admin"

            if pathname == "/":
                style = no_update

            return LAYOUTS[pathname], user_store, style
        else:
            if pathname == "/":
                user_store = dict()
                if {{cookiecutter.azure_ad}} is True:
                    user_store["username"] = request.headers.get(
                        "X-MS-CLIENT-PRINCIPAL-NAME"
                    )
                else:
                    user_store["username"] = "No Azure AD"
                return home.layout_home(), user_store, no_update

            if pathname in AUTH_REQUIRED_URLS:
                if (userstore is None) | (userstore["username"] == None):
                    user_store = dict()
                    user_store["username"] = request.headers.get(
                        "X-MS-CLIENT-PRINCIPAL-NAME"
                    )
                    return home.layout_home(), user_store, no_update
                else:
                    user_logs(userstore["username"], pathname)
                    return LAYOUTS[pathname], no_update, style
            else:
                # If the user tries to reach a different page, return home
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
