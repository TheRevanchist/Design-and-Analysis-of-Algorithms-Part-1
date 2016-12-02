import Queue

# create a graph
graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}
         
def breadthFirstSearch(G, start):
    # the function which implements the breadth-first search algorithm
    # input: graph - the graph we have
    #        start - the starting vertex
    # output: visited: the nodes the graph contains
    
    visited = [start]
    Q = Queue.Queue(100)
    Q.put(start)
    while not Q.empty():
        a = Q.get()
        for node in G[a]:
            if node not in visited:
                visited.append(node)
                Q.put(node)
                     
    return visited 
    
def depthFirstSearch(G, start, visited=[]):                                                
    # the function which implements the depth-first search algorithm
    # input: graph - the graph we have
    #        start - the starting vertex
    # output: visited: the nodes the graph contains 
    
    S = [start]
    while S:
        v = S.pop(0)
        if v not in visited:
            visited.append(v)
            S = graph[v] + S 
                
    return visited                        
    

            
       
            
                                
        
    
             