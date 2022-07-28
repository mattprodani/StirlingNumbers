from manim import *
import networkx as nx
import numpy as np
class StirlingTwoSetup(Scene):
    def construct(self):
        group = VGroup()
        
        title = Tex("Stirling Numbers of the Second Kind")
        setup = Tex("\\textbf{PS4; Question 7: }Let $A$ be an $n$-element set and let $i,j,k \\in \\mathbb{N}$ with $i + j + k = n$.", font_size = 22)
        question = Tex("How many functions $f: A \\rightarrow \\{ 1, 2, 3 \\}$ are there for which the below are satisfied", font_size = 22)
        cond = Tex(r"\begin{itemize} \item $\left|\left\{ a \in A : f(a) = 0 \right\} \right| = i$ \item $\left|\left\{ a \in A : f(a) = 1 \right\} \right| = j$ \item $\left|\left\{ a \in A : f(a) = 2 \right\} \right| = k$ \end{itemize}", font_size = 18)

        
        
        
        title.shift(UP * 3)
        setup.next_to(title, DOWN)
        question.next_to(setup, DOWN)
        cond.next_to(question, DOWN)
        
        group += title
        group += setup
        group += question
        group += cond
        
        self.play(
            LaggedStart(*[FadeIn(obj, shift=DOWN) for obj in group])
        )
        self.wait(5)
        
#         Add rule for bijection here
        
        new = Tex(r"\begin{itemize}"
                  +r"\item $i, j, k \neq 0$ \end{itemize}", font_size = 18).next_to(cond, DOWN)
        
        self.play(
            FadeIn(new, shift=RIGHT)
        )
        
        self.wait(8)
        
        
        
        
#       Remove conditions after Simplify question
        new_question = Tex("How many surjective functions $f: A \\rightarrow \\{ 1, 2, 3 \\}$ are there.", font_size = 22)

        new_question.next_to(setup, DOWN)
        
        
        self.play(
            TransformMatchingTex(question, new_question)
        )
        
        self.wait(5)
        
        cond_gr = VGroup()
        cond_gr += cond
        cond_gr += new
        
        self.play(
            FadeOut(cond_gr, shift=LEFT)
        )
        
        self.wait(5)
        
#       Adjust group

        group -= cond
        group -= question
        group += new_question
        
        
        
#       Case k = 1

        group_k1 = VGroup()
        
        case_1_question = Tex("$f: A \\xrightarrow{\\text{onto}} \\{ 1\\}$", font_size = 22)
        
        case_1_ans = Tex(r"Only one: $f(a) = 1, \forall a \in A$", font_size = 24)
        
        case_1_note = Tex(r"Also, $1= \genfrac\{ \}{0pt}{}{n}{1}$", font_size = 22)
        
        group_k1.add(case_1_question)
        group_k1.add(case_1_ans)
        group_k1.add(case_1_note)
        
        group_k1.arrange(DOWN)
        group_k1.next_to(group, DOWN, buff = 1)
        
        self.add(group_k1[0])
        
        self.wait(5)
        
        self.play(
            FadeIn(case_1_ans, shift=RIGHT)
        )
        
        
        self.wait(3)
        
        
        self.play(
            FadeIn(case_1_note, shift=RIGHT)
        )
        
        
        self.wait(5)
        
        
        self.play(
            group_k1.scale(.7).animate.move_to(LEFT*4)
        )
        
        self.wait(3)
        
        
#         Case k = 2
        

        
        group_k2 = VGroup()
        
        case_2_question = Tex("$f: A \\xrightarrow{\\text{onto}} \\{ 1, 2\\}$", font_size = 22)
        
        case_2_one = VGroup()
        
        case_2_one += Tex(r"Two possible mappings for each $a \in A$", font_size = 18)
        case_2_one += Tex(r"$2^n$ mappings onto $1$ or $2$", font_size = 18)
        case_2_one.arrange(DOWN)
        
        case_2_note = VGroup()
        case_2_note += Tex(r"The order of 1 and 2 do not matter", font_size = 18)
        case_2_note += Tex(r"So, $2^{n-1}$ mappings onto indistinguishable sets", font_size = 18)
        case_2_note += Tex(r"But one of these is the case where they all map to one set", font_size = 18)
        case_2_note.arrange(DOWN)
        
        
        case_2_ans = Tex(r"So $\genfrac\{ \}{0pt}{}{n}{1} = 2^{n-1} - 1$", font_size = 18)
        
        group_k2.add(case_2_question)
        group_k2.add(case_2_one)
        group_k2.add(case_2_note)
        group_k2.add(case_2_ans)
        
        group_k2.arrange(DOWN)
        group_k2.next_to(group, DOWN, buff = 1)
        
        self.add(group_k2[0])
        
        self.wait(5)
        
        self.play(
            FadeIn(case_2_one, shift=RIGHT)
        )
        
        
        self.wait(3)
        
        
        self.play(
            FadeIn(case_2_note, shift=RIGHT)
        )
        
        
        self.wait(5)
        
        
        self.play(
            FadeIn(case_2_ans, shift=RIGHT)
        )
        
        
        self.wait(5)
        
        
        self.play(
            group_k2.scale(.8).animate.next_to(group_k1, RIGHT)
        )
        
        self.wait(3)
        
        
        
        