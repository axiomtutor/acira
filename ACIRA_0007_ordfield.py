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
    mo.md(r"""In all that follows, let $(F,+,\times,\preceq)$ be an ordered field.""")
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
    mo.md(r"""Show that the product of two positive number is positive, the product of negatives is positive, and the product of a positive and negative is negative.  Also show corresponding facts for division.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Exercise 3""")
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
    mo.md(r"""## Exercise 4""")
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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Exercise 5""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        For $a,b\in P$ two positive numbers, show that 

        $$ a\prec b \quad \Leftrightarrow \quad a^2\prec b^2 $$

        Then generalize this to 

        $$ a\prec b \quad \Leftrightarrow \quad a^n\prec b^n, \quad \forall n\in\Bbb N $$
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Exercise 6""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Define $2 = 1+1$ and show that $1\prec 2$.

        For any two real numbers $a,b\in F$, define their **average** $\frac{a+b}2$.

        Show that if $a\prec b$ then 

        $$ a\prec \frac{a+b}2\prec b $$

        Conclude that between any two ordered field numbers, is a number.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Exercise 7""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        In this exercise we demonstrate an alternate, and often useful characterization of the supremum of a set in an ordered field.

        Let $A\subseteq F$ be a nonempty subset.  

        Show that, if $\alpha = \sup(A)$ exists, then it has the following two properties:

        1.  $\alpha\in UB_A$.

        2. For all $0\prec \varepsilon$, the we have $\alpha-\varepsilon\notin UB_A$.

        /// details | In a sense, this says that the supremum is ...

        right up against the upper boundary of $A$.  

        It's an upper bound, but if you go *any* amount lower, it's no longer an upper bound.  
        ///
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Also show that if $\beta\in F$ is such that:

        1. $\beta\in UB_A$.
        2. For all $0\prec \varepsilon$ then $\alpha-\varepsilon\in UB_A$.

        /// details | Therefore these two properties ...

        are equivalent to the property of being the supremum!  

        That is to say, something is the supremum, if and only if these two properties are satisfied.

        ///
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Exercise 8""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Let $a,b,c\in F$, with $a\prec b$ and $a\prec c$.

        Show that there is always some $0\prec \varepsilon$ such that 

        $$a\prec a+\varepsilon \prec b$$ 

        and 

        $$ a\prec a+\varepsilon \prec c $$
        """
    )
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
