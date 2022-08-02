from manim import *
from common.custom.custom_animation import *
from common.custom.custom_rate_func import rate_func_from_bezier
from common.custom.custom_rate_func import parabola
from common.utils.range_utils import real_range

config.assets_dir = "./assets"
SCENE_NAME = "TestRotating"
DISABLE_CACHE = "--disable_caching"

if __name__ == "__main__":
    command = f"manim -pqp {__file__} {SCENE_NAME}"
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

class TargetVsCopy(Scene):
    def construct(self):
        source_left = Dot()
        source_right = source_left.copy()

        VGroup(source_left, source_right).arrange(RIGHT, buff=3)

        # Left side - MoveToTarget ----------------
        source_left.generate_target()
        # Manupulate the .target attr
        source_left.target.set_style(
            fill_color=TEAL,
            stroke_width=10,
            stroke_color=ORANGE
        )
        source_left.target.scale(7)
        source_left.target.to_edge(UP)
        # Right side - Manually ----------------
        source_right_target = source_right.copy()
        source_right_target.set_style(
            fill_color=TEAL,
            stroke_width=10,
            stroke_color=ORANGE
        )
        source_right_target.scale(7)
        source_right_target.to_edge(UP)

        # Animations
        self.add(source_left, source_right)
        self.play(
            MoveToTarget(source_left),
            Transform(source_right, source_right_target),
            run_time=3
        )
        self.wait()

class TestApplyFunction(Scene):
    def construct(self):
        source = Dot()

        def custom_func(mob):
            mob.set_style(
                fill_color=TEAL,
                stroke_width=10,
                stroke_color=ORANGE
            )
            mob.scale(7)
            mob.to_edge(UP)
            # Don't forget return mob
            return mob

        self.add(source)

        self.play(
            ApplyFunction(custom_func, source),
            run_time=3
        )
        self.wait()

class TestClosures(Scene):
    def construct(self):
        source = VGroup(Dot(), Square(), Circle(), Text("A")) \
            .arrange(RIGHT, buff=2)

        self.add(source)

        self.play(
            ApplyFunction(self.custom_method(scale=7, edge=DOWN), source[0]),  # Dot
            ApplyFunction(self.custom_method(fill_color=PURPLE), source[1]),  # Square
            ApplyFunction(self.custom_method(fill_opacity=0), source[2]),  # Circle
            ApplyFunction(self.custom_method(edge=LEFT), source[3]),  # Text("A")
            run_time=3
        )
        self.wait()

    def custom_method(self,
                      fill_color=TEAL,
                      fill_opacity=1,
                      stroke_width=10,
                      stroke_color=ORANGE,
                      scale=3,
                      edge=UP,
                      ):
        def custom_func(mob):
            mob.set_style(
                fill_color=fill_color,
                fill_opacity=fill_opacity,
                stroke_width=stroke_width,
                stroke_color=stroke_color,
            )
            mob.scale(scale)
            mob.to_edge(edge)
            # Don't forget return mob
            return mob

        # Don't forget return the func
        return custom_func

class TestRotating(Scene):
    def construct(self):
        angles = [10, 30, 60, 90, 120]
        mobs = VGroup(*[
            VGroup(MathTex(f"{angle}^\\circ"), Square())
                      .arrange(DOWN, buff=1)
            for angle in angles
        ]).arrange(RIGHT, buff=0.7)

        self.add(mobs)
        self.play(
            *[
                # mob[0] is the MathTex and
                # mob[1] is the Square()
                Rotating(mob[1], radians=angle * PI / 180)
                for mob, angle in zip(mobs, angles)
            ],
            run_time=3
        )
        self.wait()
