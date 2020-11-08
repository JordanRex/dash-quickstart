import sys
import platform

import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
import flask

from app import app as app, server as server, cache, cacheconfig
import views
from helpers.utils import num_workers, cur_page
from helpers.styles import *

import warnings
warnings.filterwarnings('ignore')

###########################################################################################################################
# LAYOUT
###########################################################################################################################
base_layout = dbc.Container(
    [
        dcc.Store(id='store', storage_type='session'),
        html.Div(
            [
                dcc.Location(id='url', refresh=False),
                html.Div(id='page-content')]),
    ], style={'overflowX': 'none', 'overflowY': 'none', 'border': 'none'}
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
app.layout = serve_layout

###########################################################################################################################


###########################################################################################################################
# CALLBACKS
###########################################################################################################################

@app.callback(Output("page-content", "children"),
              [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/page_1":
        return page_1.layout_page1()
    elif pathname == "/page_2":
        return page_2.layout_page2()
    # If the user tries to reach a different page, return home
    else:
        return home.layout_home()


###########################################################################################################################
# APP
###########################################################################################################################
if __name__ == "__main__":
    # with server.app_context():
    #     cache.clear()

    mode = sys.argv[1] if len(sys.argv) > 1 else "dev"
    n = sys.argv[2] if len(sys.argv) > 2 else None
    n_workers = num_workers(n)

    options = {
        "bind": "%s:%s" % ("0.0.0.0", "8080"),
        "workers": n_workers,
    }

    if platform.system() in ["Linux", "Darwin"]:
        if mode == "prod":
            from helpers.gunicorn import StandaloneApplication

            StandaloneApplication(server, options).run()
        else:  # for mode=='dev' or simply null
            app.run_server(debug=True, host="0.0.0.0", port=8080, threaded=True)
    else:
        if mode == "prod":
            from waitress import serve

            serve(
                server,
                host="0.0.0.0",
                port=8080,
                threads=n_workers,
                channel_timeout=300,
            )
        else:  # for mode=='dev' or simply null
            app.run_server(debug=True, host="0.0.0.0", port=8080, threaded=True)
