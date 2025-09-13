def depthFirstPrint (graph, source) :
    
    stack = [ source ]
    
    while  len(stack) > 0 :
        current = stack.pop()
        print("current", current)
        for item in graph[current]:
            stack.append(item)
    
// Recursive

def depthFirstPrint (graph, source) :
    
    print("current", source)
    for neighbour in graph[source]:
        depthFirstPrint(graph, neighbour)
    



graph = {
  'a': ['c', 'b'],
  'b': ['d'],
  'c': ['e'],
  'd': ['f'],
  'e': [],
  'f': []
}

depthFirstPrint(graph,'a')
