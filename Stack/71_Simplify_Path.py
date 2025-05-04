# https://leetcode.com/problems/simplify-path
# Time Complexity: O(N)
# Space Complexity: O(N)
class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        Intuition:
        We will keep the stack for the file name or folder name.
        keep curWord buffer string
        I will put "/" at the end to ease the condtion.

        As all the path will start from "/", can start the iteration from
        1st index.

        There will be 2 cases if cur character is "/"
        then
            check if curWord == ".."
                then check if stack not empty pop the word (move one dir back)
            check if curWord != "" and curWord != "." then
                append to the stack
            Make curWord as empty string
        else
            just concat to curWord the cur char

        At last return "/"+ "/".join(stack)
        """

        stack = []
        curWord = ""
        path+="/"

        for i in range(1, len(path)):
            if path[i] == "/":
                if curWord == "..":
                    if stack:
                        stack.pop()
                elif curWord != "" and curWord != ".":
                    stack.append(curWord)                        
                curWord = ""
            else:
                curWord+=path[i]
        
        return "/"+"/".join(stack)