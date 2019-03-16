# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
import header

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv(
    'https://storage.googleapis.com/kepler-routes/data-visualization-sample-data.csv')

colors = {
    'background': '#2F7AF5',
    'text': '#ffffff'
}

#app.layout = html.Div(html.H1('Heading', style={'backgroundColor':'blue'})
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.Div([
        html.Div([
            html.Div([

                html.Div([
                    html.Img(src='https://cdn-images-1.medium.com/max/696/1*Hmw2a0YDRRN3m5TRxeFxnQ@2x.png',
                    style={
                    'height': '50px',
                    'float': 'left',
                    'position': 'relative',
                    'top': '20px',
                    'left': '30px'
                },)
                ], className="ten columns padded"),


            ], className="row gs-header")
        ]),

    html.Div([

        dcc.Graph(
        id='example-graph-2',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                }
            }
        }
    )
], style={'width': '49%', 'display': 'inline-block', 'vertical-align': 'middle'})
])
])

if __name__ == '__main__':
    app.run_server(debug=True)
