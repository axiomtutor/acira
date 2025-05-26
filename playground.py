import marimo

__generated_with = "0.13.10"
app = marimo.App(width="medium")


@app.cell
def _():
    import altair as alt
    import pandas as pd
    import numpy as np

    # Triangle coordinates and labels
    side = 1
    height = np.sqrt(3) / 2 * side

    # Points for the triangle perimeter
    points = [
        {"x": 0, "y": 0, "order": 0},                    # A (Bottom left)
        {"x": side, "y": 0, "order": 1},                 # B (Bottom right)
        {"x": side / 2, "y": height, "order": 2},        # C (Top)
        {"x": 0, "y": 0, "order": 3},                    # Close the triangle
    ]
    df_lines = pd.DataFrame(points)

    # Labels for vertices
    labels = pd.DataFrame([
        {"x": 0, "y": 0, "label": "A"},
        {"x": side, "y": 0, "label": "B"},
        {"x": side / 2, "y": height, "label": "C"},
    ])

    # Triangle outline
    triangle = alt.Chart(df_lines).mark_line().encode(
        x='x:Q',
        y='y:Q',
        order='order:O'
    )

    # Vertex labels
    text = alt.Chart(labels).mark_text(
        align='center',
        dy=-10  # Shift labels up slightly
    ).encode(
        x='x:Q',
        y='y:Q',
        text='label:N'
    )

    # Combine and remove axes
    chart = (triangle + text).properties(
        width=300,
        height=300
    ).configure_axis(
        grid=False,
        domain=False,
        ticks=False,
        labels=False
    )

    chart

    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
