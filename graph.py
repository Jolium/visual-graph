import pandas as pd
import plotly.graph_objects as go
import csv


df = pd.read_csv('elextraflex.csv')

with open('elextraflex.csv') as f:
    d_reader = csv.DictReader(f)

    # get fieldnames from DictReader object and store in list
    header = d_reader.fieldnames

fig = go.Figure(go.Bar(
    x=df[header[1]],
    y=df[header[2]],
    hovertext=df[header[3]],
    hoverinfo="text",
    marker=dict(
        color='blue'
    ),
    showlegend=False
))

fig.update_layout(title='ElectraFlex Rapport', plot_bgcolor='rgb(230, 230, 230)', showlegend=True)

fig.show()
