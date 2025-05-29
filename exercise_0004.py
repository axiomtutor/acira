import marimo

__generated_with = "0.13.14"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Exercise 1""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    If $\preceq$ is a partial order on $X$, show that the corresponding strict partial order $\prec$ is

    1. Irreflexive: $\forall a\in X$ we have $a\not\prec a$.
    2. Asymmetric: $\forall a,b\in X,$ if we have $a\prec b$ then $a\not\prec b$.
    3. Transitive: $\forall a,b,c\in X$ if $a\prec b$ and $b\prec c$, then $a\prec c$.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Exercise 2""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Find all possible partial orders on the set $\{a,b,c\}$.  Of those partial orders, decide which are total orders.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Exercise 3""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Let $\preceq$ be a partial order on the set $X$, and $\prec$ the corresponding strict partial order.  

    For $a,b\in X$ show that $a\not\preceq b$ is NOT equivalent to $b\prec a$.  

    But if $\preceq$ is a total order, then $a \not\preceq b$ is equivalent to $b\prec a$.
    """
    )
    return


@app.cell(hide_code=True)
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
