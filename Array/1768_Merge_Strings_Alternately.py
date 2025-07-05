# https://leetcode.com/problems/merge-strings-alternately
# Time Complexity: O(M+N)
# Space Complexity: O(M+N)
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        """
        Brute force:
        Take 2 pointers, i,j start with 0.
        Iterate till either exhaust and append the char alternatively.
        Then we iterate for the remaining element and put it in ans.
        return join array for ans.
        """
        ans = []
        i=0
        j=0

        while i < len(word1) and j < len(word2):
            ans.append(word1[i])
            ans.append(word2[j])
            i+=1
            j+=1
        
        while i < len(word1):
            ans.append(word1[i])
            i+=1
            
        while j < len(word2):
            ans.append(word2[j])
            j+=1

        return "".join(ans)