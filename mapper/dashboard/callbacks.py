import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

df = px.data.election()
geojson = px.data.election_geojson()
candidates = df.winner.unique()

layout = html.Div(
    [
        html.P("Candidate:"),
        dcc.RadioItems(
            id="candidate",
            options=[{"value": x, "label": x} for x in candidates],
            value=candidates[0],
            labelStyle={"display": "inline-block"},
        ),
        dcc.Graph(id="choropleth"),
    ]
)


def register_callbacks(dashapp):
    @dashapp.callback(Output("choropleth", "figure"), [Input("candidate", "value")])
    def display_choropleth(candidate):
        fig = px.choropleth_mapbox(
            df,
            geojson=geojson,
            color=candidate,
            locations="district",
            featureidkey="properties.district",
            center={"lat": 45.5517, "lon": -73.7073},
            zoom=9,
            mapbox_style="carto-positron",
            range_color=[0, 6500],
        )
        fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

        return fig
