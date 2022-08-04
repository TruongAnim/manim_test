from manim import *
from manim_lexer import ManimLexer
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from monokai_colors import ManimMonokaiStyle
import re

class PreCode(Code):
    def ensure_valid_file(self):
        """Function to validate file."""
        if self.file_name is None:
            raise Exception("Must specify file for Code")
        possible_paths = [
            os.path.join(self.file_name), #<<- this change
            self.file_name,
        ]
        for path in possible_paths:
            if os.path.exists(path):
                self.file_path = path
                return
        error = (
            f"From: {os.getcwd()}, could not find {self.file_name} at either "
            + f"of these locations: {possible_paths}"
        )
        raise OSError(error)

    def gen_html_string(self):
        """Function to generate html string with code highlighted and stores in variable html_string."""
        self.html_string = hilite_me_manim(
            self.code_string,
            self.language,
            self.style,
            self.insert_line_no,
            "border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;",
            self.file_path,
            self.line_no_from,
            self.lexer,
        )

        if self.generate_html_file:
            os.makedirs(
                os.path.join("assets", "codes", "generated_html_files"),
                exist_ok=True,
            )
            with open(
                os.path.join(
                    "assets",
                    "codes",
                    "generated_html_files",
                    self.file_name + ".html",
                ),
                "w",
            ) as file:
                file.write(self.html_string)


class ManimCode(PreCode):
    def __init__(self,
                font="Monospace",
                style="monokai",
                insert_line_no=False,
                line_spacing=0.5,
                tab_width=4,
                background="window",
                lexer=ManimLexer(),
                **kwargs):
        self.lexer = lexer
        super().__init__(
            font=font,
            style=style,
            tab_width=tab_width,
            language="python",
            background=background,
            insert_line_no=insert_line_no,
            line_spacing=line_spacing,
            **kwargs
        )

    


def insert_line_numbers_in_html(html, line_no_from):
    """Function that inserts line numbers in the highlighted HTML code.

    Parameters
    ---------
    html : :class:`str`
        html string of highlighted code.
    line_no_from : :class:`int`
        Defines the first line's number in the line count.

    Returns
    -------
    :class:`str`
        The generated html string with having line numbers.
    """
    match = re.search("(<pre[^>]*>)(.*)(</pre>)", html, re.DOTALL)
    if not match:
        return html
    pre_open = match.group(1)
    pre = match.group(2)
    pre_close = match.group(3)

    html = html.replace(pre_close, "</pre></td></tr></table>")
    numbers = range(line_no_from, line_no_from + pre.count("\n") + 1)
    format_lines = "%" + str(len(str(numbers[-1]))) + "i"
    lines = "\n".join(format_lines % i for i in numbers)
    html = html.replace(
        pre_open,
        "<table><tr><td>" + pre_open + lines + "</pre></td><td>" + pre_open,
    )
    return html


def hilite_me_manim(
    code,
    language,
    style,
    insert_line_no,
    divstyles,
    file_path,
    line_no_from,
    lexer
):
    """Function to highlight code from string to html.

    Parameters
    ---------
    code : :class:`str`
        Code string.
    language : :class:`str`
        The name of the programming language the given code was written in.
    style : :class:`str`
        Code style name.
    insert_line_no : :class:`bool`
        Defines whether line numbers should be inserted in the html file.
    divstyles : :class:`str`
        Some html css styles.
    file_path : :class:`str`
        Path of code file.
    line_no_from : :class:`int`
        Defines the first line's number in the line count.
    """
    style = style or "colorful"
    defstyles = "overflow:auto;width:auto;"

    formatter = HtmlFormatter(
        style=ManimMonokaiStyle, # <<== STYLE
        linenos=False,
        noclasses=True,
        cssclass="",
        cssstyles=defstyles + divstyles,
        prestyles="margin: 0",
    )
    if language is None and file_path:
        # lexer_ = guess_lexer_for_filename(file_path, code)
        html = highlight(code, lexer, formatter)
    elif language is None:
        raise ValueError(
            "The code language has to be specified when rendering a code string",
        )
    else:
        html = highlight(code, lexer, formatter)
    if insert_line_no:
        html = insert_line_numbers_in_html(html, line_no_from)
    html = "<!-- HTML generated by Code() -->" + html
    return html