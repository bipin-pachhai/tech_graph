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
    #______________________________________________________________check if there is path
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
   #____________________________________________________________ To count the number of connected components
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

   #_________________________________________________ To return the size of largest component in the graph
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
#_________________________________________________________Number of ISLANDS________________________________________________
    def numIslands(self, grid) -> int:
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
        

#________________________________________________Pacific atlantic Water Flow__________________________________ 
    def pacificAtlantic(self, heights):
        
        ROWS = len(heights)
        COLS = len(heights[0])
        return_list = []
        if(ROWS == 0):
            return return_list
        
        pacific, atlantic = set(), set()
        '''The logic is::: if we look in the grid, upper side is all pacific and lower edge is all atlantic. So, if we start dfs from up to down, we can check
           for pacific keeping track of prev height and them to the pacific set. Similarly, if we start from down to up, we can check for the ATLANTIC waterflow keeping
           track of prev height. We might not be able to include all the coordinates in this exploration of both atlantic and pacific. SO, we also know leftmost edge is all pacific
           and rightmost edge is all atlantic. So if we start dfs exploration for leftmost and rightmost egde, we can include other possible flow horizontally.
           if the coordinate is already include in pacific or atlantic set, we don't need exploration from that point, cause it's all included. At the end, we return the common
           coordinated from both pacific and atlantic set.
        '''
        for col in range(0, COLS):
            #explore for pacific
            self.ocean_grid(0, col, heights[0][col], pacific, ROWS,COLS, heights)
            #explore for atlantic
            self.ocean_grid(ROWS-1, col, heights[ROWS-1][col], atlantic, ROWS,COLS, heights)
            
        for row in range(0, ROWS):
            #explore for pacific
            self.ocean_grid(row, 0, heights[row][0], pacific, ROWS,COLS, heights)
            self.ocean_grid(row,COLS-1, heights[row][COLS-1], atlantic, ROWS,COLS,heights)
            
        for cor in pacific:           
                if cor in atlantic:
                    return_list.append([cor[0],cor[1]])
        
        return return_list
            
             
    def ocean_grid(self, row, col, prevHeig, ocean, ROWS,COLS, heights):
        if((row, col) in ocean):
            return
        if(row >= ROWS or col >= COLS or row < 0 or col <0):
            return
        if(prevHeig> heights[row][col]):
            return
        
        ocean.add((row, col))
        prevHeig = heights[row][col]
        
        self.ocean_grid(row-1, col, prevHeig, ocean, ROWS,COLS, heights)    
        self.ocean_grid(row+1, col, prevHeig, ocean, ROWS,COLS, heights)
        self.ocean_grid(row, col+1, prevHeig, ocean, ROWS,COLS, heights)
        self.ocean_grid(row, col-1, prevHeig, ocean, ROWS,COLS, heights)
       
#_________________________________________________________________________________________________________
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

    