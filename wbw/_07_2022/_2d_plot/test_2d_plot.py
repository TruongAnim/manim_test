from manim import *

config.assets_dir = "./assets"
SCENE_NAME = "Test2DPlot"
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
