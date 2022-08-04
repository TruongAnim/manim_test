from manim import *

config.background_color = GREEN

#manim -pqm -c config.cfg test_manim_cfg.py TestManimCfg

class TestManimCfg(Scene):
    def setup(self):
        pass

#manim -pqm test_manim_cfg.py TestManimCfg RenderMultipleScene

class RenderMultipleScene(Scene):
    config.disable_caching = True
    def setup(self):
        pass