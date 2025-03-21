import marimo

__generated_with = "0.11.23"
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
        ## Unit 1: The Axioms of the Real Numbers
        ### by Axiom Tutor
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Lesson 0006: Ordered Fields""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        The field properties tell us about the behavior of the algebraic operations $+$ and $\times$.  

        The order properties tell us about the behavior of the order relation $\preceq$.

        But up to now, we don't know how the operations and relation interact.  That is described by the concept of an "ordered field".
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Let $(F,+,\times)$ be a field and $(F,\preceq)$ a totally ordered set.

    We say that $\preceq$ is **compatible with addition** if 

    $$ a\preceq b \quad \Rightarrow \quad a+c\preceq b+c, \quad \forall a,b,c\in F $$

    We say that $\preceq$ is **compatible with multiplication** if

    $$ a\preceq b \quad \Rightarrow \quad ac\preceq bc, \quad \forall a,b,c\in F \text{ and } 0\preceq c $$

    We say that $(F,+,\times,\preceq)$ is an **ordered field** if $\preceq$ is compatible with both addition and multiplication.

    We define the set of **positives**, $P = \{x\in F: 0\prec x\}$, and **negatives**, $N = \{x\in F: x\prec 0\}$.  If $Y\subseteq F$ we define the subsets of $Y$,

    \begin{align*}
        Y^+ &= Y\cap P\\
        Y^- &= Y\cap N\\
        Y^{0\succeq} &= Y\cap (P\cup \{0\})\\
        Y^{0\preceq} &= Y\cap (N\cup \{0\})
    \end{align*}

    which are, respectively, the subset of positives, negatives, nonnegatives, and nonpositives.
    """), kind="success")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Exercises""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""In all that follows, let $(F,+,\times,\preceq)$ be an ordered field.  """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Exercise 1""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    We say that $\prec$ is **compatible with $+$** if $\forall a,b,c\in F$

    $$ a\prec b \quad \Rightarrow \quad a+c\prec b+c $$

    We say that $\prec$ is **compatible with $\times$** if $\forall a,b,c\in F$ and $0\prec c$,

    $$ a\prec b \quad \Rightarrow \quad ac \prec bc $$
    """), kind="success")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Show that $\prec$ is compatible with $+$ and $\times$.
    """), kind="danger")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Exercise 2""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Let $a,b,c,d,e\in F$.  Assume $c$ is negative, $0\prec d\prec 1 \prec e$ and $a\preceq b$.

        Show each of the following.

        1. $bc\preceq ac$
        3. $0\prec d^2 \prec d \prec 1\prec \frac 1 d$
        4. $\frac 1 e \prec 1 \prec e\prec e^2$
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Exercise 3""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Show that $0\prec 1$.  

        Hint: You already have, as an axiom of fields, that $0\ne 1$.  

        Show $0\preceq 1$ by contradiction.
        """
    )
    return


if __name__ == "__main__":
    app.run()
