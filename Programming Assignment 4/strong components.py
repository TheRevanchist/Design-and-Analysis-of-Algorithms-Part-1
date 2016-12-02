import sys
import time
import threading

#import resource

# Increase recursion depth and stack size 
sys.setrecursionlimit(100000)
#resource.setrlimit(resource.RLIMIT_STACK, (resource.RLIM_INFINITY, resource.RLIM_INFINITY))

lista = "D:/Workbench/Online Courses/Design and Analysis of Algorithms, Part 1/Programming Assignment 4/SCC.txt" 
f = open(lista, 'r')
line_list = f.readlines()
n = int(line_list[len(line_list)-1].split()[0]) # largest vertex number
G = {i: [] for i in range(1, n+1)} # construct an empty list of adjacent nodes for every vertex
GT = {i: [] for i in range(1, n+1)} # G's Transpose

# Read in the data from the text file and add them to the graphs
for line in line_list:
    curr_line = line.split()
    v1 = int(curr_line[0])
    v2 = int(curr_line[1])
    G[v1].append(v2)
    GT[v2].append(v1)
f.close() 

def dfs(G, i, explored, s, leader, time, finish):
    """Performs a depth first search in graph G starting from vertex s
    Input: G - the input graph in the adjacency list representation via a dictionary
    i - the starting vertex
    explored - a set of explored vertices
    s - current source vertex for DFS
    leader - a dictionary that set the leader node for each node
    time - the current time, aka how many nodes we have processed
    finish - a dictionary that records the finishing time of each node"""
    
    explored.add(i) # add i to the set of explored vertices
    leader[i] = s[0] # set i's leader
    for j in G[i]: # for every edge (i, j)
        if j not in explored:
            dfs(G, j, explored, s, leader, time, finish)
    time[0] += 1 
    finish[i] = time[0]

def dfs_loop(G, n):
    """Performs and outputs a topological sort of graph G using dfs
    Input: G - the input graph in the adjacency list representation via a dictionary
    n - the largest vertex number"""

    explored = set() # a set of explored vertices
    finish = {i: 0 for i in range(1, n+1)} # a dictionary that records the finishing time of each node
    leader = {i: 0 for i in range(1, n+1)} # a dictionary that set the leader node for each node.
                                           # Nodes with the same leader node are in the same SCC 
    time = [0] # number of nodes processed so far
    s = [0] # current source vertex
    
    while n > 0:
        if n not in explored:
            s[0] = n
            dfs(G, n, explored, s, leader, time, finish)
        n -= 1
    return finish, leader

def makeFinishedTimeGraph(G, n, finish):
    """Constructs a graph based on the finishing time, specifically after the first dfs_loop on G's transpose
    Input: G - the input graph in the adjacency list representation via a dictionary
    n - the largest vertex number
    finish - a dictionary that records the finishing time of each node"""
    
    finishedGraph = {}
    for i in range(1, n+1):
        temp = []
        for x in G[i]:
            temp.append(finish[x])
        finishedGraph[finish[i]] = temp
    return finishedGraph

def main():                
    finishing_time, leader = dfs_loop(GT, 875714)    
    newGraph = makeFinishedTimeGraph(G, n, finishing_time)
    nNew = max(newGraph, key=int)
    finishing_time, leader = dfs_loop(newGraph, nNew)
    lst = sorted(leader.values()) # sort the leaders
    final_stats = []
    start = 0 
    for i in range(n-1):
        if lst[i] != lst[i+1]:
            final_stats.append(i-start+1) # length of all the nodes with the same leader, i.e. in the same SCC
            start = i + 1 # the starting index of the next set of SCC components
    final_stats.append(n-start) # last SCC
    final_stats = sorted(final_stats) # sorted the final statistics in ascending order
    print("The sizes of the five largest SCCs are:", final_stats[:-6:-1]) # the biggest 5 SCCs in descending order
    
threading.stack_size(67108864) 
sys.setrecursionlimit(2 ** 20)
thread = threading.Thread(target = main)
thread.start()     