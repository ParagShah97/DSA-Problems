# https://leetcode.com/problems/is-subsequence
# Time Complexity: O(N)
# Space Complexity: O(1)
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        Intuition:
        First we check if len(s) > len(t), if yes return False.
        Now, we can use 2 pointers i and j from start.
        Iterate till i < len(s) and j < len(t)
        If ith and jth char of s and t matches increment i and j.
        else only increment j.

        At last check if i == len(s), if yes then we found all the elemnts
        of s in t (subsequence), return True.
        Else just return False.
        """
        if len(s) > len(t):
            return False
        
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i+=1
                j+=1
                
            else:
                j+=1
        # print('i and j ', i,j)
        if i == len(s):
            return True
        return False