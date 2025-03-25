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
    mo.md(r"""# 0001 Groups""")
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
def _():
    thmlst = []
    return (thmlst,)


@app.cell(hide_code=True)
def _(mo, thmlst):
    thmlst.append(1)
    mo.output.replace(mo.callout(mo.md(r"""
    Group theorem """ + f"{len(thmlst)}" + r"""

    `Unique associative operation identity, and inverses`

    ---

    Let $X$ be a nonempty set, $\ast:X^2\to X$ an operation on $X$, and $e\in X$ an identity element.  Also let $a\in X$ and suppose $a^{-1}$ exists, i.e. $aa^{-1}=e$.

    Then $e$ is the unique identity for $\ast$, and also $a^{-1}$ is the unique inverse of $a$.
    """), kind="danger"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        *Proof*: Let $y\in X$ have the identity property.  Then 

        $$ ye = y = e $$

        where the first equation is by the identity property of $e$, and the second is by the identity property of $y$.

        Therefore $e$ is the unique identity for $\ast$.

        ---

        Let $a\in X$ with $a^{-1}\in X$ an inverse of $a$.  Let $y\in X$ have the inverse property for $a$, i.e. $ya=e$.

        \begin{align*}
          a^{-1} &= a^{-1}e \\
          &= a^{-1}(ay) \\
          &= (a^{-1}a)y \\
          &= ey \\
          &= y
        \end{align*}

        Therefore $a^{-1}$ is the unique inverse of $a$. 

        $\Box$
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Group theorem

    `Unique group identity and inverse`

    ---

    The identity in $G$ is unique, and each $x\in G$ has a unique inverse.

    """), kind="danger")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        *Proof*: Since the group operation is associative, by `Unique associative operation identity and inverses`, the identity and inverses are unique in $G$.

        $\Box$
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(f"""
    Group theorem 

    `Group inverse inverse`

    ---""" + r"""

    For all $x\in G$ we have $(x^{-1})^{-1}=x$.
    """), kind="danger")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        *Proof*: Because $x^{-1}x=e$, this show that $x$ has the property of being the inverse of $x^{-1}$.  

        Since the inverse of $x^{-1}$ is uniquely $(x^{-1})^{-1}$, by the `Unique group identity and inverse` theorem, then 

        $$ x = (x^{-1})^{-1} $$


        $\Box$
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    `Group equations have unique solutions`

    ---

    Let $x,a,b\in G$ such that $xa=b$.  Then the value of $x$ is uniquely determined to be $ba^{-1}$.  
    """), "danger")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        *Proof*: From the given equation we have $xaa^{-1} = ba^{-1} = x$.  Since $a^{-1}$ uniquely determines an element of $G$, and the group operation is a function, then $ba^{-1}$ is uniquely determined.

        $\Box$
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Group theorem 3

    `Inverse of product`

    ---

    For all $a,b\in G$, the inverse of their product is 

    $$ (ab)^{-1} = b^{-1}a^{-1} $$
    """), kind="danger")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        *Proof*: 

        \begin{align*}
        (ab)(b^{-1}a^{-1}) &= a(bb^{-1})a^{-1} \\
        &= a e a^{-1}\\
        &= e
        \end{align*}

        So $b^{-1}a^{-1}$ has the property of the inverse of $ab$.

        Then by the `Unique group identity and inverse` theorem, 

        $$b^{-1}a^{-1} = (ab)^{-1} $$

        $\Box$
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Group theorem 3

    `Group exponent laws`

    ---

    For every $m,n\in\Bbb Z$ and for $a\in G$, we have 

    $$ a^ma^n = a^{m+n},\quad (a^m)^n $$

    If $a$ and $b$ commute then 

    $$ a^mb^m = (ab)^m $$
    """), kind="danger")
    return


