# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string
# Time Complexity O(N*M) 
# Space Complexity O(M)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Intuition:
        First I am checking that if len of needle should not be greater than hay
        If not then,
        Iterate from i 0 to len(hay)-len(needle)+1 {keeping index inbound}
        if ith index is start index of needle we check the hay string from
        ith index to i+len(needle) is equal to needle string if yes return
        ith index. Outside the iteration return -1.
        """
        if len(needle) > len(haystack):
            return -1
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i] == needle[0] and haystack[i: i+len(needle)] == needle:
                return i
        return -1