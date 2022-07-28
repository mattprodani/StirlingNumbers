from manim import *
import networkx as nx
import numpy as np
class StirlingOne(Scene):
    def construct(self):
        
        to_isolate = ['a', 'b', 'd', 'c', 'e', 'f', 'g', 'h', 'i', 'j']
        
        
        group = VGroup()
        
        title = Tex("Stirling Numbers of the First Kind")
        setup = MathTex(r"\textbf{Visualizing the recurrence relation: }",r"\genfrac\{ \}{0pt}{}{n + 1}{k}",
                        r"= ", r"n\genfrac\{ \}{0pt}{}{n}{k}"," + ", r"\genfrac\{ \}{0pt}{}{n}{k-1}", font_size = 22)
        question = MathTex(r"\textbf{Question: } \text{What happens to a set's Stirling number of the first kind when adding an element?}", font_size = 22)
        statement = MathTex(r"S = \{a, b, c, d, e, f, g, h, i, j\}, \sigma : S \rightarrow S", font_size = 22)
        
        TITLE_GROUP = VGroup(title, setup, statement, question).arrange(DOWN).move_to(UP * 2.5)
        self.play(
            LaggedStart(*[FadeIn(obj, shift=DOWN) for obj in TITLE_GROUP])
        )
        self.wait(5)
        
        
#         Setting up example one
        
        
        perm_function = [["a","b", "d"], ["c", "e"], ["f", "g", "h"], ["i", "j"]]
        perm_edges = [[(perm[i - 1], perm[i]) for i in range(len(perm))] for perm in perm_function]
        print(perm_edges)
        
        
        
        graph_one = Graph([i for perm in perm_function for i in perm], [i for perm in perm_edges for i in perm],
                                 layout="circular", edge_type = ArcBetweenPoints, labels=True, label_fill_color=BLUE).scale(.7)
        g1_LABEL = VGroup(MathTex(r"\sigma_1 = (a, b, d)(c, e)(f, g, h)(i ,j)", font_size = 18))
        g1_LABEL += MathTex(r"\text{Case 1:} \rightarrow n = 10, k_1 = k", font_size = 18)
        g1_setup = VGroup()
        g1_setup += MathTex(r"n\genfrac\{ \}{0pt}{}{n}{k}", font_size = 18)
        g1_setup += Tex(r"First case, we have $k$ cycles already", font_size = 16)
        g1_setup += MathTex(r"\text{There are: }\genfrac\{ \}{0pt}{}{n}{k} \text{ such permutations}}  ", font_size = 16)
        g1_setup += Tex(r"And n different ways to place it", font_size = 16)
        g1_setup.arrange(DOWN)
        graph_one.next_to(TITLE_GROUP, DOWN)
        
        g1_LABEL.arrange(DOWN).move_to(graph_one)
        
        
        
        
        self.play(
            TransformMatchingTex(setup.copy(), g1_setup[0]),
            LaggedStart(*[FadeIn(obj, shift=DOWN) for obj in g1_setup[1:2]])
        )
        self.wait()
        self.play(
            g1_setup[:2].animate.next_to(graph_one, LEFT)
        )
        
        g1_setup[2:].next_to(g1_setup[1], DOWN)
        
        
        self.play(TransformMatchingTex(statement.copy(), g1_LABEL))
        self.wait()
        self.play(g1_LABEL.animate.next_to(graph_one, DOWN), Create(graph_one))
        
        self.wait()
        self.play(
            LaggedStart(*[FadeIn(obj, shift=RIGHT) for obj in g1_setup[2:]])
        )
        
        LEFT_GROUP = VGroup(graph_one, g1_LABEL, g1_setup)
        
        self.wait()
        self.play(
            LEFT_GROUP.animate.arrange(DOWN).scale(.7).next_to(TITLE_GROUP, DOWN).shift(LEFT * 3)
        )
        
        self.wait()
        
        
        
#         Setting up example 2
        
        
        perm_function_k1 = [["c","d", "a"], ["f", "g", "j", "e"], ["h", "b", "i"]]
        perm_edges_k1 = [[(perm[i - 1], perm[i]) for i in range(len(perm))] for perm in perm_function_k1]
        graph_two = Graph([i for perm in perm_function_k1 for i in perm], [i for perm in perm_edges_k1 for i in perm],
                                 layout="circular", edge_type = ArcBetweenPoints, labels=True, label_fill_color=PURPLE).scale(.7)
        g2_LABEL = VGroup(MathTex(r"\sigma_2 = (c, d, a)(f, g, j, e)(h, b, i)", font_size = 18))
        g2_LABEL += MathTex(r"\text{Case 2:} \rightarrow n = 10, k_2 = k - 1", font_size = 18)
        
        g2_setup = VGroup()
        g2_setup += MathTex(r"\genfrac\{ \}{0pt}{}{n}{k - 1}", font_size = 18)
        g2_setup += Tex(r"Or, we have $k - 1$ cycles", font_size = 16)
        g2_setup += MathTex(r"\text{There are: }\genfrac\{ \}{0pt}{}{n}{k-1} \text{ such permutations}", font_size = 16)
        g2_setup += Tex(r"We would need to add $x$ as a singleton cycle", font_size = 16)
        g2_setup.arrange(DOWN).next_to(LEFT_GROUP, RIGHT)
        
        graph_two.next_to(g2_setup, RIGHT)
        g2_LABEL.arrange(DOWN).move_to(graph_two)
        
        
        self.play(
            TransformMatchingTex(setup.copy(), g2_setup[0]),
            LaggedStart(*[FadeIn(obj, shift=DOWN) for obj in g2_setup[1:2]])
        )
        self.wait()
        
        
        self.play(TransformMatchingTex(statement.copy(), g2_LABEL))
        self.wait()
        self.play(g2_LABEL.animate.next_to(graph_two, DOWN), Create(graph_two))
        
        self.wait()
        self.play(
            LaggedStart(*[FadeIn(obj, shift=RIGHT) for obj in g2_setup[2:]])
        )
        
        RIGHT_GROUP = VGroup(graph_two, g2_LABEL, g2_setup)
        
        self.wait()
        self.play(
            RIGHT_GROUP.animate.arrange(DOWN).scale(.7).next_to(TITLE_GROUP, DOWN).shift(RIGHT * 3)
        )
        
        
#         Animate right side
        
        self.wait()
        
        dot = LabeledDot("x", fill_color= RED)
        print(dot.get_center())
        loop = Circle(radius = dot.radius*1.7, color=WHITE).move_to([dot.radius*1.7, 0, -1])
        singleton = VGroup(loop, dot).scale(0.7).scale(0.7)
        singleton.next_to(RIGHT_GROUP, RIGHT)
        
        self.play(Create(singleton))
        self.wait()
        self.play(singleton.animate.move_to(graph_two))
        
        self.wait()
        
#         Animate left side

        g = graph_one
        
        gedges = g.edges.copy()
        LABEL = LabeledDot("x", fill_color= RED).scale(0.7).scale(0.7)
        
        for edge in [*gedges]:

            g.remove_edges(edge)

            pts = gedges[edge].points
            center = pts[len(pts)//2]

            self.play(
                g.animate.add_edges((edge[0], "x"), ("x",edge[1]), labels=True, edge_type = ArcBetweenPoints, 
                                    positions = {"x" : center}, vertex_mobjects={"x" : LABEL})
            )
            self.wait()
            g.remove_edges((edge[0], "x"), ("x",edge[1]))
            g.add_edges(edge, labels=True, edge_type = ArcBetweenPoints)
            g.remove_vertices("x")
        
        
