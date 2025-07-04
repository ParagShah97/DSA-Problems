# https://leetcode.com/problems/valid-parentheses
# Time complexity: O(N)
# Space complexity: O(N)
class Solution:
    def isValid(self, s: str) -> bool:
        """
        Intuition:
        First we can access that the length of the string is odd then definately
        there is no valid parentheses: return False.
        For other scenarios we will take stack and a mapping dic for parantheses.
        (see code for dic)
        We iterate over the string s. First we check if the val of b is present in
        dic "({[" are present then append it to the stack.
        If we get ")]}" as b's value then we first check if the stack is non empty,
        if non-empty then we check if the stack top element's mapped value == b,
        then just pop the element from the stack. Else we return False, as we get the
        closing parantheses which is not closing the current one.
        At last we return True if stack is empty else False. 
        """
        if len(s)%2 == 1:
            return False
        mappingDic = {"{":"}", "(":")", "[":"]"}
        stack = []
        for b in s:
            if b in mappingDic:
                stack.append(b)
            elif stack and mappingDic[stack[-1]] == b:
                stack.pop()
            else:
                return False
        
        return not stack