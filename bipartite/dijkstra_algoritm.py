import math

"""
    This function realize Dijkstra algorithm
    for search the shortest way via weight function
"""

def dijkstra_algorithm(graph, start_index, end_index):
    graph_edges = graph.edges
    initial_weight_structure = get_initial_weight_structure(graph_edges.length, start_index)
    determined_weight_structure = dict()
    from_vertex = graph_edges[start_index]
    to_vertex = graph_edges[end_index]
    while len(initial_weight_structure) > 0:
        min_vertex = find_min_in_weight_structure(initial_weight_structure)
        min_vertex_neighboards = get_vertex_neighbords(graph_edges[min_vertex.index])
        for neighbord_vertex in min_vertex_neighboards:
            None


def get_vertex_neighbords(node_edges):
    result = []
    for edge in node_edges:
        result.append(edge.to_vertex)
    return result

"""
    return structure with initial weight is equal to 
    None instead of infinity
"""

def get_initial_weight_structure(count, start_vertex):
    initial_structure = dict()
    for i in range(0, count):
        if i == start_vertex:
            initial_structure[i] = PathTreeNode(weigth=0, index=i)
            #initial_structure.(PathTreeNode(weigth=0, index=i))
        else:
            initial_structure[i] = PathTreeNode(index=i)
            #initial_structure.append(PathTreeNode(index=i))
    return initial_structure


def find_min_in_weight_structure(structure):
    keys = structure.keys()
    result = None
    if not len(keys):
        return result
    else:
        result = structure.get(keys[0])
    for key in keys:
        result = compare_weights(result, structure.get(key))
    return result

"""
    :return vertex with min weight
"""
def compare_weights(first, second):
    if second.weight is None:
        return first
    if first.weight is None:
        return second
    if first.weight > second.weight:
        return second
    else:
        return first

def relaxation(from_vertex, to_vertex, edge_weight):
    if from_vertex.weight is not None:
        if to_vertex.weight is None:
            to_vertex.weight = from_vertex + edge_weight
            to_vertex.parent = from_vertex.index
        else:
            if from_vertex.weight < from_vertex + edge_weight:
                to_vertex.weight = from_vertex + edge_weight
                to_vertex.parent = from_vertex.index
        return

class PathTreeNode:
    def __init__(self, index=0, parent=None, weigth=None):
        """
        :param parent: - int number from vertex
        :param weigth: - expected weight
        """
        self.index = index
        self.parent = parent
        self.weight = weigth