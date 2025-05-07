from dash import Dash, html, dash_table, dcc, callback, Input, Output
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

external_stylesheets = [dbc.themes.CERULEAN]
app = Dash(external_stylesheets=external_stylesheets)

app.layout = [
    dbc.Row([
            html.Div(children='App with Data', className='text-primary text-center fs-3')
    ]),
    
    dbc.Row([
        dbc.RadioItems(options=[{"label":x,"value":x} for x in ['pop','lifeExp','gdpPercap']],
                       value='lifeExp',inline=True, id='control_and_radio')
    ]),
    dbc.Row([
        dbc.Col([
            dash_table.DataTable(data= df.to_dict('records'),page_size=10, style_table={'overflowX': 'auto'}),
        ],width=6),
        dbc.Col(
                [dcc.Graph(figure={}, id='control_and_graphs')
                #figure=px.histogram(df, x='continent', y='lifeExp', color='continent',histfunc='avg')
        ],width=6),
    ])
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

