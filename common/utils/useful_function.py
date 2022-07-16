from manim import *

SCENE_NAME = "TestFuncion"

if __name__ == "__main__":
    command = f"manim -pql {__file__} {SCENE_NAME}"
    print(command)
    os.system(command)


class TestFuncion(Scene):
    def construct(self):
        points = [
            (0, 0, 0),
            (1, 1, 0),
            (2, 1, 0),
            (1, 2, 0)
        ]
        line = VMobject().set_points_as_corners(points)
        point = line.point_from_proportion(0.5)
        self.add(line)
        print(point)


# Get mid color from two color
mid_color = interpolate_color(RED, BLUE, 0.5)

# Get averange color from list
average_color_ = average_color(*[RED, GREEN, BLUE])

# Get a list of color along the list
gradient = color_gradient([RED, GREEN, BLUE], 10)

# Set a list object gradient color
# Use for group or text
Text("hello").set_color_by_gradient(*[RED, GREEN, BLUE])

# Set an object gradient color
Square().set_color([RED, GREEN, BLUE])

# Set how the gradient color affect
Square().set_sheen_direction(UP)

# Add background from an image
Square().color_using_background_image("facebook.png")

# Add line from given points
points = [
    (0, 0, 0),
    (1, 1, 0),
    (2, 1, 0),
    (1, 2, 0)
]
corner_line = VMobject().set_points_as_corners(points)

# Add smooth line from given points
smooth_line = VMobject().set_points_smoothly(points)

# Make the line smooth
corner_line.animate.make_smooth()

# Make the line jagged
smooth_line.animate.make_jagged()

# Concatenate more lines
line = VMobject()
another_line = VMobject().set_points_as_corners(points)
line.append_vectorized_mobject(another_line)

# Add more points
line.append_points(another_line.points)

# Get a point from line
point = line.point_from_proportion(0.5)

# Get a pa of a line
part_line = line.get_subcurve(0.3, 0.6)

# Save state and restore state of object
square = Square().save_state()
Restore(square) # self.play(Restore(square))
#=> opposite from generate_target() and MoveToTarget()

# Move a point along the path
MoveAlongPath(Dot(), part_line) #self.play(MoveAlongPath(Dot(), part_line))

# Create a rectangle surround an object
Rectangle().surround(square)
