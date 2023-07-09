import numpy as np
import pandas as pd
import re
import base64
import io
import os

from dash import html, no_update
from multiprocessing import cpu_count
from dash_extensions import Lottie

import json


#####################################################################################


# LOTTIE functions
def error404():
    url = "/assets/animations/lottie/29142-error-404.json"
    options = dict(
        loop=True,
        autoplay=True,
        rendererSettings=dict(preserveAspectRatio="xMidYMid slice"),
    )
    return html.Div(Lottie(options=options, width="25%", height="25%", url=url))


def coming_soon():
    url = "/assets/animations/lottie/34957-coming-soon.json"
    options = dict(
        loop=True,
        autoplay=True,
        rendererSettings=dict(preserveAspectRatio="xMidYMid slice"),
    )
    return html.Div(Lottie(options=options, width="25%", height="25%", url=url))


def under_construction():
    url = "/assets/animations/lottie/52975-under-construction.json"
    options = dict(
        loop=True,
        autoplay=True,
        rendererSettings=dict(preserveAspectRatio="xMidYMid slice"),
    )
    return html.Div(Lottie(options=options, width="25%", height="25%", url=url))


# flatfile reading utility function
def parse_contents(contents, filename):
    content_type, content_string = contents.split(",")
    decoded = base64.b64decode(content_string)

    try:
        if "csv" in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(io.StringIO(decoded.decode("utf-8")))
        elif "xls" in filename:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded))
    except Exception as e:
        print(e)
        return "There was an error processing this file."

    return df


def render_img_src(path):
    encoded_img = base64.b64encode(open(path, "rb").read()).decode("ascii")
    return f"data:image/png;base64,{encoded_img}"


#####################################################################################


def session_id():
    return base64.b64encode(os.urandom(16))


def lst_to_json(lst):
    return json.dumps(lst).encode("utf8")


def json_to_lst(data):
    if data is None:
        return None
    else:
        try:
            return json.loads(data.decode("utf8"))
        except:
            return json.loads(data)


def return_as_lst(lst):
    if isinstance(lst, list):
        return lst
    else:
        return list(lst)


def second_largest(numbers):
    count = 0
    m1 = m2 = float("-inf")
    for x in numbers:
        count += 1
        if x > m2:
            if x >= m1:
                m1, m2 = x, m1
            else:
                m2 = x
    return m2 if count >= 2 else None


def make_annotation_item(x, y, color, text, xloc):
    return dict(
        xref="x",
        yref="y",
        x=x,
        y=y,
        font=dict(color=color, size=16),
        xanchor=xloc,
        yanchor="middle",
        text=text,
        showarrow=False,
    )


# no update function for callbacks with multiple outputs
# type == one of ['options', 'values']
def noupdate(value, type="options", label=None):
    if value is None:
        return no_update
    else:
        if type == "options":
            if label is None:
                return [{"label": value, "value": value}]
            else:
                return [{"label": label, "value": value}]
        elif type == "values":
            if value == [] or value[0]["value"] is None:
                return no_update
            else:
                return value[0]["value"]


# np select wrapper
def select_multiple(df, newcol, choices, default, cols=[], vals=[]):
    conditions = [
        (df[cols[0]] > vals[0]) & (df[cols[1]] > vals[1]),
        (df[cols[0]] < vals[0]) & (df[cols[1]] > vals[1]),
        (df[cols[0]] < vals[0]) & (df[cols[1]] < vals[1]),
        (df[cols[0]] > vals[0]) & (df[cols[1]] < vals[1]),
    ]
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


def make_round_commasep(num, currency_prefix="$", currency_suffix="USD"):
    return f"{currency_prefix} {int(np.round(num, 0)):,} {currency_suffix}"


def findinlst(lst, val):
    return [i for i, x in enumerate(lst) if x == val]


