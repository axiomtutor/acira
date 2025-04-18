import marimo

__generated_with = "0.12.9"
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

        ## Unit 2: Sequences and Series

        by Axiom Tutor
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Lesson 0010: Sequences""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Let $m\in\Bbb R$ and $X$ a nonempty set.  Then

    $$ \Bbb N^{\ge m} = \{y\in \Bbb N: m\le y\} $$

    Let $a:\Bbb N^{\ge m}\to X$ be a function.  Then we call this a **sequence of $X$ (starting at $m$)**.  We typically write this function as $(a_k)_{k=m}$ or if $m$ is understood from context, then just $(a_k)$.  

    If $n\in\Bbb N^{\ge m}$ then we write the image of $n$ under $(a_k)$ is $a(n)$.  We call this a **term** of the sequence, and typically write this as 

    $$ a_n $$

    If $(i_k)_{k=n}$ is a strictly increasing sequence $i:\Bbb N^{\ge n}\to \Bbb N^{\ge m}$, then the composition $a\circ k$ is written 

    $$ a\circ k = (a_{i_k})_{k=n} $$

    and is called a **subsequence of $(a_k)$**.  

    If $(b_k)_{k=p}$ is another sequence, and $f(x,y):\Bbb R^2\to\Bbb R$, then we define $f((a_k),(b_k))$ to be the sequence $(c_k)_{k=\max\{m,p\}}$ given by the formula $c_k = f(a_k,b_k)$.  

    In particular, this implies $(a_k)+(b_k)$ is the sequence starting at $\max\{m,p\}$ given by $a_k+b_k$.  

    Similarly, for any $\lambda\in\Bbb R$ this defines $\lambda(a_k)$ and $(a_k)(b_k)$ and more.
    """), "success")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    We define new symbols $\infty,-\infty$ to extend the set $\Bbb R^{\ast} = \Bbb R\cup \{-\infty,\infty\}$, called the **extended real numbers**.  

    We also extend the ordering by, $\forall x\in\Bbb R^\ast$ 

    $$ -\infty\le x \le \infty $$

    We extend the function $+$ by, $\forall y\in \Bbb R$,

    $$y+\infty=\infty, \quad y-\infty = -\infty, \quad \infty+\infty=\infty,\quad -\infty-\infty = -\infty$$

    If $0<y$ then we extend $\times$ (or equivalently, $\cdot$) by

    $$y\cdot \infty = -y\cdot-\infty = \infty, \quad y\cdot -\infty = -y\cdot\infty= -\infty$$

    and 

    $$ \infty\cdot\infty, \quad \infty \cdot -\infty = -\infty, \quad -\infty\cdot-\infty = \infty $$

    $+$ is left undefined for $\infty-\infty$.  $\times$ is left undefined for $\infty\cdot 0$ and $0\cdot \infty$.  There are no additive or multiplicative inverse elements $\infty$ or $-\infty$.
    """), "success")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Let $a,b\in\Bbb R$ then we define the **absolute value of $a$** by 

    $$ |a| = \begin{cases}
      a & \text{ if } 0\le a\\
      -a & \text{ if } a<0
    \end{cases}$$

    We define the **distance between $a$ and $b$** by $|a-b|$.

    Let $\varepsilon\in\Bbb R^+$.  We say that **$a$ is within $\varepsilon$ of $b$** if the distance between $a$ and $b$ is less than $\varepsilon$. 

    Let $L\in\Bbb R$.  If $(a_k)_{k=m}$ is a sequence of real numbers, we say that **$(a_k)_{k=m}$ is within $\varepsilon$ of $L$** if every term is within $\varepsilon$ of $L$.  

    We say that $(a_k)_{k=m}$ is **eventually within $\varepsilon$ of $L$** if some tail is within $\varepsilon$ of $L$.

    We say that the **limit of $(a_k)_{k=m}$ is $L$** if, for every $\varepsilon\in\Bbb R^+$, the sequence $(a_k)_{k=m}$ is eventually within $\varepsilon$ of $L$.  When this holds, we write 

    $$\lim_{k\to\infty} a_k = L$$

    If the sequence $(a_k)$ has some limit then we say that $(a_k)$ **converges**.

    We define the closed interval $[\inf((a_k)_{k=m}, \sup((a_k)_{k=m})]$ as the **snug cell** of $(a_k)$.  Here $\inf((a_k)_{k=m}),\sup((a_k)_{k=m})\in\Bbb R^*$.  

    If $[\alpha,\beta]$ is the snug cell of the tail $(a_k)_{k=p}$, we write $\text{snug}(a_k)_{k=p} = [\alpha,\beta]$.

    If for every $M\in\Bbb R$, we have that some tail of $(a_k)$ is bounded below by $M$, then we say that $\lim_{k\to\infty}a_k = \infty$.  If for every $M$ some tail is bounded below by $M$, then we say that $\lim_{k\to\infty} a_k = -\infty$.

    """), "success")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        In all that follows, let $(a_k)_{k=m}, (b_k)_{k=n}$ be sequences of real numbers, and $L\in\Bbb R$.

        For each $m\le p$, let $\text{snug}(a_k)_{k=p} = [\alpha_p,\beta_p]$.  For each $n\le p$ let $\text{snug}(b_k)_{k=p} = [\gamma_p,\delta_p]$.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    `Limit by snug cell`

    ---

    $(a_k)$ converges if and only if $\bigcap_{k=m}^\infty [\alpha_k,\beta_k]$ is a singleton.

    Moreover $\lim_{k\to\infty}a_k = L$ if and only if $\bigcap_{k=m}^\infty [\alpha_p,\beta_p] = \{ L \}$.
    """), "danger")
    return


