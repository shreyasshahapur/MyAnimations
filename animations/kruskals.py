from manim import *
from tools.basic_graph import BasicGraph
from tools.show_positional_values_2D import *

class Temp(Scene):

    def construct(self):
        l = Line()
        t = Text("8")
        t.next_to(l, DOWN)
        self.add(l, t)



class Kruskals(Scene):

    def construct(self):
        vertices = {"A": [-4, 0], "B": [0, -3], "C": [0, 0], "D": [3, 4],
                    "E": [7, 0], "F": (6, -3), "G": (10, 2), "H": [11, 0]}
        edges = [("A", "B"), ("A", "C"), ("A", "D"),
                 ("B", "C"), ("B", "F"),
                 ("C", "D"), ("C", "E"),
                 ("D", "E"),
                 ("E", "F"),
                 ("E", "G"),
                 ("E", "H"),
                 ("G", "H")]

        g1 = BasicGraph(
            vertices=vertices.copy(),
            edges=edges.copy(),
            vertex_and_label_scale=1.3,
            weight={("A", "B"): [5, (-0.35, -0.35)]}
        ).save_state()

        self.play(
            ShowCreation(g1.scale(0.7, about_point=ORIGIN).shift(2.2*LEFT))
        )

