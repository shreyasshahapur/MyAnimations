from manim import *


class SimpleGraph(VMobject):

    def __init__(self,
                 vertices={},  # includes position
                 edges=[],  # [(v1, v2), ...]
                 labels={},
                 vertex_default=Dot(color=BLUE),
                 vertex_config={},
                 edge_default=Line(),
                 edge_config={},
                 **kwargs
                 ):
        VMobject.__init__(self, **kwargs)

        # adds vertices to corresponding position

        # turns the positions into an np array
        vertices = {vertex: np.array(pos + [0]) for vertex, pos in vertices.items()}

        # adds vertices
        for v in vertices:
            vertex_image = vertex_default.copy()
            vertex_image.move_to(vertices[v])
            self.add(vertex_image)

        # adds edges
        for (v1, v2) in edges:
            edge_image = edge_default.copy()
            edge_image.put_start_and_end_on(vertices[v1], vertices[v2])
            self.add(edge_image)

    # transforms graph g1 to g2 (only for removing and adding to the graph)
    @staticmethod
    def simple_transform(self, g1, g2, run_time=1):
        self.play(Write(g2), run_time=run_time)
        self.play(FadeOut(g1), run_time=run_time)