@app.cell(hide_code=True)
def _(mo):
    _case1 = mo.callout(mo.md(r"""
    *Case 1*: Assume $m=0$ or $n=0$.  

    Without loss of generality, specifically assume $m=0$.

    Then $a^ma^n = ea^n = a^n$ which is the same as $a^{m+n}=a^n$.
    """))

    _case2 = mo.callout(mo.md(r"""
    *Case 2*: Assume $0<m,n$.

    Simply by counting terms,

    \begin{align*}
    a^ma^n &= \overbrace{aa\cdots a}^m \ast \overbrace{aa\cdots a}^n \\
    &= \overbrace{aa\cdots a}^{m+n}\\
    &= a^{m+n}
    \end{align*}
    """))

    _case3 = mo.callout(mo.md(r"""
    *Case 3*: Assume $m<0<n$ and $-m \le n$.

    \begin{align*}
      a^ma^n &= \overbrace{a^{-1}a^{-1}\cdots a^{-1}}^{-m}\ast \overbrace{aa\cdots a}^n \\
      &= \overbrace{a^{-1}a^{-1}\cdots a^{-1}}^{-m-1}\ast e \ast \overbrace{aa\cdots a}^{n-1} \\
      &\vdots \\
      &= \overbrace{aa\cdots a}^{n-(-m)} \\
      &=a^{n+m}
    \end{align*}
    """))

    _case4 = mo.callout(mo.md(r"""
    *Case 4*: Assume $m,n<0$.  

    \begin{align*}
      a^ma^n &= \overbrace{a^{-1}a^{-1}\cdots a^{-1}}^{-m}\ast \overbrace{a^{-1}a^{-1}\cdots a^{-1}}^{-n}\\
      &= \overbrace{a^{-1}a^{-1}\cdots a^{-1}}^{-(m+n)}\\
      &= a^{m+n}
    \end{align*}
    """))

    mo.md(f" *Proof*: " + r"Assume $m\le n$." +f"""
    {_case1}

    {_case2}

    {_case3}

    {_case4}

    """+r"""*Mutatis mutandis* the proof is the same if $n\le m$.

    $\Box$
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# 0003 Rings and Fields""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Let $R$ be a nonempty set with two operations $+,\times:R^2\to R$.  

    We say that $\times$ **distributes over $+$** if $\forall a,b,c\in R$,

    $$ a\times (b+c) = (a\times b) + (a\times c) $$

    and 

    $$ (b+c)\times a = (b\times a)+(c\times a) $$

    We say that $(R,+,\times)$ is a **ring** if 

    1. Both operations are associative.
    2. $(R,+)$ is a commutative group.  We write its identity as $0$, called the **additive identity**.
    3. $\times$ has an identity element.   We write it as $1$, called the **multiplicative identity**.
    4. $\times$ distributes over $+$.

    For brevity, we write the inverse of $x\in R$ as $-x$ and we write $a+(-b)$ instead as $a-b$ for all $a,b\in R$.  We also write $a\times b$ as $ab$ and $a\times b^{-1}$ as $a/b$.  

    For $n\in\Bbb Z$ and $a\in R$, we define $na$ as repeated addition, in the exact same sense as we did for a group.  Likewise $a^n$ is repeated multiplication, in the sense we defined for a group.  

    If $(R\smallsetminus \{0\},\times)$ forms a commutative group, and if $0\ne 1$, then we say that $(R,+,\times)$ is a **field**.
    """), kind="success")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""In all that follows, assume $(R,+,\times)$ is a ring.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    `Unique ring identities and inverses`

    ---

    $0$ is the unique additive identity, and $1$ is the unique multiplicative identity.  All additive and multiplicative inverses that exist, exist uniquely.
    """), "danger")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        *Proof*: Immediate from the fact that the ring operations are associative, and `Unique associative operation identity and inverses`.  

        $\Box$
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    `Ring zero annihilates`

    ---

    For every $x\in R$, 

    $$ 0x = x0 = 0 $$
    """), "danger")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        *Proof*:  

        \begin{align*}
          0x &= (0+0)x \\
          &= 0x+0x 
        \end{align*}

        therefore 

        \begin{align*}
            0x-0x &= 0x+0x-0x\\
            &= 0\\
            &=0x
        \end{align*}

        $\Box$
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    `Ring negative is negative 1`

    ---

    For every $x\in R$, 

    $$ -x = (-1)x = x(-1)$$

    Also, for all $y\in R$

    $$ -(xy)=(-x)y = x(-y) $$
    """),"danger")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        *Proof*: 

        \begin{align*}
        (-1)x+x &= (-1)x+1x \\
        &= (-1+1)x \\
        &= 0x \\
        &= 0
        \end{align*}

        Therefore $(-1)x$ has the property of being the additive inverse of $x$ and so 

        $$ (-1)x = -x $$

        *Mutatis mutandis* the same proof applies with $-1$ on the other side of $x$.  

        Using this result, if $y\in R$ then 

        \begin{align*}
            -(xy) &= (-1)xy \\
            &= (-x)y
            &= xy(-1) \\
            &= x(-y)
        \end{align*}

        $\Box$
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    `Field equations have unique solutions`

    ---

    Show that for all $x,a,b\in F$ the equation 

    $$ ax=b $$

    has the unique solution $x=ba^{-1}$ if $a\ne 0$.
    """), "danger")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        *Proof*: If $a\ne 0$ then $a^{-1}$ exists.  

        $$ a^{-1}ax = a^{-1}b = x $$

        and $a^{-1}b$ is uniquely determined.

        $\Box$
        """
    )
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
