# https://leetcode.com/problems/evaluate-division
# Time Complexity: O(N)+O(N) = O(N)
# Space Complexity: O(N^2)
from collections import defaultdict, deque
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        """
        Intuition:
        We have to imagine the division as graph as a/b mean a:(b, val) in
        adj list.
        So First we have to create adj list.
        Then we iterate over the queries and call bfs(source, destination).
        Here we have to check the condition if src and dst present in adj
        if not then put -1.

        In bfs function, we first take queue and visit set.
        Add the incoming (src,1) node to the queue and to visit set.
        then iterate till queue is empty, popleft the node and weight
        if node == target return w.
        Else iterate over the neighbor and add the neig node and w*wigt
        to the queue (if nei node not yet visited), & add neiNode to vis.
        """
        # Make adj list.
        adj = defaultdict(list)
        for i,[s,d] in enumerate(equations):
            adj[s].append((d,values[i]))
            adj[d].append((s,1/values[i]))

        # print(adj)
        # BFS function
        def bfs(s,d):
            q,vis = deque(), set()
            q.append([s,1])
            vis.add(s)

            while q:
                node, w = q.popleft()

                if node == d:
                    return w
                
                for nei in adj[node]:
                    if nei[0] not in vis:
                        q.append([nei[0], w*nei[1]])
                        vis.add(nei[0])
            return float(-1)

        # Call the bfs for each query.
        ans = []
        for s,d in queries:
            if s in adj and d in adj:
                ans.append(bfs(s,d))
            else:
                ans.append(float(-1))
        return ans