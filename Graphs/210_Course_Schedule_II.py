# https://leetcode.com/problems/course-schedule-ii/
# Time Complexity: O(V+E)
# Space Complexity: O(V+E)

from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        '''
        Intuition: It's like Toplogical sort: Which means that for a DAG we can find the
        order in which the node to be listed so that the node which is not dependent
        on any other node will get initial order.

        We will keep the cycle and vis(viited set) to check if there is cycle and vis will
        tell in next iteration that if the node already been visited or not.
        vis -> global to all the iteration
        cycle -> is local to one iteration that is a dfs call.

        For every node we will make a dfs call and if the dfs function return False then
        return [] else we check for the next node.
        dfs function will check if node present in cycle set then return False
        dfs function will check if node present in vis set then return True
        '''
        adj = [[] for _ in range(numCourses)]
        vis = set()
        cycle = set()
        ans = []

        for take, pre in prerequisites:
            adj[take].append(pre)
        # print(adj)

        def dfs(node):
            if node in cycle:
                return False
            if node in vis:
                return True
            
            cycle.add(node)

            for nei in adj[node]:
                if not dfs(nei):
                    return False
            
            vis.add(node)
            cycle.remove(node)
            ans.append(node)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return ans