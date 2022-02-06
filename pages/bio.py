import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from app import app

bio = html.Div([
    dbc.Row([
        dbc.Col([
            html.Img(
                src=app.get_asset_url('mypic.jpg'),
                style={'width': "230px", 'height': '308px'}
            )
        ]),
        dbc.Col([
            html.H3(
                "Matt Kirby"
            ),
            html.P(
                """
                Matt is a Data Scientist and Engineer at Organic Robotics Coporation where he is 
                developing the next generation of wearable sensing technology to 
                revolutionize sports, medicine, and society.
                """
            )
        ]),
        dbc.Col([

        ])
    ])
])

layout = html.Div([bio])
