from collections import deque

def shortest_path_unweighted(graph, source, destination):
    queue = deque([source])
    visited = {source}
    distance = {source: 0}

    while queue:
        node = queue.popleft()
        if node == destination:
            return distance[node]

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                distance[neighbor] = distance[node] + 1
                queue.append(neighbor)

    return -1  # destination unreachable
