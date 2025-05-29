import marimo

__generated_with = "0.13.14"
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
    mo.md(r"""# Lesson 0004: Orders""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    The field properties contain what we will need to know about the algebraic operations of $+$ and $\times$ for the real numbers.

    We now proceed likewise, to describe how the $\le$ relation on the real numbers will behave.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Let's first consider the ordering relation $\le$ on the natural numbers.

    We call $(\Bbb N,\le)$ a "partially ordered set" because the $\le$ relation satisfies some basic properties that we expect from an ordering of a set.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    For one thing it is reflexive:  For any $a\in \Bbb N$ we have $a\le a$.  

    For another it is anti-symmetric:  If $a,b\in \Bbb N$ and we have both $a\le b$ and $b\le a$ then it follows that $a=b$.

    And finally, it is transitive: $a\le b$ and $b\le c$ imply $a\le c$.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Of course, all the same could just as well be said for the rational numbers, so this too is partially ordered by its standard ordering $\le$.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    A more provocative example is the subset relation.

    Let $X$ be a nonempty set, and set $Y =\mathcal P(X)$, the powerset of $X$.  

    Define the following relation, $\preceq$, on the set $Y$.

    $$ A\preceq B \Leftrightarrow A\subseteq B, \quad \forall A,B\in Y $$
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    One can readily check that this is also reflexive, anti-symmetric, and transitive.

    *Reflexive*: For any $A\in Y$ we have $A\subseteq A$ and therefore $A\preceq A$.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""*Anti-symmetric*: Let $A,B\in Y$.  If $A\subseteq B$ and $B\subseteq A$ it follows by basic set theory that $A=B$.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""*Transitive*:  Let $A,B,C\in Y$.  Assume $A\subseteq B$ and $B\subseteq C$.  Then, again by basic set theory, $A\subseteq C$.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Exercise""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Consider $X = \{1,2,3\}$.  Find the smallest relation $\preceq\subseteq X^2$, such that $\preceq$ is reflexive, anti-symmetric, and transitive.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// details | Solution 

    $$ \preceq \quad = \quad \{ (1,1), (2,2), (3,3) \} $$

    ///
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Let $X$ be a nonempty set and $\preceq\subseteq X^2$ a relation.

    If the following conditions are met, we call $\preceq$ a **partial order**.

    1. $\preceq$ is reflexive.

    2. $\preceq$ is anti-symmetric.

    3. $\preceq$ is transitive.

    When we want to emphasize the pair which is the set and its partial order, we say that $(X,\preceq)$ is a **partially ordered set**.  We say that $(X,\preceq)$ is a **poset** for short.  

    If $\preceq$ is a partial order, then we define the corresponding **strict partial order** $\prec$ by 

    $$ a\prec b \Leftrightarrow a\prec b\land a\ne b, \quad \forall a,b\in X $$
    """), kind="success")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    But there is something that the subset relation lacks, which we want in an order on numbers.  

    For concreteness, let's discuss $X=\{a,b,c\}$ and 

    \begin{align*}
      Y &= \mathcal P(X) \\
      & = \{\emptyset, \{a\}, \{b\}, \{c\},\\
      & \quad \{a,b\}, \{a,c\},\{b,c\},\{a,b,c\}\}
    \end{align*}

    We use the partial order discussed earlier, $U\preceq V \Leftrightarrow U\subseteq V$ for each $U,V\in Y$.  

    Note that neither $\{a\}\preceq \{b\}$ nor $\{b\} \preceq \{a\}$.  

    In a case like this, where neither direction of the ordering relation holds, we say that the elements are incommensurable.  

    But when it comes to natural numbers, integers, and rationals, we expect every two number to be commensurable.  Whence the following definition of a total order, which has this further condition on an order.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Let $\preceq$ be a partial order on $X$.

    For any $a,b\in X$, if neither $a\preceq b$ nor $b\preceq a$, then we say $a$ and $b$ are **incommensurable**.

    If no two elements of $X$ are incommensurable then we say that $\preceq$ is a **total order** on $X$.  

    We also say, in this case, that $(X,\preceq)$ is a **totally ordered set**.
    """), kind="success")
    return


if __name__ == "__main__":
    app.run()
