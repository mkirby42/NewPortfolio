import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

nlp_content = [
    dbc.CardHeader("Featured In Analytics Vidhya"),
    dbc.CardImg(src="assets/nlp.jpg", top=True,
                style={"width": "18rem", "height": "9rem"}),
    dbc.CardBody([
        html.H5("Natural Language Processing",
                className="card-title"),
        html.P(
            "Demonstrating NLP techniques with Python",
            className="card-text",
        ),

        dbc.Button(html.A(
            "See More",
            href="""
            https://medium.com/analytics-vidhya/natural
            -language-processing-with-python-cb3f83d5a393?source=friends_
            link&sk=4cbf63c34f97ca048755d172fab7ed9f
            """,
            style=dict(color='white')
        ), color="primary")
    ])]

tanzania_content = [
    dbc.CardHeader("Featured In Analytics Vidhya"),
    dbc.CardImg(src="assets/1*13eTNzkTNtrL23ksafPwqg.jpeg",
                top=True, style={"width": "18rem", "height": "9rem"}),
    dbc.CardBody([
        html.H5("Tanzanian Water Pumps", className="card-title"),
        html.P(
            "Utilizing machine learning for predictive maintenance",
            className="card-text",
        ),
        dbc.Button(html.A(
            "See More",
            href="""
            https://medium.com/analytics-vidhya/predictive-modeling-for-
            tanzanian-water-pumps-701bcc7760b2?source=friends_
            link&sk=90b471fe246badc2a32046ec763ecf90
            """,
            style=dict(color='white')
        ), color="primary")
    ])]

mushroom_content = [
    dbc.CardHeader("Featured In Towards Data Science"),
    dbc.CardImg(src="assets/0*MYwjpwXOlwC2j3Sy.jpeg", top=True,
                style={"width": "18rem", "height": "9rem"}),
    dbc.CardBody([
        html.H5("Classifying Mushrooms", className="card-title"),
        html.P(
            "Using tree-based models to classify mushrooms as edible or poisonous",
            className="card-text",
        ),
        dbc.Button(html.A(
            "See More",
            href="""https://towardsdatascience.com/
            applying-the-universal-machine-learning-workflow-
            to-the-uci-mushroom-dataset-1939442d44e7""",
            style=dict(color='white')
        ), color="primary")
    ])]

row_1 = dbc.Row([
    dbc.Col([
        dbc.Card(
            mushroom_content,
            color="light",
            style={"width": "18rem", "height": "28rem"},
        )
    ]),
    dbc.Col([
        dbc.Card(
            tanzania_content,
            color="light",
            style={"width": "18rem", "height": "28rem"},
        ),
    ]),
    dbc.Col([
        dbc.Card(
            nlp_content,
            color="light",
            style={"width": "18rem", "height": "28rem"},
        ),
    ]),
], className="mb-4")

layout = html.Div([row_1])
