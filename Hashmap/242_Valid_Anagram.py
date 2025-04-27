# https://leetcode.com/problems/valid-anagram
# Time Complexity: O(N)
# Space Complexity: O(N)
from collections import Counter
class Solution:
    """
    Intuition: 
    First if s and t are of different length return False.
    Make hashmap using Counter of either s or t.
    Iterate over the other string and check if all the character exits
    with equal freq or not.
    """
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        cntS = Counter(s)
        for i in t:
            if (i not in cntS) or (cntS[i] == 0):
                return False
            elif cntS[i] > 0:
                cntS[i]-= 1
        
        return True