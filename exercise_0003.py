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
    Let $(F,+,\times)$ be a field.  

    Define the operation $+_2$ on vectors $\begin{bmatrix}a\\b\end{bmatrix},\begin{bmatrix}c\\d\end{bmatrix}\in F^2$ by

    $$ \begin{bmatrix} a\\b\end{bmatrix} +_2 \begin{bmatrix}c\\d\end{bmatrix} = \begin{bmatrix}a+c\\b+d\end{bmatrix} $$

    and $\times_2$ defined by 

    $$ \begin{bmatrix} a\\b\end{bmatrix} \times_2\begin{bmatrix}c\\d\end{bmatrix} = \begin{bmatrix}ac\\bd\end{bmatrix} $$

    Show by a counter-example, that $(F^2,+_2,\times_2)$ is not necessarily a field.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Exercise 2""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Let $F = \{0,1,2,3\}$ and define $\oplus$ and $\otimes$ on $F$, by modular addition and multiplication, respectively.

    $$ a\oplus b = (a+b)\mod 3,\quad a\otimes b = (a\times b)\mod 3 $$

    Show that $(F,\oplus,\otimes)$ is a field.  

    Show that $(\{0,1,2,3\}, \oplus,\otimes)$, with plus and times defined by addition and multiplication mod 4, is not a field.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Exercise 3""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Show that in any ring, the additive and multiplicative identities are unqiue.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Exercise 4""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    In a previous exercise, we saw a class `Group` which modeled finite groups as a set and operation, with methods to check that the given objects formed a group.  

    Create similar classes for rings and fields.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Exercise 5""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Show that in any ring, $0x = x0 = 0$ and $-x = (-1)x$, for every $x\in R$.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Exercise 6""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Show that $(\{0\}, +,\times)$ is a ring but not a field.

    The operations are defined by $0+0=0$ and $0\times 0=0$.
    """
    )
    return


@app.cell(hide_code=True)
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
