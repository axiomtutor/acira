import marimo

__generated_with = "0.11.28"
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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# 0004 Order""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Let $X$ be a nonempty set and $\preceq \subseteq X^2$ a relation on $X$.  

    We say that $\preceq$ is a **partial order** if it is reflexive, anti-symmetric, and transitive.  

    If $\preceq$ is a partial order then we say that $(X,\preceq)$ is a **partially ordered set** or just **poset**.

    We often write $(X,\preceq)$ and just $X$, interchangeably.  So we may say that $X$ is a poset, or that $X$ is partially ordered by $\preceq$.  

    When we express $a\preceq b$ verbally we may say "$a$ precedes or equals $b$".  I personally shorten this to "$a$ left eqs $b$".  

    The notation $a\succeq b$ is syntactic sugar for $b\preceq a$.  To pronounce "$a \succeq b$" we may say "$a$ succeeds or equals $b$".  For short I use "$a$ right eqs $b$".

    For any two elements $a,b\in X$, if neither $a\preceq b$ nor $b\preceq a$ then we say that $a$ and $b$ are **incommensurable** with respect to $\preceq$.  Otherwise they are **commensurable**.

    If every two elements of $X$ are commensurable, we say that $\preceq$ is **total**, or a **total order** on $X$.  We also say that $(X,\preceq)$ is a **totally ordered set**.  

    If $\preceq$ is a partial order, then we define the relation $\prec \subseteq X^2$ by 

    $$ a\prec b \quad \Leftrightarrow \quad a\preceq b, \text{ and } a\ne b, \quad \forall a,b\in X $$

    To pronounce $a\prec b$ we say "$a$ precedes $b$".  The expression $a\succ b$ is syntactic sugar for $b\prec a$ and we say "$a$ succeeds $b$".
    """), "success")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""In all that follows, let $(X,\preceq)$ be a poset.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    `Precedence is a strict partial order`

    ---

    $\prec$ is irreflexive, asymmetric, and transitive.
    """), "danger")
    return


