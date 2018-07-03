def dfs(graph, start):
    explored = []
    q = [start]
    while q:
        node = q.pop()
        if node not in explored:
            explored.append(node)
            n = graph[node]
            for i in n:
                q.append(i)
    return explored

def dfs_iterative(graph, start):
    stack, path = [start], []

    while stack:
        vertex = stack.pop()
        if vertex in path:
            continue
        path.append(vertex)
        for neighbor in graph[vertex]:
            stack.append(neighbor)

    return path

def dfs_recursive(graph, node, path = []):
    path += [node]

    for i in graph[node]:
        if i not in path:
            path = dfs_recursive(graph, i, path)

    return path
##graph1 = {
##    'A': ['B','D','G'],
##    'B': ['A','E','F'],
##    'E': ['B','G'],
##    'G': [ 'E', 'A'],
##    'F': ['B', 'C','D'],
##    'C': ['F','H'],
##    'H': ['C'],
##    'D' : ['A','F'] }
##
##graph = {'A': ['B', 'C', 'E'],
##         'B': ['A','D', 'E'],
##         'C': ['A', 'F', 'G'],
##         'D': ['B'],
##         'E': ['A', 'B','D'],
##         'F': ['C'],
##         'G': ['C']}
graph1 ={1: [2, 3], 2: [1,4, 5],
                    3: [1,5], 4: [2,6], 5: [2,3,6],
                    6: [4,5,7], 7: [6]}
ans = dfs(graph1, 1)
print(ans)
print(dfs_iterative(graph1, 1))
print(dfs_recursive(graph1, 1, []))
