## layout_utils

## functions to generate dynamic layout for dash

from helpers.styles import *
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from app import app


###########################################################################################################################
# menu function
def get_menuheader(linkclass='home'):
    return dbc.Container(
        [
            dbc.Row(
                [
                    html.A(html.Img(
                        src=app.get_asset_url('imgs/'),
                        className="logo",
                        style=bain_logo_style,
                    ), href='/home'),
                    html.Div(
                        [html.H4(children="Application", style={'font-size': 40})],
                        style=app_title_style
                    )
                ],
                className="row all-tabs"
            ),
            dbc.Row([
                dcc.Link(
                    "Home",
                    href="/home",
                    className=f"a{' active' if linkclass == 'home' else ''}",
                    id='home-link'
                ),
                dcc.Link(
                    "Page One",
                    href="/page1",
                    className=f"a{' active' if linkclass == 'p1' else ''}",
                    id='p1-link'
                ),
            ])], style=HEADER_STYLE)


###########################################################################################################################
# dash card fn to generate dropdown boxes
def div_dropdown(div_title, div_id, linkclass, disable):
    return dbc.Card([
        dbc.CardHeader(div_title),
        dbc.CardBody([
            dcc.Dropdown(
                id=f'{div_id}-{linkclass}-dropdown',
                multi=False,
                disabled=disable,
                style=dropdown_style)
        ]),
    ], color='light')


def sidebar_filters(attr_prop, linkclass, disable=False):
    div_filters = []
    for k, v in attr_prop.items():
        if len(k) > 1:
            div_filters.append(div_dropdown(v['label'], k, linkclass, disable))
            div_filters.append(html.Br())

    return html.Div([
        dbc.Nav(
            div_filters,
            vertical=True,
            pills=True)],
        style=SIDEBAR_STYLE)

###########################################################################################################################
# dash card fn to generate scenario buttons (dynamic)
# def scenario_btn(itr, linkclass, show):
#     scenario_display_num = itr + 1
#     if f'btn-{itr}-{linkclass}' in show:
#         return dbc.Button(f'Scenario {scenario_display_num}', id=f'btn-{itr}-{linkclass}', className='button-primary', style=btn_active_style)
#     else:
#         return dbc.Button(f'Scenario {scenario_display_num}', id=f'btn-{itr}-{linkclass}', className='button-primary', style=btn_hidden_style)
# def scenarios_card(num, linkclass):
#     div_scenarios = []
#     show_scenario = [f'btn-0-{linkclass}']
#     for i in range(num):
#         div_scenarios.append(scenario_btn(i, linkclass, show_scenario))
#     if linkclass=="cs":
#         div_scenarios.append(dbc.Button('+', id="btn+", className='button-primary', style=btn_plus))
#     scenarios_card_output = html.Div([
#                 dbc.Row([
#                     dbc.Col(
#                         dbc.ButtonGroup(id=f'scenarios_card-{linkclass}', children=div_scenarios, style={'padding': '5px'}), width=12)
#                 ],
#                     justify='start'
#                 )],
#                 style=scenario_buttons_row_style)
#     return scenarios_card_output
###########################################################################################################################
