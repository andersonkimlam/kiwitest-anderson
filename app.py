# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from flask import send_from_directory
import os


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv(
    'https://storage.googleapis.com/kepler-routes/data-visualization-sample-data.csv')

colors = {
    'background': '#2F7AF5',
    'text': '#ffffff'
}

def Header():
    return html.Div([
        get_logo(),
        get_menu(),
    ])

def get_logo():
    logo = html.Div([

        html.Div([
            html.Img(src='https://cdn-images-1.medium.com/max/696/1*Hmw2a0YDRRN3m5TRxeFxnQ@2x.png',style={
            'height': '50px',
            'float': 'left',
            'position': 'relative',
            'top': '0px',
            'left': '0px'
        },)
        ], className="ten columns padded"),

    ], className="row gs-header")
    return logo

def get_menu():
    menu = html.Div([

        dcc.Link('Dashboard   ', href='/dashboard', className="tab"),
        #dcc.Link('Dashboard   ', href='/dashboard', className="tab first")

        dcc.Link('Operations   ', href='/operations', className="tab"),

        dcc.Link('Maintenance   ', href='/maintenance', className="tab"),

        dcc.Link('Users   ', href='/users', className="tab last"),

    ], className="row ")
    return menu



dashboard = html.Div([  # page 1
        #html.Div(style={'backgroundColor': colors['background']}),
        html.Div([
            Header(),

            # Row 3
            html.Div([



            ], className="row "),




        ], className="subpage")

    ], style={'backgroundColor': colors['background']}, className="page")




operations = html.Div([  # page 1
        #html.Div(style={'backgroundColor': colors['background']}),
        html.Div([
            Header(),

            # Row 3
            html.Div([



            ], className="row "),




        ], className="subpage")

    ], style={'backgroundColor': colors['background']}, className="page")





maintenance = html.Div([  # page 1
        #html.Div(style={'backgroundColor': colors['background']}),
        html.Div([
            Header(),

            # Row 3
            html.Div([



            ], className="row "),




        ], className="subpage")

    ], style={'backgroundColor': colors['background']}, className="page")






users = html.Div([  # page 1
        #html.Div(style={'backgroundColor': colors['background']}),
        html.Div([
            Header(),

            # Row 3
            html.Div([



            ], className="row "),




        ], className="subpage")

    ], style={'backgroundColor': colors['background']}, className="page")


noPage = html.Div([  # 404

    html.P(["404 Page not found"])

    ], className="no-page")


# Describe the layout, or the UI, of the app
app.layout = html.Div([
    # html.Link(
    #     rel='stylesheet',
    #     href='/static/app.css'
    # ),
    #html.H1('Heading', style={'backgroundColor': colors['background']}),
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

# Update page
# # # # # # # # #
# detail in depth what the callback below is doing
# # # # # # # # #
@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/' or pathname == '/dashboard':
        return dashboard
    elif pathname == '/operations':
        return operations
    elif pathname == '/maintenance':
        return maintenance
    elif pathname == '/users':
        return users
    else:
        return noPage


# external_css = ["https://cdnjs.cloudflare.com/ajax/libs/normalize/7.0.0/normalize.min.css",
#                 "https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css",
#                 "//fonts.googleapis.com/css?family=Raleway:400,300,600",
#                 "https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"]
#
# for css in external_css:
#     app.css.append_css({"external_url": css})


# @app.server.route('/static/<path>')
# def static_file(path):
#     static_folder = os.path.join(os.getcwd(), 'static')
#     return send_from_directory(static_folder, path)

# external_js = ["https://code.jquery.com/jquery-3.2.1.min.js"]
#
# for js in external_js:
#     app.scripts.append_script({"external_url": js})


if __name__ == '__main__':
    app.run_server(debug=True)
