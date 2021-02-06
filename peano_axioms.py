from manimlib.imports import *
from tools.grid import ScreenGrid


class Peano(Scene):
    CONFIG = {
        "r": COLOR_MAP["RED_D"],
        "g": COLOR_MAP["GREEN_D"],
        "b": COLOR_MAP["BLUE_D"],
        "y_of_dots": 2.5 * DOWN,
        "y_of_nums": 3 * DOWN
    }

    def construct(self):
        grid = ImageMobject('tools/grid.png').scale(4)
        self.add(grid)

        # self.intro()
        self.axiom1()
        # self.axiom2()
        # self.axiom3()
        # self.axiom4()
        # self.axiom5()

    def intro(self):
        # Peano Axioms Title
        title = TextMobject("Peano Axioms")
        self.play(Write(title))
        self.wait(0.7)
        self.play(FadeOut(title))
        self.wait(0.5)

    def axiom1(self):
        # Add dot representing 0
        zero_dot = Dot()
        self.play(
            Write(zero_dot),
            run_time=0.5
        )
        self.wait(0.2)

        # Add text representing 0
        zero_text = TextMobject("0").move_to(self.y_of_nums)
        self.play(
            Write(zero_text),
            run_time=0.3
        )

        # Move zero dot down to zero text
        zero_dot.generate_target()
        zero_dot.target.move_to(self.y_of_dots)
        self.play(
            MoveToTarget(zero_dot),
            run_time=1
        )
        self.wait(0.7)

        # Add axiom text
        axiom1 = TextMobject("1. 0 is a natural number")
        self.play(Write(axiom1))
        self.wait(1)

        # Move axiom text to top left
        axiom1.generate_target()
        axiom1.target.scale(0.75).move_to(6.5*LEFT + 3.5*UP,
                                          aligned_edge=UP+LEFT).set_color(self.b)
        self.play(
            MoveToTarget(axiom1),
            run_time=1.65
        )
        self.wait(1)

    def axiom2(self):
        # Add n dot and corresponding text
        nDot = Dot().move_to(2 * RIGHT).set_color(self.g)
        nText = TextMobject("n").move_to(3 * DOWN + 2 * RIGHT).set_color(self.g)
        self.play(
            Write(nDot),
            run_time=0.5
        )
        self.wait(0.2)
        self.play(
            Write(nText),
            run_time=0.3
        )

        # Move n dot down to text
        nDot.generate_target()
        nDot.target.move_to(2.5 * DOWN + 2 * RIGHT)
        self.play(
            MoveToTarget(nDot),
            run_time=0.5
        )
        self.wait(0.5)

        # Add axiom text part 1
        axiom2 = TextMobject("2. If n is a natural number, then n++ "),

        self.play(Write(axiom2))

        # Move axiom text to top left
        axiom2.generate_target()
        axiom2.target.arrange(DOWN, aligned_edge=LEFT).scale(0.75).shift(3.7 * LEFT + 2.2 * UP).set_color(self.b)
        self.play(
            MoveToTarget(axiom2, run_time=1)
        )
        self.wait(0.5)

        #

    def axiom3(self):
        pass

    def axiom4(self):
        pass

    def axiom5(self):
        pass
