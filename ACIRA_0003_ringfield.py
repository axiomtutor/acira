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
    mo.md(r"""# Lesson 0003: Rings and Fields""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Rings""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        As we discussed in the lesson on groups, the abstract definition of a group will be used to state the definition of real numbers.  Primarily, it tells about the behavior of each operation, addition and multiplication.  

        We'll next introduce the abstract definition of a ring.  This will tell us about the way in which addition and multiplication *interact with each other*.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        The integers, $\Bbb Z$ with addition and multiplication, will be our first example of a ring.  What makes this a ring is the following facts.  

        * $+$ and $\times$ are commutative operations. 

        * $(\Bbb Z,+)$ forms a commutative group.

        * $\times$ has an identity element, 1, which is not equal to 0.

        * $\times$ distributes over $+$, which means:

            $$ a(b+c) = ab+ac, \quad \forall a,b,c \in \Bbb Z $$
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Another example of a ring is the set of all $2\times 2$ matrices with coordinates in $\Bbb Z$.  We denote the set of all such matrices by $\Bbb Z^{2\times 2}$.  

        You should check each condition:  There is an addition operation, and a multiplication operation, which we'll denote $+''$ and $\times'$ for this example.  

        Both operations are associative.  

        $(\Bbb Z^{2\times 2}, +')$ forms a commutative group.  

        The identity for $\times'$ is the $2\times 2$ identity matrix, $I_2 = \begin{bmatrix}1&0\\0&1\end{bmatrix}$.

        And $\times'$ distributes over $+'$.  For any $A,B,C\in\Bbb Z^{2\times 2}$, 

        $$ A\times' (B+'C) = (A\times' B)+'(A\times'C) $$
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Let $R$ be a nonempty set with operations $+,\times:R^2\to R$.  

    We say that $\times$ **distributes over $+$** if for all $a,b,c\in R$,

    $$ a\times (b+c) = (a\times b)+(a\times c)$$

    and

    $$ (b+c)\times a = (b\times a)+(c\times a) $$

    We say that $(R,+,\times)$ is a **ring** if the following conditions are met.

    1. $(R,+)$ is a commutative group.  Its identity is denoted $0$.  

    2. $\times$ has an identity, $1$.

    3. $\times$ distributes over $+$.
    """), kind="success")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Fields""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        We have said that $(\Bbb Z^{2\times 2},+',\times')$ is a ring.

        However, it does lack some structure that we need for the real numbers.  That structure is: the existence of multiplicative invereses, for every nonzero number.  

        For example, the matrix $\begin{bmatrix}0&1\\0&0\end{bmatrix}$ is nonzero but has no multiplicative inverse.

        Not just that, but also multiplication of real numbers commutes:  $ab = ba$ for each $a,b\in \Bbb R$.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Therefore we define the notion of a field to express these additional constraints.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Let $(F,+,\times)$ be a ring.

    We call $(F,+,\times)$ a **field**, if the following conditions are met.

    * $(F\smallsetminus\{0\},\times)$ is a commutative group with identity 1.
    * $0\ne 1$
    """), kind="success")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Exercise 1""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Let $(F,+,\times)$ be a field.  Define the operation $+_2$ on vectors $\begin{bmatrix}a\\b\end{bmatrix},\begin{bmatrix}c\\d\end{bmatrix}\in F^2$ by

        $$ \begin{bmatrix} a\\b\end{bmatrix} +_2 \begin{bmatrix}c\\d\end{bmatrix} = \begin{bmatrix}a+c\\b+d\end{bmatrix} $$

        and $\times_2$ defined by 

        $$ \begin{bmatrix} a\\b\end{bmatrix} \times_2\begin{bmatrix}c\\d\end{bmatrix} = \begin{bmatrix}ac\\bd\end{bmatrix} $$

        Show by a counter-example, that $(F^2,+_2,\times_2)$ is not necessarily a field.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Exercise 2""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Let $F = \{0,1,2,3\}$ and define $\oplus$ and $\otimes$ on $F$, by modular addition and multiplication, respectively.

        $$ a\oplus b = (a+b)\mod 3,\quad a\otimes b = (a\times b)\mod 3 $$

        Show that $(F,\oplus,\otimes)$ is a field.  

        Show that $(\{0,1,2,3,4\}, \oplus,\otimes)$, with plus and times defined by addition and multiplication mod 4, is not a field.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Exercise 3""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Show that in any ring, the additive and multiplicative identities are unqiue.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Exercise 4""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        In a previous exercise, we saw a class `Group` which modeled finite groups as a set and operation, with methods to check that the given objects formed a group.  

        Create similar classes for rings and fields.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Exercise 5""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Show that in any ring, $0x = x0 = 0$ and $-x = (-1)x$, for every $x\in R$.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Exercise 6""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Show that $(\{0\}, +,\times)$ is a ring but not a field.

        The operations are defined by $0+0=0$ and $0\times 0=0$.
        """
    )
    return


if __name__ == "__main__":
    app.run()
