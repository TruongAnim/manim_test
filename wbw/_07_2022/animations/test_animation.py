from manim import *
from common.custom.custom_animation import *

config.assets_dir = "./assets"
SCENE_NAME = "TestGrowFromEdge"

if __name__ == "__main__":
    command = f"manim -pql --disable_caching {__file__} {SCENE_NAME}"
    print(command)
    os.system(command)


class TestLoadSvg(Scene):
    def setup(self):
        t = SVGMobject("facebook").set_color(RED)
        self.add(t)


class TestStroke(Scene):
    def construct(self):
        circle = Circle(stroke_width=1)
        self.play(Create(circle))

class TestGrowFromPoint(Scene):
    import numpy as np
    def setup(self):
        pass

    def construct(self):
        circle = Circle()
        self.play(GrowFromPoint(circle, np.array([3,3,0])))
        self.wait()
        self.play(ShinkToPoint(circle, np.array([3,3,0])))
        self.wait()

class TestGrowFromEdge(Scene):
    def setup(self):
        pass

    def construct(self):
        circle = Circle()
        self.play(GrowFromEdge(circle, UP))
        self.wait()
        self.play(ShinkToEdge(circle, UP))
        self.wait()
