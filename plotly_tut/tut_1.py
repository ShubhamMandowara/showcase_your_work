from dash import Dash, html, dash_table, dcc
import pandas as pd
import plotly.express as px


df = pd.DataFrame()
df['Names'] = ['Anni', 'Zane', 'Anni', 'Anni']
df['Ages'] = [10, 10, 12, 10]

app = Dash(__name__)

app.layout = html.Div(
    [
        html.Div(children='Hello, world'),
        dash_table.DataTable(data=df.to_dict('records')),
        dcc.Graph(figure=px.histogram(df, x='Names', y='Ages', histfunc='avg'))
    ]
)



if __name__ == '__main__':
    app.run(debug=True)