@app.cell(hide_code=True)
def _(mo):
    _lincap = mo.callout(mo.md(r"""
    Assume for contradiction that $L\notin \bigcap_{k=m}^\infty [\alpha_k,\beta_k]$, and let $[\alpha_q,\beta_q]$ be the first snug cell such that $L\notin [\alpha_q,\beta_q]$.  

    Consider the case that $L < \alpha_q = \inf((a_k)_{k=q})$.  

    Let $\varepsilon = \frac{\alpha_p-L}2$ and then let $(a_k)_{k=r}$ be the tail within $\varepsilon$ of $L$.  

    Set $N = \max\{q,r\}$.  For any $N\le k$ we have $a_k$ is within $\varepsilon$ of $L$ but also $a_k\in [\alpha_N,\beta_N]$.

    But since $L+\varepsilon < \alpha$ it follows that 

    $$(L-\varepsilon,L+\varepsilon)\cap [\alpha_N,\beta_N] = \emptyset$$

    Then we have $a_k\in (L-\varepsilon,L+\varepsilon)\cap [\alpha_N,\beta_N] = \emptyset$, which is a contradiction.

    The case for $\beta_q < L$ is similar.

    This shows $L\in\bigcap_{k=m}[\alpha_k,\beta_k]$.
    """))

    _onlyl = mo.callout(mo.md(r"""
    Assume $x<L$ and let $\varepsilon = \frac{L-x}2$.  Then let $(a_k)_{k=q}$ be the tail within $\varepsilon$ of $L$.  

    Since $x < L-\varepsilon$ we have

    $$x<L-\varepsilon \le \alpha_q$$ 

    and therefore $x\notin [\alpha_q,\beta_q]$.  Then 

    $$x\notin\bigcap_{k=m}^\infty [\alpha_k,\beta_k]$$

    The case $L < x$ is similar.
    """))

    mo.md(
        r"""
        *Proof*:  Let $\lim_{k\to\infty} a_k = L$.  

        Then $L\in\bigcap_{k=m}^\infty [\alpha_k,\beta_k]$, proof below.
        """ + f"{_lincap}" + r"""
        Also, if $x\ne L$ then $x\notin \bigcap_{k=m}^\infty [\alpha_k,\beta_k]$.  Proof below.
        """ + f"{_onlyl}" + r"""

        The above shows that $\bigcap_{k=m}^\infty [\alpha_k,\beta_k] = \{L\}$.

        Next we show the converse, so assume that $\bigcap_{k=m}^\infty [\alpha_k,\beta_k] = \{x\}$.  Let $\varepsilon \in\Bbb R^+$.  

        Let $(a_k)_{k=q}$ be the first tail such that $[\alpha_q,\beta_q]\subseteq (L-\varepsilon,L+\varepsilon)$.  Then the tail $(a_k)_{k=q}$ is within $\varepsilon$ of $x$ and therefore $x=\lim_{k\to\infty}a_k$.  

        $\Box$"""
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    `Limits are unique`

    ---

    Let $\lim_{k\to\infty}a_k = L\in\Bbb R$.  Then $L$ is the unique limit of $(a_k)$.  
    """), "danger")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        *Proof*:  By the previous theorem, if $L = \lim_{k\to\infty}a_k$ then $\bigcap_{k=m}^\infty [\alpha_k,\beta_k] = \{L\}$ is a singleton set.  

        Therefore if we have any limit $\lim_{k\to\infty}a_k=M$, then $\{M\}=\{L\}$ and so $L=M$.

        $\Box$
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    `Indepent of initial terms`

    ---

    Let $(a_k)_{k=p}$ be any tail of $(a_k)_{k=m}$.  Then $(a_k)_{k=m}$ converges if and only if $(a_k)_{k=p}$ does.  

    If the limit of $(a_k)_{k=m}$ is $L$ then it is also the limit of $(a_k)_{k=p}$.
    """), "danger")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        *Proof*:  Note that, for each $m\le p$, by the `Subset sup inequality`, $\alpha_m\le \alpha_p$ and also $\beta_p\le \beta_m$.  

        Therefore $[\alpha_p,\beta_p]\subseteq [\alpha_m,\alpha_p]$ and therefore 

        $$ \bigcap_{k=m}[\alpha_k,\beta_k] = \bigcap_{k=p}[\alpha_k,\beta_k] $$

        The theorem's claim now follows by the `Limit by snug cell` theorem.

        $\Box$
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Lesson 0011: Monotonicity and Subsequences""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Let $(X,\preceq_X), (Y,\preceq_Y)$ be any two posets, and $f:X\to Y$ a function.  We say that $f$ is a **monotonically increasing function** if 

    $$ \forall x,y\in\Bbb X, \quad x \preceq_X y \Rightarrow f(x)\preceq_Y f(y) $$

    We say that $f$ is **strictly increasing** if 

    $$ \forall x,y\in\Bbb X,\quad x\prec_X y \Rightarrow f(x) \prec_Y f(y) $$

    Similarly we define $f$ to be **monotonically decreasing** if $f(x) \succeq_Y f(y)$, and we define $f$ to be **strictly decreasing** if $f(x)\succ_Y f(y)$, for all $x\prec_X y$.  

    We say that $f$ is **monotonic** if it is either monotonically increasing or decreasing.

    Sequences are functions defined on a subset of $\Bbb R$ with values in $\Bbb R$.  Therefore, the above also defines **monotonically decreasing / increasing sequences**, and **strictly decreasing / increasing sequences**.  

    Let $(a_k)_{k=m}$ be a sequence of real numbers, and let the snug cell of the tail $(a_k)_{k=p}$ be the interval $[\alpha_p,\beta_p]$.  Then we define the **limit inferior of $(a_k)$** to be $\lim_{k\to\infty}\alpha_k\in\Bbb R^*$.  To denote this we write 

    $$ \lim_{k\to\infty} \alpha_k = \liminf_{k\to\infty} a_k $$

    We define the **limit superior of $(a_k)$** to be $\lim_{k\to\infty} \beta_k\in\Bbb R^*$ and denote it

    $$\lim_{k\to\infty} \beta_k = \limsup_{k\to\infty} a_k $$
    """), "success")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""In all that follows, let $(a_k)_{k=m}$ be a sequence of real numbers.  Let the snug cell of $(a_k)_{k=p}$ be $[\alpha_p,\beta_p]$.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    `Sequence monotonicity equivalence`

    ---

    $(a_k)$ is monotonically decreasing if and only if $a_{p} \ge a_{p+1}$ for every $k\le p$.  

    A similar fact gives an equivalent for $(a_k)$ being strictly decreasing, or monotonically increasing, or strictly increasing.
    """), "danger")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        *Proof*:  Suppose $(a_k)$ is monotonically decreasing and $m\le p$.  Then since $p\le p+1$, it follows immediately that $a_p\ge a_{p+1}$.

        Now suppose that $a_p\ge a_{p+1}$ for every $m\le p$.  Let $p\le q$.  Then since 

        $$ p\le p+1\le p+2 \le \cdots\le q$$

        then

        $$ a_p \ge a_{p+1} \ge \cdots \ge a_q $$

        So $a_p\ge a_q$ and therefore $(a_k)$ is monotonically decreasing.

        $\Box$
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    `Snug ends monotonic`

    ---

    Consider the sequence of left end-points of the snug cells, $(\alpha_k)_{k=m}$.  This is a monotonically increasing sequence.

    Also $(\beta_k)_{k=m}$ is a monotonically decreasing sequence.
    """), "danger")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        *Proof*: If $m\le p\le q$ then $\text{Im}(a_k)_{k=p}\supseteq \text{Im}(a_k)_{k=q}$.  Therefore by the `Subset sup` theorem, 

        $$\inf(a_k)_{k=p}=\alpha_p \le \inf(a_k)_{k=q} = \alpha_q$$

        Likewise for the rest of the theorem.

        $\Box$
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    `Bounded monotonic limits`

    ---

    Suppose that $(a_k)$ is bounded below and monotonically decreasing.  Then $\lim_{k\to\infty}a_k$ exists and equals $\inf(a_k)_{k=m}$. 

    Correspondingly if $(a_k)$ is bounded above and monotonically increasing then $\lim_{k\to\infty}a_k = \sup(a_k)_{k=m}$.  

    """), "danger")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        *Proof*: Since $(a_k)$ is bounded below, $\alpha=\inf(a_k)_{k=m}$ exists.

        Let $\varepsilon\in \Bbb R^+$.  By the equivalent characterization of the infimum, there is a point $a_p$ in the sequence such that 

        $$ \alpha \le a_p < \alpha+\varepsilon $$

        But moreover, since $(a_k)$ is decreasing, then for every $p\le q$ we also have $\alpha\le a_q\le \alpha+\varepsilon$.

        This shows that the tail $(a_k)_{k=p}$ is within $\varepsilon$ of $\alpha$, and therefore $\lim_{k\to\infty}a_k = \alpha$.

        The proof for an increasing sequence bounded above is likewise.

        $\Box$
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    `Limit equal to limsup`

    ---

    $(a_k)$ converges if and only if $\lim_{k\to\infty}\alpha_k = \lim_{k\to\infty}\beta_k$.  In this case, $\lim_{k\to\infty} a_k = \lim_{k\to\infty}\alpha_k$.
    """), "danger")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        *Proof*:  Suppose that $(a_k)$ converges and $\lim_{k\to\infty}a_k = L$.  

        $(\alpha_k)$ is a monotonically increasing sequence, by the `Snug ends monotonic` theorem.

        Also $(\alpha_k)$ is bounded above by $L$.  This follows from the fact that $\bigcap_{k=m}^\infty [\alpha_k,\beta_k] = \{L\}$, by the `Limit by snug cell` theorem.

        Therefore $\lim_{k\to\infty}\alpha_k$ exists by the `Bounded monotonic limits` theorem.  Moreover $\lim_{k\to\infty}\alpha_k\le L$.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Lesson 0012: Basic Limit Theorems""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    `Algebra of limits`

    ---

    Assume $\lim_{k\to\infty}a_k=A$ and $\lim_{k\to\infty}b_k = B$. Let $\lambda\in\Bbb R$.

    The following two equations are then jointly called the "linearity of limits".

    1. $\lim_{k\to\infty}(a_k+b_k) = A+B$
    2. $\lim_{k\to\infty}(\lambda a_k) = \lambda A$

    Moreover, 

    3. $\lim_{k\to\infty} a_kb_k = AB$
    4. If $b_k\ne 0$ for any $n\le k$ and if $B\ne 0$, then $\lim_{k\to\infty}\frac{a_k}{b_k}=\frac AB$.
    5. $\lim_{k\to\infty}|a_k| = |A|$
    """), "danger")
    return


@app.cell
def _(mo):
    _p1 = mo.callout(mo.md(r"""
    1. 
    """))

    mo.md(f"""*Proof*:  

    {_p1} """)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
