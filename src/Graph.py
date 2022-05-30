from collections import defaultdict
class Graph:
    def __init__(self):
        self.adj = defaultdict(list)
        
    def addEdge(self,u,v):
        self.adj[u].append(v)
        self.adj[v].append(u)


        
    def convert_adjmatrix(self, a):
        adjList = defaultdict(list)
        for i in range(len(a)):
            for j in range(len(a[i])):
                            if a[i][j]== 1:
                                adjList[i].append(j)
        return adjList
    
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        graph = self.convert_adjmatrix(edges)
        queue = [source]
        
        while(len(queue) !=0 ):
            source = queue.pop(0)
            for neighbor in graph[source]:
                if(neighbor == destination):
                    return True
                queue.append(neighbor)
        
        return False

    def dfs_util(self,vertex,visited):
        if(str(vertex) in visited):
            return False
        visited.add(str(vertex))
        for v in self.adj[vertex]:
            self.dfs_util(v,visited)
        
        return True
        

    def count_connectedcomp(self):
        ct = 0
        #visited = defaultdict(lambda:False)
        visited = set()
        for vertex in self.adj:
                if(self.dfs_util(vertex,visited) == True):
                    ct+=1
        return ct


    def explore(self, src, visited):
        if(src in visited):
            return 0
        curr_size = 1
        visited.add(src)
        for node in self.adj[node]:
            curr_size += self.explore(node, visited) 
        return curr_size

    def largest_component(self):
        visited = set()
        largest_size = 0
        for vertex in self.adj:
            component_size = self.explore(vertex, visited)
            if(component_size> largest_size):
                largest_size = component_size
        
        return largest_size
        


    v,e = map(int,input().split())
    g = Graph()
    for _ in range(e):
        u1,u2 = map(int,input().split())
        g.addEdge(u1,u2)

    ct = g.count_connectedcomp()
    print(ct)
    largest_comp = g.largest_component()
    print(largest_comp)

    