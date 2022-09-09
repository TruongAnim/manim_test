import random

from manim import *
import os

SCENE_NAME = "Scene7"

if __name__ == "__main__":
    print(__file__)
    os.system(f"manim --disable_caching -c production.cfg {__file__} {SCENE_NAME}")

class MyScene(Scene):
    def my_play(
            self,
            *args,
            subcaption=None,
            subcaption_duration=None,
            subcaption_offset=0,
            **kwargs,
    ):
        if "run_time" not in kwargs:
            kwargs["run_time"] = 2
        super().play(*args,
                     subcaption=subcaption,
                     subcaption_duration=subcaption_duration,
                     subcaption_offset=subcaption_offset,
                     **kwargs)
        self.wait()


def cross_product(u, v):
    return np.array([u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2], u[0] * v[1] - u[1] * v[0]])


def dist(u, v):
    return np.sqrt((u[0] - v[0]) ** 2 + (u[1] - v[1]) ** 2)


def closest_point(list, target):
    best = 0
    best_dist = dist(list[best], target)
    for i in range(len(list)):
        if dist(list[i], target) < best_dist:
            best = i
            best_dist = dist(list[best], target)
    return best


def is_in_shape(point, P_list, greater_than_one):
    n = closest_point(P_list, point)
    l = len(P_list)
    tangent_vector = P_list[(n + 1) % l] - P_list[(n - 1) % l]
    to_target_vector = point - P_list[n]
    cross_product_res = cross_product(tangent_vector, to_target_vector)
    if greater_than_one:
        return cross_product_res[2] >= 0
    else:
        return cross_product_res[2] <= 0


myTemplate = TexTemplate()
myTemplate.add_to_preamble(r"\usepackage{vntex}")
rel_obj = 50000
rel_time = 20
test_obj = 1000
test_time = 3

class Scene7(MyScene):
    def get_random_position(self):
        x = random.uniform(-2.5, 2.5)
        y = random.uniform(-2.5, 2.5)
        return np.array([x, y, 0])

    def construct(self):
        square = Square(side_length=5, stroke_color=ORANGE)
        shape = SVGMobject("bitcoin3",
                           stroke_color=ORANGE,
                           stroke_width=2).scale(2.2)
        brace = Brace(square, UP)
        side = brace.get_tex("a=", "5(m)")

        self.my_play(DrawBorderThenFill(shape))
        self.my_play(Write(square))
        self.my_play(FadeIn(brace, shift=DOWN), FadeIn(side, shift=DOWN))
        num_point = 200
        sub_point = 30
        list_point1 = [shape[0].point_from_proportion(i / num_point)
                      for i in range(num_point)]
        list_point2 = [shape[1].point_from_proportion(i / sub_point)
                      for i in range(sub_point)]
        list_point3 = [shape[2].point_from_proportion(i / sub_point)
                      for i in range(sub_point)]

        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{vntex}")

        formula = MathTex(
            r"S_",  # 0
            r"{ab}",  # 1
            r"\approx",  # 2
            r"{\text{aaaaaaaa}",  # 3
            r"\over",  # 4
            r"\text{aaaaaaaa}}",  # 5
            r"\times",  # 6
            r"25(m^2)",  # 7
            tex_template=myTemplate
        ).scale(0.7).shift(LEFT * 4.7)
        for i in (1, 3, 5):
            formula[i].set_color(BLACK)
        s_shape = shape.copy() \
            .set_stroke(width=0) \
            .set_fill(color=ORANGE, opacity=1) \
            .scale(0.05) \
            .move_to(formula[1])
        s_shape[1].set_fill(color=WHITE)
        s_shape[2].set_fill(color=WHITE)

        formula2 = formula[2].copy().shift(DOWN)
        formula3 = formula[7].copy().shift(DOWN + LEFT)

        self.my_play(LaggedStart(*[
            Write(formula),
            Write(s_shape),
            Write(formula2),
            Write(formula3[2:])
        ], lag_ratio=0.3))

        self.num_dot = 0
        self.num_green = 0

        tracker = ValueTracker(0)

        def draw_tex():
            dot_green = Text(str(self.num_green),
                             color=GREEN,
                             font_size=30,
                             font="Arial") \
                .scale(0.8) \
                .move_to(formula[3])
            dot_total = Text(str(self.num_dot),
                             color=RED,
                             font_size=30,
                             font="Arial") \
                .scale(0.8) \
                .move_to(formula[5])
            result = "0.0000"
            if self.num_dot != 0:
                result = "{:.5f}".format(25 * self.num_green / self.num_dot)
            s = Text(result,
                     color=YELLOW,
                     font_size=30,
                     font="Arial") \
                .scale(0.7) \
                .next_to(formula2, RIGHT, aligned_edge=LEFT)
            return VGroup(dot_green, dot_total, s)

        group = always_redraw(draw_tex)

        self.add(tracker, group)

        def update(obj):
            value = tracker.get_value()
            if int(value) > self.num_dot:
                more_point = int(value) - self.num_dot
                self.num_dot = int(value)
                for i in range(more_point):
                    dot = Square(side_length=0.01, stroke_width=2).move_to(self.get_random_position())
                    if is_in_shape(dot.get_center(), list_point1, True) \
                            and is_in_shape(dot.get_center(), list_point2, True) \
                            and is_in_shape(dot.get_center(), list_point3, True):
                        dot.set_color(ORANGE)
                        self.num_green += 1
                    else:
                        dot.set_color(WHITE)
                    self.add(dot)

        shape.add_updater(update)

        self.my_play(tracker.animate.increment_value(rel_obj),
                  run_time=rel_time,
                  rate_func=linear)
        self.my_play(Circumscribe(group[2]))
