from collections import deque

def breadthFirstPrint(graph, source):
    queue = deque([source])
    
    while queue:
        current = queue.popleft()
        print("current", current)
        for item in graph[current]:
            queue.append(item)
graph = {
  'a': ['c', 'b'],
  'b': ['d'],
  'c': ['e'],
  'd': ['f'],
  'e': [],
  'f': []
}

breadthFirstPrint(graph,'a')
