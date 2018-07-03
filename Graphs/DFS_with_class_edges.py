from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFS(self, v):

        return self.DFS_recursive(v)

    def DFS_recursive(self, v, path= []):
        path += [v]
        for i in self.graph[v]:
            if i not in path:
                self.DFS_recursive(i, path)
        return path
    
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print(g.DFS(2))
 


