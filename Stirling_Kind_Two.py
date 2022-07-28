from manim import *
from itertools import permutations
class StirlingTwo(Scene):
    def construct(self):
        
        ISOLATE = ["a", "b", "c"]
        
        title = Tex("Stirling Numbers of the Second Kind for $n=3$")
        subtitle = MathTex("S = \\{ a, b, c \\}", font_size = 22, substrings_to_isolate = ISOLATE)
        
        
        
        title.shift(UP * 3)
        subtitle.next_to(title, DOWN)
        
        group = VGroup(title, subtitle)
        
        self.add(group)
        
        gk1 = VGroup()
        
        strings = ["\{{ ( {0} , {1} , {2} ), (), () \}}", "\{{ (), ( {0} , {1} , {2} ), () \}}", "\{{ (), (), ( {0} , {1} , {2} ) \}}"]
        for perm in permutations(["a", "b", "c"]):
            g = VGroup(*[MathTex(s.format(*perm), font_size = 18, substrings_to_isolate = ISOLATE) for s in strings])
            g.arrange(DOWN)
            gk1.add(g)
        
        
        gk1.arrange()
        
        for g in gk1:
            for line in g:
                line.set_color_by_tex_to_color_map({
                    "a": RED,
                    "b": GREEN,
                    "c": BLUE,
                })
        
        
        titlek1 = Tex(r"$k = 1$ with 3 subsets", font_size = 20)
        subk1 = Tex(r"$\binom{3}{1}$ placements", font_size = 20)
        step2k1 = Tex(r"$3!$ permutations", font_size = 20)
        
        titlegrk1 = VGroup(titlek1, subk1, step2k1).arrange(DOWN).shift(LEFT * 2.5 + UP)
        
        
        self.play(
            FadeIn(titlegrk1[:2], shift=RIGHT)
        )
        
        self.wait(5)
        
        gk1.next_to(titlegrk1)
        
        
        self.play(
            LaggedStart(*[TransformMatchingTex(subtitle.copy(), obj)for obj in gk1[0]])
        )
        
        self.wait(5)
        
        
        self.play(
            FadeIn(step2k1, shift=RIGHT)
        )
        self.wait(5)
        
        
        gkleft = gk1[0]
        gkright = gk1[1:]
        all_one = VGroup(titlegrk1, gkleft)
    
        
        
        self.play(
            all_one.animate().shift(LEFT * 2)
        )
        
        
        gkright.next_to(gkleft)
        
        self.play(
        
            LaggedStart(*[TransformMatchingTex(gkleft[i].copy(), g[i]) for g in gkright for i in range(len(g))])
        )
        self.wait(5)
        
        all_one += gkright
        
        
        self.play(
            all_one.animate().scale(.7).next_to(group, DOWN).shift(LEFT)
        )
        self.wait(5)
        
        
        
          
        strings_k2 = ["\{{ ( {0} ), ({1}), () \}}", "\{{ (), ( {0} ), ({1}) \}}", "\{{ ( {0} ), (), ( {1} ) \}}"]
#         for perm in permutations(["a", "b", "c"]):
#             g = VGroup(*[MathTex(s.format(*perm), font_size = 18, substrings_to_isolate = ISOLATE) for s in strings])
#             g.arrange(DOWN)
#             gk1.add(g)
        
        titlek2 = Tex(r"$k = 2$ with 3 subsets", font_size = 20)
        subk2_1 = Tex(r"3 possible partitions", font_size = 20)
        subk2_2 = Tex(r"$\binom{3}{2}$ placements", font_size = 20)
        step2k2 = Tex(r"2 ways to arrange partitions", font_size = 20)
        step3k2 = Tex(r"2 ways to arrange elements", font_size = 20)
        
        titlegrk2 = VGroup(titlek2, subk2_1, subk2_2, step2k2, step3k2).arrange(DOWN)
        
        
        gk2 = VGroup()
        
        perm_types_2 = [["a", "b , c"], ["a , b", "c"], ["a , c", "b"], ["a", "c, b"], ["b, a", "c"], ["c, a", "b"]]

        for t in perm_types_2:
            g_base = VGroup()
            for perm in permutations(t):            
                [g_base.add(MathTex(s.format(*perm), font_size = 18, substrings_to_isolate = ISOLATE)) for s in strings_k2]
            g_base.arrange(DOWN)
            gk2.add(g_base)
            
        
        for g in gk2:
            for line in g:
                line.set_color_by_tex_to_color_map({
                    "a": RED,
                    "b": GREEN,
                    "c": BLUE,
                })
            
            
                
        gk2.arrange().next_to(titlegrk2, RIGHT)
        
        
        
        grk2_left = gk2[:3]
        grk2_right = gk2[3:]
        all_two = VGroup(titlegrk2, grk2_left).next_to(all_one, DOWN)
        grk2_right.next_to(grk2_left)
        
        self.play(
            FadeIn(titlegrk2[0], shift=RIGHT)
        )
        
        self.wait(3)
        
        self.play(
            FadeIn(titlegrk2[1], shift=RIGHT)
        )
        
        
        
        self.play(
            LaggedStart(*[TransformMatchingTex(subtitle.copy(), g[0]) for g in gk2[:3]])
        )
                          
        self.wait(3)
        
        
        self.play(
            FadeIn(titlegrk2[2], shift=RIGHT)
        )
        
        self.wait(3)
        
        
        self.play(
            LaggedStart(*[TransformMatchingTex(g[0].copy(), g[1:3]) for g in gk2[:3]])
        )
        self.wait(3)
        
        
        self.play(
            FadeIn(titlegrk2[3], shift=RIGHT)
        )
        
        self.wait(3)
        
        
        self.play(
            LaggedStart(*[TransformMatchingTex(g[:3].copy(), g[3:]) for g in gk2[:3]])
        )
        self.wait(3)
        
        
        self.play(
            FadeIn(titlegrk2[4], shift=RIGHT)
        )
        
        
        
