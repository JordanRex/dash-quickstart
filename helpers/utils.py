import numpy as np, pandas as pd

import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dash import no_update
from multiprocessing import cpu_count

from helpers.styles import *

from app import app as app


def make_dash_table(df):
    """ Return a dash definition of an HTML table for a Pandas dataframe """
    table = []
    for index, row in df.iterrows():
        html_row = []
        for i in range(len(row)):
            html_row.append(html.Td([row[i]]))
        table.append(html.Tr(html_row))
    return table


def second_largest(numbers):
    count = 0
    m1 = m2 = float('-inf')
    for x in numbers:
        count += 1
        if x > m2:
            if x >= m1:
                m1, m2 = x, m1
            else:
                m2 = x
    return m2 if count >= 2 else None


def make_annotation_item(x, y, color, text, xloc):
    return dict(xref='x', yref='y',
                x=x, y=y,
                font=dict(color=color, size=16),
                xanchor=xloc,
                yanchor='middle',
                text=text,
                showarrow=False)


# modify below tooltip as a callback to filter for the specific skus to display on hover (callback in retailer_view)
def make_tooltip(cell):
    try:
        num = float(cell)
        return textwrap.dedent(
            '''
            Tooltip for value **{value:+.2f}**.
            | Multiplier | Value |  Percent |
            |-------|-------|---------------|
            | 1     | {value_1:+.2f}     | {value_1:+.2f}% |
            '''.format(
                value=num,
                value_1=num
            )
        )
    except:
        return textwrap.dedent(
            '''
            Tooltip: **{value}**.
            '''.format(value=cell)
        )


# no update function for callbacks with multiple outputs
def noupdate(value, type='options', label=None):  # type == one of ['options', 'values']
    if value is None:
        return no_update
    else:
        if type == 'options':
            if label is None:
                return [{'label': value, 'value': value}]
            else:
                return [{'label': label, 'value': value}]
        elif type == 'values':
            if value == [] or value[0]['value'] is None:
                return no_update
            else:
                return value[0]['value']


# np select wrapper
def select_multiple(df, newcol, choices, default, cols=[], vals=[]):
    conditions = [
        (df[cols[0]] > vals[0]) & (df[cols[1]] > vals[1]),
        (df[cols[0]] < vals[0]) & (df[cols[1]] > vals[1]),
        (df[cols[0]] < vals[0]) & (df[cols[1]] < vals[1]),
        (df[cols[0]] > vals[0]) & (df[cols[1]] < vals[1])]
    df[newcol] = np.select(conditions, choices, default=default)
    return df


def make_pct(df, cols):
    for i in cols:
        if df[i].max() <= 1:
            df[i] = 100 * df[i]
    return df


def make_round(df, degree=1):
    temp = df.select_dtypes(include=[np.number])
    df.loc[:, temp.columns] = np.round(temp, degree)
    return df


def make_round_commasep(num):
    return f'{currency_prefix} {int(np.round(num, 0)):,} {currency_suffix}'


#####################################################################################
# bubble chart functions

def figure_bubble(x, y, name, size, color_fill, color_outline, size_max, text):
    currency = currency_prefix if currency_suffix == '' else currency_suffix
    return {
        'x': x,
        'y': y,
        'mode': 'markers',
        'name': name,
        'marker': {
            'size': size,
            'color': color_fill,
            'line': {
                'color': color_outline
            },
            'sizemode': 'area',
            'sizeref': 2. * size_max / (40. ** 2),
            'sizemin': 4
        },
        'text': text,
        'customdata': [currency] * len(x),
        'hovertemplate':
            "<b>SKU: %{text}</b><br><br>" +
            "Sales: %{marker.size:,.0f}%{customdata}<br>" +
            "Risk: %{x}%<br>" +
            "TNP: %{y}%<br>" +
            "<extra></extra>",
        'textfont': {
            'family': "Graphik Web",
            'weight': 200,
            'style': 'roman'
        }
    }


def figure_line(x, y):
    return {
        'x': x,
        'y': y,
        'mode': 'lines',
        'showlegend': False,
        'line': {'dash': 'dash', 'color': color_bain_red}
    }


def figure_layout(ann):
    return {
        'xaxis': {'title': 'X', 'autorange': "normal"},
        'yaxis': {'title': 'Y', 'autorange': "normal"},
        'hovermode': 'closest',
        'clickmode': 'event+select',
        'annotations': ann,
        'layer': 'below',
        'font': {
            'family': 'Graphik Web',
            'weight': 200,
            'style': 'roman'
        }
    }


def kpi_card(header, x, y, kpis):
    return dbc.Col(dbc.Card([
        dbc.CardHeader(header),
        dbc.CardBody(children=[html.P(kpis.iloc[x, y],
                                      style={'font-weight': 700, 'font-size': 13})])],
        color="dark", outline=True))


#####################################################################################
## utility functions

def num_workers(workers=None):
    if workers is None:
        return (cpu_count() * 2) - 1
    else:
        return workers


def cur_page(page):
    return {'page': page}


def impute_null_nan(x, y):
    r_val = ''
    if x == np.nan:
        r_val = str(y)
    elif str(x).strip() == 'nan':
        r_val = str(y)
    elif str(x).strip() == '':
        r_val = str(y)
    else:
        r_val = x

    if r_val == '':
        return 'Description Not Available'
    elif str(r_val) == 'nan':
        return 'Description Not Available'
    else:
        return r_val


def return_sankey_fn(node_labels, xpos, ypos, colors,
                     source_ids, target_ids, link_val, link_labels):
    return {
        'data': [
            {
                'type': 'sankey',
                'valueformat': '.2f',
                'node': {
                    'pad': 15,
                    'thickness': 15,
                    'line': {'color': 'black', 'width': 0.5},
                    'label': node_labels,
                    'x': xpos,
                    'y': ypos,
                    'color': colors,
                    'hovertemplate':
                        "%{label}<br>" +
                        "<extra></extra>",
                },
                'link': {
                    'source': source_ids,
                    'target': target_ids,
                    'value': link_val,
                    'label': link_labels,
                    'hovertemplate':
                        "%{label}<br>" +
                        "<extra></extra>",
                },
                'textfont': bain_font_family(200, 'roman')
            }
        ],
        'layout': {
            'xaxis': {'title': 'X', 'autorange': True},
            'yaxis': {'title': 'Y', 'autorange': True},
            'font': bain_font_family(200, 'roman'),
            'autosize': True,
            'height': 'auto', 'width': 'auto',
        }
    }
