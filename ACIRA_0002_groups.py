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
        ## Unit 1: The Real Numbers
        ### Chapter 1: The Axioms of $\Bbb R$
        
        by Axiom Tutor
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

        3. There is an identity element, $0\in\Bbb Z$.  We call this an identity element because, when you combine it with some $x\in \Bbb Z$, "it doesn't change".

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
        The condition that the function, $+$, must be an operation, is sometimes called "closure".  So for instance, $\Bbb Z$ is closed under $+$.

        For a non-example, consider the function of subtraction, $-$, defined on the natural numbers.

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

        Note, however, that $\Bbb N$ is not a group under $+$, because it lacks an identity element, which is $0$.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Let's next consider the operation of multiplication on $\Bbb Z$, which is $\times:\Bbb Z^2 \to \Bbb Z$.  

        This is an operation, since the product of two integers is an integer.  

        Moreover, this operation has an identity element.  You should test yourself by thinking about what it is, and how it fits the definition, before I reveal it!

        /// details | The identity for multiplication

        is 1.  This is because 

        $$ x\times 1 = 1\times x = x,\quad \forall x\in \Bbb Z $$
        ///
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        However, although $\times$ is an associative operation with an identity element, $\Bbb Z$ with multiplication is still not a group.  This is because it lacks inverses.  For example, 2 has no inverse, since this would require an *integer* $x\in \Bbb Z$ such that 

        $$ 2\cdot x = 1 $$

        But there is no such integer.
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
    Let $G$ be a nonempty set, and $\ast:G\times G\to G$ an operation on $G$.  

    We say that an element $e\in G$ is an **identity element** if 

    $$ e\ast x = x\ast e = x, \quad \forall x\in G $$

    If $x,y\in G$ then we say that $y$ is the **inverse of $x$** if 

    $$ x\ast y = e $$

    When $y$ is the inverse of $x$ we typically write $y = x^{-1}$.

    If the following conditions are met, we say that $(G,\ast)$ is a **group**.  

    1. The operation, $\ast$, is associative.

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
    mo.md(
        r"""
        A quick comment about notation: Officially, the symbol for the group operation is often $\ast$.  If we're working with addition, multiplication, composition, or some other more concrete operation, then we'll use its symbol instead.

        But we know that, when working with multiplication, we often just omit the symbol entirely.  For example, $ab$ is understood to mean $a\cdot b$.  

        When working with an abstract group, we adopt the same convention.  Although officially we should write $a\ast b$, we will informally write $ab$ instead.
        """
    )
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
    mo.md(r"""## Solution 7""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        We just need two elements which do not commute.  Any non-zero rotation and any reflection will do.  But since we just need one example, then for concreteness let's choose $R_{120^\circ}$ and $s_A$.

        We now compute $R_{120^\circ}\circ s_A$ and $s_A\circ R_{120^\circ}$, and demonstrate that these are not equal to each other.  

        Let us trace what each does to the vertex $A$.  

        $$ (R_{120^\circ}\circ s_A)(A) = R_{120^\circ}(s_A(A)) = R_{120^\circ}(A) = B $$

        $$ (s_A\circ R_{120^\circ})(A) = s_A(R_{120^\circ}(A)) = s_A(B) = C $$

        In fact, we can stop early.  We can already see that we must have 

        $$ R_{120^\circ}\circ s_A \ne s_A\circ R_{120^\circ} $$

        and therefore $G$ must not be commutative.

        $\Box$
        """
    )
    return


if __name__ == "__main__":
    app.run()
