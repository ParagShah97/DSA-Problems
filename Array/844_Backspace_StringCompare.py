# https://leetcode.com/problems/backspace-string-compare
# Time Complexity: O(N+M)
# Space Complexity: BF: O(N+M), Optimal O(1)
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        """
        Intuition:
        Brute force: TC O(N+M), SC O(N+M)
        We take 2 stacks, Then iterate over each str one by one, if the current character
        is '#' and stack is empty then do nothing, else if '#' then pop the prev elem
        from the stack.
        Else just add the char to the stack.
        At last compare the str formed by both the stack if equal return True else False.


        Optimized: TC O(N+M), SC O(1)
        Start at the end of the str with index_s, index_t pointer.
        Iterate till both index >=0 (or condition)
        At every index call the utility function to get the valid index.
        With that valid index compare the char, if index out of bound then
        assign "" (empty string).
        If the valid character not equal return False (not equal str).
        Decrement the current indexes.
        At last return True.

        Utility Function:
        Take str and index, and track the backspaces.
        If backspace =0 and str[index] != "#" then valid char break and return index.
        else if str[index] == "#" then we incremrnt the backspace
        else we decrement the backspace
        For all the operation we move the index to the previous val.
        At last return the index. {Here I am not check for the validity for the index
        that is done during the while loop.}
        """
        # Helper function to get the valid index to compare.
        def getValidIndex(cur_str, i):
            backspace = 0

            while i >=0:
                if backspace == 0 and cur_str[i] != "#":
                    break
                elif cur_str[i] == "#":
                    backspace += 1
                else:
                    backspace -=1
                i-=1
            # Here not cheking if the index went out of bound or not.
            return i
        
        index_s = len(s)-1
        index_t = len(t)-1
        
        while index_s>=0 or index_t>=0:
            index_s = getValidIndex(s, index_s)
            index_t = getValidIndex(t, index_t)

            cur_char_s = s[index_s] if index_s >=0 else "" 
            cur_char_t = t[index_t] if index_t >=0 else ""
            print(cur_char_s, cur_char_t)
            if cur_char_s != cur_char_t:
                return False
            
            index_s-=1
            index_t-=1
        
        return True



        # stack1 = []
        # stack2 = []

        # # Let's start with the first str
        # for c in s:
        #     if not stack1 and c=="#":
        #         continue
        #     if c == "#":
        #         stack1.pop()
        #         continue
        #     stack1.append(c)
        # for c in t:
        #     if not stack2 and c=="#":
        #         continue
        #     if c == "#":
        #         stack2.pop()
        #         continue
        #     stack2.append(c)

        # # print(stack1,stack2)
        # return "".join(stack1) == "".join(stack2)