# https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/
# Time Complexity: O(N) | optimal, O(n^2) for brute force.
# Space Complexity: O(N) | For the dictionary.

from typing import List


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        """
        Intuition:
        Brute force will be like use of nested loops and increment count if any pair diff==k.

        Optimal:
        Keep a dictionary, and a ans counter.
        Iterate over nums, every time we check for n+k and n-k if present in dict then add the
        freq of that value to the counter.
        And at last add the value to the dict with 0 or current freq + 1.
        At last return ans.
        """
        mapper = {}
        ans = 0
        for n in nums:
            ans += mapper.get(n+k, 0)
            ans += mapper.get(n-k, 0)
            if n in mapper:
                mapper[n]+=1
            else:
                mapper[n]=1
        return ans