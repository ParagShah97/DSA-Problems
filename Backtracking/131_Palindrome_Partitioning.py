# https://leetcode.com/problems/palindrome-partitioning/
# Time Complexity: O(N*2^N)
# Space Complexity: O(N) extra space.
# O(N*2^N) space for the output list.


# DFS i  0  and j  0
# For i and j 0 0  part val is  ['a']
# DFS i  1  and j  1
# For i and j 1 1  part val is  ['a', 'a']
# DFS i  2  and j  2
# For i and j 2 2  part val is  ['a', 'a', 'b']
# ### ['a', 'a', 'b']
# For i and j 2 2  part val POP **  ['a', 'a']
# For i and j 1 1  part val POP **  ['a']
# DFS i  1  and j  2
# For i and j 0 0  part val POP **  []
# DFS i  0  and j  1
# For i and j 0 1  part val is  ['aa']
# DFS i  2  and j  2
# For i and j 2 2  part val is  ['aa', 'b']
# ### ['aa', 'b']
# For i and j 2 2  part val POP **  ['aa']
# For i and j 0 1  part val POP **  []
# DFS i  0  and j  2

from typing import List


class Solution:
    """
    Intuition:
    Here first we take the global curPart and ans lists.
    Using a utility function isPalindrome to check the strinf from i to j index is palindrome or not.
    Then we have our main backtrack method, here we make an iteration from ith index to end of the 
    string over the characters.
    If the current boundry make an palindrome then we append the current substring into the
    temp array curPart, and make the bachtrack recursion call for start index as current iter
    idx(i.e j)+1.
    After making a call, remove the just added element curPart array.

    Here, if the index >= len(s) then we can save the copy of curPart as we
    get 1 path (by partitioning) for all the palindromes.

    At last return the ans.
    """
    def partition(self, s: str) -> List[List[str]]:
        curPart, ans = [], []

        def isPalindrom(l,r):
            while l<r:
                if s[l] != s[r]:
                    return False
                l,r = l+1, r-1
            return True


        def backtrack(i):
            if i >= len(s):
                # print("###", curPart)
                ans.append(curPart[:])
                return
            
            for j in range(i, len(s)):
                # print("DFS i ", i, " and j ", j)
                if isPalindrom(i,j):
                    curPart.append(s[i:j+1])
                    # print("For i and j",i,j," part val is ", curPart)
                    backtrack(j+1)
                    curPart.pop()
                    # print("For i and j",i,j," part val POP ** ", curPart)

        backtrack(0)
        return ans