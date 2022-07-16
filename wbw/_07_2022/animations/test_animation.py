from manim import *
config.assets_dir = "./assets"
SCENE_NAME = "TestStroke"

if __name__ == "__main__":
    command = f"manim -pql {__file__} {SCENE_NAME}"
    print(command)
    os.system(command)

class TestLoadSvg(Scene):
    def setup(self):
        t = SVGMobject("facebook").set_color(RED)
        self.add(t)

class TestStroke(Scene):
    def construct(self):
        circle = Circle(stroke_width=0)
        self.play(Create(circle))