from manim import *
from typing import Callable, Iterable, Optional, Tuple, Type, Union

class FillAndFade(Transform):
    def __init__(
        self,
        mobject: "Mobject",
        fill_color_: str = RED,
        rate_func: Callable[[float, Optional[float]], np.ndarray] = there_and_back,
        **kwargs
    ) -> None:
        self.fill_color_ = fill_color_
        super().__init__(mobject, rate_func=rate_func, **kwargs)

    def create_target(self) -> "Mobject":
        target = self.mobject.copy()
        target.set_fill(self.fill_color_, 0.8)
        return target