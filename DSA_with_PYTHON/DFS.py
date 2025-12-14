def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    print(start)
    visited.add(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
# Example usage
graph = {'A': ['B', 'C'], 'B': ['D'], 'C': ['E'], 'D':[], 'E':[]}
dfs(graph, 'A')
