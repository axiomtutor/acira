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
def lesson1(mo):
    mo.md(r"""# Lesson 0001: Introduction to Axioms, Generally""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Construction of $\Bbb R$""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Many real analysis textbooks begin their presentation, with a construction of the real numbers.

        This makes obvious sense.  If we're going to study real numbers, let's start from the beginning!

        And yet that is not what these notebooks will do. 🙂
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        The project of constructing all objects from the axioms of set theory is called the "foundations project".  

        It is true that real analysis must, to some degree, have one foot in this project.  After all, its fundamental object of study is the real number.  In order to guarantee that this even exists in our mathematical universe, it must be constructed from the axioms!
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        However, foundations as a field has its own set of interests.  They often do not overlap with the interests of real analysis.  

        Since the construction of the real numbers takes quite a long time, and does not really serve the interests of real analysis, it is better for us to skip this topic entirely.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        For anyone interested in the foundations project, it would be better to include these ideas in a course on set theory, or some sort of course dedicated entirely to foundations.  (The interested student can also consort a textbook like, say, Jech's *Set Theory*.)

        If I get enough requests for such a thing, I might consider making a Marimo course in foundations one day.  But at least for now, let's move efficiently to the things that are of interest to real analysis.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Axioms of $\Bbb R$""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Since we are not starting at the start, then where are we starting?

        In effect, we are just going to write down a list of *assumptions*.  The construction of the real numbers would prove that these assumptions are in fact correct.  But we will merely take these assumptions on faith.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        These assumption will tell us everything that we actually need to know about the real numbers, in practice.  They will tell us how to add, multiply, and compare real numbers, as well as ensure the existence of irrational numbers.

        These assumptions are the "axioms of the real numbers".
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        But the axioms themselves are quite long and complicated.  For this and other reasons, I want to break down the presentation of the axioms into self-contained component ideas.  These include the ideas of 

        * a group
        * a ring
        * a field
        * a poset
        * a total order
        * an ordered field
        * completeness (with respect to suprema)
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        The structure of the first few lessons will start by introducing an abstract concept, like a group or an order.

        Then, once all of these abstract concepts have been introduced, we will use them to state the axioms of the real numbers.
        """
    )
    return

if __name__ == "__main__":
    app.run()