@app.cell(hide_code=True)
def _(mo):
    _irref = mo.callout(mo.md(r"""
    *Irreflexive*:  Let $a\in X$.

    Then $a=a$ and therefore $a\not\prec a$.
    """))

    _asym = mo.callout(mo.md(r"""
    *Asymmetric*: Let $a,b\in X$ and assume $a\prec b$.  

    Then $a\ne b$ and $a\preceq b$, by definition.

    For contradiction, assume $b\prec a$ so then $b\preceq a$.  

    By the anti-symmetry of $\preceq$ we then have $a=b$.

    But this contradicts $a\ne b$ above, concluding the proof by contradiction.

    Therefore $b\not\prec a$, which shows that $\prec$ is asymmetric.
    """))

    _trans = mo.callout(mo.md(r"""
    *Transitive*: Let $a,b,c\in X$ and assume $a\prec b$ and $b\prec c$.  

    Then $a\preceq b$ and $b\preceq c$, so by the transitivity of $\preceq$ we have $a\preceq c$.

    Assume for contradiction that $a=c$.  Then $c\preceq b$ which, by anti-symmetry of $\preceq$, implies $b=c$.  

    But also from $b\prec c$ we have $b\ne c$, a contradiction.

    Therefore $a\ne c$ and therefore $a\prec c$, showing transitivity.
    """))

    mo.md(f"""*Proof*:

    {_irref}

    {_asym}

    {_trans}

    """+r"$\Box$")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    `Negating precedence`

    ---

    If $a\prec b$ then $b\not\preceq a$.

    If $(X,\preceq)$ is a totally ordered set, then if $a\not\preceq b$ it follows that $b\prec a$.
    """), "danger")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        *Proof*:  Since $a\prec b$ then $a\preceq b$. 

        If $b\preceq a$ then $a=b$, but since $a\ne b$, we must therefore have $b\not\prec a$.

        Now assume $\preceq$ is a total order, and $a\not\preceq b$.

        By totality, we must have $b\preceq a$.  

        If $b=a$ then $a\preceq b$ by reflexivity, contrary to assumption. Therefore $b\ne a$.

        So $b\prec a$.

        $\Box$
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# 0005 Bounds""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Let $(X,\preceq)$ be a poset and $A\subseteq X$ a nonempty set, and $\alpha\in X$.

    If $\forall b\in A$ we have $b\preceq\alpha$ then we call $\alpha$ an **upper bound of $A$**.  If $\forall b\in A$ we have $\alpha\preceq b$ we call $\alpha$ a **lower bound of $A$**.

    We denote the set of all upper bounds of $A$ by $UB_A$ and the set of all lower bounds as $LB_A$.  

    If $\alpha\in A\cap UB_A$ then we call $\alpha$ the **maximum of $A$** and write $\alpha=\max(A)$.  If $\alpha\in A\cap LB_A$ we call $\alpha$ the **lower bound of $A$** and write $\alpha=\min(A)$.  

    If $\alpha=\min(UB_A)$ we call $\alpha$ the **supremum of $A$**, and if $\alpha=\max(LB_A)$ we call $\alpha$ the **infimum of $A$**.  
    """), "success")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        In all that follows, let $(X,\preceq)$ be a poset, $A,B\subseteq X$ two nonempty subsets, and $\alpha\in X$.

        Each theorem about an upper bound (or maximum, or supremum) has a corresponding theorem about a lower bound (minimum, infimum), which should be easy to infer.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    `Max is sup`

    ---

    If $\alpha = \max(A)$ then $\alpha=\sup(A)$.
    """), "danger")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        *Proof*:  We have by assumption that $\alpha\in A\cap UB_A$.

        Let $\beta\in UB_A$.  Since $\alpha\in A$ we must have $\alpha\preceq \beta$.

        Therefore $\alpha=\min(UB_A) = \sup(A)$.  

        $\Box$
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    `Finite set, total order max`

    ---

    If $\preceq$ is a total order and $A$ is finite then $\max(A)$ exists.
    """), "danger")
    return


