import marimo

__generated_with = "0.13.11"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    I recommend that you solve exercises in the following way: 

    1. Read theorems in the reference section, [ACIRA Reference](https://axiomtutor.github.io/acira/), but do not read the proofs.
    2. Solve the exercises on this page.
    3. Give the proofs of the theorems in the reference section.
    4. Consult solutions to check your work.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Exercise 1""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    1. Show that $(\Bbb Q\smallsetminus \{0\},\times)$ is a group.
    2. Let $H=\{a,b\}$ and set $\ast:H^2\to H$ defined by
         $$\begin{aligned} a\ast a &= a \\ a\ast b &= a \\ b\ast a &= b \\ b\ast b &= b\end{aligned}$$
       Decide whether $(H,\ast)$ is a group.  
    4. Let $X$ be a nonempty set and define $H$ to be the set of all functions $f:X\to X$ such that $f$ is bijective.
   
         Define the operation $\circ: H^2 \to H$ to be the composition operation on $H$.

           Show that $(H,\circ)$ is a group.
    5. Let $H = \{a,b\}$ and find an operation $\ast:H^2\to H$ such that $(H,\ast)$ is a group.

           If there is more than one such operation, find them all.

           Repeat the exercise if $H = \{a,b,c\}$.
    """
    )
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
