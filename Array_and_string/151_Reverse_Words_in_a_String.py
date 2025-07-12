# https://leetcode.com/problems/reverse-words-in-a-string
# Time Complexity O(N)
# Space Complexity O(N)
class Solution:
    def reverseWords(self, s: str) -> str:
        """
        Intuition:
        First we can split the string array into str array with " " (space as 
        seperator), then we can iterate in reverse order, if split str not
        an empty str then we can append the str to ans list.
        At last we can join the list back to space seperated string.
        """
        splitStrs = s.split(" ")
        ans= []
        for s in splitStrs[::-1]:
            if s != "":
                ans.append(s)

        return " ".join(ans)