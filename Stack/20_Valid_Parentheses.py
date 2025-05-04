# https://leetcode.com/problems/valid-parentheses
# Time Complexity: O(N)
# Space Complexity: O(N)
class Solution:
    def isValid(self, s: str) -> bool:
        """
        Intuition:
        The question can be done on other way with relaively less conditions, though
        I want to cover all the cases.

        So, if the length of s is odd then return False.
        Iterate over s from index 1 to n, as 0th element already in stack.

        If the current element in compare dict then we can directly append it to 
        the stack (i.e-> (, {, [ ).
        If stack is not empty and stack top element in compare then
        if current element == value agaist the compare's stack top element, then
        pop the element from the stack, continue to next element
        else, return False (mean stack is not empty and top element not a match
        for the current element i.e. "(}" )

        At last return not stack (if stack empty return True else False)
        """

        if len(s) % 2 == 1:
            return False

        stack=[s[0]]
        compare = {"(":")", "[":"]", "{":"}"}

        for i in range(1, len(s)):
            # print("ss ", stack, s[i])
            if s[i] in compare:
                stack.append(s[i])
                continue
            if len(stack) and stack[-1] in compare:
                if compare[stack[-1]] == s[i]:
                    stack.pop()
                    continue
                return False
            else:
                return False
                
        
        return not stack 

        