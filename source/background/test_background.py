from manim import *

SCENE_NAME = "TestBackgroundJpg"

if __name__ == "__main__":
    command = f"manim -pqm -t -o transparent_png --disable_caching {__file__} {SCENE_NAME}"
    print(command)
    os.system(command)

config.assets_dir="./assets"

#Transperent video need to edit this
#1: add -t to command line

#2: class: SceneFileWriter
# .mov format
# elif config["transparent"]:
# command += ["-vcodec", "qtrle"] => ["-vcodec", "png"]

class TestBackgroundJpg(Scene):
    config.background_color = BLACK
    def setup(self):
        img = ImageMobject("green_bg.jpg")
        # self.add(img)
        print(config.pixel_width, config.pixel_height)

    def construct(self):
        group = VGroup(Square(), Circle(), Triangle(),
                       Text("Hello world!"),
                       MathTex("a^2+b^2=c^2"))
        group.arrange_in_grid(cols=3)
        self.play(Write(group), run_time=5)
        self.wait()