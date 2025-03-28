import marimo

__generated_with = "0.11.28"
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
    mo.md(r"""# Lesson 0000: Introduction""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Hello!""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Hello and welcome.

        This sequence of notebooks will attempt to "simulate" a university course in real analysis.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Content""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        This course covers most of the standard content of a university course in real analysis.

        * The axioms of the real numbers.
        * Basic properties of the real numbers, sets of real numbers, and topology.
        * Real-valued functions and sequences.
        * Series of real sequences.
        * Limits.
        * Continuity.
        * Derivatives.
        * Integrals.
        * The Fundamental Theorem of Calculus.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Prerequisites""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        This course is designed for future mathematicians, or anyone whose educational path would overlap with these interests.

        I will assume that the student has already taken courses in basic calculus and discrete mathematics.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        "Basic calculus" means the equivalent of Stewart's textbook *Calculus: Early Transcendentals*, up to the point where he introduces the Fundamental Theorem of Calculus.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        The portions of discrete mathematics that a student will find useful in this course include logic, sets, functions, relations, induction, recursion, and combinatorics.  

        These topics can be found in many books, but just to name one popular book explicitly: Rosen's *Discrete Mathematics and Its Applications*.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Structure of the Course""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        This notebook provides

        * A reference text.
        * Lectures, for pedagogy.
        * End of lecture exercises, for basic familiarization. (Easy.)
        * End of chapter homeworks, for more challenging project-based learning. (Medium to hard difficulty.)
        * Exams, for self-assessment.  (Forces the student to organize and consolidate the large collection of knowledge covered in a unit.)
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Pedagogical Sections, Reference Sections, and Exercises""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        This course practices an unusually strict "division of labor".  

        I've noticed that some textbooks are excellent as a reference but terrible as an introduction.  (Example: Kolmogorov and Fomin's *Introduction to Real Analysis*.)  

        Some texts are exactly the reverse.  (Needham's *Visual Complex Analysis*.)

        In this author's opinion, those are the best books.  They have a clear design philosophy and execute on the design well.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        But these texts do not try to serve all of the needs that a new student has. 

        Each text either does not attempt to teach, or it does not strive to provide a compact reference.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        In these notebooks I'm going to try to do both, but not in the same place.  

        I'll maintain a reference at the end of the notebook.  This is intended to be an extremely concise and efficient organization of definitions, theorems, and proofs.  

        I recommend completing each lesson in the following order.

        1. Read the lesson in the pedagogy section (i.e. the main section of the noteboook), and watch the corresponding lecture.
        2. Prove all of the theorems and claims in this section.
        3. Do the exercises at the end of the lesson.
        4. Read the corresponding reference section (toward the end of the notebook).
        5. At the end of each chapter, do the homework.
        6. At the end of each unit, do the exam.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Time""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        I am designing this course with the following logic: The typical university course meets twice a week for about 2 hours each meeting, for about 16 weeks.

        Therefore I am going to try to design this course by 

        1. Initially only including only the most absolutely essential parts of real analysis.
        2. If I find that the total lecture time is less than 2 * 16 * 2 = 64 hours, I will include more until it fills the alotted time of 64 hours.
        3. If my total lecture time is more than 64 hours, I will try to painfully cut away material until it fits the constraint.

        Therefore these lessons should really approximate what can fit into a single semester of a real analysis course.  

        I hope that this self-constraint will also make the lessons relatively lean and efficient, since I won't give myself permission to talk about things I think are interesting or optional.

        Therefore, if something is in here, it's probably important.
        """
    )
    return


if __name__ == "__main__":
    app.run()
