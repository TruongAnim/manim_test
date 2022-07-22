from manim import *
from common.custom.custom_animation import *
from common.custom.custom_rate_func import rate_func_from_bezier
from common.custom.custom_rate_func import parabola
from common.utils.custom_range import real_range

config.assets_dir = "./assets"
SCENE_NAME = "TestZoomAnimation"
DISABLE_CACHE = "--disable_caching"

if __name__ == "__main__":
    command = f"manim -pqh {__file__} {SCENE_NAME}"
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
        self.play(GrowFromPoint(circle, np.array([3, 3, 0])))
        self.wait()
        self.play(ShinkToPoint(circle, np.array([3, 3, 0])))
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


class TestShinkToCenter(Scene):
    def setup(self):
        self.hello = Text("Helllo world!")

    def construct(self):
        self.play(GrowFromCenter(self.hello))
        self.wait()
        self.play(ShrinkToCenter(self.hello))
        self.wait()


class TestCustomRateFunc(Scene):
    def setup(self):
        self.square = Square()

    def construct(self):
        handles = [1, 0, 0, 1]
        self.play(GrowFromCenter(self.square), rate_func=rate_func_from_bezier(handles, partitions=50), run_time=5)


class AnimationEx4(Scene):
    def setup(self):
        self.hello = Text("Hello world!")

    def construct(self):
        self.add(self.hello)
        handles = [.63, -0.91, .68, -0.89]
        rate_func = rate_func_from_bezier(handles)
        self.play(
            LaggedStart(
                *[ShinkToCenter(i, rate_func=rate_func) for i in self.hello]
            ),
            run_time=5
        )
        self.wait()


class TestZoomAnimation(Scene):
    def setup(self):
        pass

    def construct(self):
        dot = Dot()
        self.add(Dot(np.array([0, 3, 0])))
        self.add(dot)
        h = [0, 1.6, 1, 1.6]
        rate_func = rate_func_from_bezier(h, start_end=[0, 0])
        rf = [rate_func(i) for i in real_range(0, 1, 0.1, include=[True, True])]
        print(rf)
        self.play(dot.animate.shift(UP * 3),
                  rate_func=rate_func,
                  run_time=5)
        self.wait()
