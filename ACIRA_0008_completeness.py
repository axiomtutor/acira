import marimo

__generated_with = "0.11.24"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # A Course in Real Analysis ... In Marimo!
        ## Unit 1: The Axioms of the Real Numbers
        ### by Axiom Tutor
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Lesson 0008: Completeness""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        So far we have definitions that tell us about $+,\times,$ and $\preceq$.  

        But these definitions are all satisfied by the rational numbers.  That is to say, $(\Bbb Q,+,\times,\le)$ satisfy the properties of an ordered field.

        There is still something not yet captured by these definitions, which give the distinct properties of the real numbers.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        To see what that is, consider the set of rational numbers $L=[0,\sqrt 2)$.  

        Since the number $\sqrt 2$ is not itself a rational number, it may seem invalid to even speak of such a set of rational numbers.

        Therefore, let us express this set in a way that is more transparently valid for rational numbers.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""$$ L = \{x\in\Bbb Q: 0\le x^2<2 \}^{\succeq 0} $$""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        It is easy to confirm that $0, \ 1, \ 1.4, \ 1.41$ are all in $L$.  

        If you ask a calculator for the decimal approximation of $\sqrt 2$, it will give you something like
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    _src = (
        "images/0008_completeness/root2.png"
    )
    mo.image(src=_src)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        What this gestures at, is the fact that if you pick any upper bound for this set, it is always possible to find a smaller upper bound.

        For example, 2 is an upper bound for $L$, but so is $1.5$.  

        But so is $1.42$.

        But so is $1.415$, and so on.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""This situation is unlike what we have for an interval like $(0,1)$.  In this case, the number 1 is an upper bound, and in fact it is the least upper bound.  Any number smaller than 1 will not be an upper bound for $(0,1)$.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        And this is precisely the deficiency that the real numbers are intended to fix: We need to bound sets, and obtain a best "tightest" bound.  However, for rational numbers, this best bound does not always exist.  

        It will be an axiom of the real numbers, that whenever a nonempty set has an upper bound, it must have a least upper bound.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Let $(F,+,\times,\preceq)$ be an ordered field.  We say that this is **complete with respect to suprema** (or has the **least upper bound property**) if the following condition is met.

    For every subset $Y\subseteq F$ if $Y\ne \emptyset$ and $UB_Y\ne \emptyset$ then $\sup(Y)\in F$.  
    """),kind="success")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Real number theorems 1

    `The axiom of the real numbers`

    ---

    There is a complete ordered field, called the **real numbers**.  We denote it by $(\Bbb R,+,\times,\le)$.  
    """), kind="danger")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        We will take it for granted that the natural numbers are a subset of $\Bbb R$, which correspond to $1$ and $2=1+1$, and $3=2+1$, and so on.  We will likewise take it for granted that $\Bbb Z$ and $\Bbb Q$ are identified with a subset of $\Bbb R$ in a natural way.  

        Many real analysis courses will labor over proving the "isomorphism" inherent in these claims.  But the design philosophy of this course is to focus as much as possible on the interests of real analysis, and these sorts of concerns are not core the the interests of real analysis.  Hence we take such things for granted.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        It is likely familiar from a previous course in discrete math, that there is no rational number $x\in\Bbb Q$ such that $x^2=2$.  That is to say, $\sqrt 2\notin \Bbb Q$.  

        However, that is not the same as saying that $\sqrt 2$ is irrational!  To demonstrate *this*, we need to show that there *is* a real number $x\in\Bbb R$ such that $x^2 = 2$.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Real number theorems 2

    $\sqrt 2\in \Bbb R$

    ---

    There is a real number $x\in\Bbb R$ such that $x^2=2$.
    """), kind="danger")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        *Chatty proof*: 
        /// details | What is a "chatty proof"?

        Of course it's not an official phrase, but what I mean is that I will try to talk through the thought process for *creating* the proof, rather than just giving the end result.

        The point is to remedy a problem that occurs in many advanced mathematics texts, where proofs seem to involve objects and steps that "come from nowhere".

        Consider the proof that Rudin gives, of the theorem that we are currently working on, in his *Principles of Mathematical Analysis*:  (His $y$ is my $\alpha$, and he's immediately treating the case for a general $n$ whereas I am starting with the special case of $n=2$.  His $x$ is a general positive real number, whereas I am starting with the special case $x=2$.)

        "Assume $y^n < x$.  Choose $h$ so that $0<h<1$ and 

        $$ h < \frac{x-y^n}{n(y+1)^{n-1}}  $$
    
        "

        Many students read a line like this and are left stunned.  "Where did this random object, $\frac{x-y^n}{n(y+1)^{n-1}}$, come from?  If I have to prove similar theorems, how am I supposed to come up with an object like this?"

        The definition of such an object is not logically invalid, and the rest of the proof that Rudin gives is certainly correct.  But it comes from a background of knowledge that Rudin has, which a new student cannot possibly have.  This is bad for pedagogy.  
    
        A chatty proof is suppose to communicate a logical process for coming up with the proof in the first place.  
    
        ///
        """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        How should we prove this theorem?  One hint is from the fact that the proof must depend on the completeness axiom.  Otherwise one would be able to prove this for the rational numbers.

            In order to use the completeness axiom, we need a set with a relevantly interesting sup.  A natural guess is 

        $$ L = \{x\in\Bbb R:0\le x^2<2\}^{\ge 0} $$

            We've seen this set before, and discussed how its right edge should be where $\sqrt 2$ is.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Before that, we need to formally show that it is nonempty and bounded above, so that we can ensure its supremum must exist.

        Certainly it is nonempty because $0\in L$, which follows from $0< 0^2 = 0 <2$.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        It is bounded above because $2\in UB_L$.  To demonstrate this, let $x\in L$ so that $0\le x$ and $0\le x^2 < 2$.  

        By a previous exercise, it follows that $x\le 2$ if and only if $x^2 \le 4$.  But since we have $x^2<2$, the latter condition is met.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Since we now have that $L$ is nonempty and bounded above, the completeness axiom implies that $\alpha=\sup(L)$ exists.

        It is natural that we should now try to prove that $\alpha$ has the property $\alpha^2=2$.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        How?  We know relatively little about $\alpha$ except for its supremum properties, which have more to do with ordering than anything else.  

        Therefore, we probably want to approach this by showing that $\alpha^2 < 2$ leads to a contradiction, so that we can make use of those ordering properties.
        """
    )
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Exercises""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Exercise 1""")
    return


@app.cell
def _(mo):
    mo.md(r"""Show that ther""")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
