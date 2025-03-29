import marimo

__generated_with = "0.11.31"
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

        ## Unit 1: The Real Numbers

        ### Chapter 2: Properties of $\Bbb R$

        by Axiom Tutor
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Lesson 0010: Open Sets""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        We have earlier defined the open *intervals* of real numbers.

        Here we generalize this concept to the open *sets* of real numbers.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        What is the importance of an open interval? Consider the fairly random example, the number $2\in\Bbb R$ and the open interval $(1,3)$.  

        The open interval serves as a kind of "neighborhood" around the number 2: A set of points that are near-by.  
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Whenever we talk about things being "near-by" or "small" or "big", or any of these terms that are obviously relative comparisons, what we almost always mean is:  "It can be made as near-by (or small, or big) as you like."

        So for instance, you can have the open interval $(1.9, 2.1)$ and these points here are even nearer to 2.  And the points in $(1.99, 2.01)$ are even nearer, and so on.  

        And in general, if $\varepsilon\in\Bbb R^+$ is any positive number, then there is a neighborhood (open interval) around 2, so that all the points are closer than $\varepsilon$ to 2.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Given all this talk about "distance", we should probably make it official.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Let $a,b\in\Bbb R$.  We define **the absolute value of $a$**,

    $$ |a| = \begin{cases}
    a & \text{ if } 0\le a \\
    -a & \text{ if } a < 0
    \end{cases}$$

    We then define the **distance between $a$ and $b$** by 

    $$|a-b|$$

    For each $\varepsilon\in\Bbb R^+$ we define the **neighborhood within $\varepsilon$ of $a$** as the open interval

    $$N_\varepsilon(a) = (a-\varepsilon,a+\varepsilon) = \{x\in\Bbb R: |x-a|<\varepsilon\}$$ 

    A set $G\subseteq \Bbb R$ is called an **open set** if, for each $a\in G$ there exists a $\varepsilon\in\Bbb R^+$ such that 

    $$ N_\varepsilon(a)\subseteq G $$
    """), "success")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Notice that, according to these definitions, all open intervals are also open sets.  We will demonstrate this claim for an arbitrary bounded open interval $(a,b)$ where $a,b\in\Bbb R$ and $a<b$.

        Let $x\in(a,b)$ and we need to find a neighborhood $N_\varepsilon(x)\subseteq (a,b)$.  And really, this just means that we need to find $\varepsilon$, so that the subset relation holds.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        So-to-speak, "we don't know where $x$ is in $(a,b)$", it could be closer to $a$ or closer to $b$, or in the middle.

        Therefore, we just take $\varepsilon$ to be the least of these distances.  That is to say, 

        $$ \varepsilon = \{|x-a|,|x-b|\}$$
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        With this choice of $\varepsilon\in\Bbb R^+$, it can be shown that $N_{\varepsilon}(x)\subseteq (a,b)$.  The demonstration is left as an exercise.

        Open intervals of the form either $(a,\infty)$ or $(-\infty,a)$ are even easier to demonstrate are open sets, and again, this is left as an exercise.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        One should also note that $\emptyset$ is an open set.  This is because of "vaccuous quantification".  In the condition "for each $a\in \emptyset$", since there is no such $a$, then the conditional sentence is trivially true.

        Also $\Bbb R$ is an open set, which is trivial as well.  This time, it is trivial because $N_\varepsilon(x)\subseteq \Bbb R$ no matter the choice of either $x$ or $\varepsilon$.  
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        We can also prove that, for example, $[0,1]$ is *not* open.  In particular, if we select $x=0$, then there is no $\varepsilon\in\Bbb R^+$ such that $N_\varepsilon(0)\subseteq [0,1]$.  

        This is because $N_\varepsilon(0)$ will always contain elements in the interval $(-\varepsilon,0)$ which are not inside of $[0,1]$.  
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        It is good to check that open intervals are open sets, because this is the sort of thing we ought to expect from our new definitions.  

        But it is also good to see that there are open sets which are not open intervals, so that we can be sure that this new definition doesn't just reduce to the old.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        It is easy to check that $(0,1)\cup (2,3)$ is open.  Slightly more interesting is $(0,1)\cup(1,2)$, which is the same as $(0,2)\smallsetminus\{1\}$.  

        In fact, the union of any two open sets is open.  The proof of which, will be an exercise at the end of this notebook.  

        In fact, the union of any (even *uncountably many*) open sets, is open.  Again, an exercise at the end of this notebook.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        It is also interesting to note that the intersection of two open intervals is open, like $(0,2)\cap (1,3) = (1,2)$.

        The intersection of a *finite* number of open intervals is also open.  The proof for this is a relatively simple induction on the number of intervals.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        However, a possible surpise is: Not *all* intersections of open intervals is an open interval.  

        Consider for example $(0,2)$ intersected with $(0,1.1)$, intersected with $(0,1.01)$, intersected with $(0,1.001)$, and so on.

        This intersection is

        $$ \bigcap_{n=0}^\infty (0,1+10^{-n}) = (0,1] $$

        Notice that the 1 is inclusive, making this set not open.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Why is $\bigcap_{n=0}^\infty(0,1+10^{-n}) = (0,1]$? Well notice that every point in $(0,1]$ is in every interval $(0, 1+10^{-n})$, no matter the choice of $n$.  Therefore $(0,1]\subseteq \bigcap_{n=0}^\infty(0,1+10^{-n})$.  

        Conversely, if $x\le 0$ then $x\notin (0,2)$ for example, and therefore not in the intersection.  If $1 < x$ then there will eventually be a large enough $n$ such that $1+10^{-n} < x$.  For this $n$, we will have $x\notin (0,1+10^{-n})$ and therefore $x$ is not in the intersection.  
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Leaving the details of this example, what it shows us is that we can only trust that finite intersections of open sets are open.  Infinite intersections of open sets may not be open.  """)
    return


if __name__ == "__main__":
    app.run()
