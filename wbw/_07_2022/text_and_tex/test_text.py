from manim import *
import os

class MultipleFonts(Scene):
    def construct(self):
        xin_chao = Text("Xin chào Việt nam",  font="Times New Roman")
        morning = Text("வணக்கம்", font="Arial")
        japanese = Text(
            "日本へようこそ", t2c={"日本": BLUE}
        )  # works same as ``Text``.
        mess = Text("Multi-Language", weight=BOLD, font="Arial")
        russ = Text("Здравствуйте मस नम म ", font="arial")
        hin = Text("नमस्ते", font="sans-serif")
        arb = Text(
            "صباح الخير \n تشرفت بمقابلتك", font="sans-serif"
        )  # don't mix RTL and LTR languages nothing shows up then ;-)
        chinese = Text("臂猿「黛比」帶著孩子", font="sans-serif")
        self.add(xin_chao, morning, japanese, mess, russ, hin, arb, chinese)
        for i,mobj in enumerate(self.mobjects):
            mobj.shift(DOWN*(i-3))

SCENE_NAME = "MultipleFonts"

if __name__ == "__main__":
    print(__file__)
    os.system(f"manim -pql {__file__} {SCENE_NAME}")