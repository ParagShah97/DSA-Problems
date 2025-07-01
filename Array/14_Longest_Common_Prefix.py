# https://leetcode.com/problems/longest-common-prefix/
# Time Complexity: O(N*M)
# Space Complexity:O(1)
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        """
        Intuition:
        Brute force, we first find the smallest string from the strs.
        Then we iterate over each character of the smallest str and 
        then nestedly iterate over all the strs to check the prefix.
        If for any str the prefix is not matched then we return the prev
        calc prefix. At last we return the overall prefix.
        """
        # First find the smallest string from list.
        
        # Here take first str as placeholder to check other
        minLen = len(strs[0])
        compStr = strs[0]

        # Iterate from 2nd element
        for s in strs[1:]:
            if len(s) < minLen:
                minLen = len(s)
                compStr = s
        
        # print(compStr)
        ans = ""
        for i in range(len(compStr)):
            for ss in strs:
                if compStr[:i+1] != ss[:i+1]:
                    return ans
            ans = compStr[:i+1]    

        return ans