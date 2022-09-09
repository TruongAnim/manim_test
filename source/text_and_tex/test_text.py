from manim import *
import os

SCENE_NAME = "TestTexIndex"

if __name__ == "__main__":
    print(__file__)
    os.system(f"manim -pql {__file__} {SCENE_NAME}")


class Paragraph(Scene):
    def construct(self):
        t = Text(
            """
            Lorem Ipsum is simply dummy text of the printing and typesetting industry.
            Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
            when an unknown printer took a galley of type and scrambled it to make a
            type specimen book.
            """,
            line_spacing=1.3  # space between lines
        )
        t.width = config.frame_width - 1
        t[0].set_color(RED)
        self.add(t)


class MultipleFonts(Scene):
    def construct(self):
        xin_chao = Text("Xin chào Việt nam", font="Times New Roman")
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
        for i, mobj in enumerate(self.mobjects):
            mobj.shift(DOWN * (i - 3))


class MarkupTextTest(Scene):
    def construct(self):
        text = MarkupText(
            f'Normal <i>Italic</i> <b>Bold</b> <u>Underline</u> <span foreground="{BLUE}">Blue text</span>'
        )
        self.add(text)


class TexVsMathTex(Scene):
    def setup(self):
        #tex_environment="align*" by default
        math_tex = MathTex('a^2 + b^2 = c^2', tex_environment="align*")

        #tex_environment="center" by default
        tex = Tex('Hello', tex_environment="center")

        # formula within Tex => Error
        # tex2 = Tex('a^2', tex_environment="center")

        # formula within Tex => Need $ => $$formula$$
        tex3 = Tex('$$a^2$$', tex_environment="center")

        self.add(VGroup(math_tex, tex, tex3).arrange(DOWN))

class TestColorMap(Scene):
    def construct(self):
        t = Tex(
            "Hello my 3 ", "world",
            tex_to_color_map={
                "3": RED,
                "wor": ORANGE
            }
        )
        t2 = MathTex(
            "S = { 3 \over 2 }","{ \sqrt {{4}} a ^ 2 }",
            tex_to_color_map={
                "4": RED,
                "wor": ORANGE
            }
        )
        self.add(t2)

class TestTextIndex(Scene):
    def construct(self):
        text = Text("Hello world!")
        print(text.submobjects)
        def get_subindexes_from_text(text):
            return VGroup(*[
                Text(str(i), font_size=15, font="Times")
                .next_to(t, DOWN, buff=0.05)
                for i, t in enumerate(text)
            ])
        self.add(text, get_subindexes_from_text(text))

class TestTexIndex(Scene):
    def construct(self):
        source_tex = MathTex(r"\text{Area}=","\sqrt{", "s", "(", "s", "-", "a", ")(",
                       "s", "-", "b", ")(", "s", "-", "c", ")}","=4.01").scale(0.8)

        def get_sub_indexes(tex, color_tex=True):
            from itertools import cycle
            ni = VGroup()
            colors = cycle([RED, TEAL, GREEN, BLUE, PURPLE])
            for i in range(len(tex)):
                c = next(colors)
                n = Text(f"{i}", color=c).scale(0.3)
                n.next_to(tex[i], DOWN, buff=0.05)
                ni.add(n)
                if color_tex: tex[i].set_color(c)
            return ni
        self.add(source_tex, get_sub_indexes(source_tex))

class TestTex(Scene):
    def setup(self):
        pass
    def construct(self):
        from common.utils.mobject_utils import get_indexes
        color_map = {
            "h": GREEN,
            "b": BLUE
        }
        pytago1 = MathTex(r"S = {{h \times b} \over 2}", tex_to_color_map=color_map)
        pytago2 = MathTex(r"S = {3 \over 2}{\sqrt{3}a^2}",
                          tex_to_color_map=None)


        group = VGroup(pytago1)\
        .arrange(DOWN).shift(UP*2)

        self.add(group)
        self.add(*[get_indexes(i[4], color_tex=False) for i in group])