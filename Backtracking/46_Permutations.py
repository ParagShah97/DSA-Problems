# https://leetcode.com/problems/permutations
# Time Complexity: O(n × n!)
# Space Complexity: O(n × n!)
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Intuition: Here we will call permute method for substring 1->end, so if we have list as
        # [1,2,3] then [2,3]->[3]->[]. Base case will be if len == 0 then return [[]], when we
        # get [[]] we will iterate over it and add put nums[0] = 3 on len([])+1 places.
        # For example when we get [[3]] in return from res then we put num[0] = 2 on len([3])+1
        # places so it will become [2,3] and [3,2], similaryly for last case when we get 
        # [[2,3], [3,2]] then we put 1 at len([2,3])+1 places so 0,1,2 places

        # [[]]
        # [[]] --> []
        # [[]] -inside-> [3]
        # [[3]]
        # [[3]] --> [3]
        # [[3]] -inside-> [2, 3]
        # [[3]] -inside-> [3, 2]
        # [[2, 3], [3, 2]]
        # [[2, 3], [3, 2]] --> [2, 3]
        # [[2, 3], [3, 2]] -inside-> [1, 2, 3]
        # [[2, 3], [3, 2]] -inside-> [2, 1, 3]
        # [[2, 3], [3, 2]] -inside-> [2, 3, 1]
        # [[2, 3], [3, 2]] --> [3, 2]
        # [[2, 3], [3, 2]] -inside-> [1, 3, 2]
        # [[2, 3], [3, 2]] -inside-> [3, 1, 2]
        # [[2, 3], [3, 2]] -inside-> [3, 2, 1]


        # Base case: if len of an array is 0 then return [[]]
        if len(nums) == 0:
            return [[]]

        # We call recursion for substring starting from 1st index.
        perms = self.permute(nums[1:])
        # print(perms)

        # ans array
        res = []
        
        # Iterate over perms (returned from perms)
        for p in perms:
            # print(perms, '-->', p)
            # in range + 1 of the size of an element from param.
            for i in range(len(p)+1):
                # First make a copy of p 
                p_copy = p.copy()
                # Now insert nums[0] at i positions like at 0 ,1,2 and so on.
                p_copy.insert(i, nums[0])
                # print(perms, '-inside->', p_copy)
                res.append(p_copy)
        return res