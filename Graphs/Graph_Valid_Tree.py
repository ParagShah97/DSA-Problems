# https://leetcode.com/problems/graph-valid-tree/
# Time Complexity: O(V+E)
# Space Complexity: O(V+E)
from typing import List


class Solution:
    '''
    Intuition:
    The main idea is we need to detect if there is any cycle or not or all the 
    nodes are connected or not.

    First we need to make an adj list from the given edges.
    We also keep the visited set.

    Then we can do a dfs from node '0', if the node already visited return False.
    If not then add to visited then iterate over the node's neighbor
    Here first check the parent(prev_node) == to nei node, if yes then continue.
    Here, we are checking that while searching for the cycle we accidently don't 
    take the same edge as cycle (0->1->0).
    Then make the dfs call to the neigh, if return value is False then return False.
    At last return False from the Dfs method.

    Call to dfs(0,-1), here check if the dfs call returns True and visited set len == vertices.
    In case of disconnect graph need to check the set and vertices length.
    '''
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i:[] for i in range(n)}

        for s,d in edges:
            adj[s].append(d)
            adj[d].append(s)
        
        
        vis = set()

        def dfs(node, from_node):
            if node in vis:
                return False
            
            vis.add(node)

            for nei in adj[node]:
                if nei == from_node:
                    continue
                if not dfs(nei, node):
                    return False
            
            return True
        
        if dfs(0, -1) and len(vis) == n:
            return True
        return False