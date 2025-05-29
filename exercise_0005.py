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
        Let $A\subseteq X$ be a nonempty subset.  

        Show that if $A$ is finite, then $A$ has a maximum and minimum.
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
        Let $A\subseteq X$ be a nonempty subset.

        Show that if $A$ has a maximum and $\alpha=\max(A)$, then it follows that $\alpha=\sup(A)$.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Exercise 3""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Let $A\subseteq B\subseteq X$ all be nonempty subsets.

        Show that, if $\sup A$ and $\sup B$ exist, then 

        $$ \sup A \preceq \sup B $$

        Also state and prove a corresponding theorem for infima.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Exercise 4""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Show that if $A\subseteq X$ is a subset and $b\in A$ then 

        $$ b\in UB_{LB_A} \cap LB_{UB_A} $$
        """
    )
    return

if __name__ == "__main__":
    app.run()
