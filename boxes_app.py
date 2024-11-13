import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px
import seaborn as sns
df = sns.load_dataset('flights')
df['date'] = pd.to_datetime(df['year'].astype(str) + '-' + df['month'].astype(str), format='%Y-%b')
linegraph = px.line(data_frame=df, x="date", y="passengers")


eswdf = pd.DataFrame({'Year': [2018, 2018, 2018, 2019, 2019, 2019, 2020, 2020, 2020, 2021, 2021, 2021, 2022, 2022, 2022, 2023, 2023, 2023, 2024, 2024, 2024], 'Country': ['England', 'Scotland', 'Wales','England', 'Scotland', 'Wales','England', 'Scotland', 'Wales','England', 'Scotland', 'Wales','England', 'Scotland', 'Wales','England', 'Scotland', 'Wales','England', 'Scotland', 'Wales'], 'Rainy days': [133, 101, 136, 108, 182, 120, 147, 174, 169, 155, 132, 157, 149, 122, 108, 132, 193, 117, 111, 175, 163], 'Ice cream sales': [3200, 1043, 2920, 1131, 7820, 2320, 4103, 7001, 6740, 6628, 3179, 5104, 5200, 2740, 1381, 3193, 8992, 1200, 1400, 7610, 6294]})
engdf = eswdf[eswdf.Country=="England"]
enggraph = px.bar(data_frame=engdf, x='Year', y='Rainy days')




app = dash.Dash(__name__)
app.layout = html.Div(
    children=[
        html.H1("Passengers over time"), 
        dcc.Graph(id="first graph on page", figure=linegraph),
        html.H2("Rainy days"),
        dcc.Graph(id="second graph on page", figure=enggraph)])


if __name__ == '__main__':
    app.run_server(debug=True, port=8051)  # runs the server