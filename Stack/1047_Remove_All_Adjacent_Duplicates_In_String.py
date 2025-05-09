# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
# Time Complexity: O(N)
# Space Complexity: O(N)
class Solution:
    def removeDuplicates(self, s: str) -> str:
        """
        Intution:
        We can use stack here.
        We can iterate over the string s,evert time we will check if the stack
        is not empty and top of stack == current element then we will pop
        element from the stack.
        Else we will append the current element to the stack.
        """
        stack = []

        for i in s:
            if stack and i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)

        return "".join(stack)
        