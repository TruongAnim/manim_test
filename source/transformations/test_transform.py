###
from manim import *
from common.custom.custom_animation import *

SCENE_NAME = "DifferentRotations"

if __name__ == "__main__":
    command = f"manim -pql {__file__} {SCENE_NAME}"
    print(command)
    os.system(command)

#Transform(a, b) => b not add to screen, nothing change with b
# => a will take all property of b.

#ReplacementTransform(a, b) => a fly to b and take all property of b
# => after that a will be remove from the scene, b will be add

class TestTransform(Scene):
    def construct(self):
        circle = Circle().rotate(PI / 2)
        square = Square()
        self.play(Create(circle))
        circle.rotate(-PI / 4)

        self.play(Transform(circle, square))
        self.wait()


class T1(Scene):

    def construct(self):
        tex = MathTex(

            "\\frac{d}{dx}",  # 0

            "(",  # 1

            "u",  # 2

            "+",  # 3

            "v",  # 4

            ")=",  # 5

            "\\frac{d}{dx}",  # 6

            "u",  # 7

            "+",  # 8

            "\\frac{d}{dx}",  # 9

            "v"  # 10

        ).scale(2)
        self.play(
            Write(tex[:6])
        )

        steps = [
            [[2, 3, 4],
             [7, 8, 10]],
            [[0, 0],
             [6, 9]],
        ]
        for step in steps:
            from_, target = step
            self.play(*[ReplacementTransform(tex[i].copy(), tex[j])
                        for i, j in zip(from_, target)])
            self.wait()
        self.play(Uncreate(tex))
        self.wait()


class TestSwap(Scene):
    def setup(self):
        self.A = Square()
        self.B = Circle()
        self.G = VGroup(self.A, self.B).arrange(RIGHT, buff=LARGE_BUFF * 2)
        self.add(self.G)

    def construct(self):
        self.play(*[
            Transform(self.A, self.A.copy().move_to(self.B.get_center())),
            Transform(self.B, self.B.copy().move_to(self.A.get_center())),

        ], run_time=2)
        self.wait()
        self.G[0], self.G[1] = self.G[1], self.G[0]
        self.play(self.G[0].animate.scale(2))
        self.play(self.G[1].animate.scale(0.5))
        self.wait()

class TestReplaceTransform1(Scene):
    def setup(self):
        pass

    def construct(self):
        square = Square().shift(LEFT)
        circle = Circle().shift(RIGHT)
        # self.add(square, circle)
        # self.play(ReplacementTransform(square, circle))
        self.play(Transform(square, circle))
        self.play(square.animate.shift(UP))
        self.play(circle.animate.shift(DOWN).set_color(BLUE))

class TestContinueTransform(Scene):
    def setup(self):
        pass

    def construct(self):
        square = Square().shift(LEFT*2)
        circle = Circle()
        triangle = Triangle().shift(RIGHT*2)

        self.play(Transform(square, circle),
                  Transform(circle, triangle),
                  Transform(triangle, square, path_arc = PI))

class RotateTransform(Scene):
    def setup(self):
        pass

    def construct(self):
        square = Square().shift(LEFT * 2)
        circle = Circle()
        triangle = Triangle().shift(RIGHT * 2)
        anim = [square, circle, triangle]

        for i in range(10):
            self.play(
                ApplyFunction(lambda obj: obj.move_to(anim[1].get_center()), anim[0]),
                ApplyFunction(lambda obj: obj.move_to(anim[2].get_center()), anim[1]),
                ApplyFunction(lambda obj: obj.move_to(anim[0].get_center()), anim[2], path_arc=PI)
            )
            anim = anim[2:] + anim[0:2]

class TestReplaceTransform2(Scene):
    def setup(self):
        pass

    def construct(self):
        square = Square().shift(LEFT)
        circle = Circle().shift(RIGHT)
        dot = Dot().to_edge(RIGHT)
        # self.add(square, circle, dot)
        self.play(ReplacementTransform(square, circle))
        # self.play(Transform(square, circle))
        self.play(Transform(circle, dot))
        self.play(Transform(square, dot))

class TestTranform2(Scene):
    def construct(self):
        obj = Text("X")
        t_a = Text("A")
        t_b = Text("B")
        t_c = Text("C")
        t_d = Text("D")

        self.add(obj)
        self.play(ReplacementTransform(obj, t_a))
        self.play(ReplacementTransform(obj,t_b)) # <- This not works
        # self.play(ReplacementTransform(t_a, t_b))
        # self.play(ReplacementTransform(t_b, t_c))
        # self.play(ReplacementTransform(t_c, t_d))
        self.wait()
        t_grp = VGroup(obj, t_a, t_b, t_c) \
            .arrange(DOWN) \
            .shift(RIGHT)
        self.play(Write(t_grp))
        self.wait()


class DifferentRotations(Scene):
    def construct(self):
        left_square = Square(color=BLUE, fill_opacity=0.7).shift(2 * LEFT)
        right_square = Square(color=GREEN, fill_opacity=0.7).shift(2 * RIGHT)
        self.play(
            left_square.animate.rotate(PI), Rotate(right_square, angle=PI), run_time=2
        )
        self.wait()