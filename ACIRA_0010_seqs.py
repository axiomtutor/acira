import marimo

__generated_with = "0.12.0"
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
        ## Unit 2: Sequences and Series
        ### Chapter 2: Sequences
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Lesson 0010: Sequences of Real Numbers""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        We are working toward discussing the derivative and integral, among other things.

        One of the most important and fundamental objects that will help us to define and understand both of these, is sequences of real numbers.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## An Intuitive Connection to the Derivative and Integral""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Recall from calculus: If $f:\Bbb R\to\Bbb R$ is a function and $a\in\Bbb R$, then the derivative of $f$ at $a$ is approximated by, say, 

        $$\frac{f(a+1)-f(a)}{(a+1)-a}$$

        (Let's ignore issues about whether this derivative exists.)
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Then a better estimate is, say, 

        $$\frac{f(a+0.1)-f(a)}{(a+0.1)-a}$$

        and then a better one is

        $$ \frac{f(a+0.01)-f(a)}{(a+0.01)-a} $$

        and so on.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        As this sequence goes on, its limit approaches $f'(a)$.

        This isn't the only way to capture the notion of the derivative of a function, but it at least shows a connection between sequences and derivatives.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        The connection between sequences and integrals is probably even more familiar.  

        To compute the definite integral, $\int_a^b f \ dx$, we start by subdividing the interval $[a,b]$ into $n$ equal pieces.  Then we find approximating Riemann rectangles for each piece, and sum the rectangle areas.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        This produces the "$n$th estimate" of the definite integral.  We can find its value for $n=2$ and then $n=3$, and so on.  

        As the sequence progresses, the rectangle areas approach $\int_a^b f\ dx$.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Sequence Definitions and Notation""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Below is the technical definition of a sequence of real numbers, as a function with domain a certain subset of $\Bbb N$.  More about this later.

        This definition is technically correct, although it is often confusing for a student who's not used to the idea.  It's also not very important for the ways that we typically work with sequences.

        Therefore if you conceive of a sequence in a more intuitive and less rigorous way, as just "a number, then another, then another, and so on", that's good enough for most of our needs.  The technical definition is included here, only for the sake of completeness.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Let $X$ be any nonempty set.  Let $m\in\Bbb N$ and define $\Bbb N^{\ge m} = \{k:m\le k\}$.  

    Any function $a:\Bbb N^{\ge m}\to X$ is called a **sequence of $X$ (starting at $m$)**. 

    Typically we give this special notation.  The sequence is often written as $(a_k)_{k=m}$.  If $m$ is already understood from context then we may just write $(a_k)$ to refer to the sequence.  The sequence's image of $n\in \Bbb N^{\ge m}$ is typically written $a_n$.  

    For a sequence $(a_k)_{k=m}$, starting at $m$, and for any $n\ge m$, we define the **$n$th tail of $(a_k)$** to be $(a_k)$ restricted to $\Bbb N^{\ge n}$.  We write this as $(a_k)_{k=n}$.

    Suppose $n\in\Bbb N$ and $(i_k)_{k=m}$ is an increasing sequence of $\Bbb N^{\ge n}$.  Then if $(a_k)_{k=m}$ is a sequence of $X$ starting at $n$, the composition 

    $$ a\circ i : \Bbb N^{\ge m} \to X $$

    is a **subsequence of $(a_k)$**.  It is written as $(a_{i_k})_{\ge m}$.



    """), "success")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Consider the intuitively presented sequence $1^2, 2^2, 3^2, ...$ which is the same as $1, 4, 9, ...$.  

        This is given formally as $(a_k)_{k=1} = k^2$.  

        To give a demonstration of a random image, the image of $10$ is $a_{10} = 10^2 = 100$.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""The sequence $\frac 1 5, \frac 1 6, \frac 1 7,\dots$ is formally $(b_k)_{k=5}=\frac 1 k$.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        $(a_k)$ is an increasing sequence.  

        But we still cannot use it to form a subsequence of $(b_k)$.  The reason is that $(b_k)$ starts at 5, but $(a_k)$ is a function of $\Bbb N^{\ge 1}$.  

        However, we can take the 3rd tail, $(a_k)_{k=3}$.  Then this has codomain $\Bbb N^{\ge 9}$, and we can therefore use this to form a subsequence of $(b_k)$.  

        It is $(b_{a_k})_{k=3}$.  Note that $a_3=9$ and $a_4 = 16$ and so on.  Therefore the first few terms of $(b_{i_k})$ are

        \begin{align*}
        b_{a_3} &= b_9 = \frac 1 9\\
        b_{a_4} &= b_{16} = \frac 1 {16}\\
        b_{a_5} &= \frac{1}{25} \\
        &\vdots
        \end{align*}
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Convergence of Sequences""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        The main thing that we are interested in for any sequence, is its convergence to some particular value.  

        As we noted previously, this helps us to discuss the concept of the derivative and integral, among other things.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Let $x,y\in \Bbb R$ be any two real numbers.  We define the **absolute value of $x$** by 

    $$ |a|=\begin{cases}
      x & \text{ if } 0\le x\\
      -x & \text{ if } x < 0 
    \end{cases}$$

    We define the **distance between $x$ and $y$** by $|x-y|$.  

    For a given $\varepsilon\in\Bbb R^+$, we say that $x$ is **within $\varepsilon$ of $y$** if the distance between them is less than $\varepsilon$.  That is to say, $x$ is within $\varepsilon$ of $y$ if 

    $$ |x-y|<\varepsilon $$

    Let $(a_k)_{m=k}$ be a sequence of real numbers, and $L\in\Bbb R$.  

    For any $\varepsilon\in\Bbb R^+$ we say that $(a_k)_{k=m}$ is **within $\varepsilon$ of $L$** if each term is within $\varepsilon$ of $L$.  

    We say that $(a_k)_{k=m}$ is **eventually within $\varepsilon$ of $L$** if there is some tail which is within $\varepsilon$ of $L$.  That is to say, $(a_k)_{k=m}$ is eventually within $\varepsilon$ of $L$ if $\exists N\in\Bbb N$ such that $(a_k)_{k=N}$ is within $\varepsilon$ of $L$.  

    We say that $L$ is the **limit of $(a_k)$** if, for every $\varepsilon\in\Bbb R^+$, the sequence is eventually within $\varepsilon$ of $L$.  In this case we write 

    $$ \lim_{n\to\infty} a_n = L $$

    If the limit of $(a_k)_{k=m}$ exists, we say that $(a_k)_{k=m}$ **converges**.  

    """), "success")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Let's see an example of a sequence which has a limit.  Perhaps one of the simplest examples, which is still very useful, is the sequence given by $a_k=\frac 1 k$.  

        I claim that this sequence has limit equal to 0.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        To see this, we need to let $\varepsilon\in\Bbb R^+$ be any positive real number, and show that $(a_k)$ is eventually within $\varepsilon$ of 0.  

        To show that, we need to find an $N\in\Bbb N$ such that the $N$th tail is within $\varepsilon$ of $L$.  

        To show that, we need $|a_k-0|<\varepsilon$ for all $N\le k$.  (Keep in mind that the missing puzzle piece here is $N$.)
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        This is equivalent to finding $N\in\Bbb N$ such that $\forall k\ge N$ we have $\frac 1 k<\varepsilon$.  

        The existence of such a $k$, for any choice of $\varepsilon$, is precisely guaranteed to exist by the `1/n approaches 0` theorem.  

        This therefore tells us that $N$ exists, which ensures that $(a_k)$ is eventually within $\varepsilon$ of 0.  

        Since $\varepsilon\in\Bbb R^+$ was chosen arbitrarily, this concludes the proof that $\lim_{k\to\infty} \frac 1 k = 0$.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Let's next see an exmaple sequence with no limit.  Let's consider the sequence given by $a_k=k$.  

        Let's show that the limit of $a_k$ is not 1.  I am choosing 1 arbitrarily for demonstration purposes.  It will be an exercise for the reader, at the end of this notebook, to prove that $L$ is not the limit of $(a_k)$ for any $L\in\Bbb R$.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        To show that 1 is not the limit of $(a_k)$, we can specifically show that no tail of $(a_k)$ is within $\varepsilon=1$ of $L=1$.

        To prove this claim let $N\in\Bbb N$.  Any such tail contains a term $a_k$ with $2\le k$.  

        Then $a_k = k \ge 2$, and therefore 

        $$|a_k-1| = k-1 \ge 2-1 = 1$$
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        The above therefore shows that the $N$th tail of $(a_k)$ is not within 1, of 1.  

        Since an $\varepsilon\in\Bbb R^+$ exists such that $(a_k)$ is not within $\varepsilon$ of 1, then $L$ does not satisfy the definition of the limit of $(a_k)$.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Limits by Snug Cells""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        The above definitions are the "standard" definitions for the limit of a sequence, for the most part.  

        However, in my experience, these definitions often confuse a new student.  It can be hard to draw motivating and intuitive pictures to illustrate these ideas.

        While many mathematicians will scoff at the idea of trying to make mathematics more intuitive and easier for a student to learn, I think building intuitions is an important part of becoming a mathematician.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        There is an equivalent characterization of limits, which we will develop below, in terms of "snug containers" -- a term I have coined for this purpose.

        I hope that it is easier to understand "what is going on here", and that pictures and metaphors may be more motivating.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Let $(a_k)_{k=m}$ be a sequence of real numbers.  Let $I_m$ be the closed interval with lower end-point $\inf((a_k)_{k=m})$ and upper end-point $\sup((a_k)_{k=m})$.  

    Then we call $I_m$ the **snug cell** of $(a_k)_{k=m}$.   
    """), "success")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        For example, the snug cell of $(1/k)_{k=1}$ is the interval $[0,1]$.  It is the "smallest" closed interval, such that the sequence stays inside the interval.

        The snug cell of $(1/k)_{k=2}$ is $[0,1/2]$.  In general the snug cell of $(1/k)_{k=m}$ is always $[0,1/m]$.

        For another example, the snug cell of $(k)_{k=1}$ is $[1,\infty)$, and the snug cell of $(k)_{k=2}$ is $[2,\infty]$.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    `Limit by snug cells`

    ---

    Let $(a_k)_{k=m}$ be a sequence of real numbers, and let $I_n$ be the snug cell of the tail $(a_k)_{k=n}$.  

    Then $(a_k)_{k=m}$ converges if and only if $\bigcap_{n=m}^\infty I_n$ is a singleton set.

    Also, $\lim_{n\to\infty} a_n = L$ if and only if $\bigcap_{n=m}^\infty I_n = \{ L \}$.

    """), "danger")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        *Proof*:  Suppose that $\lim_{n\to\infty} a_n = L$.  We need to show that $\bigcap_{n=m}^\infty I_n = \{L\}$, and we start by showing that $L\in\bigcap_{n=m}^\infty I_n$.  

        Let $m\le n$, and we will show that $L\in I_n$.  Let $I_n = [\alpha,\beta]$ and we have, by definition that $\alpha=\inf((a_k)_{k=n})$.

        Let us now focus on showing $\alpha\le L$.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Assume for contradiction that $L < \alpha$.  Then with $\varepsilon=\frac{\alpha-L}2$, we must have that there is a $m\le p$ such that the $p$th tail stays within $\varepsilon$ of $L$.  

        Set $q = \max\{n,p\}$, then we must have that the $q$th tail both stays above $\alpha$, but also stays within $\varepsilon$ of $L$.

        However, there are no points in the intersection $(L-\varepsilon,L+\varepsilon)\cap [\alpha,\infty) = \emptyset$.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Since the points of the $q$th tail are in $\emptyset$, this is a contradiction.  We must therefore have $\alpha\le L$.

        The proof that $L\le \beta$ is similar, and left as an exercise.  

        Therefore $L\in I_n$.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Next we show that if $x\ne L$ then $x\notin I_n$.  Assume $x < L$ to begin.

        Let $\varepsilon = \frac{L-x}2$, and let the $p$th tail be within $\varepsilon$ of $L$.  Then $I_p=[\alpha,\beta]$ must be such that $L-\varepsilon \le \alpha \le \beta\le L+\varepsilon$.  

        But since $x\notin (L-\varepsilon,L+\varepsilon)$ then $x\notin I_n$ and therefore $x\notin \bigcap_{n=m}^\infty I_n$.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        If $L < x$ the proof is nearly the same.  Therefore in general, if $x\ne L$ then $x\notin \bigcap_{I\in\mathcal G}I$.  

        This shows that $\bigcap_{I\in\mathcal G}I\subseteq \{L\}$.  With inclusion proved in both directions, we have shown $\bigcap_{I\in\mathcal G}I = \{L\}$.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        All that now remains for us to show, is that if $\bigcap_{n=m}^\infty I_n$ is the singleton $\{x\}$, then $\lim_{n\to\infty}a_n$ exists.  

        Let $\varepsilon\in\Bbb R^+$.  There must be a first $I_n$ such that $I_n\subseteq (x-\varepsilon,x+\varepsilon)$.  Let $I_n = [\alpha,\beta]$.

        Then for any $a_k$ in the $n$th tail, we must have $x-\varepsilon < \alpha\le a_k\le \beta < x+\varepsilon$.

        This shows $\lim_{n\to\infty} a_n = x$.

        $\Box$
        """
    )
    return


if __name__ == "__main__":
    app.run()
