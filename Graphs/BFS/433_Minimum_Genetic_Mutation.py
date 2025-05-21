# https://leetcode.com/problems/minimum-genetic-mutation
# Time Complexity O(N*L^2)
# Space Complexity O(N*L)
from collections import deque
from typing import List


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        """
        Intuition:
        As we need to check the newly created string in bank we need to 
        convert the bank into a set of strings.

        Here we can apply the BFS (A bit modified), we will apply BFS on the
        newly created string by replacing a char (at a time) in the string.

        So, we initailly put the startGene in the queue and vis set,
        then iterate till the queue is not empty. At every level we need
        to find the lenght of the queue and while loop till the cur no. of 
        strings in queue is iterated.

        For every string pop from the queue we first check if it is endGene str
        if yes return level else, we nested iterate over ACGT for each char of cur str
        and replace it and then we check if newly formed string not in vis but present
        in the bank then make the new_str visited and append it ti queue.

        Once the outher while loops end we increment the level by 1.

        At last if we can't make the endGene then return -1. 
        """
        # Let make the words from the bank as set
        set_bank = set(bank)

        q = deque()
        q.append(startGene)
        vis = set()
        vis.add(startGene)
        level = 0

        while q:
            q_size = len(q)

            while q_size > 0:
                
                cur = q.popleft()
                q_size -= 1

                if cur == endGene:
                    return level

                for c in "ACGT":
                    for i in range(len(cur)):
                        nei = list(cur)
                        # We made a copy of a string and then try to put
                        # character at each locations for all 4 chars ACGT
                        nei[i] = c
                        nei = "".join(nei)

                        if nei not in vis and nei in set_bank:
                            vis.add(nei)
                            q.append(nei)
            level += 1
        return -1    