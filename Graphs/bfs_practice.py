
def bfs(graph, start):
    q = [start]
    explored = []

    while q:
        node = q.pop(0)
        if node not in explored:
            explored.append(node)
            neighbours = graph[node]
        
            for i in neighbours:
                    q.append(i)
    return explored

def bfs1(graph, start):
    explored = []
    # keep track of nodes to be checked
    queue = [start]
 
    # keep looping until there are nodes still to be checked
    while queue:
        # pop shallowest node (first node) from queue
        node = queue.pop(0)
        if node not in explored:
            # add node to list of checked nodes
            explored.append(node)
            neighbours = graph[node]
 
            # add neighbours of node to queue
            for neighbour in neighbours:
                queue.append(neighbour)
    return explored



graph = {
    'A': ['B','D','G'],
    'B': ['A','E','F'],
    'E': ['B','G'],
    'G': [ 'E', 'A'],
    'F': ['B', 'C','D'],
    'C': ['F','H'],
    'H': ['C'],
    'D' : ['A','F'] }
##
##graph = {'A': ['B', 'C', 'E'],
##         'B': ['A','D', 'E'],
##         'C': ['A', 'F', 'G'],
##         'D': ['B'],
##         'E': ['A', 'B','D'],
##         'F': ['C'],
##         'G': ['C']}

ans = bfs(graph, 'A')
print(ans)

print(bfs1(graph, 'A'))
