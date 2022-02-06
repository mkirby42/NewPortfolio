
# %%
from jupyter_dash import JupyterDash
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from pages import posts, bio

# %%
app = JupyterDash(
    __name__,
    meta_tags=[{
        'name': 'viewport',
        'content': 'width=device-width, initial-scale=1.0, maximum-scale=4, minimum-scale=0.5,'
    }],
    external_stylesheets=[
        dbc.themes.COSMO,
        'https://use.fontawesome.com/releases/v5.9.0/css/all.css',
    ]
)


# %%
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

# %%
sidebar = html.Div(
    [
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                #dbc.NavLink("Posts", href="/apps", active="exact"),
                dbc.NavLink("Essays", href="/essays", active="exact"),
                dbc.NavLink("Bio", href="/bio", active="exact"),
                dbc.NavLink(
                    "Twitter", href="https://twitter.com/matt42kirby", active="exact"),
                dbc.NavLink(
                    "LinkedIn", href="https://www.linkedin.com/in/matt-kirby-ml/", active="exact"),
                dbc.NavLink(
                    "GitHub", href="https://github.com/mkirby42", active="exact"),
                dbc.NavLink(
                    "Mail", href="mailto:6mdkirby@gmail.com", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

# %%
app.title = 'Weapons Grade Bolognium'
app.layout = html.Div([
    html.H2("Weapons Grade Bolognium",
            className="display-4", style=CONTENT_STYLE),
    html.Hr(),
    sidebar,
    dcc.Location(id='location', refresh=False),
    dbc.Container(id='main_content', className='mt-4', style=CONTENT_STYLE),
])

# %%
image_scale = 0.43
featured = html.Div([
    html.Img(
        src=app.get_asset_url('missle_row.jpg'),
        style={'width': "857px",
               'height': '570px'}
    )
])

# %%


@app.callback(Output('main_content', 'children'),
              Input('location', 'pathname'))
def display_content(pathname):
    if pathname == "/":
        return featured
    elif pathname == "/essays":
        return posts.layout
    elif pathname == "/bio":
        return bio.layout
    else:
        return dcc.Markdown('## Page not found')


# %%
server = app.server

# %%
if __name__ == '__main__':
    app.run_server(debug=False)
