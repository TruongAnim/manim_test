###
from manim import *
config.set_width = "80%"

class TestTransform(Scene):
    def construct(self):
        circle = Circle().rotate(PI/2)
        square = Square()
        self.play(Create(circle))
        circle.rotate(-PI/4)
        self.play(Transform(circle, square))
        self.wait()

SCENE_NAME = "TestTransform"

if __name__ == "__main__":
    print(__file__)
    os.system(f"manim -pql {__file__} {SCENE_NAME}")