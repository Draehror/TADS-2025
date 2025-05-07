
import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding":"2rem 1rem",
    "background-color": "#f8f9fa"
}

CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-rigth": "2rem",
    "padding": "2rem 1rem"
}

app.layout = html.Div(
    [
        dcc.Location(id='url'),
        dbc.NavbarSimple(
            children=[
                dbc.NavItem("Home", href="/",active="exact"),
                dbc.NavItem("Page 1", href="/page-1",active="exact"),
                dbc.NavItem("Page 2", href="/page-2",active="exact")
            ],
            brand="Navigation",
            color="primary",
            dark=True,
        ),
        dbc.Container(id="page-content",className="pt-4")
    ])

@app.callback(Output("page-content","children"),[Input("url","pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return html.P("Home Page")
    elif pathname == "/page-1":
        return html.P("Pagina 1")
    elif pathname == "/page-2":
        return html.P("Pagina 2")
    return html.Div([
        html.H1("404 Not Found!", className="text-danger"),
        html.Hr(),
        html.P(f"The path {pathname} was not found!")
    ], className="p-3 bg-ligth rounded-3"
    )

if __name__ == '__main__':
    app.run(port=6666)