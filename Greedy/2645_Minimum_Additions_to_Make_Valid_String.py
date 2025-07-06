# https://leetcode.com/problems/minimum-additions-to-make-valid-string/
# Time Complexity
# Space Complexity
class Solution:
    def addMinimum(self, word: str) -> int:
        """
        Intuition:
        Here we can do a greedy approach.
        We iterate from 0th index till last index.
        For every iteration we take validLen = 0, then with help of 3 cond's
        we check the successive a,b,c character. If any of the character 
        is missing increment the validLen and at last add 3-validLen to
        the ans.

        Aftr the iteration return the ans.
        """
        i=0
        ans = 0
        n = len(word)
        while i < n:
            validLen = 0

            if word[i] == 'a':
                validLen +=1
                i+=1
            if i<n and word[i] == 'b':
                validLen +=1
                i+=1
            if i<n and word[i] == 'c':
                validLen +=1
                i+=1
            
            ans += 3-validLen
        return ans