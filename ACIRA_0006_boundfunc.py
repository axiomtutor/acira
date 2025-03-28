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
    mo.md(r"""# Lesson 0006: Bounds of Functions""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""The most useful notion of a bound on a function, as we will see later in the course, is that the function's *values* stay bounded.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        For example, the function $f(x) = x$ is bounded if its domain is $[-1,1]$.  

        But it is unbounded if its domain is $\Bbb R$.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Also consider the function $g:\Bbb N\to \Bbb Q$ defined by 

        $$ g(n) = \frac 1n $$

        Intuitively, we understand that $\text{Im}(g) \subseteq (0,1]$.  

        Moreover, these bounds are "tight", in the sense that $1$ is the supremum of $g$ (in fact, its maximum!) and $0$ is its infimum (but not its minimum).
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Let $(X,\preceq)$ be a poset and $A$ any nonempty set.  Let $f: A\to X$ be a function.

    Define the **image of $f$** by 

    $$\text{Im}(f) = \{f(b): b\in A\} $$

    For $\alpha\in X$ we say that **$\alpha$ is an upper bound of $f$** if $\alpha\in UB_{\text{Im}(f)}$.  We say that **$\alpha$ is a lower bound of $f$** if $\alpha\in LB_{\text{Im}(f)}$.  We say that $f$ is a **bounded function** if $\text{Im}(f)$ is a bounded set.

    If $\alpha=\max(\text{Im}(f))$ we say that $\alpha$ is the **maximum of $f$**.  If $\alpha=\min(\text{Im}(f))$ we say that $\alpha$ is the **minimum of $f$**.

    If $\alpha = \sup(\text{Im}(f))$ exists, we say that the **supremum of $f$** is $\alpha$.  In this case, we write $\sup(f) = \alpha$.  If $\alpha=\inf(\text{Im}(f))$ exists, we say that the **infimum of $f$** is $\alpha$.  In this case, we write $\inf(f)=\alpha$.  
    """), kind="success")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""In short, the definitions above, all amount to: Apply the usual ideas of bounds, to $\text{Im}(f)$.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        There is a similar trend when writing inequalities regarding two functions.  We say that $f\preceq g$ if and only if their images stand in the same order, $f(x)\preceq g(x)$, everywhere in their shared domain. 

        The rigorous statement of this is below.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Let $(X,\preceq)$ be a poset and $A$ a nonempty set.  Let $f,g:A\to X$ be two functions.

    We define $f\preceq g$ to hold if 

    $$ f(a)\preceq g(a), \quad \forall a\in A $$
    """), kind="success")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Next we define some notions for functions of two variables.  

        The first few notions define what it means to "keep one variable fixed".
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Let $A,B,C$ be any three nonempty sets.  Let $f:A\times B\to C$ a function.  

    If $a'\in A$ we define the function $f_{(a',\cdot)}: B\to X$ by 

    $$ f_{(a',\cdot)}(b) = f(a',b), \quad \forall b \in B $$

    We call $f_{(a',\cdot)}$ the **partial function, $f$ applied to $a'$**. 

    Note that dot is in the coordinate of the variable, and $a'$ is "fixed".

    If $b'\in B$ we define $f_{(\cdot,b')}:A\to X$ by

    $$ f_{(\cdot,b')}(a) = f(a,b'), \quad \forall a\in A $$

    which is the **partial function, $f$ applied to $b''$**.  
    """), kind="success")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Next we discuss what it means to keep a variable fixed, and take the supremum over the other variable.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Let $(Z,\preceq)$ be a poset, and $A,B$ two nonemtpy sets.  Let $f:A\times B\to Z$ be a function.

    In what follows, if we assume that all suprema exist, then we define the **supremum of $f$ over $A$** to be the *function* $\sup_{a\in A} f_{(a,.)}:B\to Z$.  It is given by the equation 

    $$ \left(\sup_{a\in A} f_{(a,.)}\right)(b) = \sup(f_{(.,b)}), \quad \forall b\in B $$

    The **supremum of $f$ over $B$** is 

    $$ \left(\sup_{b\in B}f_{(.,b)}\right)(a) = \sup(f_{(a,.)}), \quad \forall a\in A $$

    Again the dot indicates which coordinate is allowed to vary.  The letter, $a$ or $b$, indicates which coordinate the sup "ranges over".
    """), kind="success")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        It may help to understand this intuitively.  

        The function $\sup_{a\in A}f_{(a,.)}$ is a function of $B$.  For an argument $b\in B$, its image is computed by:  

        * "fixing" $b$, which is to say, forming $f$ applied to $b$, and then
        * taking the supremum over all possibilities for $a\in A$.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        It is also worth appreciating that it is possible for $\sup_{a\in A} f_{(a,.)}$ to exist for some arguments $b\in B$ but not for others.  

        For example, consider $f(a,b) = \frac{a}b$ for $a,b\in\Bbb Q$ and $b\ne 0$.  

        The function $\sup_{y\in \Bbb Q} f_{(.,y)}$ exists for the argument $a=0$.  That is because the image of $\sup_{y\in\Bbb Q}f_{(.,y)}$ is just the set $\{0\}$, which has supremum equal to 0.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        However, for any other argument, $\sup_{y\in\Bbb Q}f_{(.,y)}$ does not exist.  Let us just consider the argument $a=1$, for concreteness.  

        The function $f_{(1,\cdot)}:\Bbb Q\smallsetminus \{0\} \to \Bbb Q$ is given by 

        $$ f_{(1,\cdot)}(y) = \frac 1 y $$

        Therefore we know that $\text{Im}(f_{(1,\cdot)})$ is unbounded above.  So $\sup(f_{(1,\cdot)})$ does not exist.

        Therefore $\sup_{y\in \Bbb Q}f_{(.,y)}$ does not exist for argument $a=1$.  Equivalently, we may say: $\left(\sup_{y\in\Bbb Q} f_{(.,y)}\right)(1)$ is undefined.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Having now established all of the above, we are in a position to define stacked suprema and infima of functions.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Let $(X,\preceq)$ be a poset and $A,B$ two nonempty sets.  Let $f:A\times B\to X$ be a function.

    If all of the suprema and infima involved exist, we define

    \begin{align*}
    \sup_{a\in A}\sup_{b\in B} f &= \sup_{a\in A}\left(\sup_{b\in B} f_{(.,b)}\right) 
    \end{align*}

    and in a similar, obvious fashion, define each of 

    $$\sup_{b\in B}\sup_{a\in A}f,\quad \inf_{a\in A}\inf_{b\in B}f,\quad  \inf_{b\in B}\inf_{a\in A}f$$ 

    """), kind="success")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Exercise 1""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Give an example function $f:A\to \Bbb Q$ where $A$ is a bounded set, but $f$ is unbounded.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Exercise 2""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Let $(X,\preceq)$ be a poset and $A$ a nonempty set.  Let $f,g:A \to X$ be two function, for which $\sup(f)$ and $\sup(g)$ both exist.

        Show that if $f\preceq g$ then $\sup f\preceq \sup g$.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Exercise 3""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Let $(X,\preceq)$ be a poset, $A, B$ two nonempty sets, and $f:A\times B\to X$ a function.  Also let $a\in A$.  

        Show that if $f$ is bounded, then so is $f_{(a,\cdot)}$.

        Note: You might think that we have not defined what it means for a two-variable function to be "bounded"!  But we have!  The definitions given above, in fact, are sufficient for each of the terms here to be well-defined.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Exercise 4""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Let $(X,\preceq)$ be a poset, $A,B$ two nonempty sets, $f:A\times B\to X$ a function.  

        Show that, if the suprema exist,

        $$ \sup_{a\in A}\sup_{b\in B} f = \sup_{b\in B}\sup_{a\in A} f $$
        """
    )
    return


if __name__ == "__main__":
    app.run()
