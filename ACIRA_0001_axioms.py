import marimo

__generated_with = "0.13.10"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # A Course in Real Analysis ... in Marimo!
    ## Unit 1: The Real Numbers
    ### Chapter 1: The Axioms of $\Bbb R$

    by Axiom Tutor
    """
    )
    return


@app.cell(hide_code=True)
def lesson1(mo):
    mo.md(r"""# Lesson 0001: Introduction to Axioms, Generally""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Construction of $\Bbb R$""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Many real analysis textbooks begin their presentation, with a construction of the real numbers.

    This makes obvious sense.  If we're going to study real numbers, let's start from the beginning!

    And yet that is not what these notebooks will do. 🙃
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    The construction of the real numbers takes a lot of time.  

    Moreover, once it's done, nothing much has been gained!  Once the construction is done, we never refer back to what we learned from it!  Literally the *only* value of the the construction, is to ensure that the real numbers exist.

    So from a cost-benefit analysis, going through the construction is a large cost with almost zero benefit.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Thankfully there is another way: The axiomatic approach.  

    In this presentation, we will simply write down the *axioms* of the real numbers.  The axioms of the real numbers are a minimal set of *assumptions*, from which we can do everything that we need to do.  
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Axioms of $\Bbb R$""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Although the axiomatic approach cuts out the construction steps, it still takes a while to even just state the axioms.

    Therefore we will break up the axioms into component ideas, to make each idea more digestible.  These include the ideas of 

    * a group
    * a ring
    * a field
    * a poset
    * a total order
    * an ordered field
    * completeness (with respect to suprema)
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    The structure of the first few lessons will start by introducing an abstract concept, like a group or an order.

    Then, once all of these abstract concepts have been introduced, we will use them to state the axioms of the real numbers.
    """
    )
    return


if __name__ == "__main__":
    app.run()
