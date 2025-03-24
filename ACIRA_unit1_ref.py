import marimo

__generated_with = "0.11.26"
app = marimo.App(width="medium")


@app.cell
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
    mo.md(r"""# Unit 1 Reference""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## 0001 Groups""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Let $X$ be a nonempty set, $\ast:X^2\to X$ an operation on $X$.  

    We say that $e\in X$ is an **identity element** for $\ast$ if 

    $$ e\ast a = x\ast e = a,\quad\forall a\in X $$

    For a given $a\in X$, if $b\in X$ is such that 

    $$ a\ast b=b\ast a = e $$

    then we say that $b$ is the **inverse of $a$**.  Typically, we write the inverse of $a$ as $b=a^{-1}$.  

    If $G$ is a nonempty set with operation $\ast:G^2\to G$, then we say that $(G,\ast)$ is a **group** if 

    * $\ast$ is associative,
    * $\ast$ has an identity, $e$, in $G$, and 
    * every $a\in G$ has an inverse in $G$, denoted $a^{-1}$.

    If $\ast$ is commutative then we say that $(G,\ast)$ is a commutative group.

    We also equivalently denote the group by $(G,\ast)$ or just $G$.  
    """), kind="success")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Throughout this section, assume that $(G,\ast)$ is a group with identity $e$.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Let $a\in G$.  For $n\in\Bbb N$ we define $a^n = \overbrace{a\ast a\ast\cdots\ast a}^n$, and $a^{-n}=(a^{-1})^n$.  

    We define $a^0=e$.  
    """), kind="success")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Group theorem 1

    `Unique associative operation identity, and inverses`

    ---

    Let $X$ be a nonempty set, $\ast:X^2\to X$ an operation on $X$, and $e\in X$ an identity element.  Also let $a\in X$ and suppose $a^{-1}$ exists, i.e. $aa^{-1}=e$.

    Then $e$ is the unique identity for $\ast$, and also $a^{-1}$ is the unique inverse of $a$.
    """), kind="danger")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        *Proof*: Let $y\in G$ have the identity property.  Then 

        $$ ye = y = e $$

        where the first equation is by the identity property of $e$, and the second is by the identity property of $y$.

        Let $x\in G$ and let $y\in G$ have the inverse property for $x$, i.e. $yx=e$.

        $$ 

        $\Box$
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Group theorem 2

    `Inverse of product`

    ---

    For all $a,b\in G$, the inverse of their product is 

    $$ (ab)^{-1} = b^{-1}a^{-1} $$
    """), kind="danger")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Group theorem 3

    `Group exponent laws`

    ---

    For ever $m,n\in\Bbb Z$ and for $a\in G$, we have 

    $$ a^ma^n = a^{m+n},\quad (a^m)^n $$

    If $a$ and $b$ commute then 

    $$ a^mb^m = (ab)^m $$
    """), kind="danger")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
