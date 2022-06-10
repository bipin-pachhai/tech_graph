import sys
from heapq import heappush, heappop
from collections import defaultdict

def shortest_path(n, edges,s):
    graph = defaultdict(list)
    for(u, v), w in edges.items():
        graph[u].append((w,v))
        graph[v].append((w,u))

    distance = [sys.maxsize]* (n+1)
    visited = [False]*(n+1)

    #take care of starting node
    distance[s] = 0
    minheap = [(distance[s], s)]

    while minheap:
        d, u = heappop(minheap)
        if visited[u] == True:
            continue
        visited[u] = True
        for w, v in graph[u]:
            if visited[v] == False and distance[v] > distance[u] + w:
                #update the minimum distance
                distance[v] = distance[u] + w
                #push it in the min heap
                heappush(minheap, (distance[v], v))
    #TO BE CONTINUED..
    #https://www.youtube.com/watch?v=zxfXTcL2y38







# THE MAIN METHOD IMPLEMENTATION IN PYTHON
if __name__ == '__main__':
   #check = shortest_path()
   print("this is main method")