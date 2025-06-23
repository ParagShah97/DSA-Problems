# https://leetcode.com/problems/permutation-in-string/
# Time Complexity : O(N)
# Space Complexity: O(N)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Intuition: 
        First we check if len of s1 > s2 then return False.
        We take l1 and l2 of size 26 of 0s.

        First iteration for the window size of s1.
        Where l1 and l2 index is inc if ord(s[i]) - ord('a') 
        Second iteration start from len(s1) {after initial window} and
        end at len(s2).
        then, first we check if l1==l2 return True.
        then we move window for l2 removing left element and adding
        new element for right.

        At last again we return l1==l2.  
        """
        if len(s1) > len(s2):
            return False
        
        l1 = [0]*26
        l2 = [0]*26

        for i in range(len(s1)):
            l1[ord(s1[i])-ord('a')] += 1
            l2[ord(s2[i])-ord('a')] += 1

        for j in range(len(s1), len(s2)):
            if l1==l2:
                return True
            l2[ord(s2[j-len(s1)])-ord('a')] -= 1
            l2[ord(s2[j])-ord('a')] += 1         
                        
        return l1==l2