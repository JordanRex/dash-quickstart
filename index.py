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
from views import home, page1
from helpers.utils import num_workers, cur_page
from helpers.styles import *

import warnings

warnings.filterwarnings('ignore')

###########################################################################################################################
# LAYOUT
###########################################################################################################################
base_layout = dbc.Container([
    dcc.Store(id='store', storage_type='session'),
    dcc.Store(id='current_page', storage_type='session'),
    html.Div([
        dcc.Location(id='url', refresh=False),
        html.Div(id='page-content')]),
    html.Button(id='clear', n_clicks=0, style={'display': 'none'})
], style={'overflowX': 'none', 'overflowY': 'none', 'border': 'none'}
)


def serve_layout():
    if flask.has_request_context():
        return base_layout
    return html.Div([
        base_layout,
        home.layout_home,
        page1.layout_page1
    ])


app.layout = serve_layout


###########################################################################################################################


###########################################################################################################################
# CALLBACKS
###########################################################################################################################

@app.callback([Output('store', 'clear_data')],
              [Input('clear', 'n_clicks')])
def clear_scenarios(n):
    if n is None:
        raise PreventUpdate
    return [True] * 1


@app.callback([Output("page-content", "children"), Output("current_page", "data")],
              [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/page1":
        return page1.layout_page1('page1'), cur_page('page1')
    # If the user tries to reach a different page, return home
    else:
        return home.layout_home('home'), cur_page('home')


###########################################################################################################################
# APP
###########################################################################################################################
if __name__ == '__main__':
    with server.app_context():
        cache.clear()

    options = {
        'bind': '%s:%s' % ('0.0.0.0', '8080'),
        'workers': num_workers(4),
    }

    if platform.system() in ['Linux', 'Darwin']:
        mode = sys.argv[1] if len(sys.argv) > 1 else 'prod'
    else:
        mode = 'dev'

    if mode == 'prod':
        from helpers.wsgi_settings import StandaloneApplication

        StandaloneApplication(server, options).run()
    else:  # for mode=='dev' or simply null
        app.run_server(debug=True, host='0.0.0.0', port=8080, threaded=True)
