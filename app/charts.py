import plotly.graph_objects as go


def create_gauge_chart(probability):

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=probability * 100,

            title={
                "text": "<b>Churn Probability</b>",
                "font": {"size": 24}
            },

            number={
                "suffix": "%",
                "font": {"size": 42}
            },

            gauge={
                "axis": {
                    "range": [0, 100],
                    "tickwidth": 2,
                    "tickcolor": "black"
                },

                "bar": {
                    "color": "#2563EB",
                    "thickness": 0.35
                },

                "steps": [

                    {
                        "range": [0, 40],
                        "color": "#22C55E"
                    },

                    {
                        "range": [40, 70],
                        "color": "#FACC15"
                    },

                    {
                        "range": [70, 100],
                        "color": "#EF4444"
                    }

                ],

                "threshold": {
                    "line": {
                        "color": "black",
                        "width": 6
                    },

                    "thickness": 0.8,

                    "value": probability * 100
                }
            }
        )
    )

    fig.update_layout(
        height=420,
        margin=dict(l=30, r=30, t=80, b=30),
        paper_bgcolor="white",
        font=dict(size=16)
    )

    return fig