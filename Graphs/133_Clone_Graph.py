# https://leetcode.com/problems/clone-graph
# Time complexity O(V+E)
# Space complexity O(V)

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Intuition: Here we have to create deep copy so we will call the dfs with the node,
        # moreover we will maintain a hashmap which will map the old node to new node.
        # Purpose of hashmap: Whenever we find the neighbor node which already in map then we,
        # return a new node for the connection as we are making a deepcopy.
        # DFS function will first create a deepcopy of a node and then iterate over the neigh of
        # given graph node and for every neigh we append the return deeepcopy from dfs recursion.
        mapOldNew = {}

        def dfs(node):
            if node in mapOldNew:
                return mapOldNew[node]
            
            deepcopy = Node(node.val)
            mapOldNew[node] = deepcopy
            for neigh in node.neighbors:
                deepcopy.neighbors.append(dfs(neigh))
            return deepcopy
        if node:
            return dfs(node)
        else:
            return None