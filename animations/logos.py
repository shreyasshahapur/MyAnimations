from manim import *


class Logo1(Scene):

    def construct(self):
        layers = [[0, 1, 2], [3, 4, 5, 6], [7, 8, 9]]
        edges = [(0, 3), (3, 7), (0, 1), (1, 5), (4, 5), (0, 4), (4, 7), (5, 8),
                 (7, 8), (2, 6), (6, 9)]

        graph = Graph(
            vertices=list(range(0, 10)),
            edges=edges,
            layout="partite",
            partitions=layers
        )
        self.play(ShowCreation(graph), run_time=1.5)
        self.play(Rotate(graph, angle=900*DEGREES, run_time=2))
        self.play(FadeOut(graph))
