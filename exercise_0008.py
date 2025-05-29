import marimo

__generated_with = "0.13.14"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Exercise 1""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Take the "chatty proof" above, and clean it up into an efficient and proof that $\alpha^2\ge 2$.

        Also prove that $\alpha^2\le 2$ in a similar fashion, to conclude that $\alpha^2=2$.

        Conclude that $\sqrt 2\in \Bbb R$.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Exercise 2""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Show that $\sqrt 3\in \Bbb R$ and $\sqrt[3]{2}\in\Bbb R$.

        Then generalize this to show that, for any $x\in \Bbb R$ such that $1< x$, and for any $n\in\Bbb N$, we have 

        $$ \sqrt[n]x \in\Bbb R $$

        Hint: Use the binomial theorem.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Exercise 3""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Use the above result to show that if $0< x$ then $\sqrt[n]x\in\Bbb R$.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Exercise 4""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Let $0\le x$ and show that 

        $$ y = x^n$$ 

        has a unique solution in $\Bbb R$.
        """
    )
    return

@app.cell(hide_code=True)
def _():
    import marimo as mo
    return (mo,)

if __name__ == "__main__":
    app.run()
