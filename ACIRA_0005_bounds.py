import marimo

__generated_with = "0.11.26"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Lesson 0005: Bounds""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Throughout real analysis, bounds will be important. 

        To motivate this, consider the task of determining the limit of a sequence like 

        $$ a_n = \frac{\cos n}{n} $$

        From a previous calculus course, I assume the student intuits that we should expect 

        $$ \lim_{n\to\infty} a_n = 0 $$
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        But proving this directly, because of how complicated $\cos n$ can be with integer arguments, would be hard or even impossible.

        However, with bounds, it is rather easy!
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        We know that $-1\le \cos x \le 1$ for every $x\in \Bbb R$.  This acts as a bound on $\cos n$.  

        In particular, it implies 

        $$ \frac{-1}{n} \le \frac{\cos n}n \le \frac 1 n $$
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Reasoning intuitive (which we will make rigorous later), since $\frac {-1}n \to 0$ and since $\frac 1 n\to 0$, then therefore $\frac{\cos n}n \to 0$.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        The above motivation discusses the bounds on a function.

        There will be many kinds of bounds that we discuss in real analysis:  Bounds on a set, bounds on a sequence, bounds on functions, and bounds on sequences of functions.  

        The most fundamental concept is the bound on a set, so we begin there.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Let $(X,\preceq)$ be a poset.

    Let $A\subseteq X$ be a nonempty subset, and $\alpha\in X$.  We say that $\alpha$ is an **upper bound on $A$** if 

    $$ \forall b\in A, \quad b\preceq \alpha $$

    We say that $\alpha$ is a **lower bound on $A$** if 

    $$ \forall b\in A,\quad \alpha\preceq b $$

    We denote the set of all upper bounds on $A$ by the notation $UB_A$.

    $$ UB_A = \{\alpha\in X: \forall b\in A, \ b\preceq \alpha\} $$

    and the set of lower bounds $LB_A$ is 

    $$ LB_A = \{\alpha\in X: \forall b\in A \ \alpha\preceq b\} $$
    """), kind="success")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        An upper bound is a good way to "summarize" where a set is, using a single number.  

        However, there is a somewhat obvious deficiency.  For any given set, say of rational numbers, if an upper bound exists then infinitely many upper bounds exist.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Consider, for example, the set of all rational numbers between 1 and 2.

        The number 3 is an upper bound, but so is 4.  And so is 5.  And so is 6, and so on.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Clearly the "best" upper bound is the one nearest to the set.

        In the example of the interval $[1,2]$ taken in the rational numbers, the number 2 is the "best" upper bound.

        This is the maximum of the set $[1,2]$.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Let $(X,\preceq)$ be a poset, and $A\subseteq X$ a nonempty subset.  Let $\alpha\in X$.

    If $\alpha\in A \cap UB_A$ then $\alpha$ is the **maximum of $A$**.  

    In this case, we write 

    $$ \alpha = \max(A) $$

    If $\alpha\in A\cap LB_A$ then $\alpha$ is the **minimum of $A$** and we write

    $$ \alpha=\min(A) $$

    """), kind="success")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        The concept of a maximum is very useful, but it also has a deficiency.  

        Consider for example the subset of rational numbers $(1,2)$.  Clearly, in some sense, the number 2 is *still* the "best" upper bound.  

        However, technically it is not the maximum of the set.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        So how else can we characterize the notion of the "best" upper bound?

        In the example of the set of rationals $(1,2)$, the best upper bound is 2.  This also is the *least* of all the upper bounds on this set.

        Therefore we define the notion of the "least upper bound".
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Let $(X,\preceq)$ be a poset and $A\subseteq X$ a nonempty subset.  Let $\alpha\in X$.

    If $\alpha = \min(UB_A)$ then we say that $\alpha$ is the **supremum** (or **least upper bound**) of $A$.

    If $\alpha = \max(LB_A)$ then we say that $\alpha$ is the **infimum** (or **greatest lower bound**) of $A$.  
    """), kind="success")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        But notice that, even with this expanded notion of the "best" upper bound (or lower bound), still not every set has a best upper bound.

        To demonstrate, consider the set 

        $$ L = \{x\in \Bbb Q: 0\le x, \text{ and } 0\le x^2 \le 2\} $$
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        We will not prove the following claims, but they are still useful as motivation.

        This set $L$ can be thought of as the set of rationals in the interval $[0,\sqrt 2)$.  

        This set has an upper bound, like for instance 2.  

        However, it has no *least* upper bound.  If you select any upper bound $\alpha\in UB_L$, we can aways find a $\beta \in UB_L$ such that $\beta < \alpha$.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        This is precisely the reason for the invention of the real numbers.

        The rational numbers have the short-coming that some nonempty sets bounded above do *not* have a least upper bound.  That is to say, they do not have any "best" upper bound.

        Mathematics becomes much simpler and more convenient if, whenever a nonempty subset is bounded above, it has a supremum.  

        We will discuss this idea more, after we've introduced the concept of an "ordered field".
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    I recommend solving at least 5 problems on your own, without looking at solutions, and getting them correct.

    For each problem that you get wrong, do another problem.  Repeat until you have successfully solved 5 problems on your own.  

    If you need an extra bank of exercise problems, you may want to search the internet or use a textbook that discusses similar topics.  

    As a rough guide: A textbook on discrete mathematics might be relatively introductory, but may not have enough content specifically about orders.  A textbook on orders and lattices will definitely contain relevant information, but may be more advanced than the student needs.

    ---

    I recommend spending at least an hour on a problem, before looking at its solution.  This recommendation is specifically for these problems, because they are meant to be easy.  For harder problems, like in the homeworks, you might need to spend several hours or days on them.

    If you have to look at the solution of a problem, treat it as a problem that you did not solve correctly.  Therefore, if you look at the solution, then this does not count toward the 5 problems that you successfully solve on your own.  
    """), kind="info")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""In all that follows, let $(X,\preceq)$ be a poset.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Exercise 1""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Let $A\subseteq X$ be a nonempty subset.  

        Show that if $A$ is finite, then $A$ has a maximum and minimum.
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
        Let $A\subseteq X$ be a nonempty subset.

        Show that if $A$ has a maximum and $\alpha=\max(A)$, then it follows that $\alpha=\sup(A)$.
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
        Let $A\subseteq B\subseteq X$ all be nonempty subsets.

        Show that, if $\sup A$ and $\sup B$ exist, then 

        $$ \sup A \preceq \sup B $$

        Also state and prove a corresponding theorem for infima.
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
        Show that if $A\subseteq X$ is a subset and $b\in A$ then 

        $$ b\in UB_{LB_A} \cap LB_{UB_A} $$ 
        """
    )
    return


if __name__ == "__main__":
    app.run()
