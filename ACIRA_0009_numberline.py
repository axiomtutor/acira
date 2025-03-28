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
    mo.md(r"""# Lesson 0009: The Number Line""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        We now know what the real numbers are! Hooray! 🎉🥳

        Celebartion is now over 😒, and we return to hard work, learning the basic properties of these numbers.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        In this lesson we prove theorems which justify our intuitions about the geometry of the numberline.  The first theorem which will be a tool for the other theorems, is the `Thousand miles` theorem. 

        The name is a metaphor for the saying "A journey of a thousand miles starts with a single step".

        In this theorem, $y$ will be the thousand mile journey (or just any "really large distance").  $x$ will be the size of a single step (usually "small").  $n$ will be the number of steps required.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        It is a rare occurrence that the Wikipedia page for a mathematical idea can be helpful, but in this one it is:  [Wikipedia: Archimedean Property](https://en.wikipedia.org/wiki/Archimedean_property).

        This theorem is named in honor of Archimedes, perhaps in part, because of the [Archimedes physical principle about leverage](https://en.wikipedia.org/wiki/Lever#Lever_History).  In brief he said that, with a long enough lever he could move the world.  In this metaphor, $y$ is the weight of the world, $x$ is his puny little force applied to the lever, and $n$ is the length of the lever.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    `Thousand miles` (common name: Achimedean Property)  

    ---

    Let $x\in\Bbb R^+$ and $y\in \Bbb R$.  

    Then there exists an $n\in\Bbb N$ such that $y < nx$.
    """), "danger")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""How should we approach proving this claim?""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        If the same sort of claim were made about the rationals, it would be true.  How would we prove it? Presumably by first expressing a rational as a ratio of integers, and then using knowledge about the ordering on integers.

        That technique is not available for proving facts about the real numbers, because we don't know that real numbers have an expression in terms of anything simpler (like rational numbers).
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        But the real numbers does have a property abound bounding sets, and there does seem like something here is bounded.

        In an sense, the claim is that $y$ is *not* a bound on the set of all $nx$.  Some $nx$ must be bigger than $y$.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Motivated by this idea, we may form the set 

        $$ S = \{nx: n\in\Bbb N\} $$ 

        and try to prove that $y$ does not bound it.  

        *Proof idea*:

        1. For contradiction, assume that $S$ is bounded by $y$.  
        2. Show that $S$ is nonempty and bounded above, therefore $\sup(S)$ exists.  (Handle the special case of $y\le 0$, which is trivial -- but explain why.)
        3. Go down from $\sup(S)$ by $x$, so that there must (by the `Sup ordered field characterization` theorem) be some $nx\in S$ such that $\sup(S)-x < nx\le \sup(S)$.
        4. Infer that $\sup(S)<(n+1)x$ and $(n+1)x\in S$.
        5. Infer a contradiction.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    `1/n approaches 0`

    ---

    Let $x\in\Bbb R^+$.

    Then there is an $n\in\Bbb N$ such that $\frac 1 n < x$.
    """), "danger")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        The proof of this theorem is a relatively simple appeal to the `Thousand miles` theorem.  By saying that it's simple, I don't mean that it's *easy* to think of, the first time that you try.  I do mean that the proof can be given in a small number of sentences.  

        Note that the theorem is equivalent to finding an $n\in\Bbb N$ such that $1<nx$, which will be my only hint here.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    `Q distributed in R`

    ---

    Between any two real numbers, there is a rational number.
    """),"danger")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        To prove this, let $a,b\in\Bbb R$ and $a<b$.  In particular, at least to get started, assume $0<a$.

        Think of $(a,b)$ as a region in the numberline, and we want to find a rational number in this region.  
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Using metaphors like the ones we used for the `Thousand miles` theorem, one should be able to take small enough "steps", starting at 0, eventually crossing to the other side of $a$, but not stepping so large that we immediately also step over $b$.

        To make this idea rigorous, we probably want a small step size, $\varepsilon$.  It should be smaller than $b-a$, the length of the interval $(a,b)$.  We can obtain this can appeal to the `1/n approaches 0` theorem.  

        We also want a "number of steps" which step us from 0, over $a$ and into the region $(a,b)$.  We can obtain this by a separate appeal to the `Thousand miles` theorem.  
        """
    )
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
