def bfs(graph, start):
    visited = set()
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            print(node)
            visited.add(node)
            queue.extend([n for n in graph[node] if n not in visited])
# Example usage
graph = {'A': ['B', 'C'], 'B': ['D'], 'C': ['E'], 'D':[], 'E':[]}
bfs(graph, 'A')
