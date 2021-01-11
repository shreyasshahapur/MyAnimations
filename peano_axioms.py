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
        pass

    def axiom1(self):
        zero = Dot(3*DOWN)

    def axiom2(self):
        pass

    def axiom3(self):
        pass

    def axiom4(self):
        pass

    def axiom5(self):
        pass