def find_connected_components(graph):
    """Find connected components using DFS"""
    visited = set()
    components = []
    
    def dfs(node, component):
        visited.add(node)
        component.append(node)
        print(f"  Visiting: {node}")
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor, component)
    
    print("Finding connected components:")
    for node in graph:
        if node not in visited:
            print(f"\nStarting from node {node}:")
            component = []
            dfs(node, component)
            components.append(component)
            print(f"Component found: {component}")
    
    return components

# Example usage
if __name__ == "__main__":
    # Create a simple graph with 3 components
    graph = {
        'A': ['B', 'C'],    # Component 1
        'B': ['A'],
        'C': ['A'],
        'D': ['E'],         # Component 2  
        'E': ['D'],
        'F': []             # Component 3 (isolated)
    }
    
    print("Graph:", graph)
    print()
    
    components = find_connected_components(graph)
    
    print(f"\nResult: Found {len(components)} connected components")
    for i, comp in enumerate(components, 1):
        print(f"Component {i}: {comp}")
