import dash
import dash_html_components as html
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    html.H1('Weapons Grade Bolognium',
            style={'color': 'black',
                   'fontSize': '40px'}),
    dbc.Tabs([

        dbc.Tab([

        ], label="Posts"),

        dbc.Tab([

        ], label="About")
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)