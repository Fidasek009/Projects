## How to use:

### Creating a Graph

#### Simple undirected graph from JSON format
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

#### A directed and weighted graph with 4 verticies
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

