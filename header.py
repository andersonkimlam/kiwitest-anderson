import dash_html_components as html
import dash_core_components as dcc

def Header():
    return html.Div([
        get_logo(),
    ])

def get_logo():
    logo = html.Div([

        html.Div([
            html.Img(src='https://cdn-images-1.medium.com/max/696/1*Hmw2a0YDRRN3m5TRxeFxnQ@2x.png',style={
            'height': '50px',
            'float': 'left',
            'position': 'relative',
            'top': '20px',
            'left': '30px'
        },)
        ], className="ten columns padded"),

    ], className="row gs-header")
    return logo
