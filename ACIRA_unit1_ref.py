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
    mo.md(r"""# Reference Section""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## 0002: Groups""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""


    Let $G$ be a nonempty set and $\ast:G^2\to G$ an opertion on $G$.  

    We say that $e\in G$ is an **identity element** if $e\ast x = x\ast e = x$ for every $x\in G$.  This element is typically denoted by $e$.

    For $x,y\in G$ we say that **$y$ is the inverse of $x$** if $x\ast y = y\ast x = e$.  Typically we denote the inverse of $x$ as $x^{-1}$.

    We call $G$ a **group** if 

    1. $\ast$ is associative.
    2. $G$ has an idenity element.
    3. Each element of $G$ has an inverse.

    If $\ast$ is commutative we say that $G$ is a **commutative group**.  
    """),kind="success")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""In all that follows, let $(G,\ast)$ be a group with identity $e\in G$.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Let $x\in G$ and $m\in\Bbb Z$.  If $m>0$ then we define

    $$ x^m = \overbrace{x\cdot x\cdots x}^{m} $$

    If $m=0$ then 

    $$ x^m=e $$

    and if $m < 0$ then

    $$ x^m = (x^{-1})^{|m|} $$

    """), kind="success")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Groups theorem 1

    `Unique identities`

    ---

    For any nonempty set $X$ and operation $\ast:X^2\to X$, if $\ast$ has an identity element $e\in X$, then it is unique.
    """), kind="danger")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        *Proof*:  If $a\in X$ is an identity for $\ast$, then 

        $$ ae = a = e $$

        $\Box$
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Group theorems 2

    `Unique inverses of associative operations`

    ---

    Let $X$ be a nonempty set, $\ast:X^2\to X$ an associative operation on $X$, and $e$ the identity for $\ast$.

    If $a\in X$ has an inverse $a^{-1}$ then this is its unique inverse.
    """), kind="danger")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        *Proof*: Let $b\in X$ be an inverse of $a$ so that $ab = ba = e$.

        $$ b = be = baa^{-1} = ea^{-1} = a^{-1} $$

        $\Box$
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Group theorems 3

    `Unique group identities and inverses`

    ---

    The identity and all inverse in $G$ are unique.
    """), kind="danger")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        *Proof*: Since identities of any operation are unique, then the identity of $G$ is unique.

        Since the operation of $G$ is associative, then each element $x\in G$ has a unique inverse $x^{-1}\in G$.  

        $\Box$
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Group theorems 4

    `Inverses cancel`

    ---

    For any $x\in G$,

    $$ -(-x) = x $$

    """), kind="danger")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        *Proof*: $x$ has the property $x+(-x) = e$.

        Therefore $x$ has the property of being the inverse of $-x$.  By the uniqness of inverses, therefore $x = -(-x)$.  

        $\Box$
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Groups theorem 4

    `Group cancellation`

    ---

    Let $x,y,z\in G$.  

    If $xy = xz$ then $y=z$.  
    """), kind="danger")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        *Proof*: From $xy=xz$ 

        $$ x^{-1}(xy) = x^{-1}(xz) $$

        which by associativity is 

        $$ (x^{-1}x)y = (x^{-1}x)z $$

        which by the inverse property is

        $$ ey = ez $$

        which by the identity property is 

        $$ y=z $$

        $\Box$
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Groups theorem 5

    `Group exponent laws`

    ---

    Let $x,y\in G$ and $m,n\in\Bbb Z$.  Then 

    $$ x^mx^n = x^{m+n},\quad (x^m)^n = x^{mn} $$

    $G$ is commutative if and only if 

    $$ x^m y^m = (xy)^m $$
    """), kind="danger")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        *Proof*: Assume, without loss of generality that $m\le n$.

        *Case 1*, assume $m=0$ or $n=0$.

        If $m=0$,

        \begin{align*}
        x^mx^n &= ex^n = x^n
        \end{align*}

        *Mutatis mutandis* the same proof holds if $n=0$.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        *Case 2*, assume $0 < m, n$.

        \begin{align*}
        x^mx^n &= \overbrace{x\cdot x\cdots x}^m\overbrace{x\cdot x\cdots x}^n \\ 
        &= \overbrace{x\cdot x\cdots x}^{m+n} \\
        &= x^{m+n}
        \end{align*}
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        *Case 3*, assume $m<0<n$.

        *Subcase 3a*, assume $m+n\ge 0$.

        In this case $|m|=-m$ and $-m\le n$.  Then 

        \begin{align*}
        x^mx^n &= \overbrace{x^{-1}\cdot x^{-1}\cdots x^{-1}}^{|m|} \overbrace{x\cdot x\cdots x}^{n}\\
        &= \overbrace{x^{-1}\cdot x^{-1}\cdots x^{-1}}^{|m|-1} \overbrace{x\cdot x\cdots x}^{n-1} \\
        &= \overbrace{x^{-1}\cdot x^{-1}\cdots x^{-1}}^{|m|-2} \overbrace{x\cdot x\cdots x}^{n-2} \\
        &\vdots \\
        &=\overbrace{x\cdot x\cdots x}^{n-|m|}\\
        &=\overbrace{x\cdot x\cdots x}^{n+m}
        \end{align*}
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        *Subcase 3b*, assume $m+n < 0$.  

        Then $|m|=-n$ and $n< -m$.  

        \begin{align*}
        x^mx^n &= \overbrace{x^{-1}\cdot x^{-1}\cdots x^{-1}}^{|m|} \overbrace{x\cdot x\cdots x}^{n} \\
        &= \overbrace{x^{-1}\cdot x^{-1}\cdots x^{-1}}^{|m|-1} \overbrace{x\cdot x\cdots x}^{n-1} \\
        &\vdots \\
        &= \overbrace{x^{-1}\cdots x^{-1}}^{|m|-n}\\
        &= \overbrace{x^{-1}\cdots x^{-1}}^{-(m+n)} \\
        &= x^{m+n}
        \end{align*}
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        *Case 4*, assume $m,n<0$.

        \begin{align*}
            x^mx^n &= \overbrace{x^{-1}\cdots x^{-1}}^{|m|} \overbrace{x^{-1}\cdots x^{-1}}^{|n|} \\
            &= \overbrace{x^{-1}\cdots x^{-1}}^{|m|+|n|} \\
            &= \overbrace{x^{-1}\cdots x^{-1}}^{-(m+n)} \\
            & = x^{m+n}
        \end{align*}

        $\Box$
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## 0003: Rings and Fields""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Let $R$ be a nonempty set, and $+,\times: R^2\to R$ two operations on $R$.

    We say that **$\times$ distributes over $+$** if 

    \begin{align*} 
    a\times (b+c) &= (a\times b)+(a\times c) \\
    (b+c)\times a &= (b\times a)+(c\times a), \quad \forall a,b,c\in R 
    \end{align*}

    We say $(R,+,\times)$ is a **ring** if 

    1. $+$ and $\times$ are associative.
    2. $(R,+)$ is a commutative group with identity $0\in R$.
    3. There is a multiplicative identity, $1\in R$.  
    4. $\times$ distributes over $+$.

    If in addition $(F\smallsetminus \{0\}, \times)$ is a commutative group, then we call $(F, +, \times)$ a **field**.
    """), kind="success")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""In all that follows, assume that $(R,+,\times)$ is a ring.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Ring theorems 1

    `Unique ring identities and inverses`

    ---

    In a ring, the additive and multiplicative identities and inverses are unique.
    """), kind="danger")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        *Proof*: By the `unique identites` theorem, the identity is unique for each operation.

        Because the operations are both associative, by the `unique inverses for associative operations` theorem, any inverse for each operation is unique.

        $\Box$
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Ring theorems 1

    `Zero annihilates` 

    ---

    For all $x\in R$,

    $$ 0x=x0 = 0 $$

    """), kind="danger")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        *Proof*: 

        $$ 0x = (0+0) x = 0x + 0x $$ 

        so 

        $$ 0x-0x = 0x+0x-0x $$ 

        which simplifies to

        $$ 0 = 0x $$

        *Mutatis mutandis*, the same argument applies likewise to $x0$.

        $\Box$
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    $\forall x\in R$,

    $$ -x = (-1)x $$
    """), kind="danger")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        *Proof*: 

        $$ x+(-1)x = x(1-1) = x0 = 0 $$

        Since $(-1)x$ has the property of the inverse of $x$, then by the uniqueness of inverse elements, $-x=(-1)x$.  

        $\Box$
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""In what follows, assume $(F,+,\times)$ is a field.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Field therems 1 

    `Multiplication cancellation`

    ---

    Let $a,b,c\in F$ such that 

    $$ ab = ac $$

    If $a\ne 0$ then $b=c$.
    """), kind="danger")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        *Proof*: Since $a\ne 0$ then $a^{-1}$ exists.  

        $$ a^{-1}ab = a^{-1}ac = b = c $$

        $\Box$
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## 0004: Orders""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Let $X$ be a nonempty set and $\preceq\subseteq X^2$ a relation on $X$.  We say that $\preceq$ is a **partial order** if it is reflexive, symmetric, and transitive.  

    We call $(X,\preceq)$ a **partiall ordered set** or **poset** for short.  

    If $\preceq$ is a partial order, then we define the **corresponding strict partial order, $\prec$** by 

    $$ a\prec b \text{ if and only if } a\preceq b \text{ and } a\ne b, \quad \forall a,b\in X $$

    For a poset $(X,\preceq)$ and elements $a,b\in X$, if neither $a\preceq b$ nor $b\preceq a$, then we say that $a$ and $b$ are **incommensurable**.  If no two elements in $X$ are incommensurable, then we say that $\preceq$ is a **total order** and $(X,\preceq)$ a **totally ordered set**.
    """), kind="success")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""In all that follows, assume $(X,\preceq)$ is a poset and $\prec$ the corresponding strict partial order.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Order theorem 1

    `Strict order properties`

    ---

    $\prec$ is irreflexive, asymmetric, and transitive.
    """), kind="danger")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        *Proof*:  Let $a\in X$, then $a = a$, so we cannot have $a\prec a$ by definition.  Therefore $\prec$ is irreflexive.

        Let $a,b\in X$ and assume $a\prec b$.  Therefore $a\preceq b$ and $a\ne b$ by definition.  

        Assume for contradiction that $b\prec a$, so therefore $b\preceq a$.  By the anti-symmetry of $\preceq$ we have $a=b$, a contradiction.  

        Therefore $b\not\prec a$ and this shows that $\prec$ is asymmetric.

        Finally, for $a,b,c\in X$ assume $a\prec b$ and $b\prec c$.  Then $a\preceq b$ and $b\preceq c$ by definition, and then by transitivity of $\preceq$ we have $a\preceq c$.  

        Assume for contradiction that $a=c$.  Then $a\preceq b$ and $b\preceq a$, and then by the anti-symmetry of $\preceq$ we have $a=b$.  But by definition of $a\prec b$ we have $a\ne b$, a contradiction.

        Therefore $a\ne c$, which shows $a\prec c$.  In turn, this shows $\prec$ is transitive.

        $\Box$
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Order theorem 2

    `Negating precedence`

    ---

    Let $(X,\preceq)$ be a poset and $a,b\in X$.  

    If $a\prec b$ then $b\not\preceq a$.  

    If $\preceq$ is a total order, then $a\prec b$ if and only if $b\not\preceq a$.
    """), kind="danger")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        *Proof*:  Assume $a\prec b$.  For contradiction, further assume $b\preceq a$.  

        Then $a\preceq b$ by definition of $\prec$, and so $a=b$ by anti-symmetry of $\preceq$.  But also by definition of $\prec$ we have $a\ne b$, a contradiction.

        Therefore $b\not\preceq a$.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Now assume that $(X,\preceq)$ is a total order.  We already have that if $a\prec b$ then $b\not\preceq a$ from above.

        Assume $b\not\preceq a$.  By totality, we must therefore have $a\preceq b$.  

        Assume for contradiction that $a = b$.  Then we must have $a\preceq a$ by reflexivity, and therefore $b\preceq a$,  But this contradicts $b\not\preceq a$.

        Therefore $a\ne b$, which shows $a\prec b$.  

        $\Box$
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## 0005: Bounds""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Let $(X,\preceq)$ be a poset and $Y\subseteq X$ a nonempty subset.  Let $\alpha\in X$.

    If $\forall a\in Y$ we have $a\preceq \alpha$, then we say that $\alpha$ is an **upper bound** of $Y$.  If $\forall a\in Y$ we have $\alpha\preceq a$ then we say that $\alpha$ is a **lower bound** of $Y$.

    We denote the set of all upper bounds of $Y$ by $UB_Y$ and the set of all lower bounds of $Y$ by $LB_Y$.  

    If $\alpha\in Y\cap UB_Y$ we say that $\alpha$ is the **maximum** of $Y$, and write $\alpha = \max(Y)$.  If $\alpha\in Y\cap LB_Y$ then we say that $\alpha$ is the **minimum** of $Y$, and write $\alpha = \min(Y)$.  

    If $\alpha = \min(UB_Y)$ then we say that $\alpha$ is the **supremum** or **least upper bound** of $Y$, and write $\alpha=\sup(Y)$.  If $\alpha = \max(LB_Y)$ then we say that $\alpha$ is the **infimum** or **greatest lower bound** of $Y$, and write $\alpha = \inf(Y)$.  
    """), kind="success")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""In all that follows, assume $(X,\preceq)$ is a poset.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Bound theorem 1

    `Finite set max min`

    ---

    If $(X,\preceq)$ is a totally ordered set, and if $\emptyset \ne A\subseteq X$ is finite, then both $\max(A)$ and $\min(A)$ exist.
    """), kind="danger")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        *Proof*:  If $|A|=1$ then $A = \{b\}$ for some $b\in X$.  In that case, $b\preceq b$ by reflexivity.  Immediate from this, $b = \max(A)$ and $b=\min(A)$.  

        Assume that the theorem holds for every set, with $|A|=n$.  Now let $A$ be a set with $|A|=n+1$.  Let $b\in A$.

        Then define $A' = A\smallsetminus\{b\}$, so that $|A'| = n$ and therefore $\alpha=\min(A')$ and $\beta = \max(A')$ both exist.  

        If $b\preceq \beta$ then $\beta=\max(A)$.  This follows because, if $c\in A$ then if $c=b$ we have $c\preceq \beta$.  And if $c\ne b$ then $c\in A'$, and since $\beta=\max(A')$, we have $c\preceq \alpha$.  

        On the other hand, if $\alpha\preceq b$ then $b=\max(A)$.  This follows because, if $c\in A$ then if $c=b$ we have $c\preceq b$ by reflexivity.  If $c\ne b$ then $c\in A'$ and therefore $c\preceq \beta\preceq b$.

        Since $\preceq$ is total, then the above cases are exhaustive.  Therefore we have that the maximum and minimum of $A$ both exist.

        *Mutatis mutandis* the same argument applies for the minimum.  

        $\Box$
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Bound theorem 2

    `Subset sup inf`

    ---

    Let $\emptyset\ne A\subseteq B\subseteq X$ be two nonempty subsets, for which $\sup(A)$ and $\sup(B)$ both exist.  

    Then  

    $$\sup(A)\preceq \sup(B), \text{ and } \inf(B)\preceq \inf(A) $$
    """), kind="danger")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        *Proof*:  If we show that $\sup(B) \in UB_A$ then it follows immediately that $\sup(A)\preceq \sup(B)$, as $\sup(A) = \min(UB_A)$.  

        Let $c\in A$.  Then $c\in B$  and $c\preceq \sup(B)$, so the conclusion follows.

        The proof for infima is *mutatis mutandis* the same.

        $\Box$
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## 0006: Bounds of Functions""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""In all that follows, assume $(X,\preceq)$ is a poset.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Let $A$ be a nonempty set and $f,g:A\to X$ two functions.  Let $\alpha\in X$.  

    Define the **image of $f$** as $\text{Im}(f) = \{f(b): b\in A\}$.

    We write that $f\preceq g$ if 

    $$ f(b) \preceq g(b), \quad \forall b\in A $$

    Let $\alpha\in X$.  

    * If $\alpha$ is an **upper bound of $f$** if $\alpha\in UB_{\text{Im}(f)}$ and likewise define a **lower bound of $f$**.  If $\text{Im}(f)$ is bounded then we say that $f$ is **bounded**.  
    * If $\alpha=\max(\text{Im}(f))$ then $\alpha$ is the **maximum of $f$**, and likewise for the **minimum**.
    * If $\alpha=\sup(\text{Im}(f))$ then $\alpha$ is the **supremum of $f$**, and likewise for the **infimum**.  
    """), kind="success")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Let $A,B$ be two nonempty sets and $f:A\times B\to X$ a function.  Let $c'\in A, d'\in B$.  

    We define **the partial function, $f$ applied to $c'$**, to be $f_{(c',\cdot)}: B\to X$.  It is given by  

    $$ f_{(c',\cdot)}(y) = f(c',y), \quad \forall y\in B $$

    and likewise for $f_{(\cdot,d')}:A\to X$.  

    We define **the supremum of $f$ over $A$** to be the function $\sup_{a\in A}f_{(\cdot, x)}$.  It is given by 

    $$ \left(\sup_{a\in A}f_{(\cdot,x)}\right)(c) = \sup \left(f_{(\cdot,c)}\right) $$

    Its domain is the subset of $B$ for which this supremum exists.

    Likewise for **the supremum of $f$ over $B$**, the function $\sup_{b\in B} f_{(x,\cdot)}:A\to X$.  

    And we define 

    $$ \sup_{a\in A}\sup_{b\in B} = \sup_{a\in A}\left(\sup_{b\in B}f_{(x,\cdot)}\right) $$

    and 

    $$ \sup_{b\in B}\sup_{a\in A} = \sup_{b\in B}\left(\sup_{a\in B}f_{(\cdot,x)}\right) $$

    And likewiise for the definitions of corresponding concepts involving the infima.
    """), kind="success")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Bounds of functions theorem 1

    `Sup function order`

    ---

    Let $A$ be a nonempty set and $f,g : A\to X$ be two functions.  

    If $f\preceq g$ then $\sup(f) \preceq \sup(g)$.

    """), kind="danger")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        *Proof*: We only need to show that $\sup(g)$ is an upper bound on $\text{Im}(f)$.  Let $b\in A$.

        Then $f(b)\preceq g(b)\preceq \sup(g)$.

        $\Box$
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Bounds of functions theorem 2

    `Stacked sup order`

    ---

    Let $A,B$ be two nonempty sets, and $f:A\times B\to X$ a function.

    If $\sup_{a\in A}\sup_{b\in B}f$ exists, then 

    $$ \sup_{a\in A}\sup_{b\in B}f = \sup_{b\in B}\sup_{a\in A}f $$

    and 

    $$\inf_{a\in A}\inf_{b\in B}f = \inf_{b\in B}\inf_{a\in A}f $$
    """), kind="danger")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        *Proof*:  For any $c\in A, d\in B$ we have 

        $$ f(c,d) \preceq \sup_{b\in B}f_{(x,\cdot)} $$

        Now fix $d$ and then, $f_{(\cdot, d)} \preceq \sup_{b\in B}f_{(x,\cdot)}$ as an inequality of functions sharing the same domain, $A$.  Because of the `Sup function order` theorem, then 

        $$ \sup_{a\in A}f_{(\cdot,d)} \preceq \sup_{a\in A}\sup_{b\in B} f_{(x,\cdot)} $$

        Since this is true for an arbitrary $d\in B$, we have that $\sup_{a\in A}\sup_{b\in B}f_{(x,\cdot)} = \sup_{a\in A}\sup_{b\in B} f$ is an upper bound on the function $\sup_{a\in A}f_{(\cdot, x)}$.  

        Therefore $\sup_{b\in B}\sup_{a\in A}f_{(\cdot,x)} \preceq \sup_{a\in A}\sup_{b\in B}f$, which is the same as 

        $$ \sup_{b\in B}\sup_{a\in A} f \preceq \sup_{a\in A}\sup_{b\in B} f $$

        The reverse inequality can be proved similarly, which then shows 

        $$ \sup_{b\in B}\sup_{a\in A}f  = \sup_{a\in A}\sup_{b\in B} f $$

        And *mutatis mutandis* the same proof shows the equation for infima.

        $\Box$
        """
    )
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    ztimesbtn = mo.ui.button(
        value=False, on_click=lambda value: not value, label="Show answer"
    )

    ztimeslst = [
        mo.md(
            r"""
        Note that $\Bbb Z$ is not a group if we instead take the operation to be multiplication.  

        In this example, we do have a set and operation.  The operation is associative.

        In fact, there is even an identity element!  

        It is ... 


        """
        ),
        ztimesbtn,
    ]
    return ztimesbtn, ztimeslst


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
