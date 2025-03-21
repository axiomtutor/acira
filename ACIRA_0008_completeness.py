import marimo

__generated_with = "0.11.23"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # A Course in Real Analysis ... In Marimo!
        ## Unit 1: The Axioms of the Real Numbers
        ### by Axiom Tutor
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Lesson 0008: Completeness""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        So far we have definitions that tell us about $+,\times,$ and $\preceq$.  

        But these definitions are all satisfied by the rational numbers.  That is to say, $(\Bbb Q,+,\times,\le)$ satisfy the properties of an ordered field.

        There is still something not yet captured by these definitions, which give the distinct properties of the real numbers.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        To see what that is, consider the set of rational numbers $L=[0,\sqrt 2)$.  

        Since the number $\sqrt 2$ is not itself a rational number, it may seem invalid to even speak of such a set of rational numbers.

        Therefore, let us express this set in a way that is more transparently valid for rational numbers.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""$$ L = \{x\in\Bbb Q: 0\le x^2<2 \}^{\succeq 0} $$""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        It is easy to confirm that $0, \ 1, \ 1.4, \ 1.41$ are all in $L$.  

        If you ask a calculator for the decimal approximation of $\sqrt 2$, it will give you something like 
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    _src = (
        "images/0008_completeness/root2.png"
    )
    mo.image(src=_src)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        What this gestures at, is the fact that if you pick any upper bound for this set, it is always possible to find a smaller upper bound.

        For example, 2 is an upper bound for $L$, but so is $1.5$.  

        But so is $1.42$.

        But so is $1.415$, and so on.  
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""This situation is unlike what we have for an interval like $(0,1)$.  In this case, the number 1 is an upper bound, and in fact it is the least upper bound.  Any number smaller than 1 will not be an upper bound for $(0,1)$.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        And this is precisely the deficiency that the real numbers are intended to fix: We need to bound sets, and obtain a best "tightest" bound.  However, for rational numbers, this best bound does not always exist.  

        It will be an axiom of the real numbers, that whenever a nonempty set has an upper bound, it must have a least upper bound.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Let $(F,+,\times,\preceq)$ be an ordered field.  We say that this is **complete with respect to suprema** (or has the **least upper bound property**) if the following condition is met.

    For every subset $Y\subseteq F$ if $Y\ne \emptyset$ and $UB_Y\ne \emptyset$ then $\sup(Y)\in F$.  
    """),kind="success")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Real number theorems 1

    `The axiom of the real numbers`

    ---

    There is a complete ordered field.  We denote it by $(\Bbb R,+,\times,\le)$.  
    """), kind="danger")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
