from manim import *

# NEED TO RECONFIGURE FOR MANIMCE
class Peano(Scene):
    CONFIG = {
        "r": COLOR_MAP["RED_D"],
        "g": COLOR_MAP["GREEN_D"],
        "g2": COLOR_MAP["GREEN_E"],
        "t": COLOR_MAP["TEAL_D"],
        "b": COLOR_MAP["BLUE_D"],
        "y_of_dots": 1.75 * DOWN,
        "y_of_nums": 2.25 * DOWN,

        "title_text": TextMobject("Peano Axioms"),
        "axiom1_text": TextMobject("1. 0 is a natural number"),
        "axiom2_first_temp_text": TextMobject("2. If n is a natural number..."),
        "axiom2_first_text": TextMobject("2. If n is a natural number, "),
        "axiom2_last_text": TextMobject("then n++ is a natural number"),
        "axiom3_text": TextMobject("3. 0 is not the successor of any natural number"),
        "axiom4_first_temp_text": TextMobject("4. If n, m are natural numbers and n ≠ m..."),
        "axiom4_first_text": TextMobject("4. If n, m are natural numbers and n ≠ m,"),
        "axiom4_second_text": TextMobject("then n++ ≠ m++"),
        "axiom4_third_temp_text": TextMobject("equivalently, if n++ = m++..."),
        "axiom4_third_text": TextMobject("equivalently, if n++ = m++,"),
        "axiom4_fourth_text": TextMobject("then n = m"),
        "axiom4_final_text": TextMobject("4. Different natural numbers must have different successors"),

        "zero_dot": Dot(),
        "zero_num": TextMobject("0"),
        "n_dot": Dot(),
        "n_num": TextMobject("n"),
        "succ_n_dot": Dot(),
        "succ_n_num": TextMobject("n++"),
        "m_dot": Dot(),
        "m_num": TextMobject("m"),
        "succ_m_dot": Dot(),
        "succ_m_num": TextMobject("m++"),
    }

    def construct(self):
        # grid = ImageMobject('tools/grid.png').scale(4)
        # self.add(grid)

        # self.intro()
        self.axiom1()
        self.axiom2()
        self.axiom3()
        # self.axiom4()
        # self.axiom5()

    def intro(self):
        # Peano Axioms Title
        self.play(Write(self.title_text))
        self.wait(0.7)
        self.play(FadeOut(self.title_text))
        self.wait(0.5)

    def axiom1(self):
        # Add dot representing 0
        self.play(
            Write(self.zero_dot),
            run_time=0.5
        )
        self.wait(0.2)

        # Add text representing 0
        self.zero_num.move_to(self.y_of_nums)
        self.play(
            Write(self.zero_num),
            run_time=0.3
        )

        # Move zero dot down to zero text
        self.zero_dot.generate_target()
        self.zero_dot.target.move_to(self.y_of_dots)
        self.play(
            MoveToTarget(self.zero_dot),
            run_time=1
        )
        self.wait(0.7)

        # Add axiom text
        self.play(Write(self.axiom1_text))
        self.wait(1)

        # Move axiom text to top left
        self.axiom1_text.generate_target()
        self.axiom1_text.target.scale(0.75).move_to(6.5 * LEFT + 3.3 * UP,
                                                    aligned_edge=UP + LEFT).set_color(self.b)
        self.play(
            MoveToTarget(self.axiom1_text),
            run_time=1.65
        )
        self.wait(1)

    def axiom2(self):
        # x pos of n dot and n num
        x_of_n = 2 * RIGHT

        # Add dot representing n
        self.n_dot.move_to(x_of_n).set_color(self.g)
        self.play(
            Write(self.n_dot),
            run_time=0.5
        )
        self.wait(0.2)

        # Add text representing n
        self.n_num.move_to(x_of_n + self.y_of_nums).set_color(self.g)
        self.play(
            Write(self.n_num),
            run_time=0.3
        )

        # Move n dot down to text
        self.n_dot.generate_target()
        self.n_dot.target.move_to(x_of_n + self.y_of_dots)
        self.play(
            MoveToTarget(self.n_dot),
            run_time=1
        )
        self.wait(0.7)

        # Add first part of axiom text
        self.play(Write(self.axiom2_first_temp_text))
        self.wait(0.5)

        # Move axiom text to top left
        self.play(
            ReplacementTransform(
                self.axiom2_first_temp_text,
                self.axiom2_first_text.scale(0.75).next_to(self.axiom1_text, DOWN, aligned_edge=LEFT)
                    .set_color(self.b)
            )
        )
        self.wait(0.5)

        x_of_succ_n = 3.5 * RIGHT

        # Add dot representing n++
        self.succ_n_dot.move_to(x_of_succ_n).set_color(self.t)
        self.play(
            Write(self.succ_n_dot),
            run_time=0.5
        )
        self.wait(0.2)

        # Add text representing n
        self.succ_n_num.move_to(x_of_succ_n + self.y_of_nums).set_color(self.t)
        self.play(
            Write(self.succ_n_num),
            run_time=0.3
        )

        # Move n dot down to text
        self.succ_n_dot.generate_target()
        self.succ_n_dot.target.move_to(x_of_succ_n + self.y_of_dots)
        self.play(
            MoveToTarget(self.succ_n_dot),
            run_time=1
        )
        self.wait(0.7)

        # Add second part of axiom text
        self.play(Write(self.axiom2_last_text))
        self.wait(0.7)

        # Move axiom text to top left
        self.axiom2_last_text.generate_target()
        self.axiom2_last_text.target.scale(0.75).next_to(self.axiom2_first_text, DOWN, buff=0.1, aligned_edge=LEFT) \
            .set_color(self.b)
        self.play(
            MoveToTarget(self.axiom2_last_text),
            run_time=1
        )
        self.wait(1)

    def axiom3(self):
        axiom3_motivations = TextMobject("Though right now, n++ can be anywhere...")
        self.play(Write(axiom3_motivations))
        self.wait(0.5)

        succ_n = VGroup(self.succ_n_dot, self.succ_n_num)

        succ_n.generate_target()
        succ_n.target.shift(8 * LEFT)
        self.play(
            MoveToTarget(succ_n),
            FadeOut(axiom3_motivations),
            run_time=2
        )
        self.wait(0.5)

        succ_n.generate_target()
        succ_n.target.shift(5.5 * RIGHT)
        self.play(MoveToTarget(succ_n), run_time=2)
        self.wait(0.5)

        succ_n.generate_target()
        succ_n.target.shift(3.5 * RIGHT)
        self.play(MoveToTarget(succ_n), run_time=2)
        self.wait(0.5)

        axiom3_motivations = TextMobject("...meaning it can be on zero!")
        self.play(Write(axiom3_motivations))
        self.wait(1)

        succ_n.generate_target()
        succ_n.target.shift(4.5*LEFT).set_color(self.r)
        self.play(
            MoveToTarget(succ_n),
            FadeOut(self.zero_num),
            run_time=2
        )
        self.wait(1)

        axiom3_motivations.generate_target()
        axiom3_motivations_1 = TextMobject("This shouldn't be allowed,")
        axiom3_motivations_2 = TextMobject("leading us to the third axiom...").next_to(axiom3_motivations_1, DOWN)
        axiom3_motivations.target = VGroup(axiom3_motivations_1, axiom3_motivations_2)
        self.play(MoveToTarget(axiom3_motivations))
        self.wait(3.5)

        self.play(ReplacementTransform(axiom3_motivations, self.axiom3_text))

        succ_n.generate_target()
        succ_n.target.shift(3.5 * RIGHT).set_color(self.t)
        self.play(
            MoveToTarget(succ_n),
            Write(self.zero_num),
            run_time=2
        )
        self.wait(1)

        self.axiom3_text.generate_target()
        axiom3_text_1 = TextMobject("3. 0 is not the successor of")
        axiom3_text_2 = TextMobject("any natural number").next_to(axiom3_text_1, DOWN, buff=0.1, aligned_edge=LEFT)

        self.axiom3_text.target = VGroup(axiom3_text_1, axiom3_text_2)\
            .scale(0.75)\
            .next_to(self.axiom2_last_text, DOWN, aligned_edge=LEFT)\
            .set_color(self.b)

        self.play(
            MoveToTarget(self.axiom3_text),
            run_time=1
        )

    def axiom4(self):
        pass

    def axiom5(self):
        pass
