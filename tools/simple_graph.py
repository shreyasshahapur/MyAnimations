from manim import *


class SimpleGraph(VMobject):

    def __init__(self,
                 vertices={},  # includes position
                 edges=[],  # [(v1, v2), ...]
                 labels={},
                 vertex_default=Dot(color=BLUE),
                 vertex_config={},  # key: vertex, value: associating object
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
            if v in vertex_config:
                vertex_image = vertex_config[v]
            else:
                vertex_image = vertex_default.copy()
            vertex_image.move_to(vertices[v])
            self.add(vertex_image)

        # adds edges
        for (v1, v2) in edges:
            if (v1, v2) in edge_config:
                edge_image = edge_config[(v1, v2)]
            else:
                edge_image = edge_default.copy()
            edge_image.put_start_and_end_on(vertices[v1], vertices[v2])
            self.add(edge_image)

    # transforms graph g1 to g2 (only for removing and adding to the graph)
    @staticmethod
    def simple_transform(self, g1, g2, run_time_in=1, run_time_out=1):
        self.play(Write(g2), run_time=run_time_in)
        self.play(FadeOut(g1), run_time=run_time_out)

    # for adding elements to graph
    @staticmethod
    def simple_transform_expand(self, g1, g2, run_time_in=1, run_time_out=0.05):
        SimpleGraph.simple_transform(self, g1, g2, run_time_in=run_time_in, run_time_out=run_time_out)

    # for removing elements from graph
    @staticmethod
    def simple_transform_contract(self, g1, g2, run_time_in=0.05, run_time_out=1):
        SimpleGraph.simple_transform(self, g1, g2, run_time_in=run_time_in, run_time_out=run_time_out)

