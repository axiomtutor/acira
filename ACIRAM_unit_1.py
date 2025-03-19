import marimo

__generated_with = "0.11.22"
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
        * Exams, for self-assessment.  (No hard problems, but the challenge is to organize and internalize the large )
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        This course practices an unusually strict "division of labor".  

        I've noticed that some textbooks are excellent as a reference but terrible as an introduction.  (Example: Kolmogorov and Fomin's *Introduction to Real Analysis*.)  

        Some texts are exactly the reverse.  (Needham's *Visual Complex Analysis*.)

        In this author's opinion, those are the best books because they have a clear design philosophy and execute on the design well.
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
        For anyone interested in the foundations project, it would be better to include these ideas in a course on set theory, or some sort of course dedicated entirely to foundations.  

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


@app.cell(hide_code=True)
def lesson2(mo):
    mo.md(r"""# Lesson 0002: Groups""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        In this lesson we introduce the concept of a group.

        Before giving the rigorous definition, let's just name a few examples and non-examples, so that you get an intuition for the idea.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Number Examples""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(
        mo.md(r""" 
    The **natural numbers** are the elements of the set 

    $$ \Bbb N = \{1, 2, 3, \dots\} $$

    The **integers** are the elements of

    $$ \Bbb Z = \{\dots, -2,-1,0,1,2,\dots \} $$

    The **rationals** are the elements of 

    $$ \Bbb Q = \left\{\frac p q : p,q\in\Bbb Q, \text{ and } q\ne 0 \right\} $$
    """),
        kind="success",
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        The integers, together with the operation of addition, is our first example of a group.

        This is because we have:

        1. A set of elements ($\Bbb Z$) and an operation ($+$).

            /// details | What is an "operation"?

            For a nonempty set $X$, an operation on $X$ is any function $\ast : X^2 \to X$.

           ///

        3. The operation is associative:

        $$ x+(y+z) = (x+y)+z, \quad \forall x,y,z\in\Bbb Z $$

        3. There is an identity element, $0\in\Bbb Z$.  We call this an identity element because

            $$ 0+x=x+0 = x, \quad \forall x\in \Bbb Z $$

        4. For each element $x\in \Bbb Z$ it has an inverse element, $-x$.  We call $-x$ the inverse of $x$ because, in the following sense, it "takes you back to the identity":

            $$ x+(-x) = 0 $$
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        The condition that the function, $+$, must be an operation, is sometimes called "closure".  So for instance, we sometimes asser this by saying "$\Bbb Z$ is closed under $+$."

        Consider for example the function of subtraction, $-$, defined on the natural numbers.

        $$ -: \Bbb N^2 \to \Bbb Z $$

        This is not an operation, because the range, $\Bbb Z$, does not equal the domain component, $\Bbb N$.  

        Put in the language of closure, we can equivalently say that $\Bbb N$ is not closed under $-$.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        It should be easy to see that $\Bbb Q$ and $\Bbb R$ also form groups under the addition operation, for the same reasons. 

        (Even though we have not officially introduced $\Bbb R$ yet, we still know some of the properties that we expect it to have.)

        Note, however, that $\Bbb N$ is not a group because it lacks an identity element.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo, ztimesbtn, ztimeslst):
    output = None
    if ztimesbtn.value:
        output = ztimeslst + [mo.md("*Answer*: The identity is 1.")]
    else:
        output = ztimeslst
    mo.vstack(output)
    return (output,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        However, $\Bbb Z$ is not a group because it lacks inverses.  For example, $2$ has no inverse for the operation of multiplication.  

        That would require an *integer* $x\in \Bbb Z$ such that $2\cdot x = 1$.  However, such a number is not in $\Bbb Z$.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        You might then think that perhaps $\Bbb Q$ with the operation $\times$ is a group.

        But this is not correct!  Try to see why for yourself.  

        /// details | To check your answer, expand this box.

        $(\Bbb Q,\times)$ meets almost all the conditions: A set with an operation, the operation is associative, and there is an identity (which is 1).  

        In fact, *almost* all rational numbers have a multiplicative inverse.  All but one.

        The number 0 has no multiplicative inverse.  This would require a number $x\in\Bbb Q$ such that 

        $$ x\times 0 = 1 $$

        ///
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## A Geometric Example""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Just to show you that groups are not *just* about numbers, I'll include this geometric example.

        Let $T = \triangle ABC$ be an equilateral triangle, with vertices labeled counter-clockwise in the order $A,B,C$.

        Consider the symmetry of rotating the triangle about its center, sending $A$ to $B$, and $B$ to $C$, and $C$ to $A$.  Let us call this symmetry $R_{120^\circ}$.

        We can also describe $r$ as the rotation of $T$ about its center by $120^\circ$.  You should convince yourself of this fact with some basic geometry calculations.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        There is another symmetry which sends $A$ to $C$, $B$ to $A$, and $C$ to $B$.  This can be obtained either by a rotation about $T$'s center by $240^\circ$ or $-120^\circ$.  We will call this rotation $R_{240^\circ}$.

        Finally, technically, we should include the "$0^\circ$ rotation".  This rotation leaves all the points fixed, and we denote it by $R_{0^\circ}$.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        The *objects* of this group will be the rotations themselves, $G = \{R_{0^\circ},R_{120^\circ},R_{240^\circ}\}$.  

        Note that this is a bit funny because the objects of the group are not the triangle or its vertices.  

        Rather the objects of this group are *functions*.

        For example, $R_{120^\circ}(A) = B$ and so on.  It is a mapping of points in the plane to other points.  And the function itself is an element of $G$.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        If the objects of this group are functions, then what is the operation?

        It will be ... *function composition*!  That is, the operation is $\circ : G^2\to G$.  

        Note that it is not trivial that this is an "operation".  In particular, how do you know that the composition of two elements from $G$ result in an element of $G$?
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Let us explicitly check this one:  $R_{120^\circ}\circ R_{120^\circ}$.  Let us think about what this composition does to the vertex $A$.  The first $R_{120^\circ}$ sends it to $B$ and then the second one sends it to $C$.  

        So $(R_{120^\circ}\circ R_{120^\circ})(A) = C$.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        By similar calculations, we can also show 

        \begin{align*}
          (R_{120^\circ}\circ R_{120^\circ})(B) &= A\\
          (R_{120^\circ}\circ R_{120^\circ})(C) &= B
        \end{align*}
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        But this implies that $R_{120^\circ}\circ R_{120^\circ}$ has the same element-wise mapping as $R_{240^\circ}$.  

        So therefore $R_{120^\circ}\circ R_{120^\circ}\in G$!  This is one step along the way of showing that $\circ$ is an operation on $G$.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        The student is invited to confirm the following, which will be necessary for showing that $G$ is a group:

        1. $R_{120^\circ}\circ R_{240^\circ} = R_{0^\circ}$
        2. Compute $R_{240^\circ}\circ R_{240^\circ}$.
        3. $R_{0^\circ}$ is the identity element.
        4. The inverse of $R_{120^\circ}$ is $R_{240^\circ}$, and also vice versa.
        5. The inverse of $R_{0^\circ}$ is itself.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(
        mo.md(r"""
    Let $G$ be a nonempty set, and $\cdot:G\times G\to G$ an operation on $G$.  

    We say that an element $e\in G$ is an **identity element** if 

    $$ e\cdot x = x\cdot e = x, \quad \forall x\in G $$

    If $x,y\in G$ then we say that $y$ is the **inverse of $x$** if 

    $$ x\cdot y = e $$

    When $y$ is the inverse of $x$ we typically write $y = x^{-1}$.

    If the following conditions are met, we say that $(G,\cdot)$ is a **group**.  

    1. The operation, $\cdot$, is associative.

    2. There is an identity element, which we typically denote as $e$.

    3. For each $x\in G$ there is an inverse $x^{-1}\in G$.  
    """),
        kind="success",
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""When we eventually state the axioms of the real numbers, one axiom will be that $(\Bbb R,+)$ is a group, and another will be that $(\Bbb R\smallsetminus \{0\},\times)$ is also a group.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    I recommend solving at least 5 problems on your own, without looking at solutions, and getting them correct.

    For each problem that you get wrong, do another problem.  Repeat until you have successfully solved 5 problems on your own.  

    If you need an extra bank of exercise problems, you may want to search the internet or use a textbook that discusses group theory.  

    ---

    I recommend spending at least an hour on a problem, before looking at its solution.  This recommendation is specifically for these problems, because they are meant to be easy.  For harder problems, like in the homeworks, you might need to spend several hours or days on them.

    If you have to look at the solution of a problem, treat it as a problem that you did not solve correctly.  Therefore, if you look at the solution, then this does not count toward the 5 problems that you successfully solve on your own.  
    """), kind="info")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Exercise 1""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        1. Show that $(\Bbb Q\smallsetminus \{0\},\times)$ is a group.

        2. Let $G=\{a,b\}$ and set $\ast: G^2\to G$ defined by $a\ast a = a$ and $a\ast b= a$ and $b\ast a = b$ and $b\ast b = b$.  Decide whether $(G,\ast)$ is a group.  

        3. Let $X$ be any nonempty set, and define $G$ to be the set of all $f:X\to X$ such that $f$ is bijective.  Define the operation $\circ:G^2\to G$ to be composition of functions.

               Show that $(G,\circ)$ is a group.

        4. Let $G=\{a,b\}$ and find an operation $\ast:G^2\to G$ such that $(G,\ast)$ is a group.  If there is more than one such operation, find them all.  Repeat the exercise for $G=\{a,b,c\}$.
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
        Prove that, for any group, its identity is unqiue.  That is to say, let $e$ be the group identity and $x\in G$ an element with the identity property.  Prove that $e=x$.

        Also prove that, if $x$ is a group element, then its inverse is unique.  That is to say, if $x^{-1}$ is its inverse and $y$ is an inverse of $x$, then $x^{-1} = y$.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Exercise 3""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Show that, for any group elements, $(ab)^{-1} = b^{-1}a^{-1}$.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Exercise 4""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Let $(G,\ast)$ be a group with identity $e\in G$.  

        For any $n\in \Bbb N$ and $a\in G$, define the notation $a^n$ by 

        $$ a^n = \overbrace{a\cdot a\cdots a}^{n} $$

        Also define $a^0=e$. 

        And for $n\in \Bbb Z^{<0}$ (i.e. a negative integer), define $a^n$ by 

        $$ a^n = (a^{-1})^{|n|} $$

        Prove that the group exponent laws hold, for every $m,n\in\Bbb Z$.  

        \begin{align*}
            a^{m}a^n &= a^{m+n} \\
            (a^m)^n &= a^{mn}
        \end{align*}

        /// details | Hint:

            Divide this into cases.  One is $m=0$ or $n=0$.  

            Another is $0<m,n$. 

            Another is $m<0<n$ and $0\le m+n$.

            Another is $m<0<n$ and $m+n<0$.

            Continue likewise.  Also, there is no need to consider $n<m$ since we may, without loss of generality, assume $m\le n$.  

        ///
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Exercise 5""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r""" 
    Let $(G,\ast)$ be a group.

    We say that the elements $a,b\in G$ **commute** if $a\ast b= b\ast a$.

    We say that $G$ is a **commutative group** if all elements $a,b\in G$ commute.  Equivalently, $G$ is commutative if $\ast$ is commutative.  
    """), kind="success")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        1. Prove that $a,b\in G$ commute if and only if $a = bab^{-1}$.
        2. Prove that $a^mb^m = (ab)^m$ for every $a,b\in G$ and $m\in\Bbb Z$, if and only if $G$ is commutative.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Exercise 6""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""We can represent finite groups in Python with an explicit set and function.""")
    return


@app.cell
def _():
    from itertools import product

    class Group:
        def __init__(self, st, op):
            self.group = st
            self.operation = op
            self.identity = None

        def isNotEmpty(self):
            return len(self.group) != 0

        def isOp(self):
            for x, y in product(self.group, self.group):
                if self.operation(x,y) not in self.group:
                    print(x,y)
                    return False
            return True

        def isAssoc(self):
            for x, y, z in product(self.group, self.group, self.group):
                if self.operation(x,self.operation(y,z)) != self.operation(self.operation(x,y),z):
                    return False
            return True

        def getId(self):
            if self.identity != None: return self.identity
            itsX = True
            for x in self.group:
                for y in self.group:
                    if self.operation(x,y) != y or self.operation(y,x) != y:
                        itsX = False
                        break
                if itsX:
                    self.identity =  x
                    return x
                itsX = True
            return self.identity

        def hasInv(self):
            e = self.getId()
            foundIt = False
            for x in self.group:
                for y in self.group:
                    if self.operation(x,y) == e:
                        foundIt = True
                        break
                if not foundIt: return False
            return True

        def isGroup(self):
            b = self.isNotEmpty() and self.isOp() and self.isAssoc()
            self.identity = self.getId()
            b &= self.identity != None
            return b
    return Group, product


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Here's a relatively simple demonstration of how to use this.""")
    return


