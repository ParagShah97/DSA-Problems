# https://leetcode.com/problems/course-schedule/
# Time Complexity: O(V + E)
# Space Complexity: O(V + E)
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Intuition: From the problem we can infer that, in order to take 
        # course Ai you must
        # take course Bi, so there should be no cycle as (0 --> 1 --> 0), 
        # so the problem boils
        # down to detecting the cycle in a graph.
        # Solution: First create an adj list (can by hash map also), then for all the
        #  vertices
        # run dfs to find the cycle if not cycle found for all the 
        # vertices then return True.
        # Else return False at last.

        # Create Adj and visited lists
        adj = [[] for _ in range(numCourses)]
        vis = [False]*numCourses
        # Populate the adj.
        for take, pre in prerequisites:
            adj[take].append(pre)
        
        # DFS function call to check a cycle or not.
        def dfs(node):
            # print('-->', node)
            # If node is already visited then return False (As cycle found)
            if vis[node] == True:
                return False
            # If there are no output vertices from the node then return True
            # As it implies that no cycle found on the current path.
            if adj[node] == []:
                return True
            # Make the ndoe as visited.
            vis[node] = True
            # Traverse the neighbor
            for nei in adj[node]:
                # print('int-->', nei)
                if not dfs(nei):
                    return False
            # If no cycle found on the current path then make the visit node False
            # for the next path, as the graph is a directed graph.
            # print('done for node ', node)
            vis[node] = False
            # As the path from the current node don't leads to a cycle then we can make
            # remove neigh connected nodes.
            adj[node] = []
            # print('Vis', vis)
            return True            

        # Iterate over all the vertices as starting vertices.
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True