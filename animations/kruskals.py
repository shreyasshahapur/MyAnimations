from manim import *
from tools.basic_graph import BasicGraph
from tools.show_positional_values_2D import *


class KruskalsIntro(Scene):

    def construct(self):
        text = Tex("Kruskal's Algorithm also called "
                   "the greedy algorithm", font="futura"
                   )
        text2 = Tex("it is used to find the Minimum Spanning Tree.",
                    font="futura") \
            .next_to(text, DOWN)
        self.add(
            text,
            text2)


class Kruskals1(Scene):

    def construct(self):
        vertices = {"A": (-8, 2), "B": [-3, 5], "C": [0, 0],
                    "D": [-3, -2], "E": [1, -2], "F": [3, 2]}

        edges = (("A", "B"), ("A", "D"), ("B", "C"), ("B", "F"), ("C", "D"),
                 ("C", "F"), ("E", "F"), ("D", "E"))

        weights = {("A", "B"): [5, (-0.35, 0.6)], ("A", "D"): [6, (-0.5, -0.5)],
                   ("B", "C"): [6, (-0.35, -0.6)], ("B", "F"): [7, (0.5, 0.5)],
                   ("C", "D"): [3, (-0.5, 0.5)], ("C", "F"): [3, (-0.5, 0.5)],
                   ("E", "F"): [5, (0.5, 0)], ("D", "E"): [4, (0, -0.5)]}

        g1 = BasicGraph(
            vertices=vertices,
            edges=edges,
            vertex_and_label_scale=1.3,
            weight=weights

        ).scale(0.5, about_point=ORIGIN).save_state()

        self.play(ShowCreation(g1))
        # self.add(g1)


class KruskalsMSTCreation(Scene):

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

        weight = {("A", "B"): [5, (-0.35, -0.35)], ("A", "C"): [4, (0.35, 0.5)],
                  ("A", "D"): [8, (-0.35, 0.35)], ("B", "C"): [3, (0.35, 0)],
                  ("B", "F"): [6, (0, 0.5)], ("C", "D"): [5, (0.35, -0.35)],
                  ("C", "E"): [7, (0, 0.5)], ("D", "E"): [6, (0.35, 0.35)],
                  ("E", "F"): [3, (0.35, 0)], ("E", "G"): [3, (0, 0.5)],
                  ("E", "H"): [4, (0, -0.5)], ("G", "H"): [1, (0.35, 0.25)]}

        g1 = BasicGraph(
            vertices=vertices.copy(),
            edges=edges,
            vertex_and_label_scale=1.3,
            weight=weight
        ).save_state().scale(0.7, about_point=ORIGIN).shift(2.2 * LEFT)

        edges = [("A", "C"), ("B", "C"), ("C", "D"), ("B", "F"), ("E", "F"),
                 ("E", "G"), ("G", "H")]

        g2 = BasicGraph(
            vertices=vertices,
            edges=edges,
            vertex_and_label_scale=1.3,
            weight=weight

        ).save_state().scale(0.7, about_point=ORIGIN).shift(2.2 * LEFT)

        self.play(
            ShowCreation(g1)
        )
        BasicGraph.wait(self, 3)
        self.play(ShowCreation(g2))
        self.play(Uncreate(g1, run_time=7))


class KruskalsExample2(Scene):
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

        edges1 = [("A", "B")]

        weight = {("A", "B"): [5, (-0.35, -0.35)], ("A", "C"): [4, (0.35, 0.5)],
                  ("A", "D"): [8, (-0.35, 0.35)], ("B", "C"): [3, (0.35, 0)],
                  ("B", "F"): [6, (0, 0.5)], ("C", "D"): [5, (0.35, -0.35)],
                  ("C", "E"): [7, (0, 0.5)], ("D", "E"): [6, (0.35, 0.35)],
                  ("E", "F"): [3, (0.35, 0)], ("E", "G"): [3, (0, 0.5)],
                  ("E", "H"): [4, (0, -0.5)], ("G", "H"): [1, (0.35, 0.25)]}

        g1 = BasicGraph(
            vertices=vertices.copy(),
            edges=edges,
            vertex_and_label_scale=1.3,
            weight=weight
        ).save_state().scale(0.7, about_point=ORIGIN).shift(2.2 * LEFT)

        self.play(ShowCreation(g1))
        BasicGraph.wait(self, 4)
        g1.generate_target()
        g1.target.shift(3.8 * LEFT + 2 * DOWN).scale(0.75, about_point=ORIGIN)
        BasicGraph.wait(self, 2)
        self.play(MoveToTarget(g1))

        g1_elements = BasicGraph.decompose_graph(g1)
        list_of_scenes = []
        for test in range(len(edges) - 1):
            scenes = VGroup(*g1_elements[test])
            if not list_of_scenes:
                final_scene = scenes.scale(0.65).move_to(np.array([4, 3, 0]))
            else:
                final_scene = scenes.scale(0.65) \
                    .next_to(list_of_scenes[-1], DOWN)

            list_of_scenes.append(final_scene)
        group_scenes = VGroup(*list_of_scenes)

        g2 = BasicGraph(
            vertices=vertices,
            edges=edges,
            vertex_and_label_scale=1.3,
            weight=weight,
            edge_default=DashedLine()

        ).scale(0.5, about_point=ORIGIN).shift(1.5 * LEFT + 1 * DOWN) \
            .save_state()

        self.add(g2)
        self.play(Uncreate(g1), Write(group_scenes))
        BasicGraph.wait(self, 3)

        edges = [("A", "C"), ("C", "D"), ("B", "C"), ("B", "F"),
                 ("E", "F"), ("E", "G"), ("G", "H")]

        g3 = BasicGraph(
            vertices=vertices,
            edges=edges,
            vertex_and_label_scale=1.3,
            weight=weight,
        ).scale(0.5, about_point=ORIGIN).shift(1.5 * LEFT + 1 * DOWN) \
            .save_state()

        self.remove(g2)
        self.play(Write(g3))


