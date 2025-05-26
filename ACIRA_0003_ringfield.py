import marimo

__generated_with = "0.13.11"
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
    We discussed groups in the previous lesson.  A group essentially tells us how numbers (and certain other mathematical objects) combine through an operation.    

    We'll next introduce the abstract definition of a ring.  This will tell us about the way in which two operations, addition and multiplication, *interact with each other*.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""#### $(\Bbb Z,+,\times)$""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    The integers, $\Bbb Z$ with addition and multiplication, will be our first example of a ring.  What makes this a ring is the following facts.  

    * $+$ and $\times$ are associative operations. 

    * $(\Bbb Z,+)$ forms a commutative group.

    * $\times$ has an identity element, 1.

    * $\times$ distributes over $+$, which means:

        $$ a(b+c) = ab+ac, \quad \forall a,b,c \in \Bbb Z $$

        $$ (b+c)a = ba + ca, \quad \forall a,b,c\in\Bbb Z $$
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""#### $(\Bbb Z^{2\times 2}, +, \cdot)$""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Another example of a ring is the set of all $2\times 2$ matrices with coordinates in $\Bbb Z$.  We denote the set of all such matrices by $\Bbb Z^{2\times 2}$.  

    This set has an addition and multiplication operation, which should be familiar from a previous course in either discrete math or linear algebra.  

    * The sum and product are operations, because the sum of two integer matrices is an integer matrix, and likewise for the product.  Both operations are associative.  

    * $(\Bbb Z^{2\times 2}, +)$ forms a commutative group.  

    * The identity for $\cdot$ is the $2\times 2$ identity matrix, $I_2 = \begin{bmatrix}1&0\\0&1\end{bmatrix}$.

    * And $\cdot$ distributes over $+$.  For any $A,B,C\in\Bbb Z^{2\times 2}$, 

        $$ A (B+C) = (A B)+(AC) $$

        $$ (B+C)A = BA+CA $$
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Definition""")
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

    1. $+$ and $\times$ are associative.

    1. $(R,+)$ is a commutative group.  Its identity is denoted $0$.  

    2. $\times$ has an identity, $1$.

    3. $\times$ distributes over $+$.
    """), kind="success")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Exercise""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Consider the integers mod 2.  This is the set $\{0,1\}$ with the operations $\oplus$ and $\otimes$ defined as follows.

    $x\oplus y = (x+y) \mod 2$ and $x\otimes y = (xy) \mod 2$.  

    Show that this is a ring.

    Then repeat the exercise for the integers mod 4.

    Note: In my solution, I will take for granted that modular plus and times are associative, commutative, and distributive operations.  The proofs of these facts is often encountered in a discrete math course.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// details | Solution. 

    * Associative operations: Clearly $\oplus$ and $\otimes$ are operations, since their images are each subsets of $\{0,1\}$.  The fact that modular addition and multiplication are associative and commutative, is something we will take for granted.  

    * Plus is a commutative group: Clearly 0 is an additive identity.  The inverse of 0 is 0, and the inverse of 1 is 1.  So this forms an additive group.  Since we take for granted that modular addition is commutative, then the additive group is commutative.

    * Distribution: We will also take for granted, from discrete math, that modular multiplication distributes over addition.
    ///
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Fields""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    We have said that $(\Bbb Z^{2\times 2}, +, \cdot)$ is a ring.

    Let's observe two properties of this example, which should not be properties of the real numbers.

    * Matrices are not commutative.  For example,

        $$ \begin{bmatrix} 1 & 2 \\ 0 & 3 \end{bmatrix} \begin{bmatrix} 4 & 5 \\ 6 & 0 \end{bmatrix} = \begin{bmatrix} 16 & 5 \\ 18 & 0  \end{bmatrix} $$

        but

        $$ \begin{bmatrix} 4 & 5 \\ 6 & 0 \end{bmatrix} \begin{bmatrix} 1 & 2 \\ 0 & 3 \end{bmatrix} = \begin{bmatrix} 4 & 23 \\ 6 & 12  \end{bmatrix} $$

    * Some nonzero matrices have no inverse.  For example, $\begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}$ is nonzero and has no inverse.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""The real numbers, however, should commute with multiplication, and every nonzero number should have an inverse.  These extra conditions are encoded in the definition of a field, below.""")
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
    Let $(F,+,\times)$ be a field.  

    Define the operation $+_2$ on vectors $\begin{bmatrix}a\\b\end{bmatrix},\begin{bmatrix}c\\d\end{bmatrix}\in F^2$ by

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

    Show that $(\{0,1,2,3\}, \oplus,\otimes)$, with plus and times defined by addition and multiplication mod 4, is not a field.
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
