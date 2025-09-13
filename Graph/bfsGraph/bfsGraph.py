from collections import deque

def breadthFirstPrint(graph, source):
    queue = deque([source])
    
    while queue:
        current = queue.popleft()
        print("current", current)
        for item in graph[current]:
            queue.append(item)
            
def breadthFirstPrintRecursive(graph, queue):
    if not queue:
        return
    
    current = queue.popleft()
    print("BFS:", current)
    
    for neighbour in graph[current]:
        queue.append(neighbour)
    
    
graph = {
  'a': ['c', 'b'],
  'b': ['d'],
  'c': ['e'],
  'd': ['f'],
  'e': [],
  'f': []
}

breadthFirstPrint(graph,'a')
breadthFirstPrintRecursive(graph, queue)  # recurse with updated queue

