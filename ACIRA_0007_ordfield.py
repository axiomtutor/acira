import marimo

__generated_with = "0.11.26"
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
def _(mo):
    mo.md(r"""# Lesson 0007: Ordered Fields""")
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




if __name__ == "__main__":
    app.run()
