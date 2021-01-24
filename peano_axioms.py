from manimlib.imports import *

class Peano(Scene):
    CONFIG = {
            "r":COLOR_MAP["RED_D"],
            "g":COLOR_MAP["GREEN_D"],
            "b":COLOR_MAP["BLUE_D"]
        }
    
    def construct(self):
        self.intro()
        self.axiom1()
        self.axiom2()
        self.axiom3()
        self.axiom4()
        self.axiom5()

    def intro(self):
        # Peano Axioms Title
        title = TextMobject("Peano Axioms")
        self.play(Write(title))
        self.wait(0.7)
        self.play(FadeOut(title))
        self.wait(0.5)

    def axiom1(self):
        # Add axiom text
        axiom1 = TextMobject("1. 0 is a natural number")
        self.play(Write(axiom1))
        
        # Move axiom text to top left
        axiom1.generate_target()
        axiom1.target.scale(0.75).shift(4.8*LEFT + 3*UP).set_color(self.b)
        self.play(
            MoveToTarget(axiom1, run_time=1)
        )
        self.wait(0.5)

        # Add dot and text representing 0 
        zeroDot = Dot()
        zeroNum = TextMobject("0").move_to(3*DOWN)
        self.play(
            Write(zeroDot), 
            run_time = 0.5
            )
        self.wait(0.2)
        self.play(
            Write(zeroNum), 
            run_time = 0.3
            )

        # Move zero dot down to text
        zeroDot.generate_target()
        zeroDot.target.move_to(2.5*DOWN)
        self.play(
            MoveToTarget(zeroDot),
            run_time = 0.5
        )

    def axiom2(self):
        pass

    def axiom3(self):
        pass

    def axiom4(self):
        pass

    def axiom5(self):
        pass