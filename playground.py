import marimo

__generated_with = "0.13.10"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import matplotlib.pyplot as plt
    import numpy as np
    return mo, plt


@app.cell(hide_code=True)
def _(rotate):
    rotate
    return


@app.cell
def _(counter, plt):
    r = 10
    fig, ax = plt.subplots()
    ax.set_xlim(-20, 20)
    ax.set_ylim(-5, 25)
    ax.set_aspect('equal')
    v1 = plt.Circle((-r, 0), 2, color="blue", fill=True, alpha=0.5)
    v2 = plt.Circle((r, 0), 2, color="blue", fill=True, alpha=0.5)
    v3 = plt.Circle((0, 1.7*r), 2, color="blue", fill=True, alpha=0.5)
    ax.add_patch(v1)
    ax.add_patch(v2)
    ax.add_patch(v3)

    locs = [(0,2*r), (-r-5,0), (r+5,0)]
    shift = counter.value % 3
    locs = locs[shift:] + locs[:shift]
    aloc = locs[0]
    bloc = locs[1]
    cloc = locs[2]

    plt.rcParams['text.usetex'] = True
    ax.text(*aloc, "A")
    ax.text(*bloc, "B")
    ax.text(*cloc, "C")

    if counter.value % 3 == 0:
        rotstring = "Rotation by 0 degrees"
    if counter.value % 3 == 1:
        rotstring = "Rotation by 120 degrees"
    if counter.value % 3 == 2:
        rotstring = "Rotation by 240 degrees"

    ax.text(5,20, rotstring)

    ax
    return


@app.cell
def _(mo):
    get_rot, set_rot = mo.state(0)
    def rot_btn_func():
        set_rot((get_rot()+1)%3)

    rotate = mo.ui.run_button(label="Rotate", on_change=rot_btn_func)
    return (rotate,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Second attempt""")
    return


@app.cell
def _(mo):
    counter = mo.ui.button(
        value=0, on_click=lambda value: value + 1, label="rotate"
    )
    counter
    return (counter,)


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
