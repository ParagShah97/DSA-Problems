# https://leetcode.com/problems/palindromic-substrings/
# Time Complexity: O(N^2)
# Space Complexity: O(1)
class Solution:
    def countSubstrings(self, s: str) -> int:
        # 2 Pointer approach
        '''
        Intuition: 
        For 2 pointer approach, we have to explore the idea that to check the palidromic
        string we can also start from the character and expand both the side if after the
        expansion again the char matches then we can say that we find a bigger palindrom
        and so on. 
        There can be 2 cases odd size palindorme b<-a->b
        even size: b<-a-a->b

        In Odd size we start with 2 pointer pointing at the same character
        whereas for even size we start 2 pointer from char and char+1.
        '''
        ans= 0
        #  For every character we will expand both the side
        for i in range(len(s)):
            # Odd palindrome
            # Start with the same char
            l,r = i,i
            # check if l and r are inbound and char at l and r are same then we find 
            # an odd palindrom
            while l >=0 and r<len(s) and s[l] == s[r]:
                ans+=1
                # expand <- and ->
                l -= 1
                r += 1

            # even palindrome
            # Start with the char at i and i+1
            l,r= i, i+1
             # check if l and r are inbound and char at l and r are same then we find 
            # an odd palindrom
            while l>=0 and r<len(s) and s[l]==s[r]:
                ans += 1
                # expand <- and ->
                l-=1
                r+=1
        return ans