from manim import *

SCENE_NAME = "TestNumberLine"

if __name__ == "__main__":
    command = f"manim -pql {__file__} {SCENE_NAME}"
    print(command)
    os.system(command)


class TestNumberLine(Scene):
    def setup(self):
        line1 = NumberLine(x_range=[0, 10, 1])
        self.add(line1.set_stroke(width=1))
        self.add(MathTex(r"f(x)={x}^{2}").next_to(line1, DOWN))
