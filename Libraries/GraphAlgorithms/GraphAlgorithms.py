from typing import List

# ===================================== EDGE CLASS =====================================
class Edge:
    vertex: int
    weight: int

    # weighted graph
    def __init__(self, v: int, w: int):
        self.vertex = v
        self.weight = w

# ===================================== GRAPH CLASS =====================================

class Graph():
    vertex_count: int           # number of verticies
    isDirected: bool            # wherther a graph is directed or not
    verticies: List[List[Edge]] # the structure of the graph


    # constructor
    def __init__(self, vertex_count: int, isDirected: bool = False) -> None:
        self.vertex_count = vertex_count
        self.isDirected = isDirected
        self.verticies = [[] for i in range(vertex_count)]
        #self.visited = []


    # overrides string to print a class
    def __str__(self) -> str:
        s = "VERTEX -> (VERTEX|WEIGHT)\n"
        for i in range(self.vertex_count):
            s += str(i) + " -> "
            for edge in self.verticies[i]:
                s += "(" + str(edge.vertex) + "|" + str(edge.weight) + "), "
            s += "\n"
        
        return s

    # --------------------------------- ADD/REMOVE EDGE ---------------------------------
    def add_edge(self, a: int, b: int, weight: int = 1) -> None:
        self.verticies[a].append(Edge(b, weight))
        if not self.isDirected: # reverse the direction
            self.verticies[b].append(Edge(a, weight))


    def delete_edge(self, a: int, b: int) -> None:
        for edge in self.verticies[a]:
            if edge.vertex == b: 
                self.verticies[a].remove(edge)
        
        if not self.isDirected: # delete opposite direction as well
            for edge in self.verticies[b]:
                if edge.vertex == a: 
                    self.verticies[b].remove(edge)


    # --------------------------------- BREADTH FIRST SEARCH ---------------------------------
    def BFS_tree(self, start: int) -> List[int]:
        visited: List[bool] = [False for i in range(self.vertex_count)]
        tree: List[int] = [-1 for i in range(self.vertex_count)]
        queue: List[int] = []
        v: int # current vertex

        visited[start] = True # set the starting vertex as visited
        queue.append(start)

        while queue:
            v = queue.pop(0)

            for edge in self.verticies[v]:
                vertex = edge.vertex
                if not visited[vertex]:
                    visited[vertex] = True
                    tree[vertex] = v
                    queue.append(vertex)
        
        """
        # print the tree
        for i in range(1, self.vertex_count+1):
            if tree[self.vertex_count-i] != -1: # except unreachable vertexes
                print(str(tree[self.vertex_count-i]) + "->" + str(self.vertex_count-i))
        """

        return tree
    

    def BFS(self, start: int, finish: int) -> List[int]:
        tree: List[int] = self.BFS_tree(start)
        path: List[int] = []

        if tree[finish] != -1:
            while finish != start:
                path.append(finish)
                finish = tree[finish]
            path.append(start)
            path.reverse()

        return path
    
    # --------------------------------- DEPTH FIRST SEARCH ---------------------------------
    # TODO








# TODO: make graph from Dict[Set()]

if __name__ == "__main__":
    
    g =  Graph(8)

    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(0, 3)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(4, 5)
    g.add_edge(4, 6)
    g.add_edge(5, 7)
    g.add_edge(1, 6)

    print(g.BFS(5, 0))
    print(g)
