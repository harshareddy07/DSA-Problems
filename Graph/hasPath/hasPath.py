

def has_path(graph, source, destination, visited):
    """Find the largest connected component using DFS"""
    visited.add(source)
    if source == destination:
        return True
    
    for neighbour in graph[source]:
        if neighbour not in visited:
            if has_path(graph, neighbour, destination, visited) == True:
                return True
            
    return False



graph = {
    'A': ['B', 'C'],        # Component 1: size 3
    'B': ['A', 'C'], 
    'C': ['A', 'B'],
    'D': ['E', 'F', 'G'],   # Component 2: size 4 (largest)
    'E': ['D', 'F'],
    'F': ['D', 'E', 'G'],
    'G': ['D', 'F'],
    'H': ['I'],             # Component 3: size 2
    'I': ['H'],
    'J': []                 # Component 4: size 1
}

print("Graph:", graph)
print()

visited = set()
result = has_path(graph, 'A', 'F', visited)
print("result", result)

