import marimo

__generated_with = "0.11.30"
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
        In this chapter we will prove several properties that we will prove theorems which justify some of our geometric intuitions about the real number line.  

        Some of them come directly from the fact that $\Bbb R$ is an ordered field, and therefore we have either already proved them, or they are better handled as exercises in that lesson.  
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""But some of them are either not true of the rationals, or are true or the rationals but do not carry over in a completely trivial way.  These we prove in this lesson.  """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        We try to do so with a philosophy that is not shared by every other textbook:  We first show that every real number is "well-approximated by" a rational number (or a sequence of rational numbers).  

        Then we try to use a corresponding fact which can be leveraged to prove what is needed for the real numbers.

        This hopefully does two things: Cuts down on how much we need to appeal to anything which couldn't better and more easily be handled by the rational numbers alone.  And it helps to display exactly what is different, when we finally have to appeal to something distinct about the reals.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        The first theorem which will be a tool for the other theorems, is the `Thousand miles` theorem. 

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
        2. Show that $S$ is nonempty and bounded above, therefore $\sup(S)$ exists.
        3. Go down from $\sup(S)$ by $x$, so that there must (by the `Sup ordered field characterization` theorem) be some $nx\in S$ such that $\sup(S)-x < nx\le \sup(S)$.
        4. Infer that $\sup(S)<(n+1)x$ and $(n+1)x\in S$.
        5. Infer a contradiction.

        """
    )
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