class KruskalsExample1(Scene):

    def construct(self):

        # these are the defined vertices edges and weights of the graph
        vertices = {"A": (-8, 2), "B": [-3, 5], "C": [0, 0],
                    "D": [-3, -2], "E": [1, -2], "F": [3, 2]}

        edges = [("A", "B"), ("A", "D"), ("B", "C"), ("B", "F"), ("C", "D"),
                 ("C", "F"), ("E", "F"), ("D", "E")]

        weight = {("A", "B"): [5, (-0.35, 0.6)], ("A", "D"): [6, (-0.5, -0.5)],
                  ("B", "C"): [6, (-0.35, -0.6)], ("B", "F"): [7, (0.5, 0.5)],
                  ("C", "D"): [3, (-0.5, 0.5)], ("C", "F"): [3, (-0.5, 0.5)],
                  ("E", "F"): [5, (0.5, 0)], ("D", "E"): [4, (0, -0.5)]}

        # Creates the first graph
        g1 = BasicGraph(
            vertices=vertices,
            edges=edges,
            vertex_and_label_scale=1.3,
            weight=weight

        ).scale(0.5, about_point=ORIGIN).shift(RIGHT).save_state()

        # Displays first graph in the centre
        self.play(ShowCreation(g1))
        BasicGraph.wait(self, 4)
        g1.generate_target()
        g1.target.shift(2.5 * LEFT + 1 * DOWN)
        BasicGraph.wait(self, 2)
        self.play(MoveToTarget(g1))
        BasicGraph.wait(self, 4)

        g1_elements = BasicGraph.decompose_graph(g1)
        ascending_list = sorted(g1_elements, key=lambda x: (x[0]))
        for x in g1_elements:
            del x[0]

        list_of_scenes = []
        for test in range(len(edges)):
            scenes = VGroup(*g1_elements[test])
            if not list_of_scenes:
                final_scene = scenes.scale(0.45).move_to(np.array([4, 3, 0]))
            else:
                final_scene = scenes.scale(0.45) \
                    .next_to(list_of_scenes[-1], DOWN)

            list_of_scenes.append(final_scene)
        group_scenes = VGroup(*list_of_scenes)

        g2 = BasicGraph(
            vertices=vertices,
            edges=edges,
            vertex_and_label_scale=1.3,
            weight=weight,
            edge_default=DashedLine()

        ).scale(0.5, about_point=ORIGIN).shift(1.5 * LEFT + 1 * DOWN) \
            .save_state()

        self.add(g2)
        self.play(Uncreate(g1), Write(group_scenes))
        BasicGraph.wait(self, 3)

        list_of_scenes2 = []
        for test in range(len(edges)):
            scenes = VGroup(*ascending_list[test])
            if not list_of_scenes2:
                final_scene = scenes.move_to(np.array([4, 3, 0]))
            else:
                final_scene = scenes \
                    .next_to(list_of_scenes2[-1], DOWN)

            list_of_scenes2.append(final_scene)
        group_scenes2 = VGroup(*list_of_scenes2)

        self.play(Write(group_scenes2))
        BasicGraph.wait(self, 3)

        edges = [("A", "B"), ("A", "D"), ("C", "D"), ("C", "F"), ("D", "E")]
        g3 = BasicGraph(
            vertices=vertices,
            edges=edges,
            vertex_and_label_scale=1.3,
            weight=weight,
        ).scale(0.5, about_point=ORIGIN).shift(1.5 * LEFT + 1 * DOWN) \
            .save_state()

        self.remove(g2)
        self.play(Write(g3))
