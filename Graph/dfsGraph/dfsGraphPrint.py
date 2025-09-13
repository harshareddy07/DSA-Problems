def depthFirstPrint (graph, source) :
    
    stack = [ source ]
    
    while  len(stack) > 0 :
        current = stack.pop()
        print("current", current)
        for item in graph[current]:
            stack.append(item)
    



graph = {
  'a': ['c', 'b'],
  'b': ['d'],
  'c': ['e'],
  'd': ['f'],
  'e': [],
  'f': []
}

depthFirstPrint(graph,'a')
