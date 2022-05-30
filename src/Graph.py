from collections import defaultdict
class Graph:
    def __init__(self):
        self.adj = defaultdict(list)
        
    def addEdge(self,u,v):
        self.adj[u].append(v)
        self.adj[v].append(u)

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

    