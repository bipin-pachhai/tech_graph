from collections import defaultdict
class Graph:
    def __init__(self):
        self.adj = defaultdict(list)
        
    def addEdge(self,u,v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def convert_adjmatrix(self, a):
        for u, v in a:
            self.addEdge(u,v)

    def dfs(self, edges):
        # TO DO
        pass
    def bfs(self, edges):
        # TO DO
        pass
    #check if there is path
    def validPath(self, n, edges, source, destination):
        graph = self.convert_adjmatrix(edges)
        queue = [source]
        
        while(len(queue) !=0 ):
            source = queue.pop(0)
            for neighbor in graph[source]:
                if(neighbor == destination):
                    return True
                queue.append(neighbor)
        
        return False
   # To count the number of connected components
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

   # To return the size of largest component in the graph
    def explore(self, src, visited):
        if(src in visited):
            return 0
        curr_size = 1
        visited.add(src)
        for node in self.adj[src]:
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

    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count_island = 0
        row_limit = len(grid) -1
        col_limit = len(grid[0]) -1
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if(self.explore_islands(grid, i ,j , visited, row_limit, col_limit) == True):
                    count_island += 1
                    
        return count_island
        
    def explore_islands(self, grid, i , j, visited, row_limit, col_limit):
        if((str(i)+","+str(j)) in visited):
            return False
        if(i< 0 or j <0 or i > row_limit or j > col_limit):
            return False
        if( grid[i][j] == "0"):
            return False
        
        visited.add(str(i)+","+str(j))
        #explore up
        self.explore_islands(grid, i-1 , j, visited, row_limit, col_limit)
        #explore down
        self.explore_islands(grid, i+1 , j, visited, row_limit, col_limit)
        #explore right
        self.explore_islands(grid, i , j+1, visited, row_limit, col_limit)
        #explore left
        self.explore_islands(grid, i , j-1, visited, row_limit, col_limit)
        
        return True
        
        

if __name__ == '__main__':
    v,e = map(int,input().split())
    g = Graph()
    for _ in range(e):
        u1,u2 = map(int,input().split())
        g.addEdge(u1,u2)

    ct = g.count_connectedcomp()
    print(ct)
    largest_comp = g.largest_component()
    print(largest_comp)

    