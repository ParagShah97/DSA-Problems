# https://leetcode.com/problems/valid-palindrome-ii/
# Time Complexity O(N)
# Space Complexity O(1)
class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        Intuition:
        We can do simply palinromic 2 pointer approach as soon as we get the
        case when s[l] != s[r] then we can compare 2 cases.
        1) Omitting left 1 character and compare l+1 with r in while loop
        2) Omitting right 1 character and compare l with r-1 in while loop
        return True of either of the 2 cases return True else False.
        At last we can also return True if it's true palindorme without
        any wrong character.
        """
        l = 0
        r = len(s)-1

        def compareSub(l,r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1
            return True

        while l < r:
            if s[l] != s[r]:
                if compareSub(l+1,r) or compareSub(l,r-1):
                    return True
                return False
            l+=1
            r-=1
        return True