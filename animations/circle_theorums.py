from manim import *
import numpy as np


class CircleTheorems(Scene):
    def construct(self):
        self.theorem_2()

    def theorem_2(self):
        d = Dot().set_color(BLUE).move_to(3 * UP)
        dL = Dot().set_color(BLUE).move_to(3 * LEFT)
        dR = Dot().set_color(BLUE).move_to(3 * RIGHT)
        base = VGroup(
                Circle().scale(3).set_color(WHITE),
                Dot().set_color(BLUE),
                Line(dL.get_center(), dR.get_center())
        )

        moving_line1 = always_redraw(
            lambda: Line(d.get_center(), dL.get_center()).set_color(BLUE)
            .set_stroke(width=6)
        )

        moving_line2 = always_redraw(
            lambda: Line(d.get_center(), dR.get_center()).set_color(BLUE)
            .set_stroke(width=6)
        )

        moving_lines = VGroup(moving_line1, moving_line2)

        right_angle = always_redraw(
            lambda: Square().move_to(d.get_center(), aligned_edge=(DOWN + LEFT if d.get_center()[1] < 0 else UP + LEFT))
            .rotate( (-1 if d.get_center()[1] < 0 else 1) *
                -np.arctan(
                    abs(
                        (d.get_center()[0] - dL.get_center()[0]) /
                    (d.get_center()[1] - dL.get_center()[1])
                    )
                ),
                about_point=d.get_center()
            ).scale(
                0.20,
                about_point=d.get_center()
            )
        )

        self.play(
            Write(base),
            Write(moving_lines),
            Write(dL),
            Write(dR),
            Write(right_angle)
        )
        self.play(
            Rotate(d, 45 * DEGREES, about_point=ORIGIN),
            run_time=1.7
        )
        self.wait(0.7)
        self.play(
            Rotate(d, -70 * DEGREES, about_point=ORIGIN),
            run_time=1.7
        )
        self.wait(0.7)
        self.play(
            Rotate(d, -40 * DEGREES, about_point=ORIGIN),
            run_time=1.7
        )
        self.wait(0.7)
        self.play(
            Rotate(d, 65 * DEGREES, about_point=ORIGIN),
            run_time=1.7
        )
        self.wait(0.7)
        self.play(
            Rotate(d, -200 * DEGREES, about_point=ORIGIN),
            run_time=5.1
        )