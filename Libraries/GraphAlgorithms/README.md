# How to use:

## Creating a Graph

### Simple undirected graph with 4 vertices
**method one:**
```
graph1 = {
    0: [1, 2],
    1: [3],
    2: [3],
    3: [0]
}

g = Graph(graph1)
```
**method two:**
```
g = Graph(4)

# from, to
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(3, 0)
```

### A directed and weighted graph with 4 vertices
**method one:**
```
graph2 = {
    0: [[1, 5], [2, 3]],
    1: [[3, 8]],
    2: [[3, 6]],
    3: [[0, 4]]
}

g = Graph(graph2, isDirected=True)
```
**method two:**
```
g = Graph(4, isDirected=True)

# from, to, weight
g.add_edge(0, 1, 5)
g.add_edge(0, 2, 3)
g.add_edge(1, 3, 8)
g.add_edge(2, 3, 6)
g.add_edge(3, 0, 4)
```

## Different algorithms

### Breadth-first search (BFS)
Used for finding the shortest path in an unweighted graph
<br><img src="https://upload.wikimedia.org/wikipedia/commons/4/46/Animated_BFS.gif" width="250" height="250">

### Depth-first search (DFS)
Used for searching trees
<br><img src="https://upload.wikimedia.org/wikipedia/commons/7/7f/Depth-First-Search.gif" width="250" height="250">

### Dijkstra's algorithm
Used for finding the shortest path in a weighted graph
<br><img src="https://upload.wikimedia.org/wikipedia/commons/5/57/Dijkstra_Animation.gif" width="250" height="250">