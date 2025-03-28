import marimo

__generated_with = "0.11.30"
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

        ## Unit 1: The Real Numbers

        ### Chapter 2: Properties of $\Bbb R$

        by Axiom Tutor
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Lesson 0009: The Number Line""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        We now know what the real numbers are! Hooray! 🎉🥳

        Celebartion is now over 😒, and we return to hard work, learning the basic properties of these numbers.

        In this chapter we will prove several properties that we will prove theorems which justify some of our geometric intuitions about the real number line.  

        For instance, we will show that the number line extends out to infinity (i.e. there is no largest number).  We will show that between any two real numbers there is another real number.  We will show that for any number, there is a sequence of rational numbers which approaches it (called the "density" of the rationals in the reals).  And so on.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    `Reals to infinity`

    ---

    There is no largest number.
    """), "danger")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        It is easy to prove that, for each $x\in\Bbb R$, 

        $$ x < x+1 $$
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    `Reals density`

    ---

    Between any two real numbers is a distinct real number.
    """), "danger")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        We define $2=1+1$ and clearly $1<2$.  

        If $a,b\in\Bbb R$ are any two real numbers, their average is defined as $\frac{a+b}2$.  

        One can then demonstrate that, if $a<b$, then their average is strictly in-between.
        """
    )
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
