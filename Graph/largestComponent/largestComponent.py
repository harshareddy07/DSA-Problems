def find_largest_component(graph):
    """Find the largest connected component using DFS"""
    visited = set()
    largest_component = []
    
    def dfs(node, component):
        visited.add(node)
        component.append(node)
        print(f"  Visiting: {node}")
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor, component)
    
    print("Finding largest connected component:")
    
    for node in graph:
        if node not in visited:
            print(f"\nStarting from node {node}:")
            component = []
            dfs(node, component)
            print(f"Component found: {component} (size: {len(component)})")
            
            # Update largest if current is bigger
            if len(component) > len(largest_component):
                largest_component = component
                print(f"New largest component: {largest_component}")
    
    return largest_component

# Example usage
if __name__ == "__main__":
    # Graph with components of different sizes
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
    
    largest = find_largest_component(graph)
    
    print(f"\nLargest connected component: {largest}")
    print(f"Size: {len(largest)} nodes")
