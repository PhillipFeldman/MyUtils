"""
This graph is not your typical graph where a path is the sum of all its edges. Instead, it is the product
of all the edges.  Consider edge weights to be probability of success p, with 0<p<1.  The 'best path' would
then be the 'longest path'. Luckily, this is not an NP-Complete problem.
Let Path-1 have edge weights w1,w2... and Path-2 have edge weights e1,e2,... and let
Path-1 > Path-2.
So, (w1)(w2)...>(e1)(e2)...
Then log[(w1)(w2)...] > log[(e1)(e2)...]    (because log is a monotonic increasing function)
Then -log[(w1)(w2)...] < -log[(e1)(e2)...]    (multiply by -1)
Then -log(w1)-log(w2)-... < -log(e1)-log(e2)-...    (property of logarithms)
And note that since 0<p<1, log(p)<0, so -log(p)>0
So run Djikstra's algorithm on the graph where all the edge weights w are replaced by -log(w).
This finds -log(shortest_path), which will correspond to the best path of the original graph.
Should also work with max flow/min cut, etc.
"""

import numpy as np
import copy


class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []
        self.source_map = {}

    def add_node(self, node):
        assert not node in self.nodes
        self.nodes.append(node)
        self.source_map[node] = []

    def add_edge(self, source_node, terminal_node, edge_weight):
        assert source_node in self.nodes and terminal_node in self.nodes
        edge = Edge(source_node, terminal_node, edge_weight)
        self.validate_edge(edge)
        self.edges.append(edge)
        self.source_map[source_node].append(edge)

    # not working. Also not priority. refactoring to edge objects will fix the issue anyway
    def remove_node(self, node):
        assert node in self.nodes
        self.edges = list(filter(lambda edge: node not in edge, self.edges))
        del self.source_map[node]
        self.source_map = {k: list(filter(lambda edge: node not in edge, self.source_map[k])) \
                           for k in self.source_map.keys()}

    def remove_edge(self, source_node, terminal_node):
        edge = Edge(source_node, terminal_node, 0)
        assert edge in self.edges
        self.edges.remove(edge)
        self.source_map[source_node].remove(edge)

    def validate_edge(self, edge):
        # return True
        assert edge not in self.edges

    def distance(self, edge):
        return edge.computation_weight

    def source(self, edge):
        return edge.get_source()

    def terminal(self, edge):
        return edge.get_terminal()

    def djikstras(self, source_node, terminal_node):
        prevs = {node: None for node in self.nodes}
        path = []
        unvisited = {node: True for node in self.nodes}
        unvisited_set = {node for node in self.nodes}
        distances = {node: float('inf') for node in self.nodes}
        distances[source_node] = 0
        current = source_node
        while unvisited_set:
            for edge in self.source_map[current]:
                next_node = self.terminal(edge)
                if not unvisited[next_node]:
                    continue
                old_distance = distances[next_node]
                tentative = self.distance(edge) + distances[current]
                if tentative < old_distance:
                    distances[next_node] = tentative
                    prevs[next_node] = current

            unvisited[current] = False
            try:
                unvisited_set.remove(current)
            except KeyError:  # no path
                return 0, []

            current = min(distances.keys(), key=lambda k: distances[k] if unvisited[k] else float('inf'))
            # except ValueError:  # no path
            #    return 0, []

            if not unvisited[terminal_node]:
                break

        prev = terminal_node
        while prev != None:
            path = [prev] + path
            prev = prevs[prev]

        return 2 ** -distances[terminal_node], path


class Edge:
    def __init__(self, source_node, terminal_node, weight):
        self.validate_weight(weight)
        self.source_node = source_node
        self.terminal_node = terminal_node
        self.weight = weight
        self.computation_weight = self.compute_computation_weight(weight)

    def validate_weight(self, weight):
        assert 0 <= weight <= 1

    def compute_computation_weight(self, weight):
        if weight == 0:
            return float('-inf')
        return -np.log2(weight)

    def get_source(self):
        return self.source_node

    def get_terminal(self):
        return self.terminal_node

    def get_weight(self):
        return self.weight

    def __eq__(self, other):
        return (self.source_node, self.terminal_node) == (other.source_node, other.terminal_node)

    def __str__(self):
        return str((self.source_node, self.terminal_node, self.weight))

    def __repr__(self):
        return self.__str__()

    def __contains__(self, item):
        return item == self.source_node or item == self.terminal_node
