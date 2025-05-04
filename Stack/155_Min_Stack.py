# https://leetcode.com/problems/min-stack
# Time Complexity: O(1)
# Space Complexity: O(N)

# Intuition:
# Approach 1: Consider only 1D stack for all operation except getMin and heapStack as min heap
# this will give the min value and for all other operations normal stack will work.
# Apporach 2: Better: We will take 2D stack where at 0th index we will store the pushed value
# and at 1st index we will store the min value till that point.
class MinStack:

    def __init__(self):
        self.stack = []        

    def push(self, val: int) -> None:
        # In case the stack is empty then append push value for both position.
        if len(self.stack) == 0:
            self.stack.append([val, val])
        else:
            # Current min will store the minimum value till previously pushed value. 
            curMin = self.stack[-1][1]
            # For new pushed value will add value at 0th and min of val and prev till min.
            self.stack.append([val, min(val, curMin)])
    
    def pop(self) -> None:
        # Just pop the stack value.
        self.stack.pop()
        

    def top(self) -> int:
        # return the top value.
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        # self.heapStack = self.stack[:]
        # heapq.heapify(self.heapStack)
        # return self.heapStack[0]
        
        # return the top value at 1st index
        return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()