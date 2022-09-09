import random

from manim import *
SCENE_NAME = "example"

if __name__ == "__main__":
    command = f"manim -pql {__file__} {SCENE_NAME}"
    print(command)
    os.system(command)


class CheckInside(Scene):
    def construct(self):
        A = np.array([0,0,0])
        B = np.array([1,1,0])
        C = np.array([2,0,0])
        D = np.array([2,-1,0])
        E = np.array([-0.3,-2,0])
        F = np.array([-1.5,0,0])
        ground = VMobject(fill_color=YELLOW, fill_opacity=0.5)\
            .set_points_smoothly([A,B,C,D,E,F,A])\

        point_num = 30
        border = [ground.point_from_proportion(i/point_num) for i in range(point_num)]
        dot = [Dot(border[i])
               for i in range(len(border))]
        line = [Line(start=border[i],end=border[i+1],
                     stroke_width=2,
                     color=RED)
                for i in range(len(border)-1)]

        target_dot = Dot(np.array([0.5,-2,0]), color = GREEN)
        nearest_point = 0
        length = np.linalg.norm(target_dot.get_center() - border[0])
        for index, i in enumerate(border):
            curr_length = np.linalg.norm(target_dot.get_center() - i)
            if curr_length < length:
                nearest_point = index
                length = curr_length
        nearest_dot = Dot(border[nearest_point], color=BLUE)
        self.add(ground, *dot, *line)
        print(nearest_point)
        first_vec = target_dot.get_center() - border[nearest_point]
        second_vec = border[nearest_point+1] - border[nearest_point]
        arrow1 = Arrow(border[nearest_point], target_dot.get_center(), buff=0.05, color=GREEN)
        arrow2 = Arrow(border[nearest_point], border[nearest_point+1], buff=0.05, color=BLUE)
        result = np.cross(first_vec, second_vec)
        print(result)
        if result[2] < 0:
            target_dot.set_color(RED)
        self.add(target_dot, nearest_dot, arrow1, arrow2)

class CheckInsideTest(Scene):
    def get_random_position(self):
        x = random.uniform(-2,2)
        y = random.uniform(-2,2)
        return np.array([x,y,0])
    def get_nearest_dot_index(self, target_dot):
        nearest_point = 0
        length = np.linalg.norm(target_dot.get_center() - self.border[0])
        for index, i in enumerate(self.border):
            curr_length = np.linalg.norm(target_dot.get_center() - i)
            if curr_length < length:
                nearest_point = index
                length = curr_length
        return nearest_point

    def construct(self):
        A = np.array([0,0,0])
        B = np.array([1,1,0])
        C = np.array([2,0,0])
        D = np.array([2,-1,0])
        E = np.array([-0.3,-2,0])
        F = np.array([-1.5,0,0])
        ground = VMobject(fill_color=YELLOW, fill_opacity=0.5)\
            .set_points_smoothly([A,B,C,D,E,F,A])\

        point_num = 50
        # self.border = [ground.point_from_proportion(i/point_num) for i in range(point_num)]
        self.border = ground.points
        dot = [Dot(self.border[i])
               for i in range(len(self.border))]
        line = [Line(start=self.border[i],end=self.border[i+1],
                     stroke_width=2,
                     color=RED)
                for i in range(len(self.border)-1)]
        dot_num = 1000
        dots = [Dot(self.get_random_position()) for i in range(dot_num)]
        for dot in dots:
            nearest_point = self.get_nearest_dot_index(dot)
            first_vec = dot.get_center() - self.border[nearest_point]
            second_vec = self.border[nearest_point] - self.border[nearest_point-1]
            cross = cross_product(first_vec, second_vec)
            if cross[2]>=0:
                dot.set_color(GREEN)
            else:
                dot.set_color(RED)

        border_lines = [Line(start=self.border[i], end=self.border[i+1], color=YELLOW, stroke_width=3)
                        for i in range(len(self.border)-1)]
        border_dots = [Dot(self.border[i], color=YELLOW, ).scale(0.5)
                        for i in range(len(self.border))]
        self.add(ground, *dots)
        self.add(*border_dots)


def cross_product(u, v):
    return np.array([u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2], u[0] * v[1] - u[1] * v[0]])

def dist(u, v):
    return np.sqrt((u[0] - v[0]) ** 2 + (u[1] - v[1]) ** 2)

def generate_list_of_points(shape):
    P = [shape.get_start()]
    T = np.linspace(0, 1, 20)
    for func in shape.get_curve_functions():
        for t in T:
            P.append(func(t))
    return np.array(P)

def closest_point(list, target):
    best = 0
    best_dist = dist(list[best], target)
    for i in range(len(list)):
        if dist(list[i], target) < best_dist:
            best = i
            best_dist = dist(list[best], target)
    return best

def is_in_shape(point, P_list):
    n = closest_point(P_list, point)
    l = len(P_list)
    tangent_vector = P_list[(n + 1) % l] - P_list[(n - 1) % l]
    to_target_vector = point - P_list[n]
    cross_product_res = cross_product(tangent_vector, to_target_vector)
    return cross_product_res[2] > 0

class example(MovingCameraScene):
    def get_random_position(self):
        x = random.uniform(-2,2)
        y = random.uniform(-2,2)
        return np.array([x,y,0])
    def construct(self):
        A1 = np.array([0, 0, 0])
        B1 = np.array([1, 1, 0])
        C1 = np.array([2, 0, 0])
        D1 = np.array([2, -1, 0])
        E1 = np.array([-0.3, -2, 0])
        F1 = np.array([-1.5, 0, 0])
        C = VMobject(fill_color=YELLOW, fill_opacity=0.5) \
            .set_points_smoothly([A1, B1, C1, D1, E1, F1, A1])
        dot_num = 100000
        dots = [Dot(self.get_random_position()).scale(0.1) for i in range(dot_num)]
        C_points = [C.point_from_proportion(t) for t in np.linspace(0, 1, 100)]
        # C_points = generate_list_of_points(C)
        D = Dot(radius=0.05).move_to([0.5, 0, 0])
        for dot in dots:
            if is_in_shape(dot.get_center(), C_points):
                dot.set_color(GREEN)
            else:
                dot.set_color(RED)
        self.add(C, *dots)
        # label = always_redraw(
        #     lambda: Text(f"{is_in_shape(D.get_center(), C_points)}", font_size=20).next_to(D))
        #
        # self.camera.frame.match_height(C).scale(2)
        #
        # for p in C_points:
        #     self.play(GrowFromCenter(Dot(p, radius=0.3)))
        #
        # self.add(C, D, label)
        # self.wait()
        # self.play(D.animate.move_to([1, 1, 0]), run_time=5)
        # self.wait()
        # self.play(D.animate.move_to([-1, -0.5, 0]), run_time=5)
        # self.wait()