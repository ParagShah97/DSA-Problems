# https://leetcode.com/problems/evaluate-reverse-polish-notation
# Time Complexity: O(N)
# Space Complexity: O(N)
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Intuition: We have interger(as string) and operators, 
        # if we get integer then we push to the stack and as soon we get an
        #  operator then we pop two values from the stack and 
        # do the operation we get from the token list
        # and push the resultant back to stack.

        stack = []
        op = {"+", "-", "/", "*"}

        def opre(opType, a,b):
            if opType == "+":
                return a+b
            elif opType == "*":
                return a*b
            elif opType == "-":
                return a-b
            else:
                return int(a/b)
        
        for i in tokens:
            if i not in op:
                stack.append(int(i))
            else:
                b = stack.pop()
                a = stack.pop()
                val = opre(i, a, b)
                stack.append(val)

        return stack[-1]