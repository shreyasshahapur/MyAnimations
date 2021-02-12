from manim import *


class BasicGraph(VMobject):

    def __init__(self,
                 vertices={},  # includes position {"A": [1, 0], "B": [-1, -1], ... }
                 edges=[],  # [(v1, v2), ...]
                 label_type=Text,
                 label_default={"font": "futura"},  # default parameters for labels
                 label_config={},  # adds/changes the default label parameters, for specific vertices
                 vertex_default=Dot(color=BLUE), # default vertices
                 vertex_config={},  # key: vertex, value: associating object
                 vertex_and_label_scale=1,
                 edge_default=Line(),
                 edge_config={},
                 **kwargs
                 ):
        VMobject.__init__(self, **kwargs)

        # turns the positions into an np array
        vertices = {vertex: np.array(pos + [0]) for vertex, pos in vertices.items()}

        # adds edges
        for (v1, v2) in edges:
            if (v1, v2) in edge_config:
                edge_image = edge_config[(v1, v2)]
            else:
                edge_image = edge_default.copy()
            edge_image.put_start_and_end_on(vertices[v1], vertices[v2])
            self.add(edge_image)

        # Text(letter, font="futura") centered with reference to a circle of radius=0.5
        FUTURA_CENTERING_POS = {
            "A": 0.04 * UP, "B": 0.03 * RIGHT, "C": 0.04 * LEFT, "D": 0.04 * RIGHT,
            "E": 0.01 * DOWN, "F": 0.02 * RIGHT + 0.01 * DOWN, "G": ORIGIN,
            "H": 0.004 * RIGHT, "I": ORIGIN, "J": 0.035 * LEFT, "K": 0.025 * RIGHT,
            "L": 0.025 * RIGHT, "M": 0.02 * UP, "N": ORIGIN, "O": ORIGIN,
            "P": 0.035 * RIGHT + 0.01 * DOWN, "Q": ORIGIN, "R": 0.03 * RIGHT,
            "S": ORIGIN, "T": 0.03 * DOWN, "U": 0.02 * DOWN, "V": 0.045 * DOWN,
            "W": 0.05 * DOWN, "X": 0.01 * DOWN, "Y": 0.03 * DOWN, "Z": ORIGIN
        }

        # adds vertices and labels
        for v in vertices:
            if v in vertex_config:
                vertex_image = vertex_config[v]
            else:
                vertex_image = vertex_default.copy()

            if v in label_config:
                label_image = label_type(text=v, **label_default.update(label_config[v]))
            else:
                label_image = label_type(text=v, **label_default)

            vertex_image.scale(vertex_and_label_scale).move_to(vertices[v])
            label_image.move_to(FUTURA_CENTERING_POS[v]).scale(vertex_and_label_scale).shift(vertices[v])
            self.add(vertex_image)
            self.add(label_image)

    # transforms graph g1 to g2 (only for removing and adding to the graph)
    @staticmethod
    def basic_transform(self, g1, g2, run_time_in=1, run_time_out=1):
        self.play(Write(g2), run_time=run_time_in)
        self.play(FadeOut(g1), run_time=run_time_out)

    # for adding elements to graph
    @staticmethod
    def basic_transform_expand(self, g1, g2, run_time_in=1, run_time_out=0.05):
        BasicGraph.simple_transform(self, g1, g2, run_time_in=run_time_in, run_time_out=run_time_out)

    # for removing elements from graph
    @staticmethod
    def basic_transform_contract(self, g1, g2, run_time_in=0.05, run_time_out=1):
        BasicGraph.simple_transform(self, g1, g2, run_time_in=run_time_in, run_time_out=run_time_out)
