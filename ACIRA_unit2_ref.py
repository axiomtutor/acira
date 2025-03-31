import marimo

__generated_with = "0.12.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # A Course in Real Analysis ... in Marimo!

        ## Unit 2: Sequences and Series

        by Axiom Tutor 
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Lesson 0010: Sequences""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Let $m\in\Bbb R$ and $X\subseteq \Bbb R$.  Then

    $$ X^{\ge m} = \{y\in X: m\le y\} $$

    Let $a:\Bbb N^{\ge m}\to X$ be a function.  Then we call this a **sequence of $X$ (starting at $m$)**.  We typically write this function as $(a_k)_{k=m}$ or if $m$ is understood from context, then just $(a_k)$.  

    If $n\in\Bbb N^{\ge m}$ then we write the image of $(a_k)$ under $n$ by 

    $$ a_n $$

    If $(i_k)_{k=n}$ is a strictly increasing sequence $i:\Bbb N^{\ge n}\to \Bbb N^{\ge m}$, then the composition $a\circ k$ is written 

    $$ a\circ k = (a_{i_k})_{k=n} $$

    and is called a **subsequence of $(a_k)$**.  
    """), "success")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