@app.cell
def _(Group):
    # The group consists of the set {1,2,3} and the operation of addition mod 3.
    g = Group({0,1,2}, lambda x,y: (x+y) % 3)
    # We can call each method to check that it satisfies the conditions for being a group.
    print(g.isNotEmpty())
    print(g.isOp())
    print(g.isAssoc())
    print(g.getId())
    print(g.hasInv())
    print(g.isGroup())
    return (g,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Here's a demo of an example that's not a group.""")
    return


@app.cell
def _(Group):
    h = Group({0,1,2}, lambda x,y: (x+y) % 2)
    print(h.isGroup())
    return (h,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        1. Explain which group condition `h` fails above.
        2. Write an example representation of a group with numbers 0 through 4 and use addition mod 4.  Is this a group?
        3. (Challenge): Write an example, `g2`, where `g2.group` is a set of functions from {1,2,3} to itself.  Make it such that `gs.isGroup()` evaluates to `True`.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Exercise 7""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Consider the geometric example of the group of rotations, given earlier.

        Let us now extend this example by adding some further symmetries: The reflections.

        That is to say, let $s_A$ refer to the reflection of the triangle $T$ about the line that passes through vertex $A$ and the center of the triangle.  Likewise define $s_B$ and $s_C$.

        Note that $s_A$ leaves the vertex $A$ fixed, and sends $B$ to $C$, and sends $C$ to $B$.  Likewise for the remaining reflections.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Now define $G = \{R_{0^\circ}, R_{120^\circ}, R_{240^\circ}, s_A,s_B,s_C\}$ and let the operation $\circ:G^2 \to G$ be defined by composition of symmetries.

        1. Show that $s_A \circ R_{0^\circ} = s_A = R_{0^\circ} \circ s_A$.

            Also show that $s_A \circ s_A = R_{0^\circ}$ and $s_A\circ s_B = R_{120^\circ}$.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Hint: For this exercise, we will take it for granted that the composition of symmetries is a symmetry.  And to show that any two symmetries are equal, we just have to demonstrate that they move the vertices of $T$ in the same way.

        For example, consider demonstrating 

        $$s_A\circ s_B = R_{120^\circ}$$ 

        We need to show that the symmetry on the left, and the symmetry on the right, both send vertex $A$ to the same vertex.  

        I'll give one such demonstration, for guidance.  Let's show that $s_A\circ s_B$ sends $A$ to $B$, and then show that $R_{120^\circ}$ does the same thing.

        $$(s_A\circ s_B)(A) = s_A(s_B(A)) = s_A(C) = B $$

        Next, it is immediate that $R_{120^\circ}(A)=B$.

        You should then show that each of these symmetries sends $B$ to $C$, and that each sends $C$ to $A$.  This will conclude the proof the equality.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        2. Show that $(G,\circ)$ is a group.  We take it for granted that function composition is associative, so there is no need to prove this (unless you just want to for exercise).
  
            You should give a convincing argument that $\circ$ really is an operation on $G$ -- in particular, you should argue that for any two $x,y\in G$ we have $x\circ y\in G$.

            You should identify the identity element.  And you should find the inverse of each element.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""3. Show that $(G,\circ)$ is not commutative.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Solution 1

        1. The function $\times:(\Bbb Q\smallsetminus \{0\})\times(\Bbb Q\smallsetminus \{0\}) \to \Bbb Q\smallsetminus \{0\}$ is an *operation*, since the product of two nonzero rationals is a nonzero rational.

        Multiplication of rational numbers is *associative*.

        There is a multiplicative *identity*, which is 1.  That is because for any $x\in \Bbb Q\smallsetminus\{0\}$ we have 

        $$ 1\times x = x\times 1 = x $$

        And finally, each nonzero rational has a multiplicative *inverse*.  In particular, if $x\in\Bbb Q$ is a rational number, then it is $x=\frac p q$ for both integers, $p\ne 0 \ne q$.  Therefore its inverse is $\frac q p$, which is a rational because $p,q$ are integers and $p\ne 0$.  This is because 

        $$ \frac p q\cdot \frac q p = \frac{pq}{pq} = 1 $$

        $\Box$
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Solutions for parts (2.) to (4.) are TODO.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Solution 2""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""This proof is in the reference section.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Solution 3""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""This proof is in the reference section.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Solution 4""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""This proof is in the reference section.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Solution 5""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        1. Suppose $G$ is commutative, so that if $a,b\in G$ then $ab=ba$.  Then

        $$ (ab)b^{-1} = (ba)b^{-1} $$ 

        But then by associativity, $(ab)b^{-1} = a(bb^{-1}) = ae = a$ where $e\in G$ is the group identity.

        And by associativity, we can ignore parentheses to write $(ba)b^{-1} = bab^{-1}$.

        Therefore 

        $$ a = bab^{-1} $$
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        For the converse, suppose that for any $a,b\in G$ we have $a = bab^{-1}$.  Then 

        $$ ab = bab^{-1}b $$

        and skipping the details about associativity and cancellation (since we've seen them once already), this simplifies to 

        $$ ab = ba $$

        $\Box$
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        2. Suppose $G$ is commutative and $a,b\in G$, and $m\in \Bbb Z$.

        If $m=0$ then everything trivially reduces to $e$, so the equation holds in this case.

        If $m>0$ then 

        \begin{align*}
        a^m b^m &= \overbrace{a\ast a\ast\cdots \ast a}^m \ast \overbrace{b\ast b\ast \cdots \ast b}^m
         \\
        &= \overbrace{(a\ast b) \ast (a\ast b)\ast\cdots \ast (a\ast b)}^m \\
        &= (ab)^m
        \end{align*}
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        If $m<0$ then 

        \begin{align*}
        a^m b^m &= \overbrace{a^{-1}\ast a^{-1}\ast\cdots \ast a^{-1}}^m \ast \overbrace{b^{-1}\ast b^{-1}\ast \cdots \ast b^{-1}}^{-m}
         \\
        &= \overbrace{(a^{-1}\ast b^{-1}) \ast (a^{-1}\ast b^{-1})\ast\cdots \ast (a^{-1}\ast b^{-1})}^{-m} \\
        &= \overbrace{(ab)^{-1}\ast (ab)^{-1}\ast\cdots\ast (ab)^{-1}}^{-m} \\
        &= (ab)^m
        \end{align*}
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Solution 6""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        1. `h` fails to have an identity.  One would naturally think that $0$ is an identity for this operation, and yet $0\oplus 2 = 0$.

        Parts (2.) through (4.) are TODO.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Solution 7

        """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""We just need two elements which do not commute.  These """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Lesson 0003: Rings and Fields""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Rings""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Fields""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Exercise 1""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Let $(F,+,\times)$ be a field.  Define the operation $+_2$ on vectors $\begin{bmatrix}a\\b\end{bmatrix},\begin{bmatrix}c\\d\end{bmatrix}\in F^2$ by

        $$ \begin{bmatrix} a\\b\end{bmatrix} +_2 \begin{bmatrix}c\\d\end{bmatrix} = \begin{bmatrix}a+c\\b+d\end{bmatrix} $$

        and $\times_2$ defined by 

        $$ \begin{bmatrix} a\\b\end{bmatrix} \times_2\begin{bmatrix}c\\d\end{bmatrix} = \begin{bmatrix}ac\\bd\end{bmatrix} $$

        Show by a counter-example, that $(F^2,+_2,\times_2)$ is not necessarily a field.
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
        Let $F = \{0,1,2,3\}$ and define $\oplus$ and $\otimes$ on $F$, by modular addition and multiplication, respectively.

        $$ a\oplus b = (a+b)\mod 3,\quad a\otimes b = (a\times b)\mod 3 $$

        Show that $(F,\oplus,\otimes)$ is a field.  

        Show that $(\{0,1,2,3,4\}, \oplus,\otimes)$, with plus and times defined by addition and multiplication mod 4, is not a field.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Exercise 3""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Show that in any ring, the additive and multiplicative identities are unqiue.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Exercise 4""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        In a previous exercise, we saw a class `Group` which modeled finite groups as a set and operation, with methods to check that the given objects formed a group.  

        Create similar classes for rings and fields.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Exercise 5""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Show that in any ring, $0x = x0 = 0$ and $-x = (-1)x$, for every $x\in R$.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Exercise 6""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Show that $(\{0\}, +,\times)$ is a ring (and in fact, a field!).

        The operations are defined by $0+0=0$ and $0\times 0=0$.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        We next augment the group structure so that we have a representation of the *interaction* between addition and multiplication.

        We call this augmented structure a ring.  As before, we start with examples and then give the abstract definition.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        The integers $\Bbb Z$ with the operations of $+$ and $\times$, is a ring.  This is because the integers with $+$ forms a *commutative* group, and there is an identity for $\times$ (which is 1), *and* because multiplication distributes over addition.

        $$ a(b+c) = ab+ac, \quad \forall a,b,c\in \Bbb Z $$
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Let $R$ be a nonempty set with two operations, $+, \times:R^2\to R$.  

    We say that **$\times$ distributes over $+$** if $\forall a,b,c\in R$ we have 

    $$ a\times (b+c) = (a\times b)+(a\times c) $$

    We say that $(R,+,\times)$ is a **ring** if the following conditions are met.

    1. Both $+$ and $\times$ are associative.
    2. $(R,+)$ is a commutative group with identity $0\in R$.
    3. There is an identity $1\in R$ for the multiplication operation.
    4. $\times$ distributes over $+$.

    We say that the ring $(R,+,\times)$ is a **commutative ring** if its operation $\times$ is commutative."""), kind="success")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Note that $(\Bbb Z,\times)$ does not form a group.  Nor does $(\Bbb Z\smallsetminus \{0\}, \times)$.

        We don't require a condition like this, for $(\Bbb Z,+,\times)$ to qualify as a ring.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        It is easy enough to see that square matrices form a ring, where $+$ and $\times$ are defined by matrix addition and multiplication.  

        The student is invited to confirm that, for each $n\ge 1$, the triple $(\Bbb Z^{n\times n}, +, \times)$ is a ring.  

        The functions are associative operations, $+$ forms a commutative group, there is a multiplicative identity (what is it?), and multiplication distributes over addition.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Let $X$ be a nonempty set, $G$ the set of bijective functions $f:X\to X$.  

        You showed in a previous exercise that $(G,\circ)$ is a group.  You are invited to now show that, if $|X|>2$ then $(G,\circ)$ is not a commutative group.  

        You can then infer that, no matter what operation we might give by $\ast$, the triple $(G,\circ,\ast)$ will never form a ring.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""If a structure is a ring, but moreover the multiplication operation forms a group (excepting 0), then we call this restricted kind of ring a field.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""For example, because $(\Bbb Q,+,\times)$ is a ring, but also $(\Bbb Q\smallsetminus\{0\},\times)$ is a commutative group (you should check this), then therefore $(\Bbb Q,+,\times)$ is a field.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Because square matrices do not necessarily form a group under multiplication (excepting 0), then these do not necessarily form a field.  

        It can be interesting to consider just the square *invertible* matrices.  This would certainly ensure that every matrix has a multiplicative inverse.  

        However, even that does not provide a field.  This is because invertible matrices still do not commute.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Let $(F,+,\times)$ be a ring with additive identity 0.

    If $(F\smallsetminus \{0\},+,\times)$ is a commutative group, then $(F,+,\times)$ is a **field**.
    """), kind="success")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Lesson 0004: Orders""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        The field properties contain what we will need to know about the algebraic operations of $+$ and $\times$ for the real numbers.

        We now proceed likewise, to describe how the $\le$ relation on the real numbers will behave.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Let's first consider the ordering relation $\le$ on the natural numbers.

        We call $(\Bbb N,\le)$ a "partially ordered set" because the $\le$ relation satisfies some basic properties that we expect from an ordering of a set.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        For one thing it is reflexive:  For any $a\in \Bbb N$ we have $a\le a$.  

        For another it is anti-symmetric:  If $a,b\in \Bbb N$ and we have both $a\le b$ and $b\le a$ then it follows that $a=b$.

        And finally, it is transitive: $a\le b$ and $b\le c$ imply $a\le c$.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Of course, all the same could just as well be said for the rational numbers, so this too is partially ordered by its standard ordering $\le$.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        A more provocative example is the subset relation.

        Let $X$ be a nonempty set, and set $Y =\mathcal P(X)$, the powerset of $X$.  

        Define the following relation, $\preceq$, on the set $Y$.

        $$ A\preceq B \Leftrightarrow A\subseteq B, \quad \forall A,B\in Y $$
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        One can readily check that this is also reflexive, anti-symmetric, and transitive.

        *Reflexive*: For any $A\in Y$ we have $A\subseteq A$ and therefore $A\preceq A$.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""*Anti-symmetric*: Let $A,B\in Y$.  If $A\subseteq B$ and $B\subseteq A$ it follows by basic set theory that $A=B$.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""*Transitive*:  Let $A,B,C\in Y$.  Assume $A\subseteq B$ and $B\subseteq C$.  Then, again by basic set theory, $A\subseteq C$.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Let $X$ be a nonempty set and $\preceq\subseteq X^2$ a relation.

    If the following conditions are met, we call $\preceq$ a **partial order**.

    1. $\preceq$ is reflexive.

    2. $\preceq$ is anti-symmetric.

    3. $\preceq$ is transitive.

    When we want to emphasize the pair which is the set and its partial order, we say that $(X,\preceq)$ is a **partially ordered set**.  We say that $(X,\preceq)$ is a **poset** for short.  

    If $\preceq$ is a partial order, then we define the corresponding **strict partial order** $\prec$ by 

    $$ a\prec b \Leftrightarrow a\prec b\land a\ne b, \quad \forall a,b\in X $$
    """), kind="success")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        But there is something that the subset relation lacks, which we want in an order on numbers.  

        For concreteness, let's discuss $X=\{a,b,c\}$ and 

        \begin{align*}
          Y &= \mathcal P(X) \\
          & = \{\emptyset, \{a\}, \{b\}, \{c\},\\
          & \quad \{a,b\}, \{a,c\},\{b,c\},\{a,b,c\}\}
        \end{align*}

        We use the partial order discussed earlier, $U\preceq V \Leftrightarrow U\subseteq V$ for each $U,V\in Y$.  

        Note that neither $\{a\}\preceq \{b\}$ nor $\{b\} \preceq \{a\}$.  This is what we mean when we say that elements are incommensurable.

        But when it comes to natural numbers, integers, and rationals, if you pick any two elements, $x,y$ then one or the other of $x\preceq y$ or $y\preceq x$ must hold.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Let $\preceq$ be a partial order on $X$.

    For any $a,b\in X$, if neither $a\preceq b$ nor $b\preceq a$, then we say $a$ and $b$ are **incommensurable**.

    If no two elements of $X$ are incommensurable then we say that $\preceq$ is a **total order** on $X$.  

    We also say, in this case, that $(X,\preceq)$ is a **totally ordered set**.
    """), kind="success")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    I recommend solving at least 5 problems on your own, without looking at solutions, and getting them correct.

    For each problem that you get wrong, do another problem.  Repeat until you have successfully solved 5 problems on your own.  

    If you need an extra bank of exercise problems, you may want to search the internet or use a textbook that discusses orders.

    A text on discrete mathematics would probably be accessible, but may or may not have content about orders.  A text on orders and lattices will have relevant content, but may be more advanced than a student needs for the current topic.  

    ---

    I recommend spending at least an hour on a problem, before looking at its solution.  This recommendation is specifically for these problems, because they are meant to be easy.  For harder problems, like in the homeworks, you might need to spend several hours or days on them.

    If you have to look at the solution of a problem, treat it as a problem that you did not solve correctly.  Therefore, if you look at the solution, then this does not count toward the 5 problems that you successfully solve on your own.  
    """), kind="info")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Exercise 1""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        If $\preceq$ is a partial order on $X$, show that the corresponding strict partial order $\prec$ is

        1. Irreflexive: $\forall a\in X$ we have $a\not\prec a$.
        2. Asymmetric: $\forall a,b\in X,$ if we have $a\prec b$ then $a\not\prec b$.
        3. Transitive: $\forall a,b,c\in X$ if $a\prec b$ and $b\prec c$, then $a\prec c$.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Exercise 2""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Find all possible partial orders on the set $\{a,b,c\}$.  Of those partial orders, decide which are total orders.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Exercise 3""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Let $\preceq$ be a partial order on the set $X$, and $\prec$ the corresponding strict partial order.  

        For $a,b\in X$ show that $a\not\preceq b$ is NOT equivalent to $b\prec a$.  

        But if $\preceq$ is a total order, then $a \not\preceq b$ is equivalent to $b\prec a$.
        """
    )
    return


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
    mo.md(r"""## Exercise 1""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Let $(X,\preceq)$ be a poset and $A\subseteq X$ a nonempty subset.  

        Show that if $Y$ is finite, then $Y$ has a maximum and minimum.
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
        Let $(X,\preceq)$ be a poset and $A\subseteq X$ a nonempty subset.

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
        Let $(X,\preceq )$ be a poset and $A\subseteq B\subseteq X$ all nonempty subsets.

        Show that, if $\sup A$ and $\sup B$ exist, then 

        $$ \sup A \preceq \sup B $$

        Also state and prove a corresponding theorem for infima.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Lesson 0005: Bounds of Functions""")
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


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Let $(X,\preceq)$ be a poset and $A$ any nonempty set.  Let $f: A\to X$ be a function.

    Define the **image of $f$** by 

    $$\text{Im}(f) = \{y\in X: \exists b\in A,\ f(b) = y\} $$

    For $\alpha\in X$ we say that **$\alpha$ is an upper bound of $f$** if $\alpha\in UB_{\text{Im}(f)}$.  We say that **$\alpha$ is a lower bound of $f$** if $\alpha\in LB_{\text{Im}(f)}$.  We say that $f$ is a **bounded function** if $\text{Im}(f)$ is a bounded set.

    If $\alpha = \sup(\text{Im}(f))$ exists, we say that the **supremum of $f$** is $\alpha$.  In this case, we write $\sup(f) = \alpha$.  

    If $\alpha=\inf(\text{Im}(f))$ exists, we say that the **infimum of $f$** is $\alpha$.  In this case, we write $\inf(f)=\alpha$.  
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

    which is the **partial function, $f$ applied to $b$**.  
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

    In what follows, if we assume that all suprema exist, then we define the **supremum of $f$ over $A$** to be the *function* $\sup_{a\in A} f_{(\cdot,x)}:B\to Z$.  It is given by the equation 

    $$ \left(\sup_{a\in A} f_{(\cdot,x)}\right)(b) = \sup(f_{(\cdot,b)}), \quad \forall b\in B $$

    The **supremum of $f$ over $B$** is 

    $$ \left(\sup_{b\in B}f_{(x,\cdot)}\right)(a) = \sup(f_{(a,\cdot)}), \quad \forall a\in A $$

    Note that, in this notation, the character $x$ is purely "formal".  It is does not refer to any object, and is there only to visually mark which coordinate is being held fixed as the supremum "ranges over" the coordinate with the dot.
    """), kind="success")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        It may help to understand this intuitively.  

        The function $\sup_{a\in A}f_{(\cdot,x)}$ is a function of $B$.  For an argument $b\in B$, its image is computed by:  

        * "fixing" $b$, which is to say, forming $f$ applied to $b$, and then
        * taking the supremum over all possibilities for $a\in A$.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        It is also worth appreciating that it is possible for $\sup_{a\in A} f_{(\cdot,x)}$ to exist for some arguments $b\in B$ but not for others.  

        For example, consider $f(a,b) = \frac{a}b$ for $a,b\in\Bbb Q$ and $b\ne 0$.  

        The function $\sup_{y\in \Bbb Q} f_{(x,\cdot)}$ exists for the argument $a=0$.  That is because the image of $\sup_{y\in\Bbb Q}f_{(x,\cdot)}$ is just the set $\{0\}$, which has supremum equal to 0.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        However, for any other argument, $\sup_{y\in\Bbb Q}f_{(x,\cdot)}$ does not exist.  Let us just consider the argument $a=1$, for concreteness.  

        The function $f_{(1,\cdot)}:\Bbb Q\smallsetminus \{0\} \to \Bbb Q$ is given by 

        $$ f_{(1,\cdot)}(y) = \frac 1 y $$

        Therefore we know that $\text{Im}(f_{(1,\cdot)})$ is unbounded above.  So $\sup(f_{(1,\cdot)})$ does not exist.

        Therefore $\sup_{y\in \Bbb Q}f_{(x,\cdot)}$ does not exist for argument $a=1$.  Equivalently, we may say: $\left(\sup_{y\in\Bbb Q} f_{(x,\cdot)}\right)(1)$ is undefined.
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
    \sup_{a\in A}\sup_{b\in B} f &= \sup_{a\in A}\left(\sup_{b\in B} f_{(x,\cdot)}\right) 
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


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Reference Section""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## 0002: Groups""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""


    Let $G$ be a nonempty set and $\ast:G^2\to G$ an opertion on $G$.  

    We say that $e\in G$ is an **identity element** if $e\ast x = x\ast e = x$ for every $x\in G$.  This element is typically denoted by $e$.

    For $x,y\in G$ we say that **$y$ is the inverse of $x$** if $x\ast y = y\ast x = e$.  Typically we denote the inverse of $x$ as $x^{-1}$.

    We call $G$ a **group** if 

    1. $\ast$ is associative.
    2. $G$ has an idenity element.
    3. Each element of $G$ has an inverse.

    If $\ast$ is commutative we say that $G$ is a **commutative group**.  
    """),kind="success")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""In all that follows, let $(G,\ast)$ be a group with identity $e\in G$.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Let $x\in G$ and $m\in\Bbb Z$.  If $m>0$ then we define

    $$ x^m = \overbrace{x\cdot x\cdots x}^{m} $$

    If $m=0$ then 

    $$ x^m=e $$

    and if $m < 0$ then

    $$ x^m = (x^{-1})^{|m|} $$

    """), kind="success")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Groups theorem 1

    `Unique identities`

    ---

    For any nonempty set $X$ and operation $\ast:X^2\to X$, if $\ast$ has an identity element $e\in X$, then it is unique.
    """), kind="danger")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        *Proof*:  If $a\in X$ is an identity for $\ast$, then 

        $$ ae = a = e $$

        $\Box$
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Group theorems 2

    `Unique inverses of associative operations`

    ---

    Let $X$ be a nonempty set, $\ast:X^2\to X$ an associative operation on $X$, and $e$ the identity for $\ast$.

    If $a\in X$ has an inverse $a^{-1}$ then this is its unique inverse.
    """), kind="danger")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        *Proof*: Let $b\in X$ be an inverse of $a$ so that $ab = ba = e$.

        $$ b = be = baa^{-1} = ea^{-1} = a^{-1} $$

        $\Box$
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Group theorems 3

    `Unique group identities and inverses`

    ---

    The identity and all inverse in $G$ are unique.
    """), kind="danger")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        *Proof*: Since identities of any operation are unique, then the identity of $G$ is unique.

        Since the operation of $G$ is associative, then each element $x\in G$ has a unique inverse $x^{-1}\in G$.  

        $\Box$
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Group theorems 4

    `Inverses cancel`

    ---

    For any $x\in G$,

    $$ -(-x) = x $$

    """), kind="danger")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        *Proof*: $x$ has the property $x+(-x) = e$.

        Therefore $x$ has the property of being the inverse of $-x$.  By the uniqness of inverses, therefore $x = -(-x)$.  

        $\Box$
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Groups theorem 4

    `Group cancellation`

    ---

    Let $x,y,z\in G$.  

    If $xy = xz$ then $y=z$.  
    """), kind="danger")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        *Proof*: From $xy=xz$ 

        $$ x^{-1}(xy) = x^{-1}(xz) $$

        which by associativity is 

        $$ (x^{-1}x)y = (x^{-1}x)z $$

        which by the inverse property is

        $$ ey = ez $$

        which by the identity property is 

        $$ y=z $$

        $\Box$
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Groups theorem 5

    `Group exponent laws`

    ---

    Let $x,y\in G$ and $m,n\in\Bbb Z$.  Then 

    $$ x^mx^n = x^{m+n},\quad (x^m)^n = x^{mn} $$

    $G$ is commutative if and only if 

    $$ x^m y^m = (xy)^m $$
    """), kind="danger")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        *Proof*: Assume, without loss of generality that $m\le n$.

        *Case 1*, assume $m=0$ or $n=0$.

        If $m=0$,

        \begin{align*}
        x^mx^n &= ex^n = x^n
        \end{align*}

        *Mutatis mutandis* the same proof holds if $n=0$.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        *Case 2*, assume $0 < m, n$.

        \begin{align*}
        x^mx^n &= \overbrace{x\cdot x\cdots x}^m\overbrace{x\cdot x\cdots x}^n \\ 
        &= \overbrace{x\cdot x\cdots x}^{m+n} \\
        &= x^{m+n}
        \end{align*}
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        *Case 3*, assume $m<0<n$.

        *Subcase 3a*, assume $m+n\ge 0$.

        In this case $|m|=-m$ and $-m\le n$.  Then 

        \begin{align*}
        x^mx^n &= \overbrace{x^{-1}\cdot x^{-1}\cdots x^{-1}}^{|m|} \overbrace{x\cdot x\cdots x}^{n}\\
        &= \overbrace{x^{-1}\cdot x^{-1}\cdots x^{-1}}^{|m|-1} \overbrace{x\cdot x\cdots x}^{n-1} \\
        &= \overbrace{x^{-1}\cdot x^{-1}\cdots x^{-1}}^{|m|-2} \overbrace{x\cdot x\cdots x}^{n-2} \\
        &\vdots \\
        &=\overbrace{x\cdot x\cdots x}^{n-|m|}\\
        &=\overbrace{x\cdot x\cdots x}^{n+m}
        \end{align*}
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        *Subcase 3b*, assume $m+n < 0$.  

        Then $|m|=-n$ and $n< -m$.  

        \begin{align*}
        x^mx^n &= \overbrace{x^{-1}\cdot x^{-1}\cdots x^{-1}}^{|m|} \overbrace{x\cdot x\cdots x}^{n} \\
        &= \overbrace{x^{-1}\cdot x^{-1}\cdots x^{-1}}^{|m|-1} \overbrace{x\cdot x\cdots x}^{n-1} \\
        &\vdots \\
        &= \overbrace{x^{-1}\cdots x^{-1}}^{|m|-n}\\
        &= \overbrace{x^{-1}\cdots x^{-1}}^{-(m+n)} \\
        &= x^{m+n}
        \end{align*}
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        *Case 4*, assume $m,n<0$.

        \begin{align*}
            x^mx^n &= \overbrace{x^{-1}\cdots x^{-1}}^{|m|} \overbrace{x^{-1}\cdots x^{-1}}^{|n|} \\
            &= \overbrace{x^{-1}\cdots x^{-1}}^{|m|+|n|} \\
            &= \overbrace{x^{-1}\cdots x^{-1}}^{-(m+n)} \\
            & = x^{m+n}
        \end{align*}

        $\Box$
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## 0003: Rings and Fields""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Let $R$ be a nonempty set, and $+,\times: R^2\to R$ two operations on $R$.

    We say that **$\times$ distributes over $+$** if 

    \begin{align*} 
    a\times (b+c) &= (a\times b)+(a\times c) \\
    (b+c)\times a &= (b\times a)+(c\times a), \quad \forall a,b,c\in R 
    \end{align*}

    We say $(R,+,\times)$ is a **ring** if 

    1. $+$ and $\times$ are associative.
    2. $(R,+)$ is a commutative group with identity $0\in R$.
    3. There is a multiplicative identity, $1\in R$.  
    4. $\times$ distributes over $+$.

    If in addition $(F\smallsetminus \{0\}, \times)$ is a commutative group, then we call $(F, +, \times)$ a **field**.
    """), kind="success")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""In all that follows, assume that $(R,+,\times)$ is a ring.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Ring theorems 1

    `Unique ring identities and inverses`

    ---

    In a ring, the additive and multiplicative identities and inverses are unique.
    """), kind="danger")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        *Proof*: By the `unique identites` theorem, the identity is unique for each operation.

        Because the operations are both associative, by the `unique inverses for associative operations` theorem, any inverse for each operation is unique.

        $\Box$
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Ring theorems 1

    `Zero annihilates` 

    ---

    For all $x\in R$,

    $$ 0x=x0 = 0 $$

    """), kind="danger")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        *Proof*: 

        $$ 0x = (0+0) x = 0x + 0x $$ 

        so 

        $$ 0x-0x = 0x+0x-0x $$ 

        which simplifies to

        $$ 0 = 0x $$

        *Mutatis mutandis*, the same argument applies likewise to $x0$.

        $\Box$
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    $\forall x\in R$,

    $$ -x = (-1)x $$
    """), kind="danger")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        *Proof*: 

        $$ x+(-1)x = x(1-1) = x0 = 0 $$

        Since $(-1)x$ has the property of the inverse of $x$, then by the uniqueness of inverse elements, $-x=(-1)x$.  

        $\Box$
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""In what follows, assume $(F,+,\times)$ is a field.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
    Field therems 1 

    `Multiplication cancellation`

    ---

    Let $a,b,c\in F$ such that 

    $$ ab = ac $$

    If $a\ne 0$ then $b=c$.
    """), kind="danger")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        *Proof*: Since $a\ne 0$ then $a^{-1}$ exists.  

        $$ a^{-1}ab = a^{-1}ac = b = c $$

        $\Box$
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## 0004: Orders""")
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    ztimesbtn = mo.ui.button(
        value=False, on_click=lambda value: not value, label="Show answer"
    )

    ztimeslst = [
        mo.md(
            r"""
        Note that $\Bbb Z$ is not a group if we instead take the operation to be multiplication.  

        In this example, we do have a set and operation.  The operation is associative.

        In fact, there is even an identity element!  

        It is ... 


        """
        ),
        ztimesbtn,
    ]
    return ztimesbtn, ztimeslst


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
