# https://leetcode.com/problems/word-pattern
# Time Complexity O(N)
# Space Complexity O(N)
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """
        Intuition:
        This is similar to isomorphic string problem.
        We have to take care of mapping from pattern <-> string both ways.
        So, initially we will check len(pattern) if not equals to len(splits)
        then return False.
        Then we will keep 2 hashmap for both way mapping.
        We iterate over the pattern and words split list, check
        if char in mapPS and mapPS[ch] != word or 
        word in mapSP and mapPS[word] != ch then return False.

        At last return True, means that correct mapping. 
        """
        sp = s.split(" ")
        if len(pattern) != len(sp):
            return False
        
        mapPS, mapSP = {}, {}
        
        for i in range(len(pattern)):
            c,w = pattern[i], sp[i]
            if ((c in mapPS and mapPS[c]!=w) or (w in mapSP and mapSP[w]!=c)):
                return False
            mapPS[c] = w 
            mapSP[w] = c 
        
        return True