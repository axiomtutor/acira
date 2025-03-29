import marimo

__generated_with = "0.11.31"
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
        ### Chapter 2: Sequences
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Lesson 0010: Sequences of Real Numbers""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        We are working toward discussing the derivative and integral.

        One of the most important and fundamental objects that will help us to define and understand both of these, is sequences of real numbers.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## An Intuitive Connection to the Derivative and Integral""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Recall from calculus: If $f:\Bbb R\to\Bbb R$ is a function and $a\in\Bbb R$, then the derivative of $f$ at $a$ is approximated by, say, 

        $$\frac{f(a+1)-f(a)}{(a+1)-a}$$

        (Let's ignore issues about whether this derivative exists.)
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Then a better estimate is, say, 

        $$\frac{f(a+0.1)-f(a)}{(a+0.1)-a}$$

        and then a better one is

        $$ \frac{f(a+0.01)-f(a)}{(a+0.01)-a} $$

        and so on.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        As this sequence goes on, its limit approaches $f'(a)$.

        This isn't the only way to capture the notion of the derivative of a function, but it at least shows a connection between sequences and derivatives.  
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        The connection with integrals is probably more direct than that.  

        To compute the definite integral, $\int_a^b f \ dx$, we start by subdividing the interval $[a,b]$ into $n$ equal pieces.  Then we find approximating Riemann rectangles for each piece, and sum the rectangle areas. 
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        This produces the "$n$th estimate" of the definite integral.  We can find its value for $n=2$ and then $n=3$, and so on.  

        As the sequence progresses, its limit approaches $\int_a^b f\ dx$.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Definition, Theorem, and some Proofs""")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
