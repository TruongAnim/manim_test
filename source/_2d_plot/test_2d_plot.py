from manim import *

config.assets_dir = "./assets"
SCENE_NAME = "TestDashedVMobject"
DISABLE_CACHE = "--disable_caching"

if __name__ == "__main__":
    command = f"manim -pqh {__file__} {SCENE_NAME}"
    print(command)
    os.system(command)


class Test2DPlot(Scene):
    def setup(self):
        import math
        print(math.sqrt(-1))
        Axes.c2p()

class TestDashedVMobject(Scene):
    def setup(self):
        dash_line = DashedVMobject(Line().rotate(PI/2), num_dashes=40, dashed_ratio=1)
        for index, i in enumerate(dash_line.submobjects):
            i.set_color(color=interpolate_color(RED,YELLOW, index/len(dash_line.submobjects)))
        self.add(dash_line)
        print(dash_line.submobjects)
