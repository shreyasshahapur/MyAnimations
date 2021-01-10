from manimlib.imports import *

class Pythagorus(Scene):
    CONFIG = {
            "r":COLOR_MAP["RED_D"],
            "g":COLOR_MAP["GREEN_D"],
            "b":COLOR_MAP["BLUE_D"]
        }

    def construct(self):
        # Make a triangle
        t = Polygon(np.array([0,0,0]), 4*RIGHT, 3*UP)
        t.scale(0.5, about_point=ORIGIN)
        self.play(Write(t))

        # Adding letters
        a = TexMobject("a")
        b = TexMobject("b")
        c = TexMobject("c")
        a.move_to(0.75*UP+0.25*LEFT).scale(0.8)
        b.move_to(1*RIGHT+0.25*DOWN).scale(0.8)
        c.move_to(1.15*RIGHT+0.95*UP).scale(0.8)
        self.play(
            Write(a),
            Write(b),
            Write(c)
        )

        # Make squares
        s1 = Square(side_length = 4).set_color(self.r)
        s2 = Square(side_length = 3).set_color(self.g)
        s3 = Square(side_length = 5).set_color(self.b)
        s1.move_to(2*RIGHT+2*DOWN)
        s2.move_to(1.5*LEFT+1.5*UP)
        s3.move_to(1.5*RIGHT+2.5*UP)
        s3.rotate(-np.arctan(3/4), about_point=4*RIGHT)
        s1.scale(0.5, about_point=ORIGIN)
        s2.scale(0.5, about_point=ORIGIN)        
        s3.scale(0.5, about_point=ORIGIN)
        self.play(
            Write(s1),
            Write(s2),
            Write(s3)
            ) 
        self.wait(1)

