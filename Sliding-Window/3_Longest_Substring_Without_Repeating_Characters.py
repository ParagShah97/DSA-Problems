# https://leetcode.com/problems/longest-substring-without-repeating-characters
# Time complexity: O(N)
# Space complexity: O(N)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        Intuition:
        We can use the concept of sliding window here:
        We keep the left pointer (for starting index initially 0), and ans var.
        We then iterate over the the string "s" for every char we check if it
        present in the dic if not we simple add the key as char and value as index
        and update the ans with max as curr ans or newly calculated ans.
        But if the char is present in the dic then we move the left pointer
        by max of left or char repeated previous index + 1.
        '''

        ans = 0
        l=0
        dic = {}

        for r in range(len(s)):
            if s[r] in dic:
                l = max(l, dic[s[r]]+1)
            dic[s[r]] = r
            ans = max(ans, r-l+1)
        
        return ans