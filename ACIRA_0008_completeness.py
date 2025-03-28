import marimo

__generated_with = "0.11.26"
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
        ## Unit 1: The Real Numbers
        ### Chapter 1: The Axioms of $\Bbb R$
        
        by Axiom Tutor
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
def _(mo, quote):
    mo.md(
        r"""
        *Chatty proof*: 
        /// details | What is a "chatty proof"?

        Of course it's not an official phrase, but what I mean is that I will try to talk through the thought process for *creating* the proof, rather than just giving the end result.

        The point is to remedy a problem that occurs in many advanced mathematics texts, where proofs seem to involve objects and steps that "come from nowhere".

        Consider the proof that Rudin gives, of the theorem that we are currently working on, in his *Principles of Mathematical Analysis*:  (His $y$ is my $\alpha$, and he's immediately treating the case for a general $n$ whereas I am starting with the special case of $n=2$.  His $x$ is a general positive real number, whereas I am starting with the special case $x=2$.)

        """ + f"""
        {mo.as_html(quote)}
        """+r"""

        Many students read a line like this and are left stunned.  "Where did this random object, $\frac{x-y^n}{n(y+1)^{n-1}}$, come from?  If I have to prove similar theorems, how am I supposed to come up with an object like this?"

        The definition of such an object is not logically invalid, and the rest of the proof that Rudin gives is certainly correct.  But it comes from a background of knowledge that Rudin has, which a new student cannot possibly have.  This is bad for pedagogy. 

        A chatty proof is suppose to communicate a logical process for coming up with the proof in the first place.  

        ///
        """)
    return


@app.cell(hide_code=True)
def _(mo):
    quote = mo.md(r"""
    /// admonition | 

    "Assume $y^n < x$.  Choose $h$ so that $0<h<1$ and 

    $$ h < \frac{x-y^n}{n(y+1)^{n-1}}\ \ \ \ ''$$
    """)
    return (quote,)


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


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        So assuming $\alpha^2<2$, where is our contradiction going to come from?  If we think somewhat intuitively about the real line, this probably means that $\alpha$ is now a little bit lower than the right edge of $L$, which should mean that $\alpha$ cannot be an upper bound on $L$.  

        That is a contradiction, since we assumed that $\alpha=\sup(L)$.  So this will be the nature of the contradiction that we hope to show: There is an $x\in L$ such that $\alpha<x$.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Naturally that provokes the follow-up question, how do we find this $x$?  

        It is often helpful, not just to represent this number bigger than $\alpha$, but in fact to represent *how much bigger* it is.  That is to say, it is often useful to use the quantity $\varepsilon = x-\alpha$.  The hope, then, is to find a $\varepsilon>0$ small enough that $\alpha+\varepsilon = x \in L$.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        This may seem like exchanging one challenge for an equally hard challenge: Instead of finding $x$, we now find $\varepsilon$.  How do we find $\varepsilon$?

        Well, the search for $\varepsilon$ may actually have available tools that the search for $x$ didn't.  In particular, we can now work with $\alpha+\varepsilon$ and use the algebraic structure!
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        The goal we have set for ourselves is to find $\varepsilon>0$ such that $\alpha+\varepsilon\in L$, which is to say,

        $$ (\alpha+\varepsilon)^2 < 2 $$

        which is 

        $$ \alpha^2+2\alpha\varepsilon+\varepsilon^2 < 2$$
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Solving for $\varepsilon$ the best we can, we get

        $$ 2\alpha\varepsilon+\varepsilon^2<2-\alpha^2 $$

        What a rush! So much progress and solving!  But now we are at an impasse.  

        How do we go from here, to find $\varepsilon$?
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Here is an intuitive strategy:  Try to make $2\alpha\varepsilon$ less than half of $2-\alpha^2$, and also make $\varepsilon^2$ less than half of $2-\alpha^2$.  

        The former is easy: $2\alpha\varepsilon < \frac{2-\alpha^2}2$ is equivalent to 

        $$ \varepsilon < \frac{2-\alpha^2}{4\alpha} $$

        Any choice of $\varepsilon$ such that $0<\varepsilon<\frac{2-\alpha^2}{4\alpha}$ will satisfy this condition.  Such a choice must exist because $2-\alpha^2$ is positive (prove this), and $4\alpha$ is positive (prove this), therefore the fraction is positive (prove this).  Therefore, between 0 and the fraction is some number (prove this), and any such number will satisfy our requirements.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        What's less immediate is how to find an $\varepsilon$ such that $\varepsilon^2<\frac{2-\alpha^2}2$.  We cannot simply "solve" for $\varepsilon$, since the square root is not available to us.  (After all, we're proving that a certain square root must exist!)

        But we have already proved, in an earlier exercise, that if $\varepsilon < 1$ then $\varepsilon^2<\varepsilon$.  This allows us to use a simplifying approximation.  

        Instead of finding $\varepsilon^2<\frac{2-\alpha^2}2$ we find $\varepsilon < \frac{2-\alpha^2}2$.  So long as we pick $\varepsilon < 1$, it will follow that $\varepsilon^2<\varepsilon<\frac{2-\alpha^2}2$.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        How do we guarantee that we pick $\varepsilon < 1$, and $\varepsilon < \frac{2-\alpha^2}2$, and $\varepsilon < \frac{2-\alpha^2}{4\alpha}$?  

        $$ \varepsilon = \frac{\min\left\{1,\frac{2-\alpha^2}2, \frac{2-\alpha^2}{4\alpha} \right\}}2 $$
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        The search for $\varepsilon$ is now over.  

        I claim that, if you use this choice of $\varepsilon$, you can prove (with some effort) that $(\alpha+\varepsilon)^2 \in L$, which was the plan all along.

        With this in hand, the rest of the proof by contradiction goes through quickly:  Because $\alpha<\alpha+\varepsilon$ then $\alpha\notin UB_L$ which contradicts the assumption that $\alpha=\sup(L)$.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Exercises""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Exercise 1""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Take the "chatty proof" above, and clean it up into an efficient and proof that $\alpha^2\ge 2$.

        Also prove that $\alpha^2\le 2$ in a similar fashion, to conclude that $\alpha^2=2$.

        Conclude that $\sqrt 2\in \Bbb R$.
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
        Show that $\sqrt 3\in \Bbb R$ and $\sqrt[3]{2}\in\Bbb R$.

        Then generalize this to show that, for any $x\in \Bbb R$ such that $1< x$, and for any $n\in\Bbb N$, we have 

        $$ \sqrt[n]x \in\Bbb R $$

        Hint: Use the binomial theorem.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Exercise 3""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Use the above result to show that if $0< x$ then $\sqrt[n]x\in\Bbb R$.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Exercise 4""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Let $0\le x$ and show that 

        $$ y = x^n$$ 

        has a unique solution in $\Bbb R$.
        """
    )
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
