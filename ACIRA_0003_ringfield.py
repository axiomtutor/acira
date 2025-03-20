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


@app.cell
def _(mo):
    mo.md(
        r"""
        The integers, $\Bbb Z$ with addition and multiplication, will be our first example of a ring.  What makes this a ring is the following facts.  

        * $+$ and $\times$ are commutative operations. 

        * $(\Bbb Z,+)$ forms a commutative group.

        * $\times$ has an identity element, 1.

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

    We say that $\times$ **distributes over $+$** if 

    $$ a\times (b+c) = (a\times b)+(a\times c), \quad a,b,c\in R $$

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


@app.cell
def _(mo):
    mo.callout(mo.md(r"""
    Let $(F,+,\times)$ be a ring.

    If $(F\smallsetminus\{0\},\times)$ is a commutative group, then we call $(F,+,\times)$ a **field**.
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
        Show that $(\{0\}, +,\times)$ is a ring (and in fact, a field!).

        The operations are defined by $0+0=0$ and $0\times 0=0$.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        We next augment the group structure so that we have a representation of the *interaction* between addition and multiplication.

        We call this augmented structure a ring.  As before, we start with examples and then give the abstract definition.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        The integers $\Bbb Z$ with the operations of $+$ and $\times$, is a ring.  This is because the integers with $+$ forms a *commutative* group, and there is an identity for $\times$ (which is 1), *and* because multiplication distributes over addition.

        $$ a(b+c) = ab+ac, \quad \forall a,b,c\in \Bbb Z $$
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Let $R$ be a nonempty set with two operations, $+, \times:R^2\to R$.  

    We say that **$\times$ distributes over $+$** if $\forall a,b,c\in R$ we have 

    $$ a\times (b+c) = (a\times b)+(a\times c) $$

    We say that $(R,+,\times)$ is a **ring** if the following conditions are met.

    1. Both $+$ and $\times$ are associative.
    2. $(R,+)$ is a commutative group with identity $0\in R$.
    3. There is an identity $1\in R$ for the multiplication operation.
    4. $\times$ distributes over $+$.

    We say that the ring $(R,+,\times)$ is a **commutative ring** if its operation $\times$ is commutative."""), kind="success")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Note that $(\Bbb Z,\times)$ does not form a group.  Nor does $(\Bbb Z\smallsetminus \{0\}, \times)$.

        We don't require a condition like this, for $(\Bbb Z,+,\times)$ to qualify as a ring.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        It is easy enough to see that square matrices form a ring, where $+$ and $\times$ are defined by matrix addition and multiplication.  

        The student is invited to confirm that, for each $n\ge 1$, the triple $(\Bbb Z^{n\times n}, +, \times)$ is a ring.  

        The functions are associative operations, $+$ forms a commutative group, there is a multiplicative identity (what is it?), and multiplication distributes over addition.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Let $X$ be a nonempty set, $G$ the set of bijective functions $f:X\to X$.  

        You showed in a previous exercise that $(G,\circ)$ is a group.  You are invited to now show that, if $|X|>2$ then $(G,\circ)$ is not a commutative group.  

        You can then infer that, no matter what operation we might give by $\ast$, the triple $(G,\circ,\ast)$ will never form a ring.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""If a structure is a ring, but moreover the multiplication operation forms a group (excepting 0), then we call this restricted kind of ring a field.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""For example, because $(\Bbb Q,+,\times)$ is a ring, but also $(\Bbb Q\smallsetminus\{0\},\times)$ is a commutative group (you should check this), then therefore $(\Bbb Q,+,\times)$ is a field.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Because square matrices do not necessarily form a group under multiplication (excepting 0), then these do not necessarily form a field.  

        It can be interesting to consider just the square *invertible* matrices.  This would certainly ensure that every matrix has a multiplicative inverse.  

        However, even that does not provide a field.  This is because invertible matrices still do not commute.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Let $(F,+,\times)$ be a ring with additive identity 0.

    If $(F\smallsetminus \{0\},+,\times)$ is a commutative group, then $(F,+,\times)$ is a **field**.

    For a given field, we typically write its additive identity as 0 and its multiplicative identity as 1.  We write the additive inverse of $x\in F$ as $-x$.  For any $x\ne 0$ we typically write its multiplicative inverse as $x^{-1}$.
    """), kind="success")
    return


if __name__ == "__main__":
    app.run()
