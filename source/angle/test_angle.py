from manim import *

config.assets_dir = "./assets"
SCENE_NAME = "TestRightAngle"
DISABLE_CACHE = "--disable_caching"

if __name__ == "__main__":
    command = f"manim -pqm {__file__} {SCENE_NAME}"
    print(command)
    os.system(command)

class TestRightAngle(Scene):
    def construct(self):
        A = np.array([0, 3, 0])
        B = np.array([-1.5, 0, 0])
        C = np.array([2.5, 0, 0])
        D = np.array([4, 3, 0])
        H = ORIGIN
        K = np.array([4, 0, 0])
        line1 = Line(start=A, end=ORIGIN, stroke_width=1)
        line2 = Line(start=ORIGIN, end=K, stroke_width=1)
        rightangle = RightAngle(line1, line2, quadrant=(-1,1))
        self.play(Create(rightangle), Create(line1), Create(line2))