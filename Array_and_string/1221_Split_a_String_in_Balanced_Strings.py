# https://leetcode.com/problems/split-a-string-in-balanced-strings
# Time Complexity: O(N)
# Time Complexity: O(1)
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        """
        Intuition:
        Here we just need to count the l,r count, after every character we increment either 
        l or r counter, and then check if l and r counter values are equal then increment 
        split count (ans).
        At last return split count.
        """
        
        r_cnt = 0
        l_cnt = 0
        ans = 0
        for i in s:
            if i == "R":
                r_cnt += 1
            elif i == "L":
                l_cnt += 1
            if r_cnt == l_cnt:
                ans += 1
            
        return ans