from random import choice
from copy import deepcopy

def minCut(G):
    # the function which randomly chooses the edges and fuses the nodes which are linked with that edge
    # input: the graph G, represented by a dictionary
    # output: the min cut
    
    # while the graph has more than two nodes, randomly choose two nodes and fuse them
    while len(G) > 2:
        vertex1 = choice(list(G.keys()))
        vertex2 = choice(G[vertex1])
        fuse(vertex1, vertex2, G)
        
    # pop the second element, return the length of it which is the min cut    
    return len(G.popitem()[1])
    
def fuse(node1, node2, G):
    # the function which fuses nodes based on the randomly chosen edge
    # it also removes the self edges
    # input: node1 - the first node
    #        node2 - the second node
    #        G - the graph
    
    # add the edges of node2 to node1
    G[node1].extend(G[node2])
    
    # look at all edges of node2, then go to the nodes which are linked with those
    # edges and change the direction from node2 to node1
    for edge in G[node2]:
        lst = G[edge]
        for i in range(0, len(lst)):
            if lst[i] == node2:
                lst[i] = node1
    
    # remove self-loops from node1                        
    while node1 in G[node1]:
        G[node1].remove(node1)
    
    # remove node2 from the graph      
    del G[node2] 

# read the file        
lista = "D:/Workbench/Online Courses/Design and Analysis of Algorithms, Part 1/Programming Assignment 3/file.txt" 
f = open(lista, 'r')
line_list = f.readlines()
G = {int(line.split()[0]): [int(val) for val in line.split()[1:] if val] for line in line_list if line} 

# initialize the value of mincut to a very large number  
mincut = 10000000000000

# iterate a thousand times with different random choices to get the min cut value
# In theory the number of iterations should be n^2logn, which in our case would be 305600
# On a decent computer, it would take days to run it, so instead I chose to run a thousand iterations
# The probability of getting the wrong min cut is bigger than 1/200, but it still should be small enough
# Obviously, the theoretical guarantee here is lacking, but at worst case it should give us a good min cut.
for i in range(1000):
    curr = minCut(deepcopy(G))
    if curr < mincut:
        mincut = curr
        
# print the best value from mincut        
print str(mincut)                                                                           