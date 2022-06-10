
class GClone: 
    def cloneGraph(self, node):
        oldtonew_map  = {}
        #return node only if it's not null
        return self.dfs_clone(oldtonew_map, node) if node else None

    def dfs_clone(self, mapping, node):
        if node in mapping:
            return mapping[node]
        
        copy = Node(node.val)
        mapping[node] = copy

        for neighbor in node.neighbors:
            copy.neighbors.append(self.dfs_clone(mapping, neighbor))
        #after traverse of every node in the graph
        return copy



class Node:
    def __init__(self, val):
        self.val = val
        self.neighbors = []