@app.cell(hide_code=True)
def _(mo):
    _alpha = mo.callout(mo.md(r"""
    *Case 1*: Assume $f\preceq \alpha$.

    Then for every $x\in E$ we have $x\in E'$ or $x=f$.  

    In the former case $x\preceq \alpha$ by definition.

    In the latter case $x\preceq \alpha$ by assumption.

    Therefore $\alpha = \max(E)$.  
    """))

    _f = mo.callout(mo.md(r"""
    *Case 2*: Assume $\alpha\preceq f$.

    Then for every $x\in E$ we have $x\in E'$ or $x=f$.

    In the former case $x\preceq \alpha\preceq f$ and by transitivity, $x\preceq f$.

    In the latter case $x\preceq f$ by reflexivity.  

    Therefore $f=\max(E)$.  
    """))

    mo.md(
        r"""
        *Proof*:  The base-case for induction, is any nonempty set $C\subseteq X$ such that $|C|=1$, is the case that $C$ is a singleton set $C=\{d\}$.

        In this case, trivially, $d = \max(C)$.

        Now assume that the theorem is true for any nonempty $C\subseteq X$ such that $|C|=n$, where $n\ge 1$.

        Consider any nonempty $E\subseteq X$ such that $|E|=n+1$.  Let $f\in E$.

        Define $E' = E\smallsetminus \{f\}$, so that therefore $|E'|=n$.  

        By the inductive hypothesis, let $\alpha=\max(E')$.  

        There are now two cases, since $\preceq$ is a total order.  
        """
        + f"""
        {_alpha}

        {_f}
        """
        +r"""
    Therefore in all cases, $\max(E)$ exists, concluding the proof of the inductive case, and therefore concluding the inductive proof.

        $\Box$
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    `Inf left eq sup`

    ---

    $$ \inf(A)\preceq \sup(A) $$
    """), "danger")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        *Proof*: Let $x\in A$ so that $\inf(A)\preceq x\preceq \sup(A)$.

        $\Box$
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    `Subset sup inequality`

    ---

    If $A\subseteq B$ then

    $$ \sup(A)\preceq \sup(B) $$
    """), "danger")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        *Proof*: Since $\sup(A)=\min(UB_A)$, then we only need to show that $\sup(B)\in UB_A$.

        Let $x\in A$ so therefore $x\in B$, and so $x\preceq \sup(B)$.  

        This shows $\sup(B)\in UB_A$.

        $\Box$
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# 0006 Function Bounds""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Let $A,B,C$ be any nonempty sets.  Let $f,g:A\to B$ and let $h:A\times B\to C$.

    We denote the **image of $f$** by $\text{Im}(f)$, which is 

    $$ \text{Im(f)} = \{f(c): c\in A\} $$ 

    If $c\in A$ then we define the **partial function of $h$ fixing $a$ at $c$** to be the function $h_{(c,\cdot)}:B\to C$.

    If $d\in B$ then we define the **partial function of $h$ fixing $b$ at $d$** to be the function $h_{(c,\cdot)}:A\to C$.
    """), "success")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Let $(X,\preceq)$ be a poset and $A,B$ any nonempty sets.  Let $f,g:A\to X$ and $h:A\times B\to X$.  

    We say that $\alpha\in X$ is an **upper bound for $f$** if $\alpha$ is an upper bound for $\text{Im}(f)$.  The **maximum of $f$** is the maximum of $\text{Im}(f)$.  The **supremum of $f$** is the supremum of $\text{Im}(f)$.

    We say that $f\preceq g$ if $f(c)\preceq g(c)$ for every $c\in A$. 

    Let $B'$ be the set of points $d\in B$ such that $\sup(\{f(c,d):c\in A\})$ exists.  We define the **supremum of $f$ over $A$** to be the function $\sup_{a\in A}f_{(a,\cdot)}:B'\to X$ given by 

    $$ \left(\sup_{a\in A}f_{(a,\cdot)}\right)(d) = \sup\left\{f(c,d): c\in A\right\},\quad \forall d\in B $$

    The **supremum of $f$ over $B$** is 

    $$ \left(\sup_{b\in B}f_{(\cdot,b)}\right)(c) = \sup\left\{f(c,d): d\in B\right\},\quad \forall c\in A $$

    defined for $c\in A$ where this supremum exists.

    We define 

    $$ \sup_{a\in A}\sup_{b\in B} f = \sup_{a\in A}\left(\sup_{b\in B}f_{(\cdot,b)}\right) $$

    and 

    $$ \sup_{b\in B}\sup_{a\in A} f = \sup_{b\in B}\left(\sup_{a\in A}f_{(a,\cdot)}\right) $$

    There are corresponding definitions of **bounded below**, **minimum**, and **infimum**.

    """),"success")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        In all that follows, let $(X,\preceq)$ be a poset, and $A,B$ any nonempty sets. 

        Let $f,g:A\to X$ and let $h:A\times B\to X$.

        For each theorem below, there is a natural dual theorem for infima.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    `Sup function bounds`

    ---

    Suppose $f\preceq g$.  Then 

    $$ \sup f\preceq \sup g $$
    """), "danger")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        *Proof*:  Let $c\in A$ so that $f(c)\preceq g(c)\preceq \sup(g)$.

        Then $\sup g\in UB_{\text{Im}(f)}$.

        $\Box$
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Suppose that $h$ is bounded above by $\alpha\in X$.  Then for each $c\in A$ we have that $h_{(c,\cdot)}$ is bounded above by $\alpha$. 
    """), "danger")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        *Proof*:  Let $d\in B$.  Then 

        $$h_{(c,\cdot)}(d) = h(c,d) \preceq \alpha $$

        $\Box$
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Assuming that all suprema involved in the expressions exist, 

    $$ \sup_{a\in A}\sup_{b\in B}h = \sup_{b\in B}\sup_{a\in A}h $$
    """), "danger")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        *Proof*:  Fix $c\in A$.  

        Then for all $d\in D$ we have $h_{(c,\cdot)}(d) \preceq \sup(h_{(c,\cdot)})$.

        Note that the left-hand side is the same as $h_{(\cdot,d)}(c)$.

        Also the right-hand side, because the supremum is taken over the second coordinate, is the same as $\left(\sup_{b\in B}h_{(\cdot,b)}\right)(c)$.  We therefore have

        $$ h_{(\cdot,d)}(c) \preceq \left(\sup_{b\in B}h_{(\cdot,b)}\right)(c) $$

        The order of choice can be reversed (because both quantifiers are universal).  So if we first fix any $d\in D$, the above inequality holds for all $c\in A$.

        Then the inequality $h_{(\cdot,d)}(c)\preceq \left(\sup_{b\in B} h_{(\cdot,b)}\right)(c)$ then demonstrates the inequality of functions, 

        $$ h_{(\cdot,d)} \preceq \sup_{b\in B} h_{(\cdot, b)} $$

        By the theorem `Sup function bounds`, this implies

        $$ \sup(h_{(\cdot,d)}) \preceq \sup\left(\sup_{b\in B} h_{(\cdot,b)} \right)$$

        The right-hand side is just $\sup_{a\in A}\sup_{b\in B} h$.  

        We can now view $\sup(h_{(\cdot,d)})$ as a function of $d$, which is the function $\sup_{a\in A}h_{(a,\cdot)}$.  Due to the inequality above, therefore, $\sup_{a\in A}\sup_{b\in B} h$ is an upper bound on this function.

        Therefore 

        $$ \sup_{b\in B}\sup_{a\in A}h \preceq \sup_{a\in A}\sup_{b\in B}h $$

        The reverse inequality is proved, *mutatis mutandis* the same.  One only exchanges choices made for $A$ with choices made for $B$ along the way.

        $\Box$
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# 0007 Ordered Fields""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Let $(F,+,\times)$ be a field and $(F,\preceq)$ be a totally ordered set.

    For any $a\in F$ we define the **intervals**

    \begin{align*}
      (a,\infty) &= \{c\in F:a\prec c\}\\ 
      [a,\infty) &= \{c\in F:a \preceq c\}
    \end{align*}

    The interval $(a,\infty)$ is said to be **open on the left** and $[a,\infty)$ is **closed on the left**.  

    We similarly define, for each $a,b\in F$, the intervals 

    \begin{align*}
      &({-\infty},a)\\
      &({-\infty},a]\\
      &(a,b)\\
      &(a,b]\\
      &[a,b)\\
      &[a,b]
    \end{align*}

    We call $F^* = F\cup\{\infty,-\infty\}$ the **extended set of numbers**, where $\pm \infty$ are mere symbols.  

    If $a,b\in F^*$ we call $a$ and $b$ the **endpoints** of the interval $(a,b)$ and likewise for $(a,b]$ and $[a,b)$ and $[a,b]$.

    For $a,b\in F^*$, the intervals $(a,b)$ are always called an **open intervals**.  Intervals of the form $[a,b]$ for $a,b\in F$ are **closed intervals**, and so are $[a,\infty)$ and $(-\infty,a]$.  

    If $X\subseteq F$ then we define the **subset of positives**, $X^+=X\cap (0,\infty)$, the **subset of negatives**, $X^- = X\cap (-\infty,0)$, the **subset of nonnegatives**, $X^{\succeq 0}=X^+ \cup \{0\}$, and the **subset of nonpositives** $X^{\preceq 0} = X^-\cup\{0\}$.  

    We define the **positives** as $F^+$ and **negatives** as $F^-$.  

    We say that $\preceq$ is **compatible with addition** if 

    $$ a\preceq b \quad \Rightarrow \quad a+c\preceq b+c, \quad \forall a,b,c\in F $$

    We say that $\preceq$ is **compatible with multiplication** if 

    $$ a\preceq b \quad \Rightarrow \quad ac\preceq bc, \quad \forall a,b\in F, c\in F^{\succeq 0} $$

    We say that $\prec$ is **compatible with addition** if 

    $$ a\prec b \quad\Rightarrow\quad a+c\prec b+c, \quad \forall a,b,c\in F $$

    We say that $\prec$ is **compatible with multiplication** if 

    $$ a\prec b \quad \Rightarrow \quad ac\prec bc, \quad \forall a,b\in F, c\in F^+ $$

    If $\preceq$ is compatible with addition and multiplication, then we say that $(F,+,\times,\preceq)$ an **ordered field**.
    """), "success")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""In all that follows, assume that $(F,+,\times,\preceq)$ is an ordered field, and $X\subseteq F$ a nonempty subset.  """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    $0\prec 1$

    ---

    $0\prec 1$
    """), "danger")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        *Proof*:  Assume for contradiction that $1\preceq 0$.

        Then $0\preceq -1$.  Then by compatibility with multiplication, 

        $$ 0(-1)\preceq (-1)(-1) $$

        which simplifies to 

        $$ 0\preceq 1 $$

        By anti-symmetry, therefore $0=1$, contrary to the axioms of a field.

        Therefore $0\prec 1$.

        $\Box$
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    `Strict precidence compatibility`

    ---

    $\prec$ is compatible with addition and multiplication.  
    """), "danger")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        *Proof*:  Let $a,b\in F$ and $a\prec b$.

        Then $a\preceq b$ and $a\ne b$.

        To show compatibility with addition, assume $c\in F$.  Then $a+c\preceq b+c$ by compatibility with addition of $\preceq$.

        Assume for contradiction that $a+c=b+c$, which implies $a=b$.  

        Since this contradicts $a\ne b$ above, we must have $a+c\ne b+c$ and therefore $a+c\prec b+c$.

        This concludes the demonstration of compatibility with addition.

        Next to show compatibility with multiplication, assume $c\in F^+$.  Then $ac\preceq bc$.  

        For contradiction, assume $ac=bc$.  Since $c\ne 0$ it follows that $c^{-1}$ exists.  

        Therefore $a=b$, contrary to $a\ne b$ above.  

        So $ac\ne bc$ which shows $ac\prec bc$.

        $\Box$
        """
    )
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    `Integer power ordering`

    ---

    Let $a,b,c,d\in F$ such that $0\prec a, b$ and $0\prec c\prec 1\prec d$.  

    1. $a\preceq b$ if and only if $a^n\preceq b^n$ for all $n\in\Bbb N$.
    2. $a\preceq b$ if and onlly if $\frac 1 b \preceq \frac 1 a$.
    3. $0\prec c^2\prec c\prec 1\prec \frac 1 c$.
    4. $0\prec \frac 1 d\prec 1 \prec d\prec d^2$.
    """), "danger")
    return


@app.cell(hide_code=True)
def _(mo):
    _base_ltr = mo.callout(mo.md(r"""
    $(\Rightarrow)$: Assume $a\preceq b$.

    By compatibility with multiplication $a^2\preceq ab$ and $ab\preceq b^2$.

    By transitivity, $a^2\preceq b^2$.
    """))

    _base_rtl = mo.callout(mo.md(r"""
    $(\Leftarrow)$: For the contrapositive, assume $b\prec a$.  Then $b^2\prec ab$ and $ab\prec a^2$.

    By transitivity, $b^2\prec a^2$.
    """))

    _base = mo.callout(mo.md(f""" *Base-case $n=2$*:



    {_base_ltr}

    {_base_rtl}
    """))

    _ind_ltr = mo.callout(mo.md(r"""

    """))

    mo.md(
        r"""
        *Proof*:  (1.) This is trivially true for $n=1$.  

        """+f"""
        {_base}


        """
    )
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
