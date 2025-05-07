from dash import Dash, html, dash_table, dcc, callback, Input, Output
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(external_stylesheets=external_stylesheets)

app.layout = [
    html.Div(children='App with Data', className='row', style={'textAlign': 'center', 'color': 'blue', 'fontSize': 30}),
    html.Div(className='row', children=[
        dcc.RadioItems(options=['pop','lifeExp','gdpPercap'],value='lifeExp',inline=True, id='control_and_radio'),
    ]),
    html.Div(className='row', children=[
            html.Div(className='six columns',children=[
                dash_table.DataTable(data= df.to_dict('records'),page_size=10),
        ]),
        html.Div(className='six columns',children=[
                dcc.Graph(figure={}, id='control_and_graphs')
                #figure=px.histogram(df, x='continent', y='lifeExp', color='continent',histfunc='avg')
    ])])
    ]

@callback(
    Output(component_id='control_and_graphs', component_property='figure'),
    Input(component_id='control_and_radio', component_property='value')
)
def update_graph(col_chosen):
    fig = px.histogram(df, x='continent', y=col_chosen, color='continent', histfunc='avg')
    return fig

if __name__ == '__main__':
    app.run(debug=True)