#       Shift elements left
        
        self.wait(2)
        self.play(
            all_two.animate().shift(LEFT* 2)
        )
        
        grk2_right.next_to(grk2_left)
        
        
        self.wait(2)
        self.play(
            LaggedStart(TransformMatchingTex(grk2_left.copy(),grk2_right))
        )
        self.wait(3)
        
        
        all_two += grk2_right
        
        
        self.play(
            all_two.animate().scale(.7).next_to(all_one, DOWN).align_to(all_one, LEFT)
        )
        
        self.wait(3)
        
        
                       

        titlek3 = Tex(r"$k = 3$ with 3 subsets", font_size = 20)
        subk3_1 = Tex(r"1 possible partitioning", font_size = 20)
        subk3_2 = Tex(r"$\binom{3}{3} = 1$ placement", font_size = 20)
        step2k3 = Tex(r"$3!$ arrangements", font_size = 20)
        
        s_k3 = "\{{ ( {0} ), ( {1} ), ( {2} ) \\}}"
        gk3 = VGroup(*[MathTex(s_k3.format(*perm), font_size = 18, substrings_to_isolate = ISOLATE) for perm in permutations(["a", "b", "c"])])
        gk3.arrange(DOWN)

        
        for line in gk3:
            line.set_color_by_tex_to_color_map({
                "a": RED,
                "b": GREEN,
                "c": BLUE,
            })
        
        titlegrk3 = VGroup(titlek3, subk3_1, subk3_2, step2k3).arrange(DOWN)
        all_three = VGroup(titlegrk3, gk3).arrange().next_to(all_two, DOWN)
        
        
        
        self.play(
            FadeIn(titlegrk3[0], shift=RIGHT)
        )
        
        self.wait(3)
        
        self.play(
            FadeIn(titlegrk3[1], shift=RIGHT),
            FadeIn(titlegrk3[2], shift=RIGHT)
        )
        
        
        
        self.play(
           TransformMatchingTex(subtitle.copy(), gk3[0])
        )
                          
        self.wait(3)
        
        
        self.play(
            FadeIn(titlegrk3[3], shift=RIGHT)
        )
        
        self.wait(3)
        
        
        self.play(
            TransformMatchingTex(gk3[0].copy(), gk3[1:])
        )
        
        self.wait(3)
        
        gk3_new = VGroup(gk3[:3], gk3[3:]).arrange().next_to(all_three[0])
        
        
        self.play(
            TransformMatchingTex(gk3, gk3_new)
        )
        
        self.wait(3)
        
        all_three -= gk3
        all_three += gk3_new
        
        self.play(
            all_three.animate().scale(.7).next_to(all_two, DOWN).align_to(all_two, LEFT)
        )
        self.wait(3)
        
        
        
        all_one -= gkright
        
#         Remove permutations
        self.play(
            FadeOut(gkright, shift=RIGHT),
            FadeOut(grk2_right, shift=RIGHT)
        )
    
        self.wait()
        
        all_two -= grk2_right
        
        perms = VGroup(all_one[:2], all_two, all_three)
        
        self.play(
            perms.animate().shift(LEFT * 1.5)
        )
        
        steps = VGroup()
        
        steps.add(Tex("Calculating the Stirling Number from the number of functions", font_size = 20))
        steps.add(MathTex(r"\text{Let }F = \{f : A \rightarrow \{a, b, c\}\}", font_size = 20))
        steps.add(MathTex(r"\text{Let }X(n, k, a) = |\{f \in F : |im(f)| = a\}|", font_size = 20))
        steps.add(MathTex(r"\genfrac\{ \}{0pt}{}{n}{3} = \frac{1}{n!}\left(|F| - X(n, 3, 2) - X(n, 3, 1))", font_size = 20))
        steps.add(MathTex(r"\genfrac\{ \}{0pt}{}{n}{3} = \frac{1}{3!}\left(3^3 - \binom{3}{2}(2)(2^{n-1} - 1) - \binom{3}{1}\right)", font_size = 20))
        steps.add(MathTex(r"\genfrac\{ \}{0pt}{}{n}{3} = \frac{1}{3!}\left(3^3 - \binom{3}{2}(2^n) -2\binom{3}{2} - \binom{3}{1}\right)", font_size = 20))
        steps.add(MathTex(r"\genfrac\{ \}{0pt}{}{n}{3} = \frac{1}{3!}\left(3^3 - \binom{3}{2}(2^n) + \binom{3}{1}\right)", font_size = 20))

        steps.arrange(DOWN).next_to(perms, RIGHT, buff = 1)
        
        for step in steps:
            self.play(FadeIn(step, shift=RIGHT))
            self.wait()
        