def pkl_del(path, name, find=False):
    if find == True:
        if "dropdown" in path:
            val = ""
        else:
            val = r"_[0-9]{6}_storeweek"
        escaped_project = re.escape(name)
        project_pickles = [
            f
            for f in os.listdir(path)
            if re.fullmatch(f"{escaped_project}{val}.pkl", f)
        ]
        if len(project_pickles) > 0:
            pkl_file = path + f"//{project_pickles[0]}"
        else:
            return None
    else:
        pkl_file = path + name

    # remove the identified pickle file
    try:
        os.chmod(pkl_file, 0o777)
    except:
        pass
    try:
        os.remove(pkl_file)
    except:
        pass
    return None


def miss_imputation(data):
    data.replace(r"^\s*$", "None", regex=True, inplace=True)
    data.replace(r"", "None", inplace=True)
    data.replace([None], "None", inplace=True)
    data.fillna("None", inplace=True)
    return data


#####################################################################################


# bubble chart functions
def figure_bubble(
    x,
    y,
    name,
    size,
    color_fill,
    color_outline,
    size_max,
    text,
    currency_prefix="$",
    currency_suffix="USD",
):
    currency = currency_prefix if currency_suffix == "" else currency_suffix
    return {
        "x": x,
        "y": y,
        "mode": "markers",
        "name": name,
        "marker": {
            "size": size,
            "color": color_fill,
            "line": {"color": color_outline},
            "sizemode": "area",
            "sizeref": 2.0 * size_max / (40.0**2),
            "sizemin": 4,
        },
        "text": text,
        "customdata": [currency] * len(x),
        "hovertemplate": "<b>P: %{text}</b><br><br>"
        + "Q: %{marker.size:,.0f}%{customdata}<br>"
        + "X: %{x}%<br>"
        + "Y: %{y}%<br>"
        + "<extra></extra>",
    }


def figure_line(x, y):
    return {
        "x": x,
        "y": y,
        "mode": "lines",
        "showlegend": False,
        "line": {"dash": "dash"},
    }


def figure_layout(ann):
    return {
        "xaxis": {"title": "X", "autorange": "normal"},
        "yaxis": {"title": "Y", "autorange": "normal"},
        "hovermode": "closest",
        "clickmode": "event+select",
        "annotations": ann,
        "layer": "below",
    }


def break_string_in_multiple_lines(string, threshold=50):
    if len(string) < 50:
        return string

    string = string.split(" ")

    final_string, char_count = "", 0

    for word in string:
        if len(word) + 1 + char_count > threshold:
            final_string += "<br>" + word + " "
            char_count = len(word)
            continue

        final_string += word + " "
        char_count += len(word) + 1

    return final_string


#####################################################################################
# utility functions


def num_workers(workers=None):
    if workers is None:
        return (cpu_count() * 2) + 1
    elif workers == 0:
        return 4
    else:
        return workers


def cur_page(page):
    return {"page": page}


def impute_null_nan(x, y):
    r_val = ""
    if x == np.nan:
        r_val = str(y)
    elif str(x).strip() == "nan":
        r_val = str(y)
    elif str(x).strip() == "":
        r_val = str(y)
    else:
        r_val = x

    if r_val == "":
        return "Description Not Available"
    elif str(r_val) == "nan":
        return "Description Not Available"
    else:
        return r_val


def return_sankey_fn(
    node_labels, xpos, ypos, colors, source_ids, target_ids, link_val, link_labels
):
    return {
        "data": [
            {
                "type": "sankey",
                "valueformat": ".2f",
                "node": {
                    "pad": 15,
                    "thickness": 15,
                    "line": {"color": "black", "width": 0.5},
                    "label": node_labels,
                    "x": xpos,
                    "y": ypos,
                    "color": colors,
                    "hovertemplate": "%{label}<br>" + "<extra></extra>",
                },
                "link": {
                    "source": source_ids,
                    "target": target_ids,
                    "value": link_val,
                    "label": link_labels,
                    "hovertemplate": "%{label}<br>" + "<extra></extra>",
                },
                # "textfont": ,
            }
        ],
        "layout": {
            "xaxis": {"title": "X", "autorange": True},
            "yaxis": {"title": "Y", "autorange": True},
            # "font": ,
            "autosize": True,
            "height": "auto",
            "width": "auto",
        },
    }
