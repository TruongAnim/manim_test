###
from manim import *
config.set_width = "80%"


SCENE_NAME = "T1"

if __name__ == "__main__":
    print(__file__)
    os.system(f"manim -pql {__file__} {SCENE_NAME}")

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

class TestTransform(Scene):
    def construct(self):
        circle = Circle().rotate(PI/2)
        square = Square()
        self.play(Create(circle))
        circle.rotate(-PI/4)

        self.play(Transform(circle, square))
        self.wait()
