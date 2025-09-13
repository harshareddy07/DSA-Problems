def dfsOfGraph(V, adj):
    visited = set()
    result = []

    def dfs(node):
        visited.add(node)
        result.append(node)
        for neighbour in adj[node]:
            if neighbour not in visited:
                dfs(neighbour)

    for i in range(V):   # <-- ensures all components are covered
        if i not in visited:
            dfs(i)
    
    return result
