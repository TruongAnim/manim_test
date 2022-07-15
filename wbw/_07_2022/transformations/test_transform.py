###
from manim import *
config.set_width = "80%"


SCENE_NAME = "TestSwap"

if __name__ == "__main__":
    print(__file__)
    os.system(f"manim -pql {__file__} {SCENE_NAME}")

class TestTransform(Scene):
    def construct(self):
        circle = Circle().rotate(PI/2)
        square = Square()
        self.play(Create(circle))
        circle.rotate(-PI/4)

        self.play(Transform(circle, square))
        self.wait()

class T1(Scene):

    def construct(self):

        tex = MathTex(

            "\\frac{d}{dx}",  # 0

            "(",              # 1

            "u",              # 2

            "+",              # 3

            "v",              # 4

            ")=",             # 5

            "\\frac{d}{dx}",  # 6

            "u",              # 7

            "+",              # 8

            "\\frac{d}{dx}",  # 9

            "v"               # 10

        ).scale(2)
        self.play(
            Write(tex[:6])
        )

        steps = [
            [[2,3,4],
             [7,8,10]],
            [[0, 0],
             [6, 9]],
        ]
        for step in steps:
            from_, target = step
            self.play(*[ReplacementTransform(tex[i].copy(), tex[j])
                        for i,j in zip(from_, target)])
            self.wait()
        self.play(Uncreate(tex))
        self.wait()

class TestSwap(Scene):
    def setup(self):
        self.A = Square()
        self.B = Circle()
        self.G = VGroup(self.A,self.B).arrange(RIGHT, buff=LARGE_BUFF*2)
        self.add(self.G)

    def construct(self):
        self.play(*[
            Transform(self.A, self.A.copy().move_to(self.B.get_center())),
            Transform(self.B, self.B.copy().move_to(self.A.get_center())),

        ],run_time=2)
        self.wait()
        self.G[0], self.G[1] = self.G[1], self.G[0]
        self.play(self.G[0].animate.scale(2))
        self.play(self.G[1].animate.scale(0.5))
        self.wait()
