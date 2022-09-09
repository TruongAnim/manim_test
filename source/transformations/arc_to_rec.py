###
from manim import *

SCENE_NAME = "Scene1"

if __name__ == "__main__":
    command = f"manim -pql {__file__} {SCENE_NAME}"
    print(command)
    os.system(command)


class Scene1(Scene):
    def generate_rec(self, width=0.2):

        line_up = VMobject().set_points_as_corners(
            [LEFT*4 + RIGHT*i for i in range(9)])

        def add_width(point, width):
            return np.array([point[0], point[1]-width, point[2]])

        line_down = [add_width(i, width) for i in reversed(line_up.points)]
        rec = VMobject().append_points(line_up.points)
        rec.add_line_to(line_down[0])
        rec.append_points(line_down)
        rec.add_line_to(line_up.points[0])
        return rec

    def construct(self):
        arc = AnnularSector(start_angle=PI/2, angle=PI*2)
        line = self.generate_rec(1).shift(DOWN*2)
        print(len(arc.points))
        print(arc.points)
        print(len(line.points))
        print(line.points)
        self.play(Transform(arc, line), run_time=3,)

class PathAlongArcExample(Scene):


    def construct(self):
        colors = [RED, GREEN, BLUE]

        starting_points = VGroup(
            *[
                Dot(LEFT + pos, color=color)
                for pos, color in zip([UP, DOWN, LEFT], colors)
            ]
        )

        finish_points = VGroup(
            *[
                Dot(RIGHT + pos, color=color)
                for pos, color in zip([ORIGIN, UP, DOWN], colors)
            ]
        )

        self.add(starting_points)
        self.add(finish_points)
        for dot in starting_points:
            self.add(TracedPath(dot.get_center, stroke_color=dot.get_color()))

        self.wait()
        STRAIGHT_PATH_THRESHOLD = 0.01

        PATH_FUNC_TYPE = Callable[[np.ndarray, np.ndarray, float], np.ndarray]

        def path_along_arc(arc_angle: float, axis: np.ndarray = OUT) -> PATH_FUNC_TYPE:
            """This function transforms each point by moving it along a circular arc.

            Parameters
            ----------
            arc_angle
                The angle each point traverses around a circular arc.
            axis
                The axis of rotation.

            Examples
            --------

            .. manim :: PathAlongArcExample

                class PathAlongArcExample(Scene):
                    def construct(self):
                        colors = [RED, GREEN, BLUE]

                        starting_points = VGroup(
                            *[
                                Dot(LEFT + pos, color=color)
                                for pos, color in zip([UP, DOWN, LEFT], colors)
                            ]
                        )

                        finish_points = VGroup(
                            *[
                                Dot(RIGHT + pos, color=color)
                                for pos, color in zip([ORIGIN, UP, DOWN], colors)
                            ]
                        )

                        self.add(starting_points)
                        self.add(finish_points)
                        for dot in starting_points:
                            self.add(TracedPath(dot.get_center, stroke_color=dot.get_color()))

                        self.wait()
                        self.play(
                            Transform(
                                starting_points,
                                finish_points,
                                path_func=utils.paths.path_along_arc(TAU * 2 / 3),
                                run_time=3,
                            )
                        )
                        self.wait()

            """
            if abs(arc_angle) < STRAIGHT_PATH_THRESHOLD:
                return straight_path()
            if np.linalg.norm(axis) == 0:
                axis = OUT
            unit_axis = axis / np.linalg.norm(axis)

            def path(start_points: np.ndarray, end_points: np.ndarray, alpha: float):
                nonlocal arc_angle
                vects = end_points - start_points
                centers = start_points + 0.5 * vects
                print(start_points)
                obj = VMobject()
                obj.points = start_points
                if obj.get_center()[1] > 0:
                    arc_angle=-1*arc_angle
                if arc_angle != np.pi:
                    centers += np.cross(unit_axis, vects / 2.0) / np.tan(arc_angle / 2)
                rot_matrix = rotation_matrix(alpha * arc_angle, unit_axis)
                return centers + np.dot(start_points - centers, rot_matrix.T)

            return path
        self.play(
            Transform(
                starting_points[0],
                finish_points[0],
                path_func=path_along_arc(PI),
                # path_arc=TAU*2/3,
                run_time=3,
            )
        )
        self.wait()

class SceneTest(Scene):
    def construct(self):
        def func(angle):
            def sub_func():
                new_angle = angle
                if angle >5:
                    angle=-angle
                print(angle)

            return sub_func

        temp = func(10)
        temp()
