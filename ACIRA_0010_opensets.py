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
    mo.md(r"""# Lesson 0010: Open and Closed Sets""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        We have earlier defined the open *intervals* of real numbers.

        Here we generalize this concept to the open *sets* of real numbers.

        The general concept of an open set falls within the domain of topology, which is a rich and somewhat independent topic within mathematics.  

        Because of the vastness of this topic, we cannot describe it much, or we will become too distracted by a long investigation.  
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Let $X$ be a nonempty set, and $\mathcal \tau\subseteq \mathcal P(X)$ a subset of the power-set of $X$.

    Then we call $\mathcal \tau$ a **topology on $X$** if 

    1. $\emptyset, X\in \tau$.

    2. $\tau$ is **closed under union**:  If $\mathcal Y\subseteq\tau$ then $\bigcup_{Z\in \mathcal Y}Z\in\tau$.  

    3. $\tau$ is **closed under finite intersection**: If $\{Y_1,Y_2,\dots,Y_n\}\subseteq \tau$ is any finite subset, then $\bigcap_{k=1}^n Y_k\in\tau$.
    """), "success")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Here is a simple example of a topology:  Let $X = \{1,2,3\}$ and $\tau = \{\emptyset, X\}$.

        Let's check that this satisfies the three conditions.  The first, (1.), is trivially satisfied.

        The second, (2.), requires that we consider every possible $\mathcal Y\subseteq \tau$.  The possibilities for $\mathcal Y$ are: $\emptyset, \{\emptyset\}, \{X\},\{\emptyset,X\}$.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        For any of these possibilities for $\mathcal Y$, we find that $\bigcup_{Z\in\mathcal Y}Z\in \tau$.

        If $\mathcal Y=\emptyset$ then $\bigcup_{Z\in \mathcal Y}Z = \emptyset$ and this is in $\tau$.

        If $\mathcal Y = \{\emptyset\}$ then $\bigcup_{Z\in\mathcal Y}Z = \emptyset$ again.

        If $\mathcal Y = \{X\}$ then $\bigcup_{Z\in \mathcal Y}Z = X$ and this is in $\tau$.

        If $\mathcal Y = \{\emptyset,X\}$ then $\bigcup_{Z\in\mathcal Y}Z = X$ again.
        """
    )
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
