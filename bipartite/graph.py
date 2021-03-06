"""
Created by Ivanov Roman and Maxim Dudin. This module is intended to define
structure describing graphs in this package.

https://github.com/severmore/pygraphs
"""
class Graph:
  """
  A graph representation used in the algorithms of this package. It is intended
  to use in these algos. The vertices of this graph represented by aconsecutive 
  integer numbers, end the edges -- as a list of incidence.

  Note:
      In this implementation as a list used python list that is actually an 
      array

  Attributes:
      edges (:obj:`list` of :obj:`list` of int) - a list of incidences.

      vertices_num (int) - a number of vertices

      max_degree (int) - a maximum degree of vertices of a graph
  """

  def __init__(self, edges=None, graph=None, vertices_num=0):
    """
    Create a new graph object. If none of arguments are given an empty graph 
    will be created.

    Keyword args:

      edges (:obj:`list` of :obj:`turple` of int, optional): a list of edges 
          each element of which is a tuple of size two: (start - end). Default 
          to None.
    
      graph (:obj:`Graph`, optional): a graph which edges will be copied to a 
          new graph. If `edges` and `graph` are both not None then the edges of 
          a newly created graph will contains both `graph` edges and 'edges'. 
          Default to None.

      vertices_num (int, optional): the intended number of vertices in a graph 
          created. If it is not specified it will be obtained from `edges` and 
          'graph' as a maximum of values of vertex identifiers in these 
          variables. The parameter is used to speed up. Default to 0.
    """

    if not vertices_num:
      # As a set of vertices represented as a consequtive integer number it's
      # sufficient to find the gretest one in the list given
      if edges:
        vertices_num = max(max(edges, key=lambda x: max(x[0], x[1]))) + 1
      
      # In the graph object vertices is already structed into the list
      if graph:
        v_max = len(graph.edges)
        
        if v_max > vertices_num:
          vertices_num = v_max
    
    self.vertices_num = vertices_num
    self.edges = [[] for _ in self.get_vertices()]

    if edges:
      for start, end in edges:
        self.edges[start].append(end)

    if graph:
      for start, ends in enumerate(graph.edges):
        self.edges[start].extend(ends)
    
    # Set maximum degree of vertices in the graph
    self.max_degree = 0
    self.update_max_degree()


  def __eq__(self, other):
    from collections import Counter

    return all([ Counter(i_s) == Counter(i_o) 
                   for i_s, i_o in zip(self.edges, other.edges)])


  def __str__(self):
    klass_name = self.__class__.__name__.lower()
    edges_str = ', '.join(
        [ f'[{v}]-{inc}' for v, inc in enumerate(self.edges) ]
    )
    return f'{klass_name}({edges_str})'


  def __repr__(self):
    return str(self.edges)


  def degree(self, vertex):
    """ int -> int: Returns a degree of a given edge. """
    
    return len(self.edges[vertex])


  def get_vertices(self):
    """ () -> range: Returns vertices of the graph as a range object. """
    return range(self.vertices_num)


  def update_max_degree(self):
    """ Count a maximum degree among vertices in the graph, if any, otherwise 
    return 0. 
    """
    self.max_degree = 0
    for vertex in self.edges:
      if len(vertex) > self.max_degree:
        self.max_degree = len(vertex)


  def remove_edge(self, start, end):
    """ Remove an edge from the graph. It is assumed no vertex is deleted and 
    `max_degree` is not updated. """
    self.edges[start].remove(end)


  def add_edge(self, start, end):
    """ Add an edge to a graph. It is assumed no new vertex is added and
    `max_degree` is not updated. """
    self.edges[start].append(end)


  def union(self, graph):
    """ Returns the union of the graphs. It is assumed vertices set remains
    unchanged. """
    for start, incidence in enumerate(graph.edges):
      self.edges[start].extend(incidence)



class UDGraph(Graph):
  """
  A  class for undirected graphs for using in the algorithms of this package. It
   is intended to use in these algos. The vertices of this graph represented by 
  a consecutive integer numbers, end the edges -- as a list of incidence. The 
  class is a subclass of `Graph` class.

  Note:
      In this implementation as a list used python list that is actually an 
      array
  """

  def __init__(self, edges=None, graph=None, vertices_num=0):
    """
    Create a new undirected graph object. If none of arguments are given an 
    empty graph will be created.

    Keyword args:

      edges (:obj:`list` of :obj:`turple` of int, optional): a list of edges 
          each element of which is a tuple of size two: (start - end). For 
          convenience sake the edge, specified as (start-end), is duplicated by
          an edge (end-start). Default to None.
    
      graph (:obj:`Graph`, optional): a graph which edges will be copied to a 
          new graph. If `edges` and `graph` are both not None then the edges of 
          a newly created graph will contains both `graph` edges and 'edges'. 
          Default to None.

      vertices_num (int, optional): the intended number of vertices in a graph 
          created. If it is not specified it will be obtained from `edges` and 
          'graph' as a maximum of values of vertex identifiers in these 
          variables. The parameter is used to speed up. Default to 0.
    
    Note:
      due to implementation of Graph base class for an undirected graph each 
      edge (start, end) is duplicated by an edge (end, start). Further work with
      the graph is assumed to treat this pair as a single edge.
    """
    super().__init__(edges=edges, graph=graph, vertices_num=vertices_num)
    
    if edges:
      for start, end in edges:
        self.edges[end].append(start)
    
    if graph.__class__ == Graph:
      for start, incidence in enumerate(graph.edges):
        for end in incidence:
          self.edges[end].append(start)

    self.update_max_degree()


  def remove_edge(self, start, end):
    """ Remove an edge from the graph. It is assumed no vertex is deleted and 
    `max_degree` is not updated. """
    self.edges[start].remove(end)
    self.edges[end].remove(start)


  def add_edge(self, start, end):
    """ Add an edge to a graph. It is assumed no new vertex is added and
    `max_degree` is not updated. """
    self.edges[start].append(end)
    self.edges[end].append(start)


if __name__ == '__main__':
  udgraph = UDGraph(edges=[ (0, 1), (0, 3), (1, 2), (2, 0), (2, 3) ])
  # print(udgraph)
  graph = Graph(edges=[ (0, 1), (0, 3), (1, 2), (2, 0), (2, 3) ])
  udgraph2 = UDGraph(graph=udgraph, edges=[(4,1), (4,2)])
  print(repr(graph))
  print(repr(udgraph))
  print(repr(udgraph2))
