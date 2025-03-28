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

        Note that neither $\{a\}\preceq \{b\}$ nor $\{b\} \preceq \{a\}$.  This is what we mean when we say that elements are incommensurable.

        But when it comes to natural numbers, integers, and rationals, if you pick any two elements, $x,y$ then one or the other of $x\preceq y$ or $y\preceq x$ must hold.
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


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    I recommend solving at least 5 problems on your own, without looking at solutions, and getting them correct.

    For each problem that you get wrong, do another problem.  Repeat until you have successfully solved 5 problems on your own.  

    If you need an extra bank of exercise problems, you may want to search the internet or use a textbook that discusses orders.

    A text on discrete mathematics would probably be accessible, but may or may not have content about orders.  A text on orders and lattices will have relevant content, but may be more advanced than a student needs for the current topic.  

    ---

    I recommend spending at least an hour on a problem, before looking at its solution.  This recommendation is specifically for these problems, because they are meant to be easy.  For harder problems, like in the homeworks, you might need to spend several hours or days on them.

    If you have to look at the solution of a problem, treat it as a problem that you did not solve correctly.  Therefore, if you look at the solution, then this does not count toward the 5 problems that you successfully solve on your own.  
    """), kind="info")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Exercise 1""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        If $\preceq$ is a partial order on $X$, show that the corresponding strict partial order $\prec$ is

        1. Irreflexive: $\forall a\in X$ we have $a\not\prec a$.
        2. Asymmetric: $\forall a,b\in X,$ if we have $a\prec b$ then $a\not\prec b$.
        3. Transitive: $\forall a,b,c\in X$ if $a\prec b$ and $b\prec c$, then $a\prec c$.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Exercise 2""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Find all possible partial orders on the set $\{a,b,c\}$.  Of those partial orders, decide which are total orders.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Exercise 3""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Let $\preceq$ be a partial order on the set $X$, and $\prec$ the corresponding strict partial order.  

        For $a,b\in X$ show that $a\not\preceq b$ is NOT equivalent to $b\prec a$.  

        But if $\preceq$ is a total order, then $a \not\preceq b$ is equivalent to $b\prec a$.
        """
    )
    return



if __name__ == "__main__":
    app.run()
