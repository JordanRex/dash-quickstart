###########################################################################################################################
# STYLES
###########################################################################################################################
## the header style

HEADER_STYLE = {
    "padding": "2px",
}

# the style arguments for the sidebar
SIDEBAR_STYLE = {
    'padding': '5px',
}

# the style for the main content position it to the right of the sidebar and add some padding.
TABLE_STYLE = {
    'padding': '5px',
    'width': '100%'
}

# the main container style
CONTAINER_STYLE = {
    'padding': '2px',
    'margin': '5px',
    'height': '100%',
    'width': '100%'
}

###########################################################################################################################
###########################################################################################################################
## COLOR PALETTEs

primary_color_palette = {
    "white": "rgb(255,255,255",
    "black": "rgb(0, 0, 0)",
}

secondary_color_palette = {
    "orange": "rgb(255,166,38)",
    "salmon": "rgb(255,125,130)",
    "turquoise": "rgb(0,188,212)",
    "teal": "rgb(0,191,165)",
    "sand": "rgb(204,186,161)",
    "pink": "rgb(255,128,171)",
    "bronze": "rgb(157,28,23)",
    "yellow": "rgb(250,189,43)",
    "emerald": "rgb(12,126,103)",
    "green": "rgb(105,178,74)",
    "indigo": "rgb(92,107,192)",
    "purple": "rgb(156,38,176)",
}

hover_color = primary_color_palette["black"]

###########################################################################################################################
###########################################################################################################################
## style dicts for various components

app_links_style = {'width': '100%',
                   'height': '100%',
                   'padding': '2px',
                   'font-size': '14px'}

btn_active_style = {'color': 'rgb(255,255,255)', 'backgroundColor': 'rgb(204,0,0)', 'height': '100%'}
btn_inactive_style = {'color': 'rgb(0,0,0)', 'backgroundColor': 'transparent', 'height': '100%'}
btn_hidden_style = {'display': 'none'}

btn_radio_style = {'width': '100%', 'margin': 'none'}

dropdown_style = {'width': '100%', 'margin': '5px'}

scenario_buttons_row_style = {'padding': '2px', 'width': '100%'}

style_header = {'font-weight': 500, 'whiteSpace': 'normal', 'maxWidth': '70px',
                'text-transform': 'capitalize', 'background-color': 'rgba(0,0,0,0.1)', 'overflow-wrap': 'normal',
                'font-size': 11, 'color': 'rgb(0,0,0)', 'border': 'none', 'textAlign': 'left'}
style_data = {'font-weight': 300, 'whiteSpace': 'normal', 'font-size': 9,
              'textOverflow': 'ellipsis', 'height': 'auto', 'maxWidth': '70px',
              'color': 'rgb(0,0,0)', 'background-color': 'rgb(255,255,255)', 'textAlign': 'left'}
style_filter = {'font-weight': 400, 'textOverflow': 'ellipsis', 'height': '20px', 'whiteSpace': 'normal', 'font-size': 10,
                'color': 'rgb(0,0,0)', 'background-color': 'rgb(250,250,250)', 'textAlign': 'center'}
style_table = {'maxHeight': '700px', 'minHeight': '500px', 'border': 'none', 'width': '100%'}

base_div_style = {"overflowX": "none", "overflowY": "auto"}

footer_div_style = {
    "position": "fixed",
    "bottom": "0px",
    "right": "0px",
    "left": "0px",
    "height": "30px",
    "background": primary_color_palette["black"],
    "color": primary_color_palette["white"],
    "text-align": "center",
    "width": "100%",
    "overflow": "none",
    "display": "inline-block",
    "zIndex": 1001,
}

# the main container style
CONTAINER_STYLE = {
    "margin": "none",
    "padding": "none",
    "overflow-y": "auto",
    "overflow-x": "none",
    "max-width": "none",
    "max-height": "none",
    "border": "none",
    "background-color": primary_color_palette["white"],
}

NAVBAR_STYLE = {
    "font-size": 25,
    "border": "none",
    "background-color": primary_color_palette["black"],
    "color": "white",
    "font-weight": 700,
}

Chart_Header = {
    "background-color": primary_color_palette["black"],
    "textAlign": "center",
    "hover": {"color": hover_color},
    "color": "white",
    "height": "42px",
    "font-weight": 700,
}

Section_Header = {
    "background-color": primary_color_palette["black"],
    "textAlign": "center",
    "hover": {"color": hover_color},
    "color": "white",
    "font-weight": 600,
}

Method_Selection_Header = {
    "background-color": primary_color_palette["black"],
    "textAlign": "center",
    "hover": {"color": hover_color},
    "color": "white",
    "font-weight": 400,
}

Table_Header = {
    # "font-family": "Ariel",
    "font-weight": 700,
    "font-size": "16",
    "background-color": primary_color_palette["black"],
    "color": "white",
    "whiteSpace": "normal",
    "height": "auto",
    "lineHeight": "20px",
    "overflow": "hidden",
    "textOverflow": "ellipsis",
    "minWidth": 95,
    "maxWidth": 95,
    "width": 95,
    "textAlign": "center",
}

Table_Data_Left = {
    # "font-family": "Ariel",
    "font-weight": 400,
    "padding-right": "10px",
    "whiteSpace": "pre-line",
    "height": "auto",
    "lineHeight": "20px",
    "textAlign": "left",
    "table-layout": "fixed",
}

Table_Data = {
    # "font-family": "Ariel",
    "font-weight": 400,
    "padding-right": "10px",
    "whiteSpace": "normal",
    "height": "auto",
    "lineHeight": "20px",
    "textAlign": "center",
}

# Inline with Tesco Site
Ribbon_Style = {
    "font-size": "20px",
    "border": "none",
    "color": primary_color_palette["white"],
    "weight": 700,
    "font-weight": "bold",
    "active": {"background-color": "#4CAF50"},
    "border-right": "1.5px solid rgb(246,246,246)",
    "margin": 0.5,
    "padding": -0.5,
    # "border" : 0,
    "vertical-align": "baseline",
    # "cursor":"pointer",
    # "font-style": "normal",
    # "font-variant-ligatures": "normal",
    # "font-variant-caps": "normal",
    # "font-stretch": "normal",
    # "line-height": "1.5",
}

LastItem_Ribbon_Style = {
    "font-size": "25px",
    "border": "none",
    "color": primary_color_palette["white"],
    "weight": 700,
    "font-weight": "bold",
    "background-color": primary_color_palette["black"],
    # "border-right": "1.5px solid rgb(246,246,246)"
}

Navicon_Style = {
    "border-right": "1.5px solid rgb(246,246,246)",
    "margin": 3,
    "padding": -1.5,
    "vertical-align": "baseline",
}

upload_style = {
    "borderWidth": "1px",
    "borderStyle": "dashed",
    "borderRadius": "2.5px",
    "textAlign": "center",
    "margin": "5px",
    # "background-color": primary_color_palette["black"],
    # "color": "white",
}

download_btn_style = {
    "color": primary_color_palette["white"],
    "background-color": primary_color_palette["black"],
}
save_btn_style = {
    "color": primary_color_palette["white"],
    "background-color": primary_color_palette["black"],
    "font-weight": 700,
    # "font-family": "Ariel",
    "borderRadius": "8px",
}