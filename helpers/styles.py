###########################################################################################################################
# STYLES
###########################################################################################################################
# the header style
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
    #     'overflow-y': 'auto',
    #     'overflow-x': 'none',
    'height': '100%',
    'width': '100%'
}


def bain_font_family(weight=200, style='roman'):
    return {
        'family': 'Graphik Web',
        'weight': weight,
        'style': style
    }


###########################################################################################################################

bain_logo_style = {'align': 'left',
                   'display': 'inline-block'}
app_title_style = {'font-family': 'Graphik Web', 'font-weight': 400, 'font-style': 'roman',
                   'margin': 'auto'}
app_links_style = {'width': '100%',
                   'height': '100%',
                   'padding': '2px',
                   'font-size': '14px',
                   'font-family': 'Graphik Web', 'font-weight': 200, 'font-style': 'roman'}

btn_active_style = {'color': 'rgb(255,255,255)', 'backgroundColor': 'rgb(204,0,0)', 'height': '100%'}
btn_inactive_style = {'color': 'rgb(0,0,0)', 'backgroundColor': 'transparent', 'height': '100%'}
btn_hidden_style = {'display': 'none'}

btn_radio_style = {'width': '100%', 'font-family': 'Graphik Web', 'font-weight': 600, 'font-style': 'roman',
                   'margin': 'none'}

dropdown_style = {'width': '100%', 'margin': '5px',
                  'font-family': 'Graphik Web', 'font-weight': 300, 'font-style': 'roman'}

scenario_buttons_row_style = {'padding': '2px', 'width': '100%',
                              'font-family': 'Graphik Web', 'font-weight': 200, 'font-style': 'roman'}

style_header = {'font-weight': 500, 'font-family': 'Graphik Web', 'font-style': 'roman', 'whiteSpace': 'normal',
                'maxWidth': '70px',
                'text-transform': 'capitalize', 'background-color': 'rgba(0,0,0,0.1)', 'overflow-wrap': 'normal',
                'font-size': 11, 'color': 'rgb(0,0,0)', 'border': 'none', 'textAlign': 'left'}
style_data = {'font-weight': 300, 'font-family': 'Graphik Web', 'font-style': 'roman',
              'textOverflow': 'ellipsis', 'height': 'auto', 'maxWidth': '70px',
              'whiteSpace': 'normal', 'font-size': 9,
              'color': 'rgb(0,0,0)', 'background-color': 'rgb(255,255,255)', 'textAlign': 'left'}
style_filter = {'font-weight': 400, 'font-family': 'Graphik Web', 'font-style': 'normal',
                'textOverflow': 'ellipsis', 'height': '20px', 'whiteSpace': 'normal', 'font-size': 10,
                'color': 'rgb(0,0,0)', 'background-color': 'rgb(250,250,250)', 'textAlign': 'center'}
style_table = {'maxHeight': '700px', 'minHeight': '500px', 'border': 'none', 'width': '100%'}

###########################################################################################################################
## COLOR PALETTE

color_bain_red = 'rgb(204,0,0)'


def color_bain_traffic_red(opacity):
    return f'rgba(152,0,0,{opacity})'


def color_bain_traffic_yellow(opacity):
    return f'rgba(233,201,71,{opacity})'


def color_bain_traffic_green(opacity):
    return f'rgba(80,118,100,{opacity})'


bain_color_palette = ['rgb(137,12,88)', 'rgb(80,109,133)', 'rgb(255,205,0)', 'rgb(80,120,103)',
                      'rgb(51,51,51)', 'rgb(161,61,121)', 'rgb(115,138,157)', 'rgb(255,215,51)',
                      'rgb(131,172,154)', 'rgb(102,102,102)', 'rgb(184,109,155)', 'rgb(150,167,182)',
                      'rgb(255,231,133)', 'rgb(187,202,186)', 'rgb(153,153,153)']
