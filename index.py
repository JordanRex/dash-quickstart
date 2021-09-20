# ###########################################################################################################################
# """
# uncomment below to use with gunicorn:gevent
# it is currently an issue to use gevent along with the requests module (infinite recursion depth issue)
# this has to be at the topmost level
# """
import gevent.monkey
gevent.monkey.patch_all()
# ###########################################################################################################################

import sys
import platform

import pandas as pd
from dash import Dash, callback, html, dcc, dash_table, Input, Output, State, MATCH, ALL
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
import flask

from app import app as app, server as server, cache, cacheconfig
from config import *
from views import home, page_1, page_2
from helpers.styles import *
from helpers.utils import (
    num_workers,
    cur_page,
    error404,
    coming_soon,
    under_construction,
)
from helpers.styles import *
from helpers.layout_utils import *

import warnings
warnings.filterwarnings('ignore')

pd.set_option("display.max_columns", 100)

from werkzeug.serving import WSGIRequestHandler

###########################################################################################################################
# APP
###########################################################################################################################
if __name__ == "__main__":
    with server.app_context():
        cache.clear()

    WSGIRequestHandler.protocol_version = "HTTP/1.1"

    mode = (
        sys.argv[1] if len(sys.argv) > 1 else "dev"
    )  # can take values of prod, dev and maintenance
    prod_server = sys.argv[2] if len(sys.argv) > 2 else "waitress"
    n = sys.argv[3] if len(sys.argv) > 3 else None
    n_workers = num_workers(n)
    ssl_flag = sys.argv[4] if len(sys.argv) > 4 else "no"
    flask_server = sys.argv[5] if len(sys.argv) > 5 else "no"

    ###########################################################################################################################
    # LAYOUT
    ###########################################################################################################################
    base_layout = html.Div(
        [
            get_login_header(),
            get_logo_header(),
            dcc.Store(id='user-store', storage_type='session'),
            dcc.Location(id='url', refresh=False),
            html.Div(id="page-content", style=base_div_style),
            html.Div(
                html.Footer(
                    html.P(app_footer),
                    style=footer_div_style,
                )
            ),
        ], style=CONTAINER_STYLE
    )


    validation_layout = html.Div(
            [
                base_layout,
                home.layout_home,
                page_1.layout_page1,
                page_2.layout_page2
            ]
        )

    app.validation_layout = validation_layout
    app.layout = base_layout

    ###########################################################################################################################
    # CALLBACKS
    ###########################################################################################################################

    @app.callback(Output("page-content", "children"),
                  [Input("url", "pathname")])
    def render_page_content(pathname):
        if pathname in ["/", "/home"]:
            return home.layout_home()
        elif pathname == "/page_1":
            return page_1.layout_page1()
        elif pathname == "/page_2":
            # return page_2.layout_page2()
            return coming_soon()
        else:
            return error404()

    ###########################################################################################################################

    ssl_context = ("../cer/app.cer", "../cer/app.key")

    def dashapp_fn(dashapp, flask_mode="no", ssl="no", sslcontext=None):
        params = {
            "host": "0.0.0.0",
            "port": 8050,
        }

        if ssl != "no":
            if sslcontext == None:
                sys.exit("provide ssl context")
            else:
                params["ssl_context"] = sslcontext

        if flask_mode == "no":
            params["debug"] = True
            params["threaded"] = True
            return dashapp.run_server(**params)
        else:
            params["debug"] = False
            return dashapp.run(**params)

    gunicorn_options = {
        "bind": "%s:%s" % ("0.0.0.0", "8050"),
        "workers": n_workers,
        "timeout": 3600,
        "preload_app": True,
        "keepalive": 3600,
        "worker_class": "gevent",
    }
    if ssl_flag != "no":
        gunicorn_options["certfile"] = "../cer/app.cer"
        gunicorn_options["keyfile"] = "../cer/app.key"

    if mode == "prod":
        if platform.system() in ["Linux", "Darwin"]:
            if prod_server == "waitress":
                from waitress import serve

                serve(
                    server,
                    host="0.0.0.0",
                    port=8080,
                    threads=n_workers,
                    channel_timeout=1200,
                    log_socket_errors=False,
                    url_scheme="https",
                )
            else:
                from helpers.gunicorn import StandaloneApplication

                StandaloneApplication(server, gunicorn_options).run()
        else:
            from waitress import serve

            serve(
                server,
                host="0.0.0.0",
                port=8050,
                threads=n_workers,
                channel_timeout=3600,
                log_socket_errors=False,
                url_scheme="https",
            )
    else:
        if flask_server != "no":
            dashapp_fn(server, flask_server, ssl_flag, ssl_context)
        else:
            dashapp_fn(app, flask_server, ssl_flag, ssl_context)