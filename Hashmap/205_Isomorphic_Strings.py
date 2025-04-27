# https://leetcode.com/problems/isomorphic-strings
# Time Complexity: O(N)
# Space Complexity: O(N)
class Solution:
    """
    Intuition:
    Here we need to check the mapping in both the directions, that 
    mean we need to check a char from s map to char in t and from t
    to s in 1:1 fashion no diferent mapping for same character in both
    the direction is not allowed.

    We Keep the mapping from S->T and T->S.
    Iterate on char from s and t.
    We check if c1 present in mapST and c1 not map to c2
    OR
    We check if c2 present in mapTS and c2 not map to c1
    We return False.

    At last after the loop we return True.
    """
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapST, mapTS = {}, {}

        for c1,c2 in zip(s,t):
            # c1,c2 = s[i], t[i]

            if ((c1 in mapST and mapST[c1]!=c2) or (c2 in mapTS and mapTS[c2]!=c1)):
                return False
            
            mapST[c1] = c2
            mapTS[c2] = c1
        return True