import marimo

__generated_with = "0.13.14"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    I recommend that you solve exercises in the following way: 

    1. Read theorems in the reference section, [ACIRA Reference](https://axiomtutor.github.io/acira/), but do not read the proofs.
    2. Solve the exercises on this page.
    3. Give the proofs of the theorems in the reference section.
    4. Consult solutions to check your work.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Exercise 1""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    1. Show that $(\Bbb Q\smallsetminus \{0\},\times)$ is a group.
    2. Let $H=\{a,b\}$ and set $\ast:H^2\to H$ defined by
         $$\begin{aligned} a\ast a &= a \\ a\ast b &= a \\ b\ast a &= b \\ b\ast b &= b\end{aligned}$$
       Decide whether $(H,\ast)$ is a group.  
    4. Let $X$ be a nonempty set and define $H$ to be the set of all functions $f:X\to X$ such that $f$ is bijective.

         Define the operation $\circ: H^2 \to H$ to be the composition operation on $H$.

           Show that $(H,\circ)$ is a group.

    6. Let $H = \{a,b\}$ and find an operation $\ast:H^2\to H$ such that $(H,\ast)$ is a group.

           If there is more than one such operation, find them all.

           Repeat the exercise if $H = \{a,b,c\}$.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Exercise 2""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Prove that, for any group, its identity is unqiue.  That is to say, let $x\in G$ have the identity property, and prove that $e=x$.

    Also prove that, if $x$ is a group element, then its inverse is unique.  That is to say, if $x^{-1}$ is its inverse and $y$ is an inverse of $x$, then $x^{-1} = y$.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Exercise 3""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Show that for $a,b\in G$, we always have $(ab)^{-1} = b^{-1}a^{-1}$.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Exercise 4""")
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
    mo.md(r"""# Exercise 5""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r""" 
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
    mo.md(r"""# Exercise 6""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    (This exercise is for anyone interested in implementing these ideas in code.  If you have no background or interest in programming, this will not be as interesting for you.)

    We can represent finite groups in Python with an explicit set and function.
    """
    )
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
    return (Group,)


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
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Here's a demo of an example that's not a group.""")
    return


@app.cell
def _(Group):
    h = Group({0,1,2}, lambda x,y: (x+y) % 2)
    print(h.isGroup())
    return


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
    mo.md(r"""# Exercise 7""")
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
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
