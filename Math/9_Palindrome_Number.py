# https://leetcode.com/problems/palindrome-number
# Time Complexity: O(N)
# Space Complexity: O(1)
class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Intuition:
        First approach just convert to the str and compare the
        str to it's reverse.

        Follow up:
        If need to be done without converting it to the str, then we
        can first check if the str is neg or not.
        Then we can convert the number to reverse number,
        then we check if the number is positive and equal to reverse 
        of the current number then return True, else False.
        """
        # Brute force
        # First check if the x is pos or neg
        toStr = str(x)
        if toStr == toStr[::-1]:
            return True
        return False
        
        # Follow up:
        # Let's say we can only use in integer but not str
        
        isNeg = True if x < 0 else False
        val = abs(x)

        def revert(n):
            num = 0
            while n > 0:
                rem = n % 10
                n = n//10
                num = num*10 + rem
            return num
        
        if not isNeg and revert(val) == val:
            return True
        else:
            return False