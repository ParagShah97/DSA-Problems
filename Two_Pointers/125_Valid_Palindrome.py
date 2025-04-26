# https://leetcode.com/problems/valid-palindrome
# Time Complexity: O(N)
# Space Complexity: O(N)
class Solution:
    """
    Intuition:
    We can use 2 pointer apporach, we start from left pointer i and right pointer j
    first convert the string to lower case. Then iterate til i<j.
    Inside we check if current ith or jth character point to an non alphanum then
    we iterate till we get the valid char.
    Then we check if s[i]!=s[j] then we return False.
    But if the iteration runs fine without returning False then atlast we return 
    True.
    """
    def isPalindrome(self, s: str) -> bool:
        i  = 0
        j = len(s)-1
        s = s.lower()

        while i<j:
            while i<j and not s[i].isalnum():
                i+=1
            while i<j and not s[j].isalnum():
                j-=1
            if s[i] != s[j]:
                return False
            i+=1
            j-=1
        